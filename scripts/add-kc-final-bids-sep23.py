"""Record the final bids of four sold Kansas City lots, read from their FinalBid pages on 2026-09-23."""
import json, re
from pathlib import Path

p = Path(__file__).resolve().parents[1] / 'dist'
cars = json.loads((p / 'combined80.json').read_text())
by = {c['id']: c for c in cars}
# lot, final bid, sale date, reserve met, FinalBid page
FINAL = [
    ('62420466', 3950, '2026-09-17', 'No', 'https://finalbid.vin/en/mitsubishi/eclipse-cross/2020/copart-62420466-JA4AT3AA6LZ035947'),
    ('64586406', 1000, '2026-09-15', 'No', 'https://finalbid.vin/en/ford/fusion/2016/copart-64586406-3FA6P0G76GR231039'),
    ('65120686', 7600, '2026-09-17', 'Yes', 'https://finalbid.vin/en/ford/escape/2020/copart-65120686-1FMCU0BZ2LUB78790'),
    ('65742956', 850, '2026-09-15', 'Yes', 'https://finalbid.vin/en/mazda/3/2012/copart-65742956-JM1BL1VF0C1503545'),
]
for lot, price, date, reserve, source in FINAL:
    c = by[lot]
    assert c['availability'] == 'sold' and 'finalBid' not in c and c['vin'] in source, lot
    c['finalBid'] = dict(price=price, date=date, reserveMet=reserve, source=source, checkedAt='2026-09-23')
(p / 'combined80.json').write_text(json.dumps(cars, ensure_ascii=False, indent=2) + '\n')

def gap(c):
    d = c['finalBid']['price'] - c['maxBid']
    return f"입찰 상한 ${c['maxBid']:,}보다 ${abs(d):,} {'높음' if d > 0 else '낮음'}"

patched = 0
for name in ['combined.html', 'index.html', 'suv.html']:
    text = (p / name).read_text()
    def patch(m):
        global patched
        block = m[0]
        lot = next((lot for lot, *_ in FINAL if f'id="lot-{lot}"' in block), None)
        if not lot: return block
        c, f = by[lot], by[lot]['finalBid']
        block, n1 = re.subn(r'(<span class="current-state[^"]*">)판매 완료 \(Sold\)<br>현재 입찰 미표시 · 조회 9/\d+(</span>)',
                            rf"\g<1>판매 완료 · 낙찰가 ${f['price']:,}<br>{gap(c)} · 9/23 확인\g<2>", block)
        block, n2 = re.subn(r'판매 완료 \(Sold\) · 현재 입찰 미표시',
                            f"판매 완료 (Sold) · <b>낙찰가 ${f['price']:,}</b> · {f['date']} · Reserve met: {f['reserveMet']} · "
                            f"<a href=\"{f['source']}\" target=\"_blank\" rel=\"noopener\">FinalBid 기록 ↗</a>", block)
        assert n1 == 1 and n2 == 1, (name, lot, n1, n2)
        patched += 1
        return block
    (p / name).write_text(re.sub(r'<article\b.*?</article>', patch, text, flags=re.S))

t = (p / 'es.html').read_text()
old = "${saleLabels[c.availability]}${c.needsBroker"
assert t.count(old) == 1
(p / 'es.html').write_text(t.replace(old, "${saleLabels[c.availability]}${c.finalBid?' · Precio final '+money(c.finalBid.price):''}${c.needsBroker"))

assert patched == 8, patched  # combined 4 + index 2 + suv 2
print('Final bids recorded for', ', '.join(f'{lot} ${price:,}' for lot, price, *_ in FINAL))
