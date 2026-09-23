"""Apply Copart public-page observations made on 2026-09-23 CDT."""
import json, re, html, copy, math
from pathlib import Path
p = Path(__file__).resolve().parents[1] / 'dist'
cars = json.loads((p/'combined80.json').read_text())
by = {c['id']: c for c in cars}
assert len(cars) == 87, 'One-time migration: do not apply twice'
# Each pair is an observed current bid, not a final sale price. - means not shown.
raw = '''89131265 -
73342175 300
66018206 0
67303746 0
61144086 175
62951896 -
57882066 0
67463736 0
67824346 0
68040146 0
52447896 -
66708186 725
59820326 100
66255136 0
68347506 0
68074766 1000
60234636 2100
62026146 0
85979535 0
67089566 0
67289766 0
56644356 -
61411886 0
60953876 -
62801036 175
67222806 225
67767886 0
57783336 125
63031466 3100
61707486 -
56681616 -
67181256 0
65809996 0
62560656 0
67360886 100
68021716 0
63509536 -
75971465 0
62295176 0
48953663 -
67092526 0
68544326 0
65709846 0
67201176 450
64200676 -
59114686 175
62966806 550
67126866 2800
85972145 -
58358206 0
61161096 -
68787566 0
68542176 0
68671526 0
61899356 -
60613726 -
60467806 -
50791176 0
65487846 -
64587966 -'''
bids = {i: None if b == '-' else int(b) for i,b in (s.split() for s in raw.splitlines())}
sold = {'60953876','64200676','65487846','64587966'}
ended = {'89131265'}
schedule = {}
for date, ids in [
 ('Tue. Sep 29, 2026 12:00 PM CDT','67463736 58358206'),
 ('Thu. Sep 24, 2026 12:00 PM CDT','66708186 60234636 65809996 67201176'),
 ('Mon. Sep 28, 2026 12:00 PM CDT','61411886'),
 ('Fri. Sep 25, 2026 12:00 PM CDT','62801036'),
 ('Wed. Sep 23, 2026 12:00 PM CDT','63031466 67126866'),
 ('Tue. Sep 22, 2026 12:00 PM CDT','60953876 64200676 89131265'),
 ('Mon. Sep 21, 2026 12:00 PM CDT','65487846 64587966')]:
 for i in ids.split(): schedule[i] = date
changed_titles = {'57882066','61411886','62560656','62966806'}
changes = []
for i,bid in bids.items():
 c = by[i]
 old = {k:c.get(k) for k in ['currentBid','availability','auction','titleDocument','currentCheckedAt']}
 c['previousCheck'] = old
 c['currentBid'] = bid
 c['availability'] = 'sold' if i in sold else 'ended' if i in ended else 'scheduled' if i in schedule else 'upcoming' if bid is None else 'future'
 c['auction'] = schedule.get(i, 'Upcoming lot' if bid is None else 'Future')
 c['currentCheckedAt'] = '2026-09-23'
 c['currentCheckWindow'] = '2026-09-23 CDT · Copart 공개 상세 직접 조회'
 c['currentSource'] = f'https://www.copart.com/lot/{i}'
 c['overBidCeiling'] = bid is not None and bid > c['maxBid']
 c['auctionNote'] = '현재 입찰가는 최종 낙찰가가 아닙니다. 판매 완료 차량의 최종 가격은 공개 화면에 미표시.'
 if i in ended: c['auctionNote'] = 'Sale ended · On approval: 판매자 승인 대기. 판매 완료나 최종 낙찰가는 미확인.'
 if i in changed_titles:
  c.update(title='Salvage',titleState='MO',titleDocument='MO - Salvage Certificate Of Title',needsBroker=True,eligibility='MO 소재 Salvage · 일반 개인은 브로커 필요 · 직접 구매 후보 제외',eligibilitySource='https://www.copart.com/Content/us/en/licensing/united-states/missouri')
 if any(c.get(k) != old[k] for k in old if k != 'currentCheckedAt'):
  changes.append({'id':i,'vehicle':c['vehicle'],'before':old,'after':{k:c.get(k) for k in old}})

# New discoveries: provisional budget ceilings, not appraisals or inspection results.
base = by['50791176']
new_data = [
 dict(id='69125816',vehicle='2017 Toyota Corolla SE',region='KS',body='Sedan',yard='KC',location='KS - KANSAS CITY',title='Salvage',titleState='MO',titleDocument='MO - Salvage Certificate Of Title',vin='5YFBURHE5HP******',miles=122147,damage='Hail',seller='USAA',engine='1.8L 4 · Automatic · FWD',vinEngine='1.8L',currentBid=0,auction='Future',availability='future',sourceUpdated='09/18/2026 4:39 pm',maxBid=3000,copartFees=1000,salesTaxReserve=500,transportReserve=300,repairReserve=2500,roundedTotal=8000,image='0926/092d1b78d01c447796113a6d95293b18_hrs.jpg',inspection='유리·루프·센서, 냉간 시동, CVT 상태와 실제 수리 견적 확인 필요.'),
 dict(id='67610536',vehicle='2019 Buick Encore Preferred',region='MO',body='SUV',yard='STL',location='MO - ST. LOUIS',title='Clean',titleState='MO',titleDocument='MO - Certificate Of Title',vin='KL4CJASBXKB******',miles=99083,damage='Normal Wear',seller='공개 화면 미표시',engine='1.4L 4 · Automatic · FWD',vinEngine='1.4L',currentBid=0,auction='Fri. Sep 25, 2026 12:00 PM CDT',availability='scheduled',sourceUpdated='09/22/2026 5:12 pm',maxBid=3000,copartFees=1000,salesTaxReserve=500,transportReserve=900,repairReserve=3000,roundedTotal=9100,image='0926/93f2106ab5b84228a1e76897ede6426b_hrs.jpg',inspection='Normal Wear는 무고장 보증이 아닙니다. 냉각계·누유·터보·변속기 진단과 시운전 필요.'),
 dict(id='66032736',vehicle='2022 Subaru Crosstrek Premium',region='KS',body='SUV',yard='KC',location='KS - KANSAS CITY',title='Salvage',titleState='KS',titleDocument='KS - Cert Of Title-salvage',vin='JF2GTAPC8N8******',miles=66913,damage='Hail',seller='공개 화면 미표시',engine='2.0L 4 · Automatic · AWD',vinEngine='2.0L',currentBid=150,auction='Thu. Sep 24, 2026 12:00 PM CDT',availability='scheduled',sourceUpdated='09/21/2026 3:32 pm',maxBid=4000,copartFees=1200,salesTaxReserve=600,transportReserve=350,repairReserve=3000,roundedTotal=9900,image='0826/48e95be9dac84d86aa65eca5a080010c_hrs.jpg',inspection='유리·루프·안전 센서, AWD·변속기 및 실제 수리 견적 확인 필요. 판매자 최소가 미충족, 상한 이하 낙찰 보장 없음.')
]
new_cars=[]
for rank, d in enumerate(new_data,88):
 c=copy.deepcopy(base)
 for key in ['previousCheck','auctionNote']: c.pop(key,None)
 img=d.pop('image');c.update(d)
 c.update(rank=rank,isNew=True,firstObservedAt='2026-09-23',currentCheckedAt='2026-09-23',currentCheckWindow='2026-09-23 CDT · Copart 공개 상세 직접 조회',overBidCeiling=False,needsBroker=False,titleAbsent=False,vinTrim='미확인',condition='Run and Drive',saleType='Minimum bid' if c['id']=='66032736' else 'Pure sale' if c['id']=='69125816' else '미표시',sellerNote='Copart 공개 상세 기준',eligibility=('KS Salvage' if c['region']=='KS' else 'MO Clean')+' 일반 규정 해당 · 본인 계정 Eligibility 미확인',photos=[{'path':'https://cs.copart.com/v1/AUTH_svc.pdoc00001/ids-c-prod-lpp/'+img}],photoFinding='Copart 대표 사진 링크 · 전체 사진 평가는 수행하지 않음',evidence='기본 정보 직접 조회 · 사진·엔진음·VIN 이력 정밀 평가 전',audioAssessment='직접 청취하지 못함',budgetNote='임시 예산 배분이며 수리 견적·최종 수수료가 아닙니다. 입찰 상한 이하 낙찰 및 실차 진단이 조건이며, 우박 차량의 전체 외관 복원은 제외합니다.',url='https://www.copart.com/lot/'+c['id'],currentSource='https://www.copart.com/lot/'+c['id'])
 assert math.ceil(sum(c[k] for k in ['maxBid','copartFees','salesTaxReserve','transportReserve','repairReserve','registrationInspectionReserve','membershipReserve','prepurchaseInspectionReserve'])/100)*100==c['roundedTotal']<=10000
 cars.append(c);by[c['id']]=c;new_cars.append(c)
labels={'sold':'판매 완료 (Sold)','ended':'경매 종료 · 판매자 승인 대기','scheduled':'경매 예정','future':'Future · 날짜 미정','upcoming':'Upcoming · 아직 입찰 불가'}
def state(c):
 bid='미표시' if c['currentBid'] is None else f'${c["currentBid"]:,}'
 caution=' · 개인 직접 구매 제외 (브로커 필요)' if c.get('needsBroker') else ' · 입찰 상한 초과' if c['overBidCeiling'] else ''
 return f'<span class="current-state{ " warning" if caution or c["availability"] in ["sold","ended"] else ""}">{labels[c["availability"]]}{caution}<br>현재 입찰 {bid} · 조회 9/23</span>'
def current_info(c):
 return f'<p class="current-info"><b>2026-09-23 Copart 직접 조회</b><br>경매: {html.escape(c["auction"])}<br>타이틀: {html.escape(c["titleDocument"])}<br>{html.escape(c["eligibility"])}<br>{html.escape(c.get("auctionNote","현재 입찰가는 최종 낙찰가가 아닙니다."))}</p>'
def patch(m):
 a=m[0];i=re.search(r'id="lot-(\d+)"',a)[1]
 if i not in bids:return a
 c=by[i]
 if i in changed_titles:
  a=a.replace(c['previousCheck']['titleDocument'],c['titleDocument']).replace('MO Clean 일반 규정 해당 · 본인 계정 Eligibility 미확인',c['eligibility'])
  a=a.replace('<article ', '<article data-needs-broker="true" ',1)
 a=re.sub(r'data-availability="[^"]*"',f'data-availability="{c["availability"]}"',a)
 a=re.sub(r'data-over-budget="[^"]*"',f'data-over-budget="{str(c["overBidCeiling"]).lower()}"',a)
 a=re.sub(r'<span class="current-state[^\"]*">.*?</span>',lambda _:state(c),a,flags=re.S)
 if 'class="current-info"' in a:a=re.sub(r'<p class="current-info">.*?</p>',lambda _:current_info(c),a,flags=re.S)
 else:a=a.replace('<div class="detail">','<div class="detail">'+current_info(c),1)
 return a

def new_card(c):
 return f'''<article class="vehicle" id="lot-{c['id']}" data-region="{c['region']}" data-yard="{c['yard']}" data-body="{c['body']}" data-tier="2" data-name="{(c['vehicle']+' '+c['id']+' '+c['vin']).lower()}" data-mpg="0" data-cost="{c['roundedTotal']}" data-rank="{c['rank']}" data-new="true" data-availability="{c['availability']}" data-over-budget="false"><details><summary><span class="rank">＋</span><span class="carname"><b>{c['vehicle']}</b><small>{c['region']} · {c['body']} · {c['yard']} · {c['titleDocument']} · LOT {c['id']}</small><small class="damage-summary"><b>Primary damage:</b> {c['damage']}</small>{state(c)}<span class="status tier2">신규 · 정밀 점검 전</span></span><span class="metric"><small>주행거리</small>{c['miles']:,} mi</span><span class="metric"><small>복합 연비</small>미조회</span><span class="metric"><small>임시 입찰 상한</small>${c['maxBid']:,}</span><span class="metric"><small>조건부 총액</small><b>${c['roundedTotal']:,}</b></span><span class="metric market-median"><small>유사 경매 수집 평균</small><b>수집 기록 없음</b></span><span class="expand">＋</span></summary><div class="detail"><img src="{c['photos'][0]['path']}" alt="{c['vehicle']} Copart 대표 사진" loading="lazy"><div><h3>9월 23일 발견 후보 · 종합 순위 미평가</h3>{current_info(c)}<p>VIN: {c['vin']} · 전체 VIN 이력 미조회<br>Seller: {c['seller']}<br>{c['condition']} · {c['engine']}</p><p>입찰 ${c['maxBid']:,} + 수수료 적립 ${c['copartFees']:,} + 세금 적립 ${c['salesTaxReserve']:,} + 운송 ${c['transportReserve']:,} + 수리 적립 ${c['repairReserve']:,} + 등록·멤버십·점검 $700 = ${c['roundedTotal']:,}</p><p>{c['budgetNote']}</p><p>{c['inspection']}</p><p>{c['evidence']}</p><a href="{c['url']}" target="_blank" rel="noopener">Copart 매물 보기 ↗</a></div></div></details></article>'''
ko_note='<section class="current-notice"><h2>9월 23일 갱신 · 신규 후보 3대</h2><p>기존 60대를 직접 재조회했습니다. 4대의 판매 완료를 확인했고 Sentra 89131265는 경매 종료·판매자 승인 대기입니다. 미주리 Forte 57882066, Tucson 61411886, Encore 62560656, Bronco Sport 62966806은 Salvage 서류로 변경되어 개인 직접 구매 기본 보기에서 제외했습니다.</p><p>Corolla SE 69125816 · Encore 67610536 · Crosstrek 66032736을 추가해 총 90대 기록입니다. 새로 발견한 후보이며 최초 등록일은 미확인입니다. 신규 3대는 사진·엔진음·VIN 이력 정밀 평가 전이며 기존 순위와 별도로 표시합니다. 비용은 임시 예산입니다. 다른 차량은 카드별 조회일 기준입니다.</p><p><a href="copart-refresh-2026-09-23.json">오늘 변경 기록</a> · <a href="https://www.copart.com/Content/us/en/licensing/united-states/missouri">MO 개인 구매 규정</a> · 조회 당시 상태로 실시간 자동 갱신이 아닙니다.</p></section>'
for name in ['combined.html','index.html','suv.html']:
 t=(p/name).read_text();t=re.sub(r'<article\b.*?</article>',patch,t,flags=re.S)
 t=re.sub(r'<section class="current-notice">(.*?)</section>',lambda m:'<details class="current-notice"><summary>이전 갱신 기록</summary>'+m[1]+'</details>',t,flags=re.S)
 t=t.replace('<details class="current-notice">',ko_note+'<details class="current-notice">',1)
 if name=='combined.html':
  t=t.replace('</div><section class="method">',''.join(new_card(c) for c in new_cars)+'</div><section class="method">',1)
  t=t.replace('87대','90대').replace('추가 후보 7대','추가 후보 10대')
  t=t.replace("v==='watch'&&!['sold','ended'].includes(c.dataset.availability)","v==='watch'&&c.dataset.needsBroker!=='true'&&!['sold','ended'].includes(c.dataset.availability)")
  t=t.replace('판매 완료·종료 제외</option>','개인 구매 후보 · 판매 완료·브로커 필요 제외</option>')
 (p/name).write_text(t)
t=(p/'es.html').read_text().replace('20260921-refresh','20260923-refresh')
t=re.sub(r'<section class="current-notice">(.*?)</section>',lambda m:'<details class="current-notice"><summary>Actualización anterior</summary>'+m[1]+'</details>',t,flags=re.S)
es_note='<section class="current-notice"><h2>Actualización · 23 de septiembre · 3 candidatos añadidos</h2><p>60 vehículos revisados: 4 ventas confirmadas y un Sentra pendiente de aprobación. Cuatro lotes de Missouri cambiaron a Salvage y se excluyen de la vista inicial por requerir intermediario: 57882066, 61411886, 62560656 y 62966806.</p><p>90 registros en total. Nuevos: Corolla SE 69125816, Encore 67610536 y Crosstrek 66032736. Fecha de publicación original desconocida; fotos, audio e historial VIN sin evaluación detallada. Presupuestos provisionales, sin garantía de adjudicación por debajo del límite.</p></section>'
t=t.replace('<details class="current-notice">',es_note+'<details class="current-notice">',1).replace('87 vehículos','90 vehículos').replace('7 candidatos añadidos','10 candidatos añadidos')
t=t.replace("v==='watch'&&!['sold','ended'].includes(c.availability)","v==='watch'&&!c.needsBroker&&!['sold','ended'].includes(c.availability)")
t=t.replace("${saleLabels[c.availability]}","${saleLabels[c.availability]}${c.needsBroker?' · Requiere intermediario':''}")
t=t.replace('Excluir vendidos/terminados','Excluir vendidos/terminados y lotes que requieren intermediario')
(p/'es.html').write_text(t)
(p/'combined80.json').write_text(json.dumps(cars,ensure_ascii=False,indent=2)+'\n')
(p/'copart-current.json').write_text(json.dumps({'note':'Mixed observation dates; consult currentCheckedAt. Final sale prices were not publicly shown.','lots':[{k:c.get(k) for k in ['id','availability','currentBid','auction','titleDocument','needsBroker','currentCheckedAt','currentSource']} for c in cars]},ensure_ascii=False,indent=2)+'\n')
(p/'copart-refresh-2026-09-23.json').write_text(json.dumps({'checkedAt':'2026-09-23 CDT','existingChecked':list(bids),'changes':changes,'newCandidates':[c['id'] for c in new_cars],'searchScope':'First visible result pages: Kansas Toyota Corolla; Missouri clean SUV and sedan; Kansas salvage hail SUV. Not exhaustive.','notAdded':[{'id':'67914696','reason':'Title Absent; VIN/vehicle identity requires verification.'},{'id':'69570896','reason':'Title Absent; inspection pending.'}],'note':'Read-only observations of Copart public detail pages. New candidates have no full VIN, photo or audio assessment. Budget reserves are provisional.'},ensure_ascii=False,indent=2)+'\n')
for name in ['combined.html','index.html','suv.html','es.html']:
 t=(p/name).read_text()
 t=re.sub(r'<details class="current-notice">.*?</details>',lambda m:m[0].replace('총 90대','총 87대').replace('90 vehículos','87 vehículos'),t,flags=re.S)
 t=t.replace('현재 경매 상태는 2026-09-16 직접 조회했습니다.','현재 경매 상태는 카드별 조회일 기준이며, 최근 재조회일은 2026-09-23입니다.').replace('현재 판매 상태 확인: 2026-09-16.','최근 판매 상태 확인: 2026-09-23 (카드별 조회일 참조).')
 t=t.replace('먼저 볼 차: Forte · Corolla · HR-V','기존 순위 평가 · 당시 기준 (판매 상태는 아래 카드 참조)').replace('COPART · KANSAS + MISSOURI · 2026.09.16','COPART · KANSAS + MISSOURI · 2026.09.23')
 t=t.replace('16 SEP 2026','23 SEP 2026').replace('80 vehículos anteriores y 6 candidatos añadidos','80 vehículos originales y 10 candidatos añadidos')
 t=t.replace('운송 $350 + 수리 적립 $3,000 + 등록·멤버십·점검 $700 = $9,900','운송 $350 + 수리 적립 $3,000 + 등록·멤버십·점검 $700 = $9,850 (조건부 총액 $9,900으로 올림)')
 (p/name).write_text(t)
assert len(bids)==60 and len(cars)==90 and len(by)==90
assert (p/'combined.html').read_text().count('<article ')==90
assert all(by[i]['needsBroker'] for i in changed_titles)
print(f'Updated {len(bids)} existing lots; {len(changes)} changed; {len(new_cars)} added; total {len(cars)}')
