import json,re,html,copy
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'dist';cars=json.loads((p/'combined80.json').read_text());by={c['id']:c for c in cars}
ids='54713756 66458476 66814326 65278226 68630226 73342175 66018206 67303746 61144086 62951896 57882066 67463736 67824346 68040146 52447896 66708186 59820326 66255136 68347506 89131265 62630566 68074766 68787566 68542176 68671526 61899356 60613726 60467806'.split()
bids=[6000,None,None,None,None,175,0,0,200,None,None,0,0,0,None,0,100,0,0,1150,None,1000,0,0,0,None,None,None]
for id,bid in zip(ids,bids):
 c=by[id];c['previousCheck']={k:c.get(k) for k in ['availability','currentBid','auction','currentCheckedAt']};c['currentBid']=bid;c['overBidCeiling']=bid is not None and bid>c['maxBid'];c['currentCheckedAt']='2026-09-20';c['currentCheckWindow']='2026-09-20 CDT · Copart 직접 조회'
 if id in ['66458476','66814326','65278226','68630226','62630566']:c['availability']='sold'
 if id=='89131265':c['availability']='scheduled';c['auction']='Tue. Sep 22, 2026 12:00 PM CDT'
 if id=='68671526':c['availability']='future';c['auction']='Future'
 c['auctionNote']='Copart 2026-09-20 직접 재조회. 현재 입찰가는 최종 낙찰가가 아닙니다.'
c=dict(id='50791176',vehicle='2021 Toyota Corolla LE',rank=87,isNew=True,region='KS',body='Sedan',yard='KC',title='Salvage',titleState='KS',titleDocument='KS - Cert Of Title-salvage',vin='5YFEPMAE3MP******',vinStatus='공개 VIN 뒷자리 가림 · 사양·이력 미조회',miles=86235,odometerStatus='Actual',damage='Hail',seller='USAA',sellerNote='Copart 공개 상세 표기',engine='1.8L 4 · Automatic · FWD',vinEngine='1.8L',vinTrim='미확인',condition='Run and Drive',auction='Future',availability='future',currentBid=0,maxBid=4000,copartFees=1000,salesTaxReserve=500,transportReserve=300,repairReserve=2500,roundedTotal=9000,registrationInspectionReserve=400,membershipReserve=100,prepurchaseInspectionReserve=200,titleAbsent=False,overBidCeiling=False,location='KS - KANSAS CITY',sublot='',saleType='Pure sale',mpgCombined=None,mpgCity=None,mpgHighway=None,mpgSource='',mpgNote='정확한 연비 사양 미조회',photos=[{'path':'https://cs.copart.com/v1/AUTH_svc.pdoc00001/ids-c-prod-lpp/0426/6504b3073a0b4565ad26616de01401ac_hrs.jpg'}],photoFinding='Copart 공개 대표 사진 링크. 이번 추가에서 전체 사진·엔진음은 평가하지 않았습니다.',evidence='매물 기본 정보 직접 확인 · 사진·엔진음·VIN 상세 이력 평가 전',inspection='우박·유리·센서·냉간 시동·CVT 진단과 실제 수리 견적 확인 필요.',tier=2,status='신규 · 정밀 점검 전',eligibility='KS Salvage 일반 규정 해당 · 본인 계정 Eligibility 미확인',comparisonAverage=None,comparisonAverageCount=0,comparisonMedian=None,comparisonSampleCount=0,comparisonRecords=0,currentCheckedAt='2026-09-20',currentCheckWindow='2026-09-20 CDT · Copart 직접 조회',sourceUpdated='09/02/2026 3:27 pm',url='https://www.copart.com/lot/50791176',currentSource='https://www.copart.com/lot/50791176',source='combined.html',audioAssessment='직접 청취하지 못함',budgetNote='입찰 상한 $4,000 + 수수료 임시 적립 $1,000 + 세금 임시 적립 $500 + 운송 $300 + 수리 $2,500 + 등록·멤버십·점검 $700 = $9,000. 확정 견적이 아니며 우박 전체 외관 복원은 제외.')
cars.append(c);by[c['id']]=c
(p/'combined80.json').write_text(json.dumps(cars,ensure_ascii=False,indent=2)+'\n')
labels={'future':'Future · 날짜 미정','upcoming':'Upcoming · 아직 입찰 불가','scheduled':'경매 예정','sold':'판매 완료 (Sold)','ended':'경매 종료 · 판매 결과 미확인','live':'경매 진행 표시'}
def live(c):
 bid='미표시' if c['currentBid'] is None else f"${c['currentBid']:,}"
 return f'<span class="current-state {"warning" if c["overBidCeiling"] or c["availability"]=="sold" else ""}">{labels[c["availability"]]}'+(' · 입찰 상한 초과' if c['overBidCeiling'] else '')+f'<br>현재 입찰 {bid} · 조회 9/20</span>'
def update(m):
 a=m[0];id=re.search(r'id="lot-(\d+)"',a)[1]
 if id not in ids:return a
 c=by[id];a=re.sub(r'data-availability="[^"]*"',f'data-availability="{c["availability"]}"',a);a=re.sub(r'data-over-budget="[^"]*"',f'data-over-budget="{str(c["overBidCeiling"]).lower()}"',a)
 a=re.sub(r'<span class="current-state[^\"]*">.*?</span>',lambda _:live(c),a,flags=re.S)
 a=re.sub(r'<p class="current-info">.*?</p>',lambda _:f'<p class="current-info"><b>Copart 현재 상태 · 2026-09-20 조회</b><br>{labels[c["availability"]]} · 현재 입찰 '+('미표시' if c['currentBid'] is None else f'${c["currentBid"]:,}')+f'<br>경매: {html.escape(c["auction"])}<br>타이틀: {html.escape(c["titleDocument"])}<br>Seller: {html.escape(c["seller"])}<br>{html.escape(c["eligibility"])}<br>현재 입찰가는 최종 낙찰가가 아닙니다.</p>',a,flags=re.S)
 return a
note='<section class="current-notice"><h2>9월 20일 부분 갱신 · 신규 후보 1대</h2><p>상위 22대와 기존 신규 후보 6대, 총 28대를 직접 재조회했습니다. 나머지는 카드에 표시된 기존 조회일 기준입니다. Corolla·Civic·Legacy·Forte 4대가 추가로 판매 완료됐고, Forte 54713756은 현재 $6,000으로 기존 상한을 초과했습니다. 2021 Corolla LE 50791176을 추가했습니다. 새로 발견한 후보이며 최초 등록일은 확인하지 않았습니다.</p></section>'
for f in ['combined.html','index.html','suv.html']:
 t=(p/f).read_text();t=re.sub(r'<article\b.*?</article>',update,t,flags=re.S);t=t.replace('<section class="current-notice">',note+'<section class="current-notice">',1)
 if f=='combined.html':
  card=f'''<article class="vehicle" id="lot-50791176" data-region="KS" data-yard="KC" data-body="Sedan" data-tier="2" data-name="2021 toyota corolla le 50791176" data-mpg="0" data-cost="9000" data-rank="87" data-new="true" data-availability="future" data-over-budget="false"><details><summary><span class="rank">＋</span><span class="carname"><b>2021 Toyota Corolla LE</b><small>KS · Sedan · KC · KS - Cert Of Title-salvage · LOT 50791176</small><small class="damage-summary"><b>Primary damage:</b> Hail</small>{live(c)}<span class="status tier2">신규 · 정밀 점검 전</span></span><span class="metric"><small>주행거리</small>86,235 mi</span><span class="metric"><small>복합 연비</small>미조회</span><span class="metric"><small>입찰 상한</small>$4,000</span><span class="metric"><small>조건부 총액</small><b>$9,000</b></span><span class="metric market-median"><small>유사 경매 수집 평균</small><b>수집 기록 없음</b></span><span class="expand">＋</span></summary><div class="detail"><img src="{c['photos'][0]['path']}" alt="2021 Corolla LE Copart 대표 사진" loading="lazy"><div><h3>9월 20일 추가 후보</h3><p>VIN: {c['vin']} · 전체 VIN 이력 미조회<br>Seller: USAA · Run and Drive · 1.8L · FWD<br>경매: Future · 날짜 미정</p><p>{c['budgetNote']}</p><p>{c['inspection']}</p><p>{c['evidence']}</p><p>{c['eligibility']}</p><a href="{c['url']}" target="_blank" rel="noopener">Copart 매물 보기 ↗</a></div></div></details></article>'''
  t=t.replace('</div><section class="method">',card+'</div><section class="method">',1).replace('86대','87대').replace('이번 추가 6대','추가 후보 7대')
 (p/f).write_text(t)
t=(p/'es.html').read_text().replace('20260917-rogue','20260920-refresh').replace('86 vehículos','87 vehículos').replace('6 candidatos nuevos','7 candidatos añadidos').replace(' · Consulta 16/9',' · Consulta ${c.currentCheckedAt}')
t=t.replace('<section class="current-notice">','<section class="current-notice"><h2>Actualización parcial · 20 de septiembre</h2><p>28 vehículos anteriores revisados y un Corolla LE 2021 añadido. Cuatro ventas confirmadas más. Los demás conservan su fecha de consulta anterior. Nuevo Corolla: límite provisional $4,000 y presupuesto $9,000, sin inspección completa ni historial VIN.</p></section><section class="current-notice">',1)
(p/'es.html').write_text(t)
assert len(cars)==87 and (p/'combined.html').read_text().count('<article ')==87
print('28 existing vehicles rechecked; one new Corolla candidate; 87 cards.')
