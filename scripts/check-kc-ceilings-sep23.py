"""Check Kansas City bid ceilings against the seven KC lots whose final bids are known (2026-09-23).

Adds the final bids of three more sold KC lots (FinalBid pages), then rates each unsold KC lot's bid
ceiling: ceiling / similar-auction average is compared with final bid / average of the sold KC lots.
"wins" counts how many of those sold lots the ceiling would have won. Seven lots are a small sample.
"""
import json, re, statistics
from pathlib import Path

p = Path(__file__).resolve().parents[1] / 'dist'
cars = json.loads((p / 'combined80.json').read_text())
by = {c['id']: c for c in cars}
FINAL = [
    ('66814326', 8600, '2026-09-17', 'Yes', 'https://finalbid.vin/en/honda/civic/2018/copart-66814326-19XFC2F52JE003328'),
    ('65278226', 4800, '2026-09-17', 'No', 'https://finalbid.vin/en/subaru/legacy/2017/copart-65278226-4S3BNAC67H3033961'),
    ('65599336', 4400, '2026-09-15', 'Yes', 'https://finalbid.vin/en/honda/cr-v/2017/copart-65599336-7FARW5H3XHE008335'),
]
for lot, price, date, reserve, source in FINAL:
    c = by[lot]
    assert c['yard'] == 'KC' and c['availability'] == 'sold' and 'finalBid' not in c and c['vin'] in source, lot
    c['finalBid'] = dict(price=price, date=date, reserveMet=reserve, source=source, checkedAt='2026-09-23')

kc = [c for c in cars if c['yard'] == 'KC']
sold = [c for c in kc if c.get('finalBid')]
assert len(sold) == 7 and all(c['availability'] == 'sold' for c in sold)
ratios = sorted(c['finalBid']['price'] / c['comparisonAverage'] for c in sold)
open_lots = [c for c in kc if c['availability'] not in ('sold', 'ended')]
for c in open_lots:
    k = c['maxBid'] / c['comparisonAverage']
    c['ceilingCheck'] = dict(ratio=round(k, 2), wins=sum(r <= k for r in ratios), of=len(ratios), checkedAt='2026-09-23')
(p / 'combined80.json').write_text(json.dumps(cars, ensure_ascii=False, indent=2) + '\n')

lo, hi, mid = ratios[0], ratios[-1], statistics.median(ratios)
spread = f'{lo:.2f}–{hi:.2f}배(중앙값 {mid:.2f}배)'
won = [c for c in sold if c['finalBid']['price'] <= c['maxBid']]

def gap(c):
    d = c['finalBid']['price'] - c['maxBid']
    return f"입찰 상한 ${c['maxBid']:,}보다 ${abs(d):,} {'높음' if d > 0 else '낮음'}"

counts = {}
for name in ['combined.html', 'index.html', 'suv.html']:
    text = (p / name).read_text()
    def patch(m):
        block = m[0]
        lot = (re.search(r'id="lot-(\d+)"', block) or [None, None])[1]
        c = by.get(lot)
        if not c or c['yard'] != 'KC': return block
        if lot in {x[0] for x in FINAL}:
            f = c['finalBid']
            block, n1 = re.subn(r'(<span class="current-state[^"]*">)판매 완료 \(Sold\)<br>현재 입찰 미표시 · 조회 9/\d+(</span>)',
                                rf"\g<1>판매 완료 · 낙찰가 ${f['price']:,}<br>{gap(c)} · 9/23 확인\g<2>", block)
            block, n2 = re.subn(r'판매 완료 \(Sold\) · 현재 입찰 미표시',
                                f"판매 완료 (Sold) · <b>낙찰가 ${f['price']:,}</b> · {f['date']} · Reserve met: {f['reserveMet']} · "
                                f"<a href=\"{f['source']}\" target=\"_blank\" rel=\"noopener\">FinalBid 기록 ↗</a>", block)
            assert n1 == n2 == 1, (name, lot)
        elif 'ceilingCheck' in c:
            k = c['ceilingCheck']
            block, n1 = re.subn(r'(<span class="current-state[^"]*">.*?)(</span>)',
                                rf"\g<1><br>상한 승산 {k['wins']}/{k['of']} · 평균의 {k['ratio']:.2f}배\g<2>", block, count=1, flags=re.S)
            block, n2 = re.subn(r'(<p class="current-info">.*?)(</p>)',
                                rf"\g<1><br><b>상한 점검</b>: 입찰 상한(${c['maxBid']:,})은 유사 경매 평균(${round(c['comparisonAverage']):,})의 "
                                rf"{k['ratio']:.2f}배입니다. 낙찰가가 확인된 KC 판매 완료 {k['of']}대는 평균의 {spread}에 팔렸고, "
                                rf"이 상한이면 그중 {k['wins']}대를 낙찰받았을 수준입니다.\g<2>", block, count=1, flags=re.S)
            assert n1 == n2 == 1, (name, lot)
        else:
            return block
        counts[name] = counts.get(name, 0) + 1
        return block
    text = re.sub(r'<article\b.*?</article>', patch, text, flags=re.S)
    if name == 'combined.html':
        buckets = [('승산 2대 이상', [c for c in open_lots if c['ceilingCheck']['wins'] >= 2]),
                   ('1대', [c for c in open_lots if c['ceilingCheck']['wins'] == 1]),
                   ('0대', [c for c in open_lots if c['ceilingCheck']['wins'] == 0])]
        notice = (f'<section class="current-notice"><h2>9월 23일 추가 · Kansas City 입찰 상한 점검</h2>'
                  f'<p>KC 판매 완료 {len(sold)}대의 실제 낙찰가를 FinalBid에서 확인했습니다. 입찰 상한 이하로 팔린 차는 '
                  f'{len(won)}대({", ".join(c["vehicle"] for c in won)})뿐이고, 낙찰가는 유사 경매 평균의 {spread}였습니다. '
                  f'비교 기록 대부분이 충돌 손상이라 우박 차량 시세를 낮게 잡은 것으로 보입니다. 입찰 상한은 총예산 $10,000에서 역산한 값이며 시세 추정이 아닙니다.</p>'
                  f'<p>미판매 KC {len(open_lots)}대 카드에 <b>상한 승산</b>을 붙였습니다: 이 상한으로 판매 완료 {len(sold)}대 중 몇 대를 낙찰받을 수 있었는지입니다. '
                  + ' · '.join(f'{label} {len(v)}대' for label, v in buckets) +
                  f'. 표본이 {len(sold)}대뿐이고 3대는 Reserve 미충족 상태의 판매자 승인 거래라 참고용입니다.</p></section>')
        anchor = '<p><a href="marketplace.html">차종별 비교·FB 추천 매물 보기</a>'
        i = text.index(anchor)
        j = text.index('</section>', i) + len('</section>')
        text = text[:j] + notice + text[j:]
    (p / name).write_text(text)

t = (p / 'es.html').read_text()
old = "${c.overBidCeiling?' · Supera el límite':''}"
assert t.count(old) == 1
(p / 'es.html').write_text(t.replace(old, old + "${c.ceilingCheck?' · Límite vs. ventas KC: '+c.ceilingCheck.wins+'/'+c.ceilingCheck.of:''}"))

assert counts == {'combined.html': 31, 'index.html': 12, 'suv.html': 13}, counts
print('sold ratios', [round(r, 2) for r in ratios], '| wins per open lot:',
      dict(sorted(((c['id'], c['ceilingCheck']['wins']) for c in open_lots), key=lambda x: -x[1])))
