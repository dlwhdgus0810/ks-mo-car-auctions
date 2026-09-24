"""Fill detail-page data for Facebook Marketplace listings that were feed-only ('상세 미조회') in the 2026-09-23 snapshot.

On 2026-09-23 Facebook rate-limited detail requests after about 1,330 pages, so 727 listings went in with feed data only.
On 2026-09-24, 414 of them were fetched one at a time before further automated requests were stopped; 313 stay feed-only.
Title status, warnings, dealer flags and notes use the same keyword rules as the third pass
(scripts/add-marketplace-under8k-sep23.py). Parts-only cars and down-payment ads under $3,500 are dropped, as in that pass.
Year, model, price and city stay as snapshotted on 2026-09-23; the exact odometer replaces the feed's rounded one.
Also fixes three 2011-2013 Grand Cherokees that the feed-title parser had keyed as the 2021+ Grand Cherokee L.
"""
import json
from pathlib import Path

p = Path(__file__).resolve().parents[1] / 'dist'
path = p / 'marketplace-2026-09-23.json'
d = json.loads(path.read_text())
todo = {x['id']: x for x in d['listings'] if '상세 미조회' in x['note']}
assert len(todo) == 727, 'One-time migration'

# id|title|flags|odometer|price now|model from detail page|trim|notes, or id|gone (listing deleted by 2026-09-24)
raw = '''1065018872537393|clean||220000|1500|GMC Terrain|SLT|
2859276854445602|unknown||165000|1200|BMW 3 Series|328i|
887159170742577|clean||187462|1300|Chevrolet Malibu|LT|
1304133128461854|clean|avoid|134000|800|Chevrolet Traverse|LT|엔진 수리 필요 기재
1372294068200440|unknown|avoid,parts|271000|1000|Kia Borrego|LX|수리용 차량 · 누유·누수 기재 · 엔진 소음 기재
1556009269263090|clean||224569|1700|Chevrolet Impala|LTZ|
1578019247236217|clean|avoid|182000|1200|Audi Q5|3.2 Quattro Premium Plus|운행·시동 불가 기재
2531813317248122|clean|avoid,parts|247000|1100|Hyundai Sonata||수리용 차량 · AS IS 판매
1360854699309638|clean||199000|1900|Chevrolet Impala|LTZ|AS IS 판매
985794324447175|clean||208355|1000|Nissan Murano|AWD|
1020419160401409|clean||260789|1500|Ford Expedition|XLT|엔진 경고등 기재 · 엔진 소음 기재
27331653953143129|unknown|||500|Nissan Murano||
2043869333182837|clean||266000|1600|Ford Edge||
978742671688140|unknown|avoid|200320|1200|Ford Edge|SE|헤드개스킷 문제 기재
1302854661804137|unknown||128000|1800|Nissan Sentra|SR|엔진 경고등 기재
3474374966046049|unknown||214543|1500|Ford F-150|XLT|변속기 이상 기재
1919899191993876|rebuilt|avoid|163317|1100|Ford Focus|Titanium|타이틀 없음·분실 기재
2650411335418680|unknown||238000|800|Chevrolet Impala|Lt|
1116601640701019|unknown|avoid,parts|120000|850|Chevrolet Malibu|1LT|타이틀 없음·분실 기재 · AS IS 판매
1050090298025219|clean||250000|899|Mazda C5||
1379771256957537|clean||140752|800|Jeep Liberty||AS IS 판매
1021928504216200|unknown|avoid,parts|111111|950|Chevrolet Traverse|LT|운행·시동 불가 기재
1098308316206082|clean||166964|950|Chrysler Sebring|LX|
888181120687702|unknown||293000|900|Honda Civic|EX-L|
1536309037969257|clean|parts|220000|800|Chrysler Sebring||AS IS 판매
2235682767165174|clean||230000|800|Kia Forte|LX|
972079502526267|unknown|parts|195000|800|Chrysler 200|200S|
2110678396552623|clean|dealer|175166|950|Chrysler Town & Country|Town & country|과열 기재
1645299583592552|clean||198000|1500|Ford E-Series||
1627146005516730|unknown||131000|1500|Jeep Compass|Latitude|변속기 이상 기재
1054318814267693|unknown|avoid|19000|1700|Chrysler 300|300 Motown|엔진 수리 필요 기재
3177595035763674|clean||179000|1850|Saturn Outlook|XE|
2060938607869576|unknown||285000|1000|Nissan Maxima|GLE|
2977366162601581|unknown|avoid|125674|1100|Chevrolet Malibu|LS|헤드개스킷 문제 기재 · 누유·누수 기재
1443343310937737|clean||194195|1250|Mitsubishi Galant|ES|
1706492110633986|unknown||160000|1000|Honda Civic|SE|
1228728016985713|unknown|avoid,parts|15000|1300|Nissan Murano|S|엔진 수리 필요 기재
954301137471600|clean||202358|1200|GMC Acadia|SLE|
930679949769428|clean||150000|1800|Jeep Compass||
1621316289338553|unknown||200000|2800|Subaru Impreza||
1127305819859015|clean||293000|2800|GMC Yukon|SLT|
2004863533466458|unknown||235000|2400|Ford Fusion||
4659911954239023|unknown||183458|2500|Jeep Liberty||
1854663802179606|unknown||214000|2000|Volkswagen CC|2.0T Executive|
1060696966761244|unknown||209000|2500|Volkswagen Tiguan|2.0T 4Motion|
1821697969268905|unknown||1757|2000|Chevrolet Traverse|6|
1418120223630687|clean||167800|2900|Ford Escape|XLT|
2358858904850347|clean||270000|2900|Toyota Corolla|LE|
1519801250165185|clean||247000|2000|Honda Accord|V6|
1795428194827145|unknown||140121|2000|Toyota Corolla|LE|
1569663881575044|clean||245000|2900|Chevrolet Impala||
1125913079789094|unknown||244242|2000|Chevrolet Malibu|LS|
3462875297217981|rebuilt||226872|2800|Kia Soul|+|
1647821373476240|clean||235000|2500|Ford Edge|Limited|엔진 소음 기재
1437499314899056|clean||158000|2850|Chevrolet Captiva||
2069369833945747|clean||192000|2895|Ford Escape||
2978998835766707|unknown||287000|2500|Mazda CX-9|Grand Touring|
1422178752951218|unknown||198999|2100|Volkswagen Jetta|Black|
1791313631906278|unknown||151500|2600|Nissan Rogue||엔진 경고등 기재 · AS IS 판매
3502492733244131|clean||118000|2500|Chevrolet Sonic|LT|
1099578485793041|clean||195000|2500|Buick Enclave|CXL|
1752562399368626|unknown||194000|2300|Ford Escape||설명 없음
1704228491702842|clean||178258|2500|Ford Escape|XLT|AS IS 판매
3516136109233906|clean||222000|2000|Mazda CX-5|2.5 S Select|
2869420333415012|clean||213930|2500|Ford Escape|SE|
1482720700360978|clean||148246|2500|Dodge Avenger|SXT|
2135226690754831|clean||175950|2000|Toyota Matrix||
939869061930905|unknown||270000|2700|Ford Explorer||
2115770292372632|clean||300000|2450|Ford Focus|S|
1393893602168705|clean||133000|2100|Kia Soul||
1650605659996106|unknown||183000|2000|Ford Focus|SE|
1615925090066227|clean|avoid|190957|2500|Nissan Pathfinder|Platinum|수리용 차량
1068721882564142|clean|avoid|152131|2000|Chevrolet Malibu||수리용 차량 · 엔진 경고등 기재
1695516611523354|unknown||145123|2000|Nissan Altima|S|
4032339320404137|unknown||170000|2500|Chevrolet Impala||
1609919630824858|clean||159000|2600|Pontiac G6||
1404434088520563|clean||180000|2400|Ford Escape|Active|
1688643425542050|clean||219949|2999|Nissan Altima|2.5 SL|
1062805033218144|unknown||202000|2500|Mazda3||
1540453337369262|unknown||178000|2700|Ford Focus|Titanium|
1058491120435754|clean||200000|2500|Chevrolet Cruze|LS|AS IS 판매
1051234594489831|clean||140000|2200|Ford Fiesta|SE|
1051260284489205|rebuilt||135000|2000|Ford Focus|SEL|변속기 이상 기재 · 에어컨 고장 기재
2306213273245959|clean||239000|2000|Volvo S60|2.5T|누유·누수 기재 · AS IS 판매
1746971426504432|clean||244614|2850|Chevrolet Volt|LT|
1370460328623949|unknown||199500|2000|Chevrolet Cruze|LT|
1361763369450931|clean||250000|2200|Chevrolet Cobalt||
1743723623513946|unknown||200000|2500|Nissan Pathfinder|LE|
2200967800481670|unknown||146000|2500|Nissan Versa Note||
1616146263286084|unknown||215000|2500|Dodge Ram 1500|SLT|
1842095253622739|clean||186815|2524|Dodge Journey||
2388411331964523|clean||205338|2700|Chrysler Sebring|LX|
1279919370821152|unknown||175000|2000|Nissan Sentra|1.8 S|
1036016729315390|clean||191656|2500|Scion xB||
4112334148902471|clean||258000|2800|Honda Accord|EX|
1479148004233565|clean||242000|2400|Kia Sorento|LX|
1384140960556206|clean||163000|2500|Chevrolet Malibu|LT|AS IS 판매
888944900648617|clean||220822|2750|Hyundai Sonata|GLS|
1485566316481763|unknown||100000|2000|Ford Focus||변속기 이상 기재
1431541165701923|unknown|avoid|246000|2800|Ford Fusion|SE|타이틀 없음·분실 기재
2354761388674489|unknown||174000|2500|Nissan Altima|2.5 S|변속기 이상 기재
1715321952919828|clean||201000|2800|Ford Expedition|King Ranch|
1865271414434351|unknown||186881|2800|Nissan Altima|2.5 S|
2233991884082656|clean||245235|2500|Dodge Journey|Limited|
890385220383809|clean||235235|2700|Jeep Patriot|Sport SE|
1756409082032639|rebuilt||150000|2000|Cadillac SRX|Luxury Collection|
2019579841999630|unknown||220000|2500|Nissan Altima|2.5 S|
1767137390977026|unknown||242674|2000|Nissan Altima|2.5 SL|
1614547973573108|clean||100000|2000|Infiniti G37x|Base|누유·누수 기재
27879252515020458|unknown||214000|2500|BMW 5 Series|535xi|
914003274345419|unknown|avoid|146000|2500|Ford Focus||타이틀 없음·분실 기재
795302683610033|unknown||140000|2700|Chevrolet Spark||
1487999536411856|unknown||192046|2800|Nissan Altima|2.5 S|
2076115996447081|clean||160000|2850|Chevrolet Impala|LT|
4110572795909951|unknown||182000|2200|Dodge Avenger||
787299627744613|unknown||193000|2500|Kia Rio|LX|
995550666529671|unknown||161000|2100|Chevrolet Cruze|LT|
990820353492936|clean||212000|2899|Nissan Quest|Other|
2136009354001364|unknown||160000|3000|Dodge Journey|Crossroad Plus|
948972028261840|unknown|avoid|16600|3300|Chevrolet Trax||운행·시동 불가 기재
2235369560367290|unknown||230000|3500|Audi A4|2.0T|
2166356777244462|clean||183650|3000|Dodge Grand Caravan|ES|
1714126083021404|unknown||213598|3000|Honda Civic||
1851436716269844|clean||153000|3000|Chevrolet Traverse||
1754888942469190|unknown||139843|3000|Buick LaCrosse|Touring|
2095467297843439|unknown||170000|3000|Jeep Liberty|Limited Edition|
1087734100322199|unknown||228000|3000|Ford Escape|XLT|
1783567129644910|clean||172000|3000|Nissan Maxima||
4021173091523282|clean||127010|3200|Nissan Rogue|S|
1614590776683337|clean||196635|3500|Kia Sportage||
1638021494601099|unknown||198000|3500|Chrysler 200|200S|
1385520713693818|unknown||175000|2900|Chevrolet Cruze|2LT|
1448599853781347|clean|avoid|193179|3000|Ford Escape||헤드개스킷 문제 기재 · 누유·누수 기재 · AS IS 판매
821828107656879|unknown||128000|3000|Chevrolet Sonic|LS|설명 없음
1392325289752315|clean||270000|3500|Dodge Ram 1500|Sport|엔진 경고등 기재
1096932056252692|clean||200000|3500|Chevrolet Cobalt|Sport|
953449827777651|clean||185000|3500|Nissan Rogue||
1337942681469242|clean||178000|3000|Dodge Durango||엔진 경고등 기재
985250427937382|clean||250000|3000|Nissan Maxima||
4361952090786559|unknown||190000|3500|Chevrolet Cruze|Eco|
4308584859393142|clean||206000|3000|Nissan Altima|2.5 Platinum|
3468928886608990|clean||186382|3900|Jeep Compass||
1615338697044269|clean||184000|3999|Ford Explorer|Limited|
1727630918358740|clean||216000|3200|Chevrolet Equinox|L|
2108710270530379|unknown||131342|3950|Chevrolet Aveo|LT|
1650128213357523|unknown||206682|3500|Ford Explorer||AS IS 판매
1762282294920527|clean||272000|3700|Toyota Corolla|LE|
2018586238793367|unknown||250000|3000|GMC Terrain|AT4|
1628267509000179|clean||242277|3200|Kia Sorento|EX|
1214619424179690|unknown||318000|3000|Ford F-150|FX2|
1220461440223739|clean||125000|3750|Volkswagen Eos|3.2L Hard Top|
1536765257523896|unknown||165000|3000|GMC Acadia|SLT|
1077921547905884|clean||190000|3500|Chrysler 200|200C|
855040357689224|unknown||170000|3500|Kia Forte||
1099239476113179|unknown||197800|3000|Volkswagen Touareg|VR6|
1551751859762366|clean||288000|3000|Ford Transit Connect|XLT|변속기 이상 기재
1650423816057426|unknown||200942|3000|Chevrolet Cruze|LTZ|
2039301713623242|clean||233000|3800|Dodge Dart||
1269212376266055|unknown||154043|3000|Nissan Rogue|S|
4322913261352562|unknown||175000|3800|Ford Edge|Limited|
1067744315816636|clean||172000|3000|Chevrolet Equinox|LTZ|
1049192214354911|clean||233333|3500|Ford Taurus|SHO|
1800882700878796|clean||233805|3500|Honda Pilot|LX|
1036330508790137|unknown||158000|3000|Ford Focus||
1576009800850059|clean||192000|3800|Chevrolet Malibu||
1031910642829874|clean||200000|3000|Ford Edge|Limited|
1673963230308426|clean||203993|3500|Kia Sorento|LX|
26976731918609675|unknown||194000|3000|Nissan Rogue Select||
2281083289352709|clean||237000|4500|Toyota Sienna|LE|
3225682770953093|clean||220000|4500|Dodge Journey|R/T|
2208587913053962|clean||232845|4000|GMC Acadia|SLT|
4217961388464363|clean||202300|4500|Ford Escape|Limited|
907857105493352|clean||165222|4200|Ford Escape|SEL|에어컨 고장 기재
2881333328906800|unknown||133000|4000|Chevrolet Cruze|LT|
1087211740622841|salvage||212050|4700|Ford F-150|XLT|
1635050298051828|unknown||148000|4500|Toyota Corolla|S|
1052879527373110|clean|dealer|152785|4700|GMC Terrain|SL|
1411366084286730|unknown||250000|4500|Lexus GS|GS 350 F SPORT|
1055732617261292|clean||197521|4200|Hyundai Santa Fe||
1864162665023326|clean||139306|4000|Ford Fiesta|SE|
1073079208654675|clean||140000|4300|Hyundai Elantra|Touring|
1105569538541298|rebuilt|avoid|180000|4000|Chevrolet Tahoe|LT|변속기 수리 필요 기재
1070859952589458|clean||140200|4500|GMC Acadia||
1058302453685640|rebuilt||109000|4500|Kia Rio||
2077909049486137|clean||240766|4500|Ford F-150|FX4|
2285923495577759|clean||157521|4500|Lexus LS|LS 460|
2158598814691410|unknown||145123|4000|Jeep Patriot|Limited|
1092638206674363|unknown||213949|4100|Kia Sportage||
1324264313117928|clean||175500|4500|Ford Focus|Titanium|
1382656436829962|clean||134787|4500|Mazda3|i Touring|
1562552024881048|unknown||284286|4500|Ford Edge|Limited|
1464931348989063|clean||179000|4295|Chevrolet Spark|LS|
1034739209567403|clean||222000|4000|Chevrolet Traverse|LT|
1390363882501173|rebuilt|dealer|190000|4500|Honda Odyssey|EX-L w/Navigation|
1059569380048411|unknown||208000|4200|Toyota Camry|CE|
1785331269126861|clean||170000|4300|Jeep Patriot|Latitude|
1495024485766997|unknown||190000|4600|Cadillac XTS|Luxury|
1832372061434339|gone
1012667551791694|clean||160000|4500|Audi A3|2.0T S-Line|누유·누수 기재 · AS IS 판매
1717481946199742|clean||88500|4000|Ford Focus||
2160343078165797|clean||143000|4000|Toyota Prius|Four Touring|엔진 경고등 기재 · AS IS 판매
2389805911824485|unknown||123671|4500|Volkswagen Passat||설명 없음
850831644787083|clean||165222|4000|Ford Escape|Active|
1038252792173913|rebuilt||222222|4250|Acura TL|3.2|
1261340149384528|clean||275000|4700|Ford F-150|King Ranch Short Bed 4D|
1063143412922537|clean||146000|4500|Jeep Compass||
1081653704443632|clean||270000|4100|Toyota Corolla|S|
1043791958447567|clean||180000|4000|Nissan Pathfinder|Platinum|
1590705682630952|unknown||108000|4300|Chevrolet Spark||
1039103698739845|clean||154400|4700|Nissan Rogue|SL|
1602978674824483|unknown||216798|4500|Ford F-150|King Ranch 4D|
2576499142785553|unknown||170000|4000|Ford Explorer|XLT|
1560306242508334|clean||165412|4400|Ford Escape|S|
1501032425374741|clean||150000|4600|Ford Edge|Sel|
1036540915815221|clean||195000|4500|Chevrolet Traverse|LT|
2197432347490605|unknown||120088|4000|Chevrolet Cruze|LT|
4480257228906899|unknown||136283|4500|Chevrolet Cruze||
2528884760940701|unknown||183000|4500|Audi Q5|3.2 Quattro Premium Plus|
1581609886910974|clean||173188|4500|Dodge Dart||
1734913627715216|clean||163000|4500|Chevrolet Malibu|Eco|
1078450628003962|unknown||111000|4500|Kia Optima|LX|
1205303535101405|clean||126750|4300|Smart Fortwo|Passion|
1556573039346524|clean||150000|4500|Nissan Juke|SL|
924202907379866|clean||230000|4500|Nissan Pathfinder||
27345006365192600|clean||190000|4500|Infiniti M37x||
1585269103114910|clean||183000|4200|Hyundai Accent|GL|
1995471111336127|unknown||220000|4300|Hyundai Tucson|Limited|
2143105609933522|clean||184000|4200|Chevrolet Cruze|LT|누유·누수 기재
2455779931608955|rebuilt||150000|4500|Audi Q5||
987448287661923|unknown||163222|4000|Ford Escape|Tela|
1382320477104586|clean||127000|4000|Ford Focus||
1950762328942625|clean||125000|4000|BMW 5 Series|535i|
1281748880478625|clean||19000|4500|Volkswagen Jetta|2.0L Base|
1341453377363874|clean||170000|4000|Nissan Rogue|S|
3921955148101059|unknown||184860|4200|Volkswagen GTI|1.8T|
1514878973708293|clean||220000|4000|Chevrolet Traverse|LS|
1731120988243685|clean||171535|4700|Chevrolet Impala|LS|
2988825851449773|unknown||140000|4500|Cadillac CTS|3.0 Luxury Collection|엔진 경고등 기재
1766613167811021|clean||138500|4000|Mercedes-Benz C-Class|C 250 Luxury|
2165029144427789|clean||127000|5450|BMW 3 Series|328i xDrive|
1079938621630428|clean||137000|5250|Volkswagen Passat|2.0T|
1036780562732441|rebuilt||169000|4800|Honda Civic|LX|
2007576393291015|clean|pending|143000|4800|GMC Acadia|SLE-2|
1080656864888570|unknown||130000|5000|Mazda3|2.0|
4590405921281181|clean||152000|5200|Honda Accord|DX|
1645424837249620|clean|dealer|221438|4999|Volkswagen Passat|TDI SEL Premium|
1753113799241855|unknown|dealer|85359|4895|Dodge Dart||
2316368479160065|unknown||200721|5000|Lincoln MKX|Premiere|
1109418928090779|clean||203000|5100|Jeep Liberty|Limited|
1369083941927839|clean||160000|5000|Kia Forte|EX|
1645180657182342|clean||116000|5400|Mercury Mariner|Premier|
1583979599770595|unknown||142000|4999|Ford Escape|SE|
1417907763609496|clean||152819|4800|Nissan Quest|SL|
1686678015770398|rebuilt||86000|5499|Chevrolet Trax|LT|
2478470102676362|clean||148000|5300|Jeep Renegade||
1090077783606629|rebuilt|dealer|171000|5300|Subaru Forester|2.5X|
2951622831865087|clean||190000|5000|Jeep Renegade||엔진 경고등 기재
2091530474793861|clean||175000|5250|Dodge Grand Caravan|GT|
2154542038461340|clean||126488|4950|Chevrolet Cruze|LT|
1427909152523784|clean||140000|4750|Mercedes-Benz C-Class|4matic sport|
1861228755284461|unknown|downpay|145062|4990|Chevrolet Sonic||다운페이·할부 광고
1117556447272159|clean||250000|4800|Lexus GS|GS 350 Crafted Line|
1805558103951124|unknown||215751|4800|Acura TSX||
1554346576376878|clean||108000|4999|Kia Soul||
1370674128483785|clean|dealer|184508|4965|Ford Fusion|S|
1096847783302425|clean||153000|5000|Dodge Journey|SXT|
991960120528890|clean||160000|5000|Ford Fusion||
1044976168413746|rebuilt||141805|5000|Hyundai Santa Fe|SE|
1405745084829663|clean||215000|5000|Infiniti JX35||
28470069329347379|unknown||200000|5200|Nissan Pathfinder|SL|
1693512822392354|clean||147087|5000|Jeep Compass||
1202289682596847|unknown||87080|5300|Chevrolet Sonic|LT|
1620925139712137|unknown||175595|4995|Mazda3|Sport|
1817775852714931|clean||171000|5499|Buick LaCrosse|Premium I|
1583938970040693|clean|dealer|160000|4750|Chevrolet Equinox|Sport|
1040708368773303|clean||160000|5300|Ford Edge|SEL|
2136405363957504|clean||122700|5200|Chevrolet Trax||
1181204031752755|clean||186723|5300|GMC Terrain|SLE|
2129292334649142|unknown||138000|5000|Buick Encore|Essence|
1566502375210691|unknown||166000|5200|GMC Yukon||
1723557608864450|clean||137000|5000|Dodge Journey||
1002560436126549|clean||202000|4950|Toyota Sienna|LE|
1366441962286362|clean|dealer|190123|5000|Jeep Grand Cherokee|Overland|
1799105207762716|clean||253500|4999|Honda Odyssey|Touring Elite|
28025205173840642|clean||137700|5000|Dodge Avenger|SXT|
1024021563780352|clean||178074|4900|Chevrolet Cruze||
1065709619440787|clean||188000|5000|Kia Soul|e|
2338652430206622|clean|dealer|155000|4999|Dodge Journey|SE|
1200273245628456|clean|dealer|158000|4999|Dodge Grand Caravan|SXT|
2526921261086585|clean||175903|5000|Nissan Rogue|SV|
1056320410326530|rebuilt||128571|5000|Ford Flex|SE|
1077713498283633|unknown||200000|5000|GMC Acadia|Denali|
937630235279498|unknown||205000|5000|Dodge Ram 1500|ST|
1670153524058633|clean||121000|5000|Dodge Avenger|SE|
1474770314686437|clean||197000|5000|Nissan Maxima|SL|
1594562528892883|unknown||195619|4999|Honda Pilot|LX|
988078434260343|clean||144355|4895|Ford Edge|SEL|
1304789511603845|clean||123700|4999|Buick Enclave|CXL|
1059733296648121|clean||193000|5000|Jeep Grand Cherokee|Overland|
2302320253935140|clean||165081|4800|Ford Escape|S|
1371672064419168|clean|dealer|248000|4990|Toyota Camry|LE|
4502292070058965|clean||106000|5000|Cadillac ATS||
4310414289219300|unknown||150327|5000|Jeep Compass||
2563080764105633|clean||134000|5000|Subaru Impreza|2.5i Premium|
1021452510784970|clean||187000|4999|Chevrolet Traverse|LT|
1040494481669197|unknown||98123|5200|MINI Countryman|Classic Cooper S ALL4|
1678196317198957|clean||158000|5000|Chrysler 200|200C|
846595711718424|unknown||173000|5499|Honda Odyssey|EX-L|
1026975943377606|clean||158200|5300|Subaru Forester||
1324767199419594|unknown||235984|5000|Honda CR-V||
1062164412859404|unknown||230000|5200|Volkswagen Passat|2.0T S|
2284380065697748|clean||152000|4900|BMW X1|xDrive28i|
1429055179032551|rebuilt||114183|4900|Nissan Juke|S|
1593882118979971|clean||159000|5250|Ford Flex|SEL|
1551422146529476|unknown||145000|4999|Nissan Pathfinder|S|
1705870507400278|clean||217200|5000|GMC Sierra 1500|Long Bed|엔진 경고등 기재 · 누유·누수 기재
1480271057206084|clean||154000|4800|Chevrolet Silverado 1500|LT|AS IS 판매
1509974950516675|unknown||16000|5000|Chevrolet Camaro|LT|
1638452510770603|clean||192663|5000|GMC Acadia|Denali|
1291001925968083|clean||179088|4999|Ford Flex|Limited|
981801921376871|clean||138407|5000|Ford Ranger|Xlt|변속기 이상 기재 · AS IS 판매
4479243859007300|clean||130000|5000|Volkswagen CC|2.0T Sport|엔진 경고등 기재
1355226603330040|unknown||119000|4800|Land Rover Range Rover Sport|Autobiography|
1833265437657867|clean||123250|5500|Nissan Murano|Cross-Cabriolet|
1498580762142715|unknown||290000|6000|Dodge Ram 1500|Tradesman|AS IS 판매
1758350562115300|clean||174000|6000|Nissan Maxima||
2150055882527177|unknown|dealer|215350|5950|Toyota Prius|I|
1038215275939120|clean|dealer|176000|5999|GMC Terrain|SLE|
1266571475572575|clean||150000|5800|Honda Odyssey|EX-L w/Navigation & RES|
2162270047659958|clean||155982|5500|Hyundai Santa Fe|SE|
1644805993825623|clean||192541|6000|Subaru Accord||설명 없음
1109949561564187|clean||125000|5500|Hyundai Tucson||
1613329863659357|clean||100976|5900|Pontiac Solstice|GXP|
2659358217834659|unknown||1300|5500|Chevrolet Equinox||설명 없음
38616685391279602|clean||109000|5500|Smart Fortwo||
4384940381760834|unknown||152784|5500|GMC Terrain||
28854092660862070|unknown||148000|5900|BMW 3 Series|328i xDrive|
3313884498795552|rebuilt||175020|5700|Toyota Prius|III|
1332833678796220|unknown||191000|5500|Toyota Prius||
1790590198952276|clean||195000|6200|Ford Explorer|XLT 4x4|
1100964542322147|clean||134460|5750|Hyundai Sonata|GLS|
1632743191843806|unknown|dealer|195300|5985|Jeep Latitude||
1617214946626962|clean|dealer|118000|5950|Nissan Rogue||
2042267499791962|unknown||95000|6200|Dodge Journey|Crossroad|
1798846294866211|clean||108338|5995|Chevrolet Cruze||
1089501150291510|clean||155000|5500|Pontiac G6|GXP|
2180258839557638|clean||124000|5500|Chevrolet Cruze|1LT|
1598292605122652|clean||90000|6000|Kia Forte||
4634609383479838|salvage||152000|5500|Ford Mustang|Premium|우박 이력
1109711591616515|unknown||120000|6000|Volkswagen GTI|2.0T|
1027139056813774|clean||200087|5500|GMC Yukon XL|SL|
950501091430806|clean||221000|5700|Mitsubishi Lancer||
1381877020186333|clean||205500|5800|Honda Pilot|Touring|
2204898720072170|salvage||157882|6000|Honda Civic|Touring|
1063568706438241|unknown||246159|5700|Toyota Camry|XLE|
1593238722209680|unknown||140000|5950|Buick Encore||
28223644943961458|unknown||109835|5700|Jeep Patriot||
1025246220514742|unknown||159000|5500|Jeep Liberty|Latitude|
1417121590265112|unknown||166000|6000|Volkswagen Jetta|1.8T SEL|
1389054950772050|unknown||170000|5500|Chevrolet Traverse|LS|
2232753957515022|clean||160300|5999|Kia Sportage|EX|AS IS 판매
2144055726141587|salvage||111423|5550|Lincoln MKX||
1026777613515603|unknown||284499|5800|Toyota RAV4|LE|누유·누수 기재
1682712576131558|unknown||88000|5500|Ford F-150|XLT|
2329531724250643|unknown||176900|5500|Toyota Camry|LE|
1040201815452847|clean||148800|6000|Lincoln MKX||
2771191469920464|rebuilt|dealer|184541|5995|Toyota Highlander||
1455756279918984|clean||187360|5500|Jeep Grand Cherokee|Limited|
1731254244590295|unknown||184587|5700|Ford Edge||
1633642125093530|clean||170172|5500|Ford Edge|SEL Plus|
1603245971347112|clean||137000|5500|Cadillac SRX|Luxury Collection|
1877521676750871|salvage||130000|6100|Ford Taurus|SHO|엔진 경고등 기재
1371704107680705|unknown||121448|6000|Nissan Versa||
1510081214224414|unknown||236676|5995|Honda Odyssey||
1747931539561466|unknown||136000|6000|Buick Enclave|Enclave|
1482505267254832|clean||121000|6000|Kia Rio|S|
1610436760728461|clean||187758|5889|Chrysler Pacifica|Touring L|
2147840042790076|clean|dealer|222124|5999|Toyota Highlander||
1456220836269004|unknown||140000|5500|Ford Escape|Titanium Hybrid|
1040673962037615|unknown||20800|5999|Chevrolet Silverado 1500|Long Bed|
1041743164994826|clean||148545|5850|Ford Edge||
1570876844448885|clean||102700|6000|Buick Regal|Turbo Premium 1|엔진 경고등 기재
1566051798397075|clean||235252|5950|Ford Edge|SEL|
3259909224188790|unknown||199955|5500|Chevrolet Equinox||
1554405376227012|clean|dealer|162017|6000|Jeep Compass||
1689423118983456|clean||160115|5500|Jeep Compass|75th Anniversary|
845138655351164|clean||155467|5500|GMC Terrain||
1371093041647097|clean||191000|5500|Ford Taurus|SEL|
1007732131891115|unknown||167000|5950|Chevrolet Traverse|LT|
1693468841923818|unknown||123456|6000|Chevrolet Silverado 1500|Short Bed|
1647136676394085|clean||238000|5500|Nissan Rogue||
1458503936657689|clean||180000|5950|Chevrolet Malibu|LT|
2511849302585739|unknown||167700|6000|Ford Explorer|XLS|설명 없음
1677084373410926|clean|dealer|142070|5995|Mazda3||
2092906678319241|unknown||85000|6000|Kia Forte|GT-Line|
865483556185690|clean||140000|6000|Dodge Charger|R/T Max|엔진 경고등 기재
26797146876630519|unknown||207937|5999|Chevrolet Silverado 1500|Long Bed|
1537163021403138|rebuilt||149566|5900|Cadillac SRX||
1568057125113106|clean||134000|5500|Buick Enclave|Leather|
993386516568530|unknown||13100|6000|Volkswagen Golf||
1318493973584626|clean||161345|6000|Kia Sportage|LX|
1504821741111415|unknown||217000|5500|Lincoln MKZ|Hybrid|엔진 경고등 기재
1298875965185027|clean||137000|6000|Ford Escape|Titanium|
811204251542869|unknown|dealer|288450|5500|Subaru Forester|2.5i|
1051828934346119|clean||166000|6500|Chevrolet Traverse|2LT|설명 없음
1402339501315497|unknown||145000|6400|Toyota Corolla||
1800425167766245|unknown||205988|6546|Toyota Avalon|XLS|
1065088863020690|unknown||152000|6500|Jeep Patriot|Latitude|
1450016180322001|clean|dealer|171500|6950|Ford Explorer||
1664441985291614|clean||127000|6999|Chrysler Town & Country|Touring|
1095331826288539|clean||193000|6300|Dodge Durango|SXT|
1608736377590972|unknown||58769|6600|Ford Fiesta|S|
2159618334981936|clean|dealer|153000|6999|Acura TSX||
1022473150818527|clean||115000|6500|Ford Focus|SE|'''

filled, dropped, gone = 0, [], 0
for line in raw.splitlines():
    f = line.split('|')
    x = todo[f[0]]
    if f[1] == 'gone':
        gone += 1
        continue
    i, title, flags, odo, _, _, trim, notes = f
    flags = set(filter(None, flags.split(',')))
    assert title in {'clean', 'rebuilt', 'salvage', 'unknown'} and flags <= {'avoid', 'dealer', 'parts', 'downpay', 'pending'}, line
    if 'parts' in flags or ('downpay' in flags and x['price'] < 3500):
        dropped.append(i)
        continue
    old = [n for n in x['note'].split(' · ') if n != '상세 미조회']
    if odo:
        old = [n for n in old if not n.startswith('주행거리 표기 이상')]
        x['miles'] = int(odo)
        if x['year'] <= 2023 and x['miles'] < 2000 * (2026 - x['year']):
            old.append(f"주행거리 표기 이상(원문 {x['miles']:,} mi)")
            x['miles'] = None
    if trim:
        x['vehicle'] = f"{x['year']} {x['model']} {trim}"
    x.update(title=title, avoid='avoid' in flags, dealer=x['dealer'] or 'dealer' in flags,
             note=' · '.join(filter(None, notes.split(' · ') + old)))
    filled += 1

drop = set(dropped)
d['listings'] = [x for x in d['listings'] if x['id'] not in drop]
for x in d['listings']:
    if x['model'] == 'Jeep Grand Cherokee L' and x['year'] < 2021:
        x['model'] = 'Jeep Grand Cherokee'
        x['vehicle'] = x['vehicle'].replace('Grand Cherokee L l ', 'Grand Cherokee ').replace('Grand Cherokee L ', 'Grand Cherokee ')
left = sum('상세 미조회' in x['note'] for x in d['listings'])
assert (filled, len(dropped), gone, left) == (406, 7, 1, 314), (filled, len(dropped), gone, left)
path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print(f"filled {filled}, dropped {len(dropped)} parts-only, {gone} deleted; still feed-only {left}; total {len(d['listings'])}")
