import json,re,html
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'dist';cars=json.loads((p/'combined80.json').read_text())
sold='54713756 62420466 65957186 85613475 42068106 55442176 65120686 64769036'.split();ended=['65487846','64587966'];bids={'68074766':1000,'68347506':0,'89131265':1150,'50791176':0,'73342175':300,'61144086':2100,'64200676':175,'58358206':300};ids=set(sold+ended+list(bids));by={c['id']:c for c in cars}
for id in ids:
 c=by[id];c['previousCheck']={k:c.get(k) for k in ['currentBid','availability','auction','currentCheckedAt']};c['currentCheckedAt']='2026-09-21';c['currentCheckWindow']='2026-09-21 CDT · Copart 직접 조회';c['currentBid']=bids.get(id);c['availability']='sold' if id in sold else 'ended' if id in ended else 'scheduled' if id in ['89131265','64200676','58358206'] else 'future';c['overBidCeiling']=c['currentBid'] is not None and c['currentBid']>c['maxBid'];c['auctionNote']='Copart 2026-09-21 직접 조회. 판매 완료 차량의 최종 낙찰가는 공개 화면에서 미확인.'
 if id in ['64200676','58358206','89131265']:c['auction']='Tue. Sep 22, 2026 12:00 PM CDT'
 if id in ended:c['auction']='Mon. Sep 21, 2026 12:00 PM CDT'
(p/'combined80.json').write_text(json.dumps(cars,ensure_ascii=False,indent=2)+'\n')
labels={'sold':'판매 완료 (Sold)','ended':'경매 종료 · 판매 결과 미확인','scheduled':'경매 예정','future':'Future · 날짜 미정'}
def patch(m):
 a=m[0];id=re.search(r'id="lot-(\d+)"',a)[1]
 if id not in ids:return a
 c=by[id];bid='미표시' if c['currentBid'] is None else f'${c["currentBid"]:,}'
 a=re.sub(r'data-availability="[^"]*"',f'data-availability="{c["availability"]}"',a);a=re.sub(r'data-over-budget="[^"]*"','data-over-budget="false"',a)
 a=re.sub(r'<span class="current-state[^\"]*">.*?</span>',lambda _:f'<span class="current-state">{labels[c["availability"]]}<br>현재 입찰 {bid} · 조회 9/21</span>',a,flags=re.S)
 a=re.sub(r'<p class="current-info">.*?</p>',lambda _:f'<p class="current-info"><b>2026-09-21 Copart 직접 조회</b><br>{labels[c["availability"]]} · 현재 입찰 {bid}<br>경매: {html.escape(c["auction"])}<br>타이틀: {html.escape(c["titleDocument"])}<br>본인 계정 구매 자격 미확인 · 현재 입찰가는 최종 낙찰가가 아닙니다.</p>',a,flags=re.S)
 return a
for name in ['combined.html','index.html','suv.html']:
 t=(p/name).read_text();t=re.sub(r'<article\b.*?</article>',patch,t,flags=re.S)
 # Previous update notices are historical snapshots; collapse them to avoid contradictory current totals.
 t=re.sub(r'<section class="current-notice">([\s\S]*?)</section>',lambda m:'<details class="current-notice"><summary>이전 갱신 기록</summary>'+m[1]+'</details>',t)
 note='<section class="current-notice"><h2>9월 21일 부분 갱신</h2><p>18대 재조회: 8대 판매 완료 추가 확인, 2대 종료·결과 미확인. 판매 완료·종료 차량은 통합 목록 기본 보기에서 숨깁니다. 재조회하지 않은 차량은 카드에 표시된 이전 조회일 기준입니다. 신규 후보는 9월 20일 추가한 Corolla LE를 포함해 총 87대이며, 오늘 새 차량을 추가하지 않았습니다.</p></section>'
 t=t.replace('<details class="current-notice">',note+'<details class="current-notice">',1);(p/name).write_text(t)
t=(p/'es.html').read_text().replace('20260920-refresh','20260921-refresh');t=re.sub(r'<section class="current-notice">([\s\S]*?)</section>',lambda m:'<details class="current-notice"><summary>Actualización anterior</summary>'+m[1]+'</details>',t);t=t.replace('<details class="current-notice">','<section class="current-notice"><h2>Actualización parcial · 21 de septiembre</h2><p>18 vehículos revisados: 8 ventas adicionales confirmadas y 2 subastas terminadas sin resultado confirmado. Los demás conservan su fecha anterior. 87 vehículos; sin candidatos nuevos hoy.</p></section><details class="current-notice">',1);(p/'es.html').write_text(t)
(p/'copart-current.json').write_text(json.dumps({'note':'Mixed observation dates; consult currentCheckedAt for each lot.','lots':[{k:c.get(k) for k in ['id','availability','currentBid','auction','titleDocument','currentCheckedAt','currentSource']} for c in cars]},ensure_ascii=False,indent=2)+'\n')
assert len(ids)==18 and len(cars)==87
print('18 lots updated; 8 new sold, 2 ended; 87 total.')
