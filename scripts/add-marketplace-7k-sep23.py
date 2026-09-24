"""Add the 2026-09-23 second Facebook Marketplace pass: $7,000-$7,999 Cars & Trucks near Overland Park.

353 listings were read. Kept: passenger cars, SUVs, vans and pickups of model year 2008+, posted within
180 days, not already in the snapshot. Dropped trailers, golf carts, boats, motorcycles and a forklift,
one parts-only truck, and repeat posts of the same car (one post kept). Unlike the first pass, every
model is kept, not only models that match a Copart lot. Title and notes come from each detail page.
"""
import json
from pathlib import Path

p = Path(__file__).resolve().parents[1] / 'dist'
path = p / 'marketplace-2026-09-23.json'
d = json.loads(path.read_text())
assert d['search']['priceMax'] == 7500, 'One-time migration'

# id|year|model|trim|price|miles|city|days since posted|title|flags|note
raw = '''1701642304295465|2009|Acura TL|3.2|7500|137000|Kansas City, MO|120|clean||
1531142348420959|2010|Audi Q5|3.2 V6|7450|152987|Kansas City, KS|88|clean|dealer|
26900651019596290|2012|Audi Q5|2.0T Premium|7999|73395|Kansas City, KS|117|clean||
1283437270261870|2014|Audi Q7|3.0T Quattro Prestige|7500|150000|Raymore, MO|96|clean||7인승
1572049178053061|2014|BMW 3 Series|328i|7500|142114|Kansas City, MO|9|clean||
1543234184043110|2014|BMW 3 Series|320i|7100|90000|Kansas City, MO|126|unknown||
2008909159755417|2015|BMW 3 Series|320i|7500|149000|Liberty, MO|24|clean||최근 컨트롤암·타이어 교체
2650491418717310|2013|BMW 3 Series|328xi AWD|7500|127000|Kansas City, MO|8|clean|dealer|정비 이력 기재
1548388523690269|2012|BMW 5 Series|535i|7500|137000|Peculiar, MO|32|unknown||M 스포츠 부품 개조
1349246243693851|2015|BMW 5 Series|528i xDrive|7200|114328|Olathe, KS|2|clean||
1466246125536564|2014|BMW X1|xDrive28i|7250|99850|Kansas City, MO|87|clean||BMW 딜러 정비 기재
2068793950343781|2011|BMW X5|xDrive35i Premium|7900|158000|Lee's Summit, MO|140|unknown||워터펌프·라디에이터 교체
2171840670432951|2016|Buick Enclave|Premium AWD|7500|232000|Kansas City, MO|26|rebuilt||3열
2896369034075607|2017|Buick Encore|Preferred|7950|88000|Belton, MO|11|rebuilt|dealer|
1473944551156596|2012|Buick LaCrosse|Premium|7995|127000|Independence, MO|51|unknown||
1081544177716578|2011|Buick LaCrosse|CXL|7499|112827|Bonner Springs, KS|22|clean||
1246955173823576|2012|Buick Verano||7999|140265|Olathe, KS|166|clean||
1784163442697485|2014|Buick Verano|Convenience|7500|125846|Kansas City, KS|4|unknown||2인 소유 · 경미한 외관 흠
1101615202208736|2014|Cadillac ATS|2.0T Luxury|7000|124500|Overland Park, KS|21|unknown||새 타이어·브레이크 기재
4464042020589991|2011|Cadillac STS|3.6 V6|7600|89450|Shawnee, KS|35|unknown||
1893202784993584|2009|Chevrolet Silverado 1500|Extended Cab|7000|230019|Independence, MO|1|clean||변속기 교체 · 차체 녹
2119955908894142|2008|Chevrolet Silverado 2500HD|Crew Cab Duramax|7500|214000|Pleasant Hill, MO|1|unknown|avoid|림프 모드 경고 코드 반복(P0193·P0652)
1397818025890558|2014|Chevrolet Cruze|1LT|7300|119000|Kansas City, MO|16|rebuilt|dealer|
1737138417417720|2015|Chevrolet Cruze|LTZ|7000|160000|Kansas City, MO|64|clean||
1378837897753987|2019|Chevrolet Cruze|LS|7900|107696|Kansas City, KS|6|clean|dealer|할부 가능 기재
1037462112447162|2016|Chevrolet Cruze|Limited LT|7499|122174|Bonner Springs, KS|14|clean||
4049726355328370|2015|Chevrolet Equinox|LT AWD|7000|129334|Smithville, MO|20|clean||엔진 교체 기재
893678046935516|2017|Chevrolet Equinox|LT|7900|69685|Kansas City, MO|17|salvage||앞범퍼 손상
1260769629477071|2017|Chevrolet Equinox|LS|7900|69500|Shawnee, KS|22|salvage||후드·그릴 교체
2255388111983073|2019|Chevrolet Equinox|LT|7000|111000|Shawnee, KS|9|rebuilt||
2165146721066453|2019|Chevrolet Equinox||7999|125256|Kansas City, MO|39|clean|dealer|60일 임시번호판 · 할부 광고
1291520710702162|2020|Chevrolet Equinox|LT 1.5T|7995|186597|Kansas City, MO|51|unknown|dealer|
1098938982728214|2014|Chevrolet Impala|LT|7900|141581|Grandview, MO|1|clean|dealer|3개월 파워트레인 보증
27924396537155924|2011|Chevrolet Malibu|LTZ|7000|180000|Harrisonville, MO|60|clean||조수석 유리 금
1007332175655332|2013|Chevrolet Malibu|LS|7900|125028|Olathe, KS|0|clean||설명 없음 · 같은 차 2건 게시
1432138428345514|2016|Chevrolet Malibu||7500|160000|Grandview, MO|0|clean||
1089389543554635|2016|Chevrolet Malibu|LT|7995|160423|Grandview, MO|14|clean|dealer|할부 가능 기재
1514430817116503|2018|Chevrolet Malibu||7500|146000|Kansas City, KS|6|unknown||설명 없음
1859233765236956|2022|Chevrolet Malibu|LT|7699|148000|Kansas City, MO|1|clean||1인 소유
1088333007478245|2012|Chevrolet Silverado 1500|Crew Cab LT|7600|167000|Independence, MO|21|unknown||적재함 녹
1832471831096703|2015|Chevrolet Sonic||7995|106607|Lee's Summit, MO|27|unknown|dealer|
1401004008801123|2020|Chevrolet Sonic|LT|7900|91000|Kansas City, MO|6|clean||
978329124637973|2014|Chevrolet Tahoe||7700|148000|Kansas City, MO|7|clean||
1080837944882031|2009|Chevrolet TrailBlazer|SS AWD|7900|256000|Kansas City, KS|24|clean||로워링 개조
1440559224675642|2017|Chevrolet Traverse|LS|7100|119000|Kansas City, MO|10|clean||새 타이어·배터리
1057315497221202|2017|Chevrolet Traverse|LT AWD|7750|169741|Shawnee, KS|13|clean|dealer|할부 광고
1488067756365726|2019|Chevrolet Trax|LT|7900|122000|Independence, MO|46|clean||외관 손상
1404357475232639|2020|Chevrolet Trax|LS|7999|63500|Olathe, KS|5|clean|pick|같은 차 2건 게시
2428321840974364|2015|Chrysler 200|C 3.6 AWD|7999|128941|Bonner Springs, KS|151|clean||
1580347013472256|2012|Chrysler 300||7000|167789|Independence, MO|25|clean||연료펌프 교체
2005162626849315|2019|Dodge Grand Caravan|SXT|7350|101722|Shawnee, KS|4|salvage||우박 손상
1473847984648999|2017|Dodge Dart||7997|102885|Kansas City, KS|14|unknown||설명은 2015년식
1382537763952246|2015|Dodge Durango|SXT AWD|7900|190412|Mission, KS|5|clean||
3552886561540520|2018|Dodge Durango||7500|134000|Lawrence, KS|3|unknown||
2170032800239614|2008|Dodge Ram 1500|Quad Cab SLT|7500|154000|Kansas City, MO|62|clean||5.7 Hemi
2108093736762254|2015|Dodge Ram 1500|Regular Cab ST 4x4|7799|150201|Kansas City, KS|6|clean||
1600742258371655|2013|Ford Edge||7995|134316|Lee's Summit, MO|19|unknown|dealer|
1541555084012704|2014|Ford Edge|Sport|7100|152500|Kansas City, KS|71|clean||3.7 V6
1083383644389817|2017|Ford Edge|Titanium|7895|155711|Kansas City, MO|13|clean|dealer|현금 전용 매장
1564846978457204|2017|Ford Escape|1.5T AWD|7995|106000|Independence, MO|30|unknown||
2221112228660273|2014|Ford Escape|Titanium 1.6T|7500|125000|Belton, MO|130|clean|dealer|
1440428451479986|2017|Ford Expedition EL|XLT 4x4|7450|194000|Kansas City, MO|1|clean|dealer|같은 차 2건 게시
27185840577744079|2013|Ford Explorer|XLS|7800|178000|Shawnee, KS|106|unknown||엔진 교체(44K mi)
1350909890300691|2014|Ford Explorer|Police Interceptor AWD|7500|105468|Independence, MO|95|unknown|dealer|
1918978226155097|2016|Ford Explorer|XLT 2.3T AWD|7500|153000|Kansas City, KS|2|clean|dealer|3열 · 임시번호판
1510992260712178|2016|Ford Explorer|XLT|7000|177000|Blue Springs, MO|8|unknown||
1608405970791266|2019|Ford Explorer||7500|1800|Independence, MO|10|clean|avoid|주행거리 1,800mi·가격 비정상 표기
1603244494929121|2011|Ford F-150||7900|167550|Kansas City, MO|14|unknown||설명 없음
2297353187722912|2012|Ford F-150||7695|207501|Kansas City, MO|5|unknown|dealer|현금 전용 매장
1651360099274481|2014|Ford F-150|XLT 3.5T 4WD|7800|184000|Basehor, KS|77|clean||
1636386401150863|2013|Ford F-150|FX4 3.5T|7500|226199|Kansas City, KS|16|clean||
1391301422382709|2011|Ford F-150|Lariat SuperCrew 4x4|7999|253313|Mission, KS|19|clean|dealer|
1767317344527538|2008|Ford F-150|SuperCab STX 4x4|7500|197000|Liberty, MO|18|clean||
2143307026399279|2013|Ford F-150|SuperCrew Lariat 3.5T|7800|208523|Independence, MO|1|unknown||캠 페이저 등 정비 이력
2364030764422080|2013|Ford F-150|SuperCrew XL 4x4|7999|141000|Kansas City, KS|35|salvage||뒤 모서리 경미 손상
969999106137279|2016|Ford F-150|SuperCrew XL|7500|125958|Kansas City, KS|6|clean||
2850300925338363|2009|Ford F-250|Super Duty XL|7500|174640|Mission, KS|6|clean|dealer|
1375781074697300|2014|Ford Fiesta||7000|79000|Kansas City, MO|47|unknown||설명 없음
1069656439248992|2012|Ford Flex|Limited|7500|124326|Paola, KS|4|clean||
1109714191737559|2018|Ford Focus|ST|7900|141000|Kansas City, KS|13|rebuilt||배기 개조
1815710606130576|2013|Ford Fusion|SE|7450|195432|Spring Hill, KS|16|clean|dealer|
1599240821602510|2013|Ford Fusion|SE|7800|153000|Shawnee, KS|20|unknown||2인 소유
1315055840793821|2013|Ford Fusion||7950|153907|Independence, MO|75|clean|dealer|할부(반액 선납) 광고
1439803647910276|2016|Ford Fusion|S|7800|110000|Kansas City, MO|60|rebuilt||이전 salvage 기재
1803779410935974|2017|Ford Fusion|SE|7999|128833|Kansas City, KS|7|unknown||경미한 외관 손상
1417784770213631|2017|Ford Fusion|Hybrid|7500|148628|Harrisonville, MO|68|unknown||
1048092471547392|2010|Ford Mustang|Convertible|7990|175000|Kansas City, MO|15|clean||엔진 교체(120K mi) · 같은 차 2건 게시
2263632217821076|2015|Ford Taurus|Limited AWD|7800|132000|Kansas City, MO|7|clean||
1562761555604061|2008|Ford F-350|Super Duty XLT|7500|277000|Mission, KS|15|unknown||
1470646864884775|2015|GMC Acadia|SLE-1|7000|129681|La Cygne, KS|0|unknown||8인승
1376195444380192|2016|GMC Acadia|Denali|7000|151665|Weston, MO|78|unknown||타이밍·워터펌프·토크컨버터 교체
1375846104140881|2016|GMC Acadia|SLT|7996|120000|De Soto, KS|120|rebuilt||
1625466622629311|2011|GMC Canyon|Crew Cab SLE 4WD|7800|222000|Kansas City, MO|4|unknown||약간의 녹
4583732981864305|2009|Hummer H3||7900|201000|Independence, MO|13|unknown||제목은 Hummer EV, 설명은 H3
924478790342795|2017|GMC Terrain|Denali|7999|113755|Kansas City, KS|3|unknown||
2269842663809328|2017|GMC Terrain||7995|161606|Kansas City, MO|90|unknown||
856007890795899|2013|GMC Yukon|Hybrid Denali|7800|229047|Olathe, KS|38|clean||3열
2899001573792086|2008|Honda Accord|EX-L 쿠페|7999|140227|Belton, MO|32|clean|dealer|
1408006294611046|2014|Honda Civic|LX|7000|118000|Liberty, MO|6|rebuilt|avoid|R/S 타이틀 · 현재 문제 있다고 기재 · 배기 개조
1407675441480251|2014|Honda CR-V|LX|7980|156000|Grain Valley, MO|4|clean|pick|
1478725437406521|2014|Honda CR-V|EX 4WD|7000|200000|Kansas City, KS|25|unknown||설명엔 $7,500
1134105196173100|2012|Honda Odyssey|EX|7700|136653|Kansas City, MO|1|clean|pick|미니밴 · 에어컨 컴프레서 교체
2727395371064361|2014|Honda Odyssey|Elite|7000|215000|Grandview, MO|23|clean||미니밴
939644785433805|2009|Honda Pilot|EX-L|7300|164347|Kansas City, MO|21|unknown|dealer|3열
3496320743876851|2015|Honda Pilot|EX-L|7995|177371|Grandview, MO|2|clean|dealer|3열 · 2인 소유
1568603181431850|2016|Hyundai Santa Fe Sport|2.4 SE|7250|126870|Kansas City, MO|24|clean||클린 Carfax · 2인 소유 기재
2214893435748042|2017|Hyundai Santa Fe Sport|AWD|7500|116000|Kansas City, MO|4|clean|pick|무사고 기재
2040024929938000|2018|Hyundai Sonata|SE|7200|67451|Overland Park, KS|125|unknown||무사고 기재
1058312109918528|2017|Hyundai Tucson|Sport 1.6T AWD|7000|78000|Belton, MO|80|unknown|avoid|기계적 문제로 as-is 판매 기재
1814319102929822|2013|Infiniti JX35||7800|135790|Excelsior Springs, MO|12|unknown||3열
2459241694566612|2015|Infiniti QX80||7900|205000|Kansas City, KS|30|clean|dealer|3열
1561874181970805|2017|Jaguar XE|35t Prestige|7999|132881|Kansas City, MO|86|unknown||설명 없음
2138508406705487|2015|Jeep Cherokee|Latitude V6 4x4|7600|120000|Lawrence, KS|2|clean||
4688265611457031|2015|Jeep Cherokee|Altitude|7500|78000|Peculiar, MO|12|rebuilt||앞범퍼·헤드램프 손상 이력
1309605947765981|2013|Jeep Grand Cherokee|Overland Summit|7000|171000|Independence, MO|13|unknown||
1092560690297648|2017|Jeep Cherokee||7459|127000|Grandview, MO|0|clean||제목은 Grand Cherokee, 설명은 Cherokee 4기통
2254253925377285|2018|Jeep Grand Cherokee|Laredo E|7999|116000|Overland Park, KS|56|clean||에어컨 고장(증발기 교체 필요)
876661758611423|2018|Kia Forte|LX|7750|101958|Kansas City, KS|43|clean|dealer|
1740464380601594|2021|Kia Forte|EX|7900|79300|Spring Hill, KS|74|rebuilt|dealer|우박 Kansas rebuilt
1434972141850110|2013|Kia Optima|SXL|7500|138700|Blue Springs, MO|2|clean||60K mi에 Kia가 엔진 교체
28270847099265400|2017|Kia Optima|EX|7900|89867|Kansas City, MO|19|rebuilt||
2905907233117880|2018|Kia Optima|LX|7845|141514|Olathe, KS|9|clean||2인 소유 · 같은 차 2건 게시
2896690240685735|2009|Kia Rio|LX|7500|69445|Olathe, KS|0|clean||설명 없음
2118664708750828|2015|Kia Sedona|EX|7000|18000|Kansas City, KS|0|clean||주행거리 18,000mi 표기 확인 필요
1453602363254230|2015|Kia Sorento|LX|7500|160764|Mission, KS|10|unknown|dealer|할부 광고
1793337522048668|2015|Kia Sorento||7000|161269|Independence, MO|58|clean||7인승
1694453958870380|2014|Kia Soul||7500|33813|Kansas City, MO|1|unknown||설명 없음
1663577958622784|2017|Kia Soul||7200|86600|Kansas City, MO|3|clean|dealer|같은 차 3건 게시
1742236960255336|2017|Kia Soul||7500|69000|Kearney, MO|47|unknown||
27679092608443582|2019|Kia Soul|+|7950|96000|Belton, MO|76|clean|dealer|
1652992823277986|2014|Kia Soul||7499|108948|Bonner Springs, KS|13|clean||
27252268067724977|2008|Land Rover Range Rover Sport|Supercharged|7300|185932|Kansas City, MO|128|clean||
1625362649239583|2011|Lexus ES|350|7600|160000|Peculiar, MO|9|unknown||
1059291566847828|2015|Mazda CX-9||7000|124000|Rantoul, KS|34|unknown||설명 없음
1033390953019186|2009|Mercedes-Benz C-Class|C300 Sport|7000|159000|Kansas City, MO|36|clean||배기 개조
1419001726861717|2014|Mercedes-Benz C-Class|C250 쿠페|7000|113000|Kansas City, MO|19|clean||
1334435901861600|2012|Mercedes-Benz GL-Class|GL450 4MATIC|7000|187966|Kansas City, MO|14|unknown||3열
1734184958025657|2014|Mercedes-Benz GL-Class|GL450 4MATIC|7500|180000|Kansas City, MO|98|clean||3열
1562384035600641|2012|Mercedes-Benz GLK-Class||7200|147000|Lee's Summit, MO|62|clean||
1022672174155238|2012|MINI Cooper|Coupe S 6단 수동|7500|105000|Belton, MO|14|clean|dealer|
3284342878440279|2015|Mitsubishi Outlander Sport|GT AWD|7500|113204|Kansas City, MO|72|clean||
1054388227372486|2021|Mitsubishi Outlander Sport|SE|7950|155000|Kansas City, KS|20|clean|dealer|할부 광고
1065398796137328|2013|Nissan Altima|2.5 S|7350|105000|Kansas City, MO|23|clean|dealer|설명은 2014년식
942435508518285|2013|Nissan Altima|2.5|7000|107000|Ottawa, KS|160|rebuilt||
2052244608727502|2017|Nissan Altima|2.5 S|7900|94962|Kansas City, MO|56|clean||
2701254903605914|2017|Nissan Altima|2.5 SV|7750|140900|Grandview, MO|62|clean||
792268190610742|2018|Nissan Altima|2.5 S|7900|60128|Independence, MO|54|rebuilt||앞부분 교체·도색
1059454216634538|2016|Nissan Sentra||7000|103096|Grandview, MO|46|unknown||설명 없음
2580411919086457|2012|Nissan Juke|SL AWD|7000|108000|Lee's Summit, MO|20|clean||
1383735460546236|2012|Nissan Maxima|SL|7995|125904|Overland Park, KS|47|clean||
1106967811983646|2014|Nissan Maxima|SV|7000|128000|Independence, MO|6|clean|dealer|
1562362971539929|2014|Nissan Maxima|SE|7000|99845|Independence, MO|15|unknown||앞 브레이크 캘리퍼 고착 기재
1616061890044784|2014|Nissan Murano|AWD|7900|110000|Olathe, KS|9|clean||경미한 외관 흠
2358159965039215|2013|Nissan Rogue|SV AWD|7000|119105|Kansas City, KS|7|clean||
1080544808039536|2017|Nissan Rogue|SL AWD|7950|127861|Kansas City, MO|1|clean|dealer|
1452712300016666|2015|Nissan Sentra|SV|7600|101100|Overland Park, KS|47|clean||
829981716749028|2019|Nissan Sentra|SL|7600|125326|Kansas City, MO|61|clean||
1100305479356832|2011|Nissan Titan||7500|179000|Shawnee, KS|9|unknown||
3170547899812018|2009|Pontiac G8|V6|7400|125137|Grain Valley, MO|18|unknown|dealer|
1783200269775486|2013|Subaru Forester|2.5X Limited|7500|156000|Eudora, KS|49|clean||엔진 교체 기재 · 설명엔 $7,200 OBO
1854896632346976|2014|Subaru Outback|2.5i|7999|131156|Bonner Springs, KS|0|clean||
1063308036458169|2010|Toyota Corolla|S Special Edition|7500|162200|Independence, MO|31|unknown||
1253643653574669|2012|Toyota Corolla|LE|7000|126960|Overland Park, KS|4|clean|pick|
2142819553114055|2014|Toyota Corolla|LE|7950|120000|Shawnee, KS|3|rebuilt|dealer|$2,500 다운페이 할부 광고
1576589850915252|2013|Toyota Prius|Three|7500|118000|Blue Springs, MO|26|rebuilt||
1063044763213517|2013|Toyota Prius v||7900|168000|Gardner, KS|5|clean||
1528780682014447|2014|Toyota RAV4 EV||7900|83121|Kansas City, MO|149|clean||전기차
28459254157031302|2009|Volkswagen Passat|2.0T S|7500|45000|Olathe, KS|37|unknown||
1131186402917300|2013|Volkswagen Passat|1.8T Limited|7500|114000|Overland Park, KS|52|clean||
2637107923428557|2014|Volkswagen Passat|1.8T Limited|7500|132000|Blue Springs, MO|35|unknown||
973119402459560|2014|Volkswagen Passat|2.5 SE|7980|95984|Kansas City, MO|71|clean|dealer|
1378323507452584|2016|Volkswagen Passat|1.8T S|7200|116626|Kansas City, MO|114|salvage||
27593826306958222|2014|Volkswagen Tiguan|SEL 4Motion|7750|101000|Kansas City, MO|2|clean||
4153810601576645|2015|Volkswagen Tiguan|2.0T S 4Motion|7500|97000|Harrisonville, MO|54|unknown||
1372540655072165|2017|Volkswagen Tiguan|Limited 2.0T|7900|66775|Olathe, KS|34|rebuilt||
1098681872633821|2015|Volkswagen Tiguan|SE 4Motion|7999|125872|Belton, MO|0|clean|dealer|'''

have = {x['id'] for x in d['listings']}
rows = []
for line in raw.splitlines():
    i, year, model, trim, price, miles, city, days, title, flags, note = line.split('|')
    flags = set(filter(None, flags.split(',')))
    assert i not in have and title in {'clean', 'rebuilt', 'salvage', 'unknown'} and flags <= {'pick', 'avoid', 'dealer'}, line
    assert 7000 <= int(price) <= 7999 and int(year) >= 2008 and int(days) <= 180, line
    rows.append(dict(id=i, year=int(year), model=model, vehicle=f'{year} {model} {trim}'.strip(), price=int(price), miles=int(miles),
                     city=city, days=int(days), title=title, pick='pick' in flags, avoid='avoid' in flags, dealer='dealer' in flags, note=note))
assert len(rows) == len({r['id'] for r in rows}) == 176

d['listings'] += rows
d['search'].update(priceMax=7999, scanned=717 + 353, passes=[
    dict(price='$4,000–$7,500', scanned=717, kept='Copart 동일 차종 + 추천·주의 매물'),
    dict(price='$7,000–$7,999', scanned=353, kept='승용차·SUV·밴·픽업 전체')])
path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
matched = sum(r['model'] in set(d['lots'].values()) for r in rows)
print(f"added {len(rows)} ({matched} match a Copart model); total {len(d['listings'])}; "
      f"picks {sum(r['pick'] for r in rows)}, avoid {sum(r['avoid'] for r in rows)}")
