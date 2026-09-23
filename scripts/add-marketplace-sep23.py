"""Build the 2026-09-23 Facebook Marketplace snapshot compared with the Copart lots.

Search: Overland Park, KS, 40 mi, $4,000-$7,500, Cars & Trucks, newest first. 717 listings
were read; the rows below are same-model matches for the Copart lots (model year 2008+,
posted within 180 days) plus the clean-title picks and warnings from the same scan. Title,
mileage and notes come from each listing's detail page as stated by the seller.
"""
import json
from pathlib import Path

p = Path(__file__).resolve().parents[1] / 'dist'
out = p / 'marketplace-2026-09-23.json'
assert not out.exists(), 'One-time snapshot: do not rebuild over the published file'

# id|year|model|trim|price|miles|city|days since posted|title|flags|note
raw = '''1097175889929500|2010|Toyota Corolla|S|7400|164629|Lawrence, KS|0|unknown||
1968531700475662|2007|Toyota Corolla|S|5300|121466|Kansas City, KS|32|clean|avoid|제목은 2020년식이지만 VIN·설명은 2007년식
900758743097756|2012|Toyota Corolla|LE|6500|135000|Mission, KS|44|rebuilt||Kansas rebuilt 타이틀
1779022579947735|2017|Toyota Corolla|LE Eco Plus|7200|140000|Lawrence, KS|33|unknown||설명 없음
1885362032628617|2016|Toyota Camry|SE|6950|149000|Shawnee, KS|1|rebuilt|dealer|$2,500 다운페이 할부 광고
1603029057929982|2011|Toyota Camry|XLE Hybrid|6500|175851|Shawnee, KS|2|unknown||앞유리 금·작은 덴트
1102205642338739|2012|Toyota Camry|XLE|5350|185000|Kansas City, MO|21|clean|avoid|변속기 떨림 기재 · 제목 2013, VIN 2012
1376716494064377|2012|Toyota Camry|LE|5450|213751|Lenexa, KS|17|clean||
2007598423288238|2009|Toyota Camry|LE|4550|176000|Olathe, KS|21|unknown||최근 정비·새 타이어 기재
1019552367777131|2014|Toyota Camry|Hybrid LE|7200|198100|Kansas City, MO|25|clean||하이브리드 배터리 양호 기재
1257399176464936|2011|Toyota Camry|Hybrid|6000|177000|Kansas City, MO|30|clean|dealer|AS IS · 임시번호판 제공
1493985622497828|2014|Toyota Camry|L|6750|248541|Kansas City, KS|57|clean||
4508235036092160|2011|Toyota Camry|Hybrid LE|4500|239000|Kansas City, MO|65|clean||
987905757223492|2008|Toyota Camry|LE|5000|155963|Independence, MO|122|clean||
2531179250660814|2011|Honda Civic|LX|5250|147000|Overland Park, KS|6|clean|pick|이전 소유자 2명
1444300280954238|2015|Honda Civic|LX|7450|170750|Kansas City, MO|2|clean|pick|AutoCheck 무사고 기재
1127453399630236|2012|Honda Civic|Si|7300|142300|Blue Springs, MO|0|clean||6단 수동
1533137581901693|2012|Honda Civic|LX|6900|92000|Lawrence, KS|2|rebuilt|dealer|Lawrence autosales 판매
1034404035873380|2011|Honda Civic|EX|7500|172000|Olathe, KS|36|clean||
29345546845032749|2009|Honda Accord||5500|152000|Kansas City, KS|1|clean||
2316007052545773|2017|Honda Accord|Sport SE|7200|215000|Ottawa, KS|18|unknown||대부분 고속도로 주행 기재
3833552373462627|2010|Honda CR-V|EX|6250|178000|Kansas City, MO|1|clean||
1626949912166922|2013|Honda CR-V|EX AWD|7500|155000|Independence, MO|2|unknown||설명 없음
1572138048046451|2011|Honda CR-V|SE AWD|6900|135000|Lawrence, KS|2|rebuilt|dealer|Lawrence autosales 판매
1123251680380568|2013|Honda CR-V|EX-L|5000|218000|Independence, MO|0|unknown||
1120432017339805|2008|Honda CR-V|EX-L|5800|201000|Overland Park, KS|8|unknown||
1910649396580980|2015|Kia Forte||4200|94000|Independence, MO|9|clean||30일 임시번호판
1376695870811656|2017|Kia Forte|LX|5400|105121|Kansas City, MO|16|rebuilt||
927712493106819|2016|Kia Forte|LX|5900|135000|Kansas City, KS|32|clean||도난방지 업그레이드 완료 기재
4626988640878071|2019|Kia Forte|LXS|5000|216911|Kansas City, MO|9|unknown||
1769093670949216|2016|Kia Forte|Koup SX|4800|156100|Kansas City, MO|20|clean||쿠페 · SC 타이틀
2065682490723452|2017|Kia Sorento||7200|112000|Olathe, KS|23|rebuilt||
1149599788007713|2015|Kia Sorento|LX|4000|163000|Kansas City, MO|21|rebuilt||우박 이력 · 3열
1712110024247611|2015|Kia Sportage||6200|142000|Shawnee, KS|6|clean||무사고 기재 · 새 타이어·배터리
1155406217443412|2019|Hyundai Elantra|SEL|5500|98000|Kansas City, MO|1|rebuilt||
1052746570727764|2016|Hyundai Elantra|GL|5500|121000|Kansas City, KS|1|unknown||
28342256735436483|2017|Hyundai Elantra|Value Edition|6500|157000|Overland Park, KS|2|unknown||
2349700349173390|2019|Hyundai Elantra|Blue|6900|113800|Shawnee, KS|2|salvage||
858492397257790|2018|Hyundai Elantra|SE|6500|137900|Kansas City, MO|8|clean||
1750608366172357|2016|Hyundai Elantra|Limited|5500|156178|Overland Park, KS|5|clean||
1688424999173151|2016|Hyundai Elantra|GT 해치백|6350|83500|Lawrence, KS|125|rebuilt|dealer|Lawrence autosales 판매
1048322144871640|2016|Nissan Versa||4199|130000|Overland Park, KS|1|clean||
1117858210678572|2013|Nissan Sentra|SR|6500|90000|Kansas City, MO|6|clean||
1016973024715398|2016|Nissan Sentra|S|7000|108000|Stilwell, KS|12|clean||설명 없음
1534917801178992|2013|Nissan Sentra|SE|5500|80500|Grandview, MO|31|unknown||변속기 교체 기재
2237200970452290|2018|Nissan Sentra|SV|5995|155293|Lee's Summit, MO|12|clean||
1425745836284127|2010|Nissan Sentra||4000|139000|Roeland Park, KS|21|clean||설명엔 $3,800 OBO
1449751223658593|2015|Nissan Sentra|S|5250|144000|Mission, KS|47|unknown||
1768952064263761|2015|Nissan Sentra|SV|5000|171000|Independence, MO|87|unknown||
1072487642163672|2013|Nissan Altima|2.5 S|4900|144000|Raytown, MO|0|clean||
1511687240976391|2015|Nissan Altima|2.5 S|7500|93295|Overland Park, KS|28|clean||
1001133539605768|2019|Nissan Altima||7100|188551|Lenexa, KS|16|unknown||
1271936091612158|2017|Nissan Altima|2.5 SV|7000|150000|Kansas City, KS|38|unknown||설명엔 $7,500 OBO
1037879258729078|2017|Nissan Altima|2.5 S|5500|175345|Independence, MO|73|clean||
1488285219430263|2011|Nissan Altima|2.5|5900|124160|Kansas City, KS|117|clean|dealer|
1434183585347089|2016|Nissan Rogue|S AWD|6950|129000|Lenexa, KS|15|rebuilt||
4407614039493495|2016|Nissan Rogue|SV|5000|175000|Leawood, KS|3|unknown||
1041581515592158|2010|Toyota RAV4|Sport AWD|6900|152000|Olathe, KS|1|clean|pick|가죽시트·선루프
1867149474694675|2008|Toyota RAV4|Base|6599|207000|Kansas City, KS|1|clean||
879473601511100|2009|Toyota RAV4|Limited AWD|7499|150000|Kansas City, MO|64|clean|dealer|3개월 보증·할부 광고
1399491058820833|2010|Subaru Forester|2.5X Limited|5500|143000|Kansas City, MO|2|clean|pick|타이밍벨트 교체 기재
4426151627634480|2011|Subaru Outback||6500|144700|Kearney, MO|2|unknown||사슴 충돌 수리 이력
4005145136456246|2011|Subaru Outback||6487|182431|Kansas City, MO|2|unknown||
1787960935632896|2008|Mitsubishi Outlander|SE|6000|130000|Liberty, MO|10|unknown||
1052480560517969|2014|Mitsubishi Outlander Sport|SE|6500|127748|Pleasant Valley, MO|39|clean|dealer|할부 광고
2263524191261748|2014|Mazda3|Grand Touring|6500|141000|Kansas City, KS|2|rebuilt||경미한 우박으로 rebuilt 기재
1336600561563850|2015|Mazda3|i Touring|5900|89000|McLouth, KS|48|unknown||사이드미러 테이프·브레이크 교체 예정
4521266154816850|2016|Mazda6|Sport|7500|182782|Prairie Village, KS|40|clean||작은 녹·덴트
1568156234942061|2016|Mazda6|i Sport|7500|179388|Kansas City, MO|61|unknown||
2496821574135053|2013|Ford Edge|Limited|4500|187145|Kansas City, MO|1|unknown||워터펌프·타이밍체인 교체 기재
2107391383317546|2015|Ford Edge|SEL AWD|4500|168000|Kansas City, KS|2|unknown||
978671551916040|2013|Ford Edge|SEL|5600|175100|Kansas City, MO|8|clean||
2219847085619205|2018|Ford Taurus|SEL|5000|98000|Pleasant Hill, MO|2|unknown|avoid|내부 워터펌프 냉각수 누수 · 판매자 수리 안 함
1108200951667891|2016|Ford Taurus|SEL|5895|136791|Kansas City, MO|1|unknown|dealer|현금 전용 매장
1821944399156473|2014|Ford Taurus|Limited|6500|153000|Overland Park, KS|9|clean||클린 CarFax 기재
1579215406999740|2013|Ford Taurus|SEL|4300|182008|Kansas City, MO|24|unknown||
2503479173416149|2018|Ford Taurus|Police Interceptor AWD|5900|148583|Platte City, MO|61|unknown|dealer|경찰차 출신
2203761943814748|2014|Ford Fusion|Titanium|6995|171433|Kansas City, MO|1|clean|dealer|3개월 보증·임시번호판
2036845277035801|2018|Ford Fusion|SE 1.5T|6450|143910|Kansas City, KS|2|clean||OBO
2165370024327815|2016|Ford Fusion|SE|6500|118700|Independence, MO|7|clean|pick|작은 덴트 · 안전검사 예정 기재
1379264174193590|2016|Ford Fusion|Titanium AWD|6950|167000|Parkville, MO|0|clean||
1757114505333053|2012|Ford Fusion|S Hybrid|4500|160758|Independence, MO|5|clean||새 타이어·배터리
2197672464146312|2017|Ford Fusion|Titanium Hybrid|5600|198000|Lee's Summit, MO|7|clean||
2566962167153302|2014|Ford Fusion|SE|6995|199914|Liberty, MO|7|clean||
1524117896152046|2015|Ford Fusion||5500|166000|Kansas City, MO|10|clean||122K mi에서 엔진 교체 기재
1784187162731713|2012|Ford Fusion|SE|4250|121307|Kansas City, MO|10|clean|dealer|할부 광고 · MO 검사
1435993505112931|2017|Ford Fusion|SE 1.5T|7500|141740|Smithville, MO|11|clean||
1008254835597139|2014|Ford Fusion|S|6400|161900|Olathe, KS|13|clean||앞 펜더 덴트
1381925430256317|2017|Ford Fusion|SE 2.0|5500|172213|Kansas City, MO|19|clean|dealer|엔진 상부 오일 누유 기재
2879413779100971|2013|Ford Fusion|SE 1.6T|4200|155280|Eudora, KS|32|unknown||수리 필요 항목 기재
2123609051903529|2017|Ford Fusion||6999|139414|Kansas City, MO|39|unknown||설명 없음
1969448280437175|2016|Ford Fusion||6500|141000|Kansas City, MO|40|unknown||
2089308668331562|2016|Ford Fusion|S|7500|110000|Kansas City, MO|62|rebuilt||이전 salvage 기재
1076424295186918|2013|Ford Fusion|SE|4450|185000|Kansas City, MO|2|clean|dealer|임시번호판
1450555276836555|2013|Ford Fusion|SE 1.6|4600|178000|Lee's Summit, MO|86|unknown||
2047696652769196|2018|Ford Fusion|S|5400|200000|Independence, MO|133|unknown||
1108133621693125|2017|Ford Explorer||7000|149585|Kansas City, MO|2|clean||3열 · 앞쪽 외관 손상
2588932998201080|2014|Ford Explorer|Limited 4WD|4850|205977|Kansas City, KS|1|clean||3열
2396517687545591|2019|Ford Escape|SE|7450|108536|Lee's Summit, MO|5|clean|pick|
1426867219349197|2018|Ford Escape||7000|106586|Kansas City, KS|5|unknown||
1635862734832453|2014|Ford Escape|SE|5850|139920|Kansas City, MO|4|clean||OBO
1658449049228851|2017|Ford Escape|SEL|4500|150000|Kansas City, MO|0|clean||
4469384283323395|2014|Ford Escape|Titanium|6000|135000|Kansas City, MO|19|unknown||
1115159097510150|2016|Ford Escape|Titanium AWD|6750|169000|Kansas City, MO|24|clean||1인 소유·정비기록 기재
2233206210789425|2018|Ford Escape|SE 1.5T|6899|148300|Kansas City, MO|66|clean||
4151413991816410|2018|Ford Escape|SE AWD|7250|117500|Olathe, KS|159|clean||클린 CarFax·2인 소유 기재
1108630611611823|2013|Chevrolet Traverse|LS AWD|5300|139000|Overland Park, KS|1|unknown||
1775342606925663|2011|Chevrolet Traverse|LT|6500|205000|Lee's Summit, MO|1|unknown||조수석 창문 모터 고장
1573464457851757|2011|Chevrolet Traverse|LT|6500|205000|Blue Springs, MO|1|clean||에어컨 고장 기재
2206855993507497|2016|Chevrolet Malibu|1.5T|7200|92000|Parkville, MO|12|clean|dealer|TPMS 센서 교체 필요
1435821598403237|2018|Chevrolet Malibu|LS|5950|118715|Kansas City, MO|11|clean||우박 자국
3769663506507665|2018|Chevrolet Malibu|1LT|4750|203000|Kansas City, MO|1|clean||
2497474867412878|2020|Chevrolet Malibu|LT|6900|167380|Olathe, KS|6|clean|dealer|
1447474873921781|2019|Chevrolet Malibu|LT|7500|198000|De Soto, KS|45|unknown||설명엔 $10,000
1081490321462908|2008|Chevrolet Impala|LT|4000|280000|Lee's Summit, MO|1|clean||타이어 교체 필요 기재
1003381872762872|2019|Chevrolet Equinox|LT|7400|138431|Independence, MO|2|unknown||앞유리 돌 파손
914022414837034|2014|Chevrolet Equinox|LT|5000|137000|Stilwell, KS|2|clean||외부 녹
1171015368747603|2016|Chevrolet Equinox|LT|6000|139000|Kansas City, MO|42|clean||TPMS·에어백 센서 경고등
1438064651586594|2010|Chevrolet Equinox||4100|169000|Independence, MO|1|unknown||설명 없음
1766417247945895|2016|Chevrolet Cruze|LS|6500|113000|Lenexa, KS|1|clean|pick|클린 CarFax 기재 · 설명은 2018년식
1779801873355227|2014|Chevrolet Cruze|LT|4995|100898|Kansas City, MO|1|clean||
1381762960116684|2018|Chevrolet Cruze|LS|6900|102774|Shawnee, KS|22|rebuilt||
1763137911554088|2014|Chevrolet Cruze|2LT|5499|131000|Kansas City, MO|5|clean|dealer|
1268608666342565|2015|Chevrolet Cruze|Diesel|5400|190000|Kansas City, MO|9|clean||
1419472196948957|2014|Chevrolet Cruze|LT|4900|125000|Independence, MO|9|clean||
2126151864654683|2016|Chevrolet Cruze|LT|4600|107000|Shawnee, KS|8|rebuilt||우박 rebuilt · 관용차 출신
3216397755210953|2016|Chevrolet Cruze|LT|5900|120000|Kansas City, MO|23|unknown||설명엔 $6,100
1789441822359293|2019|Buick Encore||6595|125470|Kansas City, MO|14|clean|pick|1인 소유 · MO 안전검사 포함
1585045313103793|2017|Buick Encore|Premium|6995|169000|Smithville, MO|2|clean||정비기록 32건 기재
3774959089347169|2017|Buick Encore|Preferred|4399|141571|Kansas City, MO|2|unknown||설명 없음
1026516683778015|2018|Jeep Renegade|Altitude|6350|118000|Kansas City, MO|10|rebuilt||펜더 손상 rebuilt
2208239950077363|2015|Jeep Renegade|Limited 4WD|6700|136000|Lenexa, KS|1|clean||클린 CarFax 기재
1100919889033528|2017|Jeep Renegade||5500|150000|Wellsville, KS|31|clean||헤드개스킷 교체 기재
1659973175753567|2017|Jeep Renegade|Latitude|6500|156000|Wellsville, KS|37|clean||테일램프 파손
1398883589084631|2012|Jeep Grand Cherokee|Laredo 4WD|4250|173000|Kansas City, MO|1|clean||
1649949616753460|2012|Jeep Grand Cherokee||5800|156120|Kansas City, MO|22|clean||
1646696987016003|2014|Hyundai Accent|GLS|4990|91000|Kansas City, MO|12|clean|pick|이전 소유자 2명
1532183214780246|2019|Kia Soul||6900|80443|Sugar Creek, MO|36|clean|pick|
1727066491705457|2016|Nissan Pathfinder|Platinum 4WD|7000|139000|Lawrence, KS|9|clean|pick|3열 · 두 번째 소유자
1578862983399889|2019|Dodge Grand Caravan|GT|6500|153919|Kansas City, MO|2|clean|pick|미니밴 · 임시번호판
38406012769047425|2010|Ford F-150|XLT V8 8ft|6400|146237|Lenexa, KS|24|clean|pick|픽업
1091016910124544|2014|Ford F-150|SuperCrew FX2|4500|176000|Kansas City, MO|36|unknown|avoid|기어 빠짐·에어컨 고장·경고등 기재
38481469934829977|2015|Kia Optima|EX|4500|100080|Grandview, MO|6|clean||
27640111288996281|2013|Kia Optima|EX|5700|68000|Olathe, KS|4|clean|avoid|사고 이력·엔진 경고등(O2 센서) 기재
970533682740389|2020|Kia Rio|LX|5000|137000|Olathe, KS|21|clean||
1082914647817789|2017|Hyundai Sonata||6300|147503|Kansas City, MO|1|clean||OBO
1359807689469047|2016|Hyundai Santa Fe Sport|2.4 AWD|6000|143112|Kansas City, MO|8|clean|dealer|보증·임시번호판
1802739624478574|2014|Volvo S60|T5|6800|120300|Riverside, MO|2|clean||작은 덴트
1642320947504282|2014|Volkswagen Jetta|2.0|5350|109150|Lone Jack, MO|9|clean||5단 수동
1601441718183824|2017|Jeep Cherokee|Latitude|6500|127000|Grandview, MO|21|clean||할부 가능 기재'''

listings = []
for line in raw.splitlines():
    i, year, model, trim, price, miles, city, days, title, flags, note = line.split('|')
    flags = set(filter(None, flags.split(',')))
    assert title in {'clean', 'rebuilt', 'salvage', 'unknown'} and flags <= {'pick', 'avoid', 'dealer'}, line
    listings.append(dict(id=i, year=int(year), model=model, vehicle=f'{year} {model} {trim}'.strip(),
                         price=int(price), miles=int(miles), city=city, days=int(days), title=title,
                         pick='pick' in flags, avoid='avoid' in flags, dealer='dealer' in flags, note=note))

# Longest first, so "Nissan Rogue Sport" never falls through to "Nissan Rogue".
MODELS = sorted('''Toyota Corolla|Toyota Camry|Toyota RAV4|Toyota Highlander|Honda Civic|Honda Accord|Honda CR-V|Honda HR-V
Kia Forte|Kia K4|Kia Sorento|Kia Sportage|Hyundai Elantra|Hyundai Tucson|Hyundai Kona|Nissan Versa|Nissan Sentra
Nissan Altima|Nissan Rogue Sport|Nissan Rogue|Subaru Legacy|Subaru Forester|Subaru Outback|Subaru Crosstrek
Mitsubishi Eclipse Cross|Mitsubishi Outlander Sport|Mitsubishi Outlander|Mazda3|Mazda6|Mazda CX-5|Ford Edge
Ford Taurus|Ford Fusion|Ford Explorer|Ford Escape|Ford Bronco Sport|Chevrolet Traverse|Chevrolet Malibu
Chevrolet Impala|Chevrolet Equinox|Chevrolet Cruze|Buick Envista|Buick Encore|Jeep Renegade|Jeep Grand Cherokee'''
                .replace('\n', '|').split('|'), key=len, reverse=True)
cars = json.loads((p / 'combined80.json').read_text())
lots = {}
for c in cars:
    name = c['vehicle'].split(' ', 1)[1]
    lots[c['id']] = next(m for m in MODELS if name == m or name.startswith(m + ' '))

data = dict(
    checkedAt='2026-09-23',
    source='Facebook Marketplace 공개 목록·상세 페이지 (로그인 상태에서 직접 조회)',
    search=dict(center='Overland Park, KS', radiusMiles=40, priceMin=4000, priceMax=7500,
                category='Cars & Trucks', scanned=717, minYear=2008, maxDays=180),
    costRule=dict(taxRate=0.10, registration=400, inspection=200, maintenance=500),
    listings=listings,
    lots=lots,
)
out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')

matched = [x for x in listings if x['model'] in set(lots.values())]
assert len({x['id'] for x in listings}) == len(listings) and len(lots) == len(cars) == 90
assert sum(x['pick'] for x in listings) == 13 and sum(x['avoid'] for x in listings) == 5
print(f'{len(listings)} listings, {len(matched)} same-model matches across {len({x["model"] for x in matched})} Copart models')
