import json,re
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'dist';target='68074766'
d=json.loads((p/'auction-comps.json').read_text())
rows=[]
for lot,vin,price,date,miles,damage,drive,location,state,source in [
 ('57262816','5N1AT3CA7MC818939',6600,'2026-08-31',98879,'Hail','FWD','Cleveland West, OH, USA','OH','https://finalbid.vin/en/nissan/rogue/2021/copart-57262816-5N1AT3CA7MC818939'),
 ('55154406','JN8AT3CA2MW000106',4650,'2026-09-14',60639,'Front end + Side','FWD','Houston East, TX, USA','TX','https://cararam.com/en/nissan/rogue/2021/copart-55154406-JN8AT3CA2MW000106'),
 ('60924086','5N1AT3CB9MC696092',5800,'2026-08-28',40572,'Side + Rear end','AWD','Des Moines, IA, USA','IA','https://cararam.com/en/nissan/rogue/2021/copart-60924086-5N1AT3CB9MC696092')]:
 rows.append(dict(targetLot=target,lot=lot,vin=vin,vehicle='2021 Nissan Rogue SL',price=price,date=date,miles=miles,damage=damage,title='Salvage',condition='Run & drive',location=location,state=state,source=source,checkedAt='2026-09-17',reserveMet='Yes',status='Sold',trim='SL',engine='2.5L',drive=drive,targetRegion='KS',targetYard='KC',included=drive=='AWD',exclusion='',flags=['driveDifferent'] if drive=='FWD' else [],damageMatch=damage=='Hail',mileageDifference=miles-73630,similarity='reference'))
d['comparables']=[r for r in d['comparables'] if r['targetLot']!=target]+rows
d['summaries']=[s for s in d['summaries'] if s['targetLot']!=target]+[dict(targetLot=target,vehicle='2021 Nissan Rogue SL',count=1,records=3,median=None,min=5800,max=5800,bidCeiling=4600,ceilingMinusMedian=None)]
d['uniqueRecords']=len({r['source'] for r in d['comparables']});d['checkedAt']='2026-09-17'
(p/'auction-comps.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
cars=json.loads((p/'combined80.json').read_text());c=next(c for c in cars if c['id']==target)
c.update(comparisonAverage=sum(r['price'] for r in rows)/3,comparisonAverageCount=3,comparisonSampleCount=1,comparisonMedian=None,comparisonRecords=3,comparisonCheckedAt='2026-09-17')
(p/'combined80.json').write_text(json.dumps(cars,ensure_ascii=False,indent=2)+'\n')
for name in ['combined.html','suv.html']:
 t=(p/name).read_text()
 def patch(m):
  a=m[0]
  if 'id="lot-'+target+'"' not in a:return a
  a=re.sub(r'<span class="metric market-median">.*?</span>','<span class="metric market-median"><small>유사 경매 수집 평균</small><b>$5,683</b><small>수집 3건 · 수수료 제외</small></span>',a,flags=re.S)
  if 'data-target="'+target+'"' not in a:a=a.replace('</article>','<div class="auction-slot" data-target="'+target+'" data-lang="ko"></div></article>')
  return a
 (p/name).write_text(re.sub(r'<article\b.*?</article>',patch,t,flags=re.S))
t=(p/'auction-records.js').read_text().replace('FinalBid의 제3자 공개 기록','FinalBid·Cararam의 제3자 공개 기록').replace('Registros públicos de FinalBid','Registros públicos de FinalBid y Cararam').replace("fetch('auction-comps.json')","fetch('auction-comps.json?v=20260917-rogue', {cache:'no-store'})")
(p/'auction-records.js').write_text(t)
t=(p/'es.html').read_text().replace('20260916-owner-results','20260917-rogue');(p/'es.html').write_text(t)
assert len(rows)==3 and round(c['comparisonAverage'])==5683
assert len({r['vin'] for r in rows})==3
assert 'data-target="68074766"' in (p/'combined.html').read_text()
print('Three unique Rogue SL sold records; average $5,683.33; mean includes FWD references.')
