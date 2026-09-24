"""Add the 2026-09-23 third Facebook Marketplace pass: every Cars & Trucks listing $0-$7,999 near Overland Park.

Facebook caps each search, so the $0-$7,999 range was split into price bands until new listings stopped
appearing (5,384 unique listings, Overland Park 40 mi). Kept: passenger cars, SUVs, vans and pickups of
model year 2008+, posted within 180 days, $500+, not already in the snapshot. Dropped parts-only cars,
down-payment ads priced under $3,500, repeat posts of one car, and prices that are implausible for the
model year (likely scams or placeholder prices, see implausible()). Odometers under 2,000 mi per year of age on
2023-or-older cars are treated as unknown (typo or thousands shorthand). Title status comes from the detail
page field or the seller's words; notes are keywords extracted automatically from the description.
"""
import json
from pathlib import Path

p = Path(__file__).resolve().parents[1] / 'dist'
path = p / 'marketplace-2026-09-23.json'
d = json.loads(path.read_text())
assert d['search']['priceMin'] == 4000 and d['search']['priceMax'] == 7999, 'One-time migration'

# id|year|model|trim|price|miles|city|days since posted|title|flags|note (built in the page from each detail page)
raw = '''2159108907976146|2011|Chevrolet Equinox|L|1300|180000|Kansas City, KS|0|unknown||
2268864800578055|2017|Kia Forte|LX|4900|106000|Kansas City, MO|0|rebuilt||
939528162553901|2011|Chevrolet Silverado 1500|Short Bed|5800|280000|Lenexa, KS|0|unknown||우박 이력
1506219248196160|2009|Toyota Sienna||3400|222104|Kansas City, KS|0|clean||
1393938912935906|2015|Volkswagen CC|(Only 88K Miles)|6750|88250|Kansas City, MO|0|clean||
1734153451191790|2015|Chevrolet Trax|LS|6400|95300|Smithville, MO|0|clean||
1097995446081284|2017|Hyundai Accent|SE|5999|116000|Kansas City, MO|0|clean||
1814782853169892|2014|Kia Forte|SX|4450|146000|Kansas City, MO|0|clean||
1453498153589330|2014|Jeep Compass|Latitude|5300|163000|Smithville, MO|0|clean|dealer|
2901645883536277|2012|Chevrolet Cruze|LT|4650|112865|Independence, MO|0|clean||
1555272856367659|2016|Volkswagen Jetta|1.4T SE|6250|179500|Kansas City, MO|0|clean||
28347671858260063|2016|Jeep Compass||3995|181713|Grandview, MO|0|clean||
1132943149399356|2013|Ford Fusion|SE|2400|227000|Kansas City, KS|0|clean||엔진 경고등 기재 · 누유·누수 기재
4581295908819239|2008|Hyundai Elantra|Eco|4200|200000|Olathe, KS|0|unknown||
1618776749784269|2016|Dodge Grand Caravan|GT|5950|151000|Blue Springs, MO|0|clean||
28074822692189338|2012|Mercedes-Benz C-Class|C 300 4MATIC Luxury|5900|120000|Olathe, KS|0|rebuilt||
1385018503788701|2012|Ford Fusion|SE|3600|145000|Kansas City, KS|0|unknown||
2532342377209397|2012|Hyundai Elantra|Limited|3500|157000|Kansas City, MO|0|clean||
946810447948092|2014|Ford Focus|SE|6000|99000|Blue Springs, MO|0|clean||
1416818499826635|2013|Hyundai Sonata|Limited|4500|155355|Overland Park, KS|0|clean||
1460234969506394|2015|Chevrolet Equinox||4300|143000|Lee's Summit, MO|0|unknown||
28465658583102371|2014|Nissan Sentra|E|6499|98500|Grandview, MO|1|unknown||
1684758826604740|2011|GMC Yukon||5500|252000|Lee's Summit, MO|1|clean||
3127208904139746|2015|Chrysler 200||3500|107000|Kansas City, KS|1|rebuilt||
1338373178371198|2019|Nissan Rogue Sport|S|6500|159963|Kansas City, KS|1|clean||
4484790928441539|2015|Kia Soul|Sport|3850|133528|Kansas City, MO|1|clean||
1584256346306870|2011|Ford Escape|Limited|3950|148000|Kansas City, MO|1|clean||
1288980783283926|2010|Chevrolet Malibu||3000|235000|Overland Park, KS|1|unknown||
1806714673670550|2016|Jeep Compass||5500|137100|Kansas City, MO|1|clean||
1876543837089758|2020|Chevrolet Trax|LS|6500|56726|Kansas City, KS|1|rebuilt||AS IS 판매 · 우박 이력
2914613382217711|2015|Kia Optima|EX|5300|123085|Kansas City, MO|1|clean||
1484164150203936|2013|Kia Soul||3000|198000|Kansas City, KS|1|unknown||
1082700251176187|2009|Toyota Prius|Standard|4000|167000|Kansas City, MO|1|clean||
28547291284879347|2015|Chrysler 200|200C|5000|114000|Grandview, MO|1|clean||
1466518728868024|2014|Ford F-150|XL STX|5950|265523|Independence, MO|2|unknown||
1847257583127627|2014|Jeep Grand Cherokee|All New Limited|5500|229000|Kansas City, MO|2|clean||
1553969956010544|2018|Chevrolet Malibu|Lt|6500|163209|Kansas City, MO|2|clean||
969792742048266|2015|Kia Optima||5300|122007|Kansas City, MO|2|clean||같은 차 2건 게시
2488760938313750|2014|Chevrolet Cruze||2500|133000|Overland Park, KS|2|unknown||설명 없음
1075498401903157|2014|Chrysler 300|300 Limited|6300|200000|Shawnee, KS|2|clean||
2025969681455771|2011|BMW 3 Series|328i|750|101000|Grandview, MO|3|unknown|avoid|수리용 차량
2083822998891459|2008|Hyundai Sonata|SE|6700|84030|Kansas City, MO|3|clean||
1706286027120197|2013|Ford Fusion|Híbrido|1800|220000|Kansas City, MO|3|clean||
891584640552308|2008|Buick Lucerne||800|149000|Grandview, MO|3|unknown||
4230137470454380|2015|Hyundai Elantra|SE|3500|140000|Ottawa, KS|3|clean||
2027462707938636|2017|Kia Sportage|LX|6900|121000|Lawrence, KS|4|clean||
1440462074627871|2008|Dodge Avenger||2500|144000|Lawrence, KS|4|clean||엔진 경고등 기재 · AS IS 판매
1775849977090289|2019|Nissan Sentra|S|3999|96818|Kansas City, KS|4|clean||
1047281288303781|2013|Ford Escape|SEL|2500|265185|Lawrence, KS|4|clean||
3565746986913089|2009|GMC Acadia|SLT|2500|140000|Independence, MO|4|unknown|avoid|변속기 수리 필요 기재
1396857991961772|2017|Jeep Cherokee|Latitude|6999|134000|Overland Park, KS|4|rebuilt||
28386453241009299|2009|Cadillac CTS||5200|165000|Kansas City, KS|5|unknown||
1383870003381596|2010|Ford Escape|XLT|2200|200636|Kansas City, MO|5|unknown||
1635100741644726|2017|Chevrolet Sonic|LT|6500|48615|Overland Park, KS|6|rebuilt||우박 이력
1394162242300269|2012|Ford Taurus|SEL|3800|168000|Kansas City, MO|6|unknown||
1061221133426830|2013|Dodge Durango|Citadel|1500|260000|Mission, KS|6|rebuilt||
1039497832425457|2015|Volkswagen Passat||4300|170000|Lee's Summit, MO|7|clean||
1101103618935616|2023|Dodge Ram 2500||600||Peculiar, MO|7|unknown||
2281178279368493|2010|Mazda6|Touring|3750|166000|Raytown, MO|7|clean||
1288094343364658|2016|Hyundai Sonata||6900|140420|Kansas City, MO|7|clean||
2122292698394961|2013|Chrysler Town & Country|SX|3200|242724|Baldwin City, KS|7|clean||
2065167657425379|2014|Mazda3|Sport|6900|90000|Shawnee, KS|7|rebuilt||
1098424552655554|2009|Kia Rio|Rio5 SX|2500|100544|Ottawa, KS|7|unknown||
1045946214887814|2012|Nissan Rogue|S (2017.5)|3000|250000|Kansas City, MO|7|clean||
2425375344656222|2012|Kia Sportage||5000|166819|Lawrence, KS|7|unknown||설명 없음
2014616952591103|2013|Ford Escape|4WD SEL|6300|169751|Independence, MO|7|unknown||
866355299829038|2008|Toyota Camry|LE|4900|176000|Overland Park, KS|8|unknown||
2236272247154066|2013|Ford Focus|Titanium|3300|176240|Kansas City, MO|8|unknown||
1108799595038797|2010|BMW 5 Series|528i|5200|120903|Shawnee, KS|8|rebuilt||
1401728287994215|2008|Ford Focus|ZXW SES|500|115000|Kansas City, MO|9|unknown|avoid|엔진 수리 필요 기재
1961454305240287|2011|Ford Taurus|SEL|3500|255000|Tonganoxie, KS|9|unknown||
1049474537860801|2018|Nissan Murano|SV|5900|217000|Kansas City, KS|9|clean|dealer|
1628349535474549|2014|Ford Focus|SE|5000|105679|Kansas City, MO|9|clean||
1057127193790153|2009|Chevrolet Cobalt||2300|250000|Olathe, KS|9|unknown||
1161619823049794|2016|Ford Focus|SE|5500|187000|Kearney, MO|11|clean||
2518900391911469|2014|Nissan Sentra|SR|3700|175252|Overland Park, KS|11|clean||엔진 경고등 기재
930221393016090|2012|Hyundai Elantra|Blue|3800|170000|Independence, MO|11|clean||
1668733301378335|2013|Volkswagen Jetta|2.5|4200|128567|Overland Park, KS|11|rebuilt||
1470743038435962|2011|Chevrolet Impala|LT Eco|1275|247500|Eudora, KS|11|clean|avoid|수리용 차량
1072831732201823|2013|Ford Explorer|Limited|5150|224673|Lee's Summit, MO|12|clean|dealer|
1410234767710696|2009|Hyundai Sonata|Limited 2.0T|4000|165000|Kansas City, MO|12|unknown||
1624621009249829|2015|Ford Focus||5500|131000|Shawnee, KS|12|clean||
1408680871415986|2019|Jaguar XE|XE 25t R-Sport|5500|96688|Independence, MO|12|clean||
1112264168124793|2008|Ford Taurus|Límite|1500|164000|Kansas City, MO|12|unknown||
1012791278487191|2014|Volkswagen Passat|1.8T SEL Premium|5000|159000|Kansas City, MO|12|clean||엔진 경고등 기재
1572633920753105|2015|Chrysler 200|Limited|5000|150000|Kansas City, MO|12|clean||
1762873938090116|2015|Subaru Forester||3900|201025|Kansas City, MO|14|rebuilt||
2139743820308711|2008|BMW 5 Series|528xi|1900|159000|Kansas City, MO|14|clean||엔진 경고등 기재
2293203594810647|2012|Hyundai Veloster||4600|118000|Lawrence, KS|14|unknown||
938540862648141|2021|Chevrolet Malibu||6500|139322|Raytown, MO|14|unknown||
1587739956153366|2019|Kia Optima|LX|6800|119613|Overland Park, KS|14|rebuilt||
1414735757472196|2010|Toyota Prius||4000|210000|Overland Park, KS|15|unknown||
2298332757644503|2011|Ford Edge|SEL|2000|189631|Wellsville, KS|15|clean|avoid|수리용 차량 · 과열 기재 · AS IS 판매
2346179666172798|2016|Volkswagen Passat|1.8T SE|6000|170000|Shawnee, KS|16|clean||
1082175284341576|2016|Ford Fusion|SE|5999|168907|Lee's Summit, MO|16|clean|dealer|
949353360848108|2016|Jeep Cherokee|Limited|5500|170000|Kansas City, MO|16|rebuilt||
1521992069948057|2013|Hyundai Sonata|GLS|3600|220707|Lenexa, KS|16|clean||
903696435938200|2012|Lexus ES|ES 350|5750|208000|Lee's Summit, MO|16|clean||
1601568051368587|2012|Jeep Compass|Upland|1300|227927|Kansas City, MO|16|unknown|avoid|운행·시동 불가 기재
1343492764526923|2010|Chevrolet Tahoe|LT|2200|292000|Oskaloosa, KS|17|unknown|avoid|변속기 수리 필요 기재 · AS IS 판매
1250227557244138|2013|Mercedes-Benz C-Class|C 250 Luxury|5500|94799|Olathe, KS|18|clean||
1210744058799250|2012|Dodge Hornet|GT Plus|3500|194000|Liberty, MO|18|unknown||
1521225896420374|2014|Ford Flex||4975|190000|Kansas City, MO|17|clean||
2006310400062806|2014|Volkswagen Passat|1.8T SE|5000|159133|Kansas City, MO|19|clean||
1768232827810341|2009|Chevrolet Malibu|1LT|1500|280000|Tonganoxie, KS|20|unknown||AS IS 판매
1014510751621987|2013|Lincoln MKX||3800|208000|Kansas City, MO|20|clean||
1816743919695573|2010|Ford F-150|XL|6200|192000|Lawrence, KS|20|clean||
1256023530930412|2013|Scion FR-S||3250|65723|Lawrence, KS|21|salvage|avoid|수리용 차량 · 엔진 경고등 기재 · 누유·누수 기재 · 엔진 소음 기재
1849792109350930|2016|Hyundai Sonata|Limited|5000|106000|Grain Valley, MO|21|clean||엔진 경고등 기재
2559888721139633|2014|Honda Civic|LX|4250|224000|Overland Park, KS|22|clean||
1066674169567115|2016|Ford Focus|SE|5500|115000|Grandview, MO|23|clean||AS IS 판매
1581467266857017|2011|Nissan Rogue|SL|1500|179000|Ottawa, KS|23|unknown||
1033926156145792|2011|Mercedes-Benz C-Class|C 300 4MATIC Sport|4000|260000|Kansas City, MO|25|clean||
1788021152221482|2017|Hyundai Sonata|Sonata|5500|162526|Kansas City, MO|25|clean||
1547649683804285|2014|Nissan Sentra|1.8 S|1600|123000|Kansas City, MO|26|unknown||
4377621902454728|2016|Ford Edge||6700|171234|Kansas City, KS|27|unknown||설명 없음
1055247197129273|2015|Nissan Altima|2.5 SV|5950|114000|Olathe, KS|27|rebuilt||
1623443282790683|2013|Ford Edge|Limited|5950|124991|Kansas City, MO|27|rebuilt||우박 이력
1369304071533036|2016|Hyundai Sonata|SE|6500|175000|Kansas City, KS|28|clean||
1213116151012016|2015|Ford Fusion|Hybrid|6300|99000|Kansas City, MO|28|rebuilt||
4641396196097238|2013|Dodge Dart|SXT|5000|109300|Kansas City, MO|28|unknown||
1048296058187594|2016|Chevrolet Trax||6500|127863|Kansas City, MO|28|clean||
2032237894085457|2011|Hyundai Sonata|Eco|6500|115000|Lenexa, KS|28|clean||
1408252524552240|2012|Mitsubishi Eclipse|GS Spyder|5500|126000|Lawrence, KS|29|unknown||
2126784101241903|2012|Ford Fusion|SEL|3500|208000|Lawrence, KS|30|unknown||
3290403307832986|2015|Nissan Altima|2.5 S|5499|149650|Kansas City, MO|30|clean||
2333595197382588|2016|Hyundai Sonata|Limited|5700|122000|Lee's Summit, MO|31|unknown||
1423124856353466|2013|Infiniti M37x||5500|156000|Lee's Summit, MO|31|rebuilt||
1027696096951487|2008|GMC Acadia|SLT-1|4400|176000|Independence, MO|30|clean||같은 차 2건 게시
1000213729750895|2011|Dodge Ram 1500|SLT|4500|211000|Kansas City, MO|30|clean||엔진 경고등 기재
1035942782665691|2018|Ford F-150|FX4|850|111111|Kansas City, KS|32|unknown||
2347563279404650|2010|Audi A4|2.0T Quattro Premium|5950|125000|Kansas City, MO|34|clean||
1583002246797151|2014|Audi A4|2.0T Quattro Premium|6600|171000|Smithville, MO|34|clean||
1774854490524930|2019|Kia Optima|LX|6700|119000|Olathe, KS|36|rebuilt||
2635764136856202|2013|Audi Q5|2.0T Quattro Premium|5000|170000|Kansas City, KS|36|clean||
1037602252198075|2012|Cadillac SRX|Performance Collection|5950|140101|Kansas City, MO|36|clean||
1744206267301888|2018|Hyundai Elantra|SE|6200|151000|Olathe, KS|37|clean||
1098731549217414|2012|Volkswagen Passat|TDI SEL Premium|6000|240000|Belton, MO|37|clean||
1073217041807712|2009|Chevrolet Malibu|LTZ|1000|179768|Kansas City, MO|41|clean|avoid|엔진 수리 필요 기재
2208175490039243|2012|Jeep Liberty|Limited|5500|159019|Kansas City, MO|42|clean||
1398853678842954|2014|Hyundai Elantra||3400|177000|Raytown, MO|42|clean||
1496969318933283|2026|Chevrolet Silverado 2500HD||2500||Basehor, KS|42|unknown||
1062655326224107|2019|Chevrolet Equinox|LT|5500|195000|Lenexa, KS|42|clean||
4467107836952699|2011|Toyota Sienna||4900|199000|Grandview, MO|43|clean||
1022603370682809|2015|Kia Soul|!|4200|149771|Kansas City, KS|43|clean||
2352504888627937|2010|Nissan Rogue|SL|4450|194000|Kansas City, MO|43|clean|dealer|
1838987890420294|2013|Kia Optima|EX|3999|173715|Belton, MO|44|clean||
1338906748396983|2014|Ford Fusion|SE|3900|109246|Kansas City, MO|45|clean||엔진 경고등 기재
1771532700541094|2013|Ford Fusion|Titanium|6950|116357|Kansas City, MO|46|rebuilt||
1358767769770190|2014|Nissan Altima|2.5 S|2300|221566|Lee's Summit, MO|49|clean||AS IS 판매
1365347782329408|2008|Isuzu i-290|4*2|1700|1800|Kansas City, KS|51|clean||
2567089177046575|2016|Chevrolet Trax|LS|5800|160000|Kansas City, KS|51|clean||
1412062474190073|2013|Chevrolet Equinox|LS|3000|200773|Creighton, MO|53|unknown||
1755764432344421|2018|Kia Niro||6000|200000|Overland Park, KS|53|clean||
1368561311287372|2023|Ford F-250||800|220000|Kansas City, MO|53|unknown||
2338027183397878|2020|Ford F-150||500|2000|Oak Grove, MO|53|unknown||
1266901738733468|2011|Dodge Nitro|SE|850|135680|Blue Springs, MO|54|unknown|avoid,dealer|운행·시동 불가 기재
27607375538903147|2016|Jeep Cherokee||2590|130000|Kansas City, MO|54|clean||
2112653346266710|2021|Jeep Grand Cherokee|Laredo|750|100000|Kansas City, MO|55|unknown||
1929976524318375|2010|Kia Sedona|L|1500|304399|Shawnee, KS|56|clean||
1318370236950052|2019|Kia Forte|FE|6500|112000|Grain Valley, MO|58|salvage||
1352568660342299|2013|Kia Optima|LX|3900|173463|Kansas City, MO|59|unknown||
2036580543625316|2011|Volkswagen Touareg|V6 Executive|4500|202540|Kansas City, MO|62|clean||엔진 경고등 기재
1339998984971314|2018|Ford Escape|St line|3500|163222|Kansas City, KS|69|clean||
1774911073939769|2016|Volkswagen Jetta||6950|180000|Kansas City, MO|70|clean||
1011809788367178|2024|Jeep Wrangler|All New Rubicon|500|9000|Kansas City, MO|70|unknown||
1968580233824650|2014|Ford Focus|Se|3200|184500|Kansas City, MO|70|unknown||
868271596040047|2015|Hyundai Sonata|Sport|5300|148740|Kansas City, MO|73|clean||
2008958796478315|2012|Chevrolet Malibu|LT|1234|160000|Kansas City, KS|73|unknown||
1238099661653330|2013|Ford Escape|SE|1234|203900|Independence, MO|80|clean||누유·누수 기재
3007882212887802|2016|Volkswagen Jetta|TSI|6500|140000|Grain Valley, MO|83|clean||
1532247451686907|2013|BMW 5 Series|528i xDrive|5000|146000|Kansas City, MO|83|clean||
1365161118400020|2013|Nissan Sentra||5760|110000|Kansas City, MO|84|clean||
1680897149824890|2009|Honda Civic|LX|3000|18350|Kansas City, MO|88|clean||
1005318698577936|2015|Volkswagen Passat|1.8T Limited Edition|6899|90200|Kansas City, MO|96|salvage||
1527752072334847|2016|Hyundai Accent|GL|3000|115000|Kansas City, KS|97|salvage||
972334538745857|2010|Ford 550||6500||Greenwood, MO|99|unknown||
1765420771561297|2018|Ford Focus|SE|4000|131000|Independence, MO|99|unknown||
998857836101090|2012|Chevrolet Silverado 1500||3000|245139|Kansas City, MO|100|clean||AS IS 판매
944956205200399|2013|Dodge Dart|SE|5500|109000|Kansas City, MO|100|unknown||같은 차 3건 게시
3631057503701134|2013|GMC Terrain|SLE-2|6950|176832|Spring Hill, KS|104|clean||
1010180284778088|2012|Ford Edge|SEL|3400|268000|Leavenworth, KS|122|unknown||
1011221374911315|2016|Toyota Camry|LE|6900|195000|Kansas City, MO|137|clean||
2073989450139421|2014|Kia Optima||4300|140000|Kansas City, MO|138|clean||
1335520128471477|2009|Audi Q7|3.0 TDI Quattro Premium|6650|158000|Kansas City, MO|141|clean||엔진 경고등 기재
1444671833400162|2018|Chevrolet Cruze|1LT|6900|146707|Harrisonville, MO|161|unknown||
3330801540413062|2012|Ford Escape|XLT|6999|207287|Olathe, KS|163|clean||
1426312979453008|2013|Nissan Pathfinder|LE Platinum Edition|4750|153000|Leavenworth, KS|0|clean||
1803698441054322|2014|BMW Series||4500|149000|Independence, MO|0|unknown||
2182623002691136|2012|Chevrolet Malibu||4500|192000|Orrick, MO|0|clean||
2065076857468446|2013|Chevrolet Sonic|LT|5300|95100|Gardner, KS|0|clean||
1114024894896725|2016|Dodge Journey||5000|101200|Lee's Summit, MO|1|unknown||AS IS 판매
1364638569053449|2009|Ford Crown Victoria||4600|120000|Olathe, KS|2|unknown||
2245974782910628|2010|Ford Crown Victoria|P71|4000|182000|Olathe, KS|2|clean||
1291081024094334|2017|Chevrolet Sonic|LT-RS|4999|164000|Kansas City, MO|2|clean||
1035521649507857|2015|Chevrolet Equinox||5000|15326|Overland Park, KS|3|rebuilt||
1797232721410514|2009|Ford Edge||4200|205000|Overland Park, KS|3|clean||
2044049726474748|2012|GMC Acadia|Denali|4800|157000|Olathe, KS|3|clean||
1676246304177149|2012|Dodge Ram 1500|Sport|4000|218000|Raymore, MO|3|unknown||AS IS 판매
1616094686974600|2015|Nissan Altima||5000|163000|Kansas City, MO|3|clean||
1724439578662127|2010|Mercedes-Benz E-Class|E 350 4MATIC|4950|183139|Overland Park, KS|3|clean||AS IS 판매
942073042292423|2012|Cadillac SRX|Premium Collection|4400|190000|Olathe, KS|3|rebuilt||
1575059241085551|2014|Hyundai Elantra||4300|144000|Overland Park, KS|3|clean||
2501136607047953|2011|Chevrolet Impala|LT|4500|180000|Gardner, KS|3|clean||누유·누수 기재
1095209343441551|2011|Honda Odyssey|EX-L w/DVD Res|4300|227000|Kansas City, MO|3|clean||
1834427944240004|2013|Acura TL|SH-AWD|4500|158638|Kansas City, MO|4|unknown||
1430345065623853|2010|Mazda3||4790|179520|Kansas City, MO|4|clean||
4518195105121297|2014|Volkswagen Jetta|2.0L S|5300|149000|Kansas City, MO|4|clean||
1432457768697434|2012|Acura TL||4500|197000|Lee's Summit, MO|4|clean||
1738371097416476|2009|Honda Accord|EX-L|4500|167048|Kansas City, KS|5|clean||
1564058995754069|2012|Ford F-150|XLT|4200|242000|Kansas City, KS|5|rebuilt||엔진 경고등 기재 · 누유·누수 기재 · AS IS 판매
1424909272893189|2013|Mercedes-Benz C-Class||4950|170000|Belton, MO|5|rebuilt|dealer|
1086523550495864|2012|Jeep Patriot|Latitude|4599|137501|Grandview, MO|6|unknown|dealer|
1832036348159375|2016|Nissan Rogue|SL|5450|183550|Gardner, KS|6|unknown||
1439800284954550|2013|Ford Escape||4200|181683|Kansas City, KS|6|clean||
1572808923828680|2010|Nissan Altima||5000|150466|Kansas City, KS|6|unknown||설명 없음
937284135627996|2008|Lexus IS|IS 250 Sport|4250|246037|Odessa, MO|7|clean||
1694573986003369|2008|Ford Crown Victoria||4500|138819|Olathe, KS|7|clean||
1992714188113952|2010|Chevrolet Equinox|LT|4499|168000|Kansas City, MO|7|clean||엔진 경고등 기재 · AS IS 판매
1790573715588734|2015|Ford Focus|S|4200|130000|Independence, MO|7|unknown||
1631909454945234|2008|Chevrolet HHR||4995|183894|Liberty, MO|8|clean|dealer|
39526163466970719|2013|Jeep Wrangler|Sport S (JK)|4000|139000|Independence, MO|8|unknown||
1080975944811231|2011|BMW 3 Series|328i|5000|11700|Olathe, KS|8|unknown||
1608385300789853|2014|Ford Taurus||4850|162358|Kansas City, MO|9|unknown||
1328503989360019|2011|Hyundai Santa Fe|GLS|5350|108000|Kansas City, MO|9|unknown||
991330150649354|2013|Infiniti G37|X|5000|188000|Kansas City, MO|9|unknown||
1100912379344870|2014|Hyundai Sonata|Sport 2.0T|4550|150000|Kansas City, MO|10|clean||
1062695553315217|2010|Kia Soul|!|4500|177000|Kansas City, MO|11|clean||
1054865723849455|2012|Chevrolet Equinox|LT|4000|15000|Kansas City, MO|11|clean||
1613885840150661|2008|Toyota Prius||5400|154000|Olathe, KS|11|clean||
1074016641877109|2008|Lexus GS||4000|250000|Overland Park, KS|11|clean||
1855681439142883|2013|Ford Escape|SE|4950|123959|Kansas City, MO|12|rebuilt||
1373289827844842|2017|Land Rover Discovery Sport|HSE LUX|4200|121000|Kansas City, MO|12|clean|avoid|엔진 수리 필요 기재
1601827044985523|2010|Dodge Avenger|Express|4000|192000|Olathe, KS|12|unknown||
1615701863623444|2016|Chevrolet Equinox|LT|5000|133000|Kansas City, MO|12|clean||
2137905223816218|2013|Toyota Avalon||4500|172000|Kansas City, MO|13|clean||
2112540076324615|2011|Mercedes-Benz C-Class|C 300 4MATIC Sport|5000|179000|Kansas City, MO|14|clean||
1453287753622421|2018|Chevrolet Malibu|2LT|4000|210000|Lee's Summit, MO|14|clean||
2000061520662095|2013|Buick Regal|Premium 2|4000|176000|Kansas City, MO|14|rebuilt||
1687070159062091|2014|Volkswagen Passat|1.8T SE|4500|170000|Kansas City, KS|15|clean||우박 이력
1061557099955571|2016|Ford Fusion|SE|5350|190272|Lee's Summit, MO|15|clean|dealer|
3431712530331704|2010|Nissan Sentra|SR|4000|140000|Kansas City, MO|15|unknown||
1386265323020199|2010|Nissan Altima|2.5 S|4299|151793|Grandview, MO|15|unknown|dealer|
1065308282922884|2008|Chevrolet Suburban|LS|4500|195000|Kansas City, MO|15|unknown||
837073559426716|2014|Volkswagen Passat|TDI SE|5000|135000|Garden City, MO|16|clean||
2808975546138316|2014|Mazda CX-5||5000|196000|Overland Park, KS|16|clean||
1555534446313545|2015|Chevrolet Equinox|LT|4271|153055|Kansas City, MO|17|unknown||
2544873885976730|2009|Honda CR-V|EX-L|5300|212875|Independence, MO|17|unknown||
1548243336627968|2008|Toyota Grand Highlander|MAX Limited|4300|293000|Kansas City, KS|18|clean||
937581652730714|2013|Ford Escape|SE|5200|156000|Lenexa, KS|18|clean||
2159791044939519|2014|Nissan Altima|2.5 S|4500|196000|Independence, MO|19|clean||
4487576054815522|2014|Jeep Compass||4700|147087|Independence, MO|19|clean||
1060353953553811|2012|Audi A3||5000|160000|Independence, MO|18|unknown||누유·누수 기재 · AS IS 판매
1692546588479579|2014|Jeep SRT|Jeep|5000|1000|Kansas City, MO|19|clean||
1547126906614146|2011|Toyota Prius||4500|224152|Independence, MO|20|unknown||
1606659014369689|2012|Jeep Grand Cherokee||4000|228569|Kansas City, MO|20|unknown||설명 없음
1316662203701276|2009|Chevrolet Malibu|1LT|5200|140000|Overland Park, KS|21|unknown||
2379427832465506|2013|Ford Focus|SE|4500|143157|Independence, MO|21|clean|avoid|엔진 수리 필요 기재
2630718850758140|2015|Kia Soul||4990|157000|Kansas City, MO|21|clean||
1057179073591807|2012|Chevrolet Cruze|L|5250|99000|Kansas City, KS|22|unknown||
2046619702646786|2016|Nissan Versa|SV|4300|203000|Kansas City, KS|15|clean||
1063605066248931|2016|Ford Focus||4000|138000|Independence, MO|22|unknown||
28096385323352271|2014|Ford Explorer||4999|214480|Belton, MO|23|clean|dealer|
1623886809174596|2013|Toyota Prius||4000|250723|Kansas City, MO|23|unknown||
1078832484730016|2010|Dodge Journey||4000|180000|Olathe, KS|23|unknown||설명 없음
1510562227506364|2013|Ford Focus|SE|4000|150000|Lee's Summit, MO|28|unknown||
1708475253548713|2012|Chevrolet Cruze|LT|4300|100814|Kansas City, MO|28|clean||
1531847831580747|2015|Audi A4|2.0T Quattro Premium|4500|85415|Independence, MO|28|clean||
1392744056393634|2014|Dodge Journey||4700|100000|Kansas City, MO|28|unknown||
2160840284867688|2011|Toyota Prius||4000|203000|Independence, MO|29|unknown||
1807216430700135|2016|Dodge Journey|Crossroad|4500|175581|Independence, MO|29|clean||
2410907206104016|2013|Ford Escape|SE|4500|149861|Independence, MO|29|clean||
1785434449548295|2010|Audi A6|3.0T Prestige|4000|192000|Kansas City, MO|31|clean||
1410186834375876|2010|Ford Fusion|Sport|5000|280000|Kansas City, MO|31|unknown||
2163594124218074|2014|Toyota Prius|LE|4500|243000|Belton, MO|31|clean||
1461925385984916|2011|Toyota Camry|LE|4000|240250|Overland Park, KS|31|clean||
1577703050768505|2019|Ford Fiesta|SE|4500|132633|Kansas City, KS|32|clean||
1536189757823875|2011|Toyota Prius||4000|202000|Independence, MO|32|clean||
1053411294342774|2010|Ford Edge||4500|127000|Independence, MO|32|unknown||
1035466875788425|2014|Toyota Prius|V Five|4500|203000|Kansas City, MO|33|clean||
992316590508417|2014|Kia Forte|EX|4950|178234|Bates City, MO|35|unknown||
1809441293383095|2012|Ford Edge|SEL|5000|161000|Kansas City, MO|36|clean||
2022306749171917|2013|Kia Soul||4500|130240|Kansas City, MO|37|clean||같은 차 2건 게시
4049221155208816|2010|Chevrolet Silverado 1500||5400|202000|Peculiar, MO|38|unknown||
2377096422817506|2012|Ford Fusion|SEL|4800|204153|Blue Springs, MO|39|unknown||
1048238578133448|2017|Ford Focus|SE|5000|90000|Kansas City, MO|39|unknown||
2296834674054252|2013|Subaru Crosstrek|Premium|5000|225000|Overland Park, KS|42|clean||
1101987695582949|2016|Ford Fusion|Titanium|5000|215017|Kansas City, MO|42|clean||
1055414620193475|2014|Chrysler Town & Country||4500|179850|McLouth, KS|44|unknown||
1391065879618591|2014|Ford Fusion||4000|203000|Freeman, MO|44|unknown||
2478257889316575|2016|Audi A6|2.0T Premium Plus|4000|249578|Kansas City, MO|46|unknown||
1061518866736223|2016|Kia Rio||4300|175000|Blue Springs, MO|47|unknown||
1027979540011956|2013|Hyundai Sonata||4000|166000|Kansas City, MO|48|unknown||
1592084362461315|2012|Ford Fusion|SE|5000|187000|Kansas City, MO|49|unknown||우박 이력
2850403755456411|2008|Toyota Camry||4000|159000|Independence, MO|49|clean||
1026068026923327|2011|Mercedes-Benz M-Class||5400|165300|Lenexa, KS|51|unknown||
27742898898701214|2011|BMW X3|sDrive28i|4000|247567|Kansas City, KS|53|clean||
1576568767415957|2011|Chevrolet Cruze|2LT|5000|103500|Lawrence, KS|56|unknown||
1722651398629496|2016|Volkswagen Passat||4900|175285|Liberty, MO|58|clean||AS IS 판매
27682212574763354|2016|Kia Forte|LX|4700|166450|Kansas City, KS|59|unknown||설명 없음
3321194808081751|2019|Kia Sorento|EX|4000|280590|Kansas City, MO|65|unknown||
1057815956934128|2014|Nissan Altima|2.5 SV|4500|164000|Kansas City, MO|65|unknown||
1851412996201031|2010|Chrysler Sebring||4600|117938|Olathe, KS|67|rebuilt||
2935395250143691|2015|Kia Forte|LX|5000|226452|Kansas City, MO|69|unknown||
1751437916206897|2010|Nissan Altima|2.5 S|4100|142000|Kansas City, MO|69|clean||
27718372237759254|2016|Ford Escape|SE|5000|173484|Lenexa, KS|70|unknown||
1355576260038856|2012|Honda Civic|LX|4500|180000|Blue Springs, MO|71|rebuilt||
2217478482369977|2016|Ford Fiesta|SE|4500|175000|Grandview, MO|71|clean||
1331136268686298|2014|Kia Forte|LX|4000|102515|Overland Park, KS|72|clean||
1555677029495809|2009|GMC Yukon||4800|300000|Leavenworth, KS|73|unknown||엔진 소음 기재
1532919855200245|2016|Nissan Versa|S|4999|130000|Olathe, KS|77|clean||
1436049415212984|2013|Nissan Rogue|SV|4500|123705|Shawnee, KS|87|rebuilt||
1765092978259615|2016|Hyundai Accent|SE|4800|95600|Smithville, MO|93|rebuilt||
1698884848031351|2017|Volkswagen Jetta|1.4T S|4999|195510|Kansas City, MO|99|clean||
2396656464141444|2017|Infiniti QX60|3.5|5000|156786|Kansas City, MO|147|clean||엔진 경고등 기재
1379049296931825|2012|Nissan Altima||4500|162608|Kansas City, KS|77|clean||AS IS 판매
1616448253602581|2016|Ford Explorer||5500|115503|Independence, MO|0|clean||
1740605857196722|2015|Dodge Durango|SXT|6500|171400|Kansas City, MO|0|clean||
28028745083474535|2011|GMC Acadia|SLT|6550|125000|Kansas City, MO|0|clean||
1296397093564354|2015|Hyundai Santa Fe Sport||6450|150500|Kansas City, MO|1|clean||
1872040034154609|2013|Chevrolet Express||6000|199874|Tonganoxie, KS|1|clean||
1144819881233805|2008|Nissan 350Z|Enthusiast|6500|213000|Lenexa, KS|1|unknown||
1813333060095565|2018|Jeep Cherokee||6985|172741|Kansas City, MO|2|unknown|dealer|
3105013353028819|2019|Dodge Ram 1500|Tradesman|5750|241000|Kansas City, MO|2|clean||
2066474890730523|2019|Dodge Grand Caravan|GT|6500|153919|Kansas City, MO|2|clean||
3432462340294008|2013|Kia Rio|LX|6000|75600|Kansas City, KS|2|unknown||
1523535689806044|2011|BMW 5 Series|535d xDrive|5999|169000|Kansas City, MO|2|unknown||
1819454262509121|2013|Dodge Ram 1500||5500|254886|Eudora, KS|2|unknown||엔진 경고등 기재
1527933652431465|2013|Nissan Sentra|S|6800|133000|Lee's Summit, MO|2|clean||
1413390297428604|2013|Chevrolet Tahoe|LS|5500|216374|Kansas City, MO|3|unknown||
1091720320003789|2016|Ford Explorer||6300|176000|Kansas City, KS|3|clean||
2046783399355249|2008|BMW 3 Series|335i|6500|135000|Kansas City, KS|3|unknown||
1066042833081998|2013|Ford Edge|Limited|5800|122700|Kansas City, MO|3|salvage||
1052681761011892|2008|Toyota Camry|XLE|5950|161211|Kansas City, MO|4|clean||
1077673055229315|2016|GMC Acadia|SLT|6200|203000|Raytown, MO|6|rebuilt||
1408163601290064|2010|Lincoln MKT||5950|170937|Mission, KS|6|clean||
4504694349797205|2019|Chevrolet Equinox|Let|6500|137900|Independence, MO|6|unknown||
1373645501197466|2015|Jeep Cherokee||6850|163246|Kansas City, MO|7|clean||
2515307849290737|2014|Ford Focus|SE|6000|104995|Kansas City, KS|7|clean|dealer|다운페이·할부 광고
4590729397877898|2011|Chevrolet Silverado 1500||6500|238000|Bonner Springs, KS|7|unknown||
2147725136178106|2009|Toyota Corolla||5500|338000|Lenexa, KS|7|clean||
2105818806995884|2013|Chevrolet Silverado 2500HD|WT|5500|172641|Kansas City, MO|8|clean||
2472796633213003|2014|Volkswagen Passat|1.8T Wolfsburg Edition|5950|182813|Bates City, MO|9|unknown||
1425622796177388|2011|Honda CR-V||5500|213000|Kansas City, MO|10|clean||
1791355802125835|2014|Dodge Charger|R/T|6200|136000|Kansas City, KS|10|rebuilt||
28415993334707218|2020|Chrysler Pacifica|Limited|5500|175000|Overland Park, KS|10|clean||엔진 경고등 기재 · AS IS 판매
1069079055860546|2013|Jeep Grand Cherokee|Overland|6400|166700|Shawnee, KS|10|clean||
1514688953830714|2012|Chevrolet Cruze|LS|5800|53000|Shawnee, KS|10|clean||
1042268158800869|2013|Dodge Ram 1500|SLT|6000|180000|Kansas City, MO|10|unknown||
3357638544407800|2014|Nissan Maxima|SV|6500|147700|Lee's Summit, MO|10|clean||
1607751881005767|2013|Nissan Murano|SV|6500|125000|Liberty, MO|11|unknown||
1069780735777657|2014|BMW 3 Series|328i|5999|180000|Grain Valley, MO|11|clean||
1124173243387415|2009|Dodge Sprinter|Standard Roof w/144" WB|6750|250000|Belton, MO|11|unknown||AS IS 판매
1103308659326275|2014|Ford Explorer|XLT|6400|157283|Raymore, MO|12|clean||
1343642227576273|2015|Ford Explorer||6000|140000|Kansas City, KS|12|clean||
1402691808034779|2017|Kia Sportage|LX|6900|129000|Kansas City, MO|13|clean||
1078257947948798|2013|GMC Acadia|SL|6850|149166|Olathe, KS|13|clean||
1065940486185965|2021|Nissan Rogue Sport|S|6600|142000|Kansas City, KS|14|salvage||
1746646369724063|2017|Chevrolet Malibu||6990|150447|Kansas City, MO|14|unknown|dealer|다운페이·할부 광고
1112804855056193|2010|Toyota Venza||6995|183500|Harrisonville, MO|15|clean||
2078536122766140|2012|Chevrolet Malibu|LT|5500|130000|Pleasant Hill, MO|16|clean||
4619870131581724|2014|Mercedes-Benz C-Class|C 300 4MATIC|6500|155000|Gardner, KS|17|clean||
1738423104071472|2015|Chevrolet Impala|LTZ|5599|198000|Overland Park, KS|17|unknown||
1382382280774924|2009|Chevrolet Silverado 1500|Long Bed|6500|2000|Kansas City, MO|17|clean||
1081242670966565|2008|MINI Cooper||5800|99828|Lenexa, KS|17|clean||
4421100824796811|2014|BMW 3 Series||6200|148000|Grandview, MO|18|clean||
1838638330630549|2012|Kia Sorento|EX|5700|163222|Kansas City, MO|18|unknown||
1048119994506588|2019|Ford Fusion|SE Hybrid|6950|189000|Kansas City, MO|20|clean||
1623289026182170|2009|Dodge Challenger||6500|208919|Independence, MO|20|clean||설명 없음
1044225945123167|2017|Volkswagen Jetta|1.4T S|5500|166000|Kansas City, MO|21|unknown||
1110906751280817|2015|Kia Sorento|LX|6000|143000|Kansas City, MO|21|unknown||같은 차 2건 게시
1052255297616941|2011|Mercedes-Benz GLK-Class|GLK 350 4MATIC|6500|145000|Lee's Summit, MO|21|clean||엔진 경고등 기재
1965704697439996|2016|Kia Sorento|LX|6995|144000|Independence, MO|22|clean||
1548686603674440|2013|Ford Fusion||6950|135000|Belton, MO|23|clean|dealer|
1591823999115222|2016|Jeep Cherokee|Latitude|6900|123520|Overland Park, KS|23|unknown||
27625701290466360|2011|Chevrolet Impala||5995|171074|Liberty, MO|23|clean||
1040997462093313|2015|Chevrolet Cruze|LT|6800|104805|Pleasant Hill, MO|23|unknown||
952454351232412|2013|Hyundai Veloster||5950|150000|Belton, MO|23|clean|dealer|
1223551856611441|2008|Ford Escape|Limited|6000|161000|Prairie Village, KS|24|unknown||
2941661996177931|2018|Hyundai Santa Fe|Santa Fe Sport|6250|169000|Overland Park, KS|24|clean||
1964590970921756|2011|Volkswagen CC|2.0T Sport|5900|140000|Kansas City, KS|24|clean||
2292623264611769|2014|Buick Regal|Gran Sport|6500|230946|Independence, MO|24|clean||
1403330841769707|2015|Chrysler 200|200C|6499|81000|Kansas City, MO|25|clean|dealer|
2016166959043036|2012|Chevrolet Camaro|LT|6500|185917|Independence, MO|26|unknown||
1711680706760869|2018|Nissan Altima|2.5 SV|5500|117657|Kansas City, KS|27|salvage||
1631966551706744|2020|Dodge Journey|AVP|6200|110000|Ottawa, KS|27|unknown||
1775448096926179|2018|Nissan Rogue||5950|167781|Kansas City, MO|27|clean||
1095901259669254|2012|Toyota Prius||5950|205780|Kansas City, MO|28|clean||
1364379989097020|2013|Infiniti QX56||6900|241000|Belton, MO|28|clean|dealer|
1760527685195233|2013|Volvo XC60|T6 AWD, 3.0L Turbo|5700|156955|Kansas City, KS|28|clean||
1697804544618617|2014|Nissan Rogue Select|S|5800|111249|Shawnee, KS|29|rebuilt||
1535117957928778|2016|Hyundai Elantra|SE|6000|170000|Liberty, MO|29|unknown||
1441711061347543|2011|Hyundai Sonata||5995|131375|Lee's Summit, MO|30|unknown||
2824310367943324|2014|Nissan Frontier||6200|173600|Lee's Summit, MO|30|clean||
1075902738497703|2010|Honda Civic||6500|183000|Leavenworth, KS|31|clean||
1311923727486517|2012|Ford Escape|XLT|5995|110580|Kansas City, MO|31|clean||
934095929741947|2017|Nissan Rogue Sport|SV|5900|148500|Kansas City, MO|32|clean||
1419830313332663|2018|Ford EcoSport|SE|6000|154785|Kansas City, KS|32|clean|dealer|다운페이·할부 광고
1381514794182123|2012|Kia Optima|EX|6600|131000|Kansas City, MO|32|clean||변속기 이상 기재 · 우박 이력
1724205795452220|2017|Dodge Grand Caravan||5600|165000|Kansas City, MO|33|clean||
2251639375690831|2014|Honda Accord|EX-L|6000|174500|Olathe, KS|33|clean||
1096786279585713|2012|BMW 5 Series|528i xDrive|6500|132000|Kansas City, MO|33|unknown||
1038592862308293|2013|Hyundai Elantra||6500|100000|Belton, MO|34|clean|dealer|
1335697468334005|2018|Ford Fiesta|S|6000|100650|Independence, MO|35|unknown||AS IS 판매
1377499791190272|2018|Dodge Grand Caravan|SXT Plus|5700|214000|Gardner, KS|36|clean||
1638764024405787|2013|Chevrolet Silverado 1500||6500|2000|Kansas City, KS|37|clean||
1596430482131359|2015|Kia Sorento|LX|6999|100000|Kansas City, KS|37|clean|dealer|
27939527695703959|2018|Jeep Cherokee||5999|161000|Grandview, MO|38|clean|dealer|우박 이력
983759801348924|2012|BMW 3 Series|328i|5500|98500|Shawnee, KS|38|clean||
2299768554124758|2019|Dodge Grand Caravan|SXT|5500|150101|Kansas City, MO|39|clean||
1037425579178538|2018|Hyundai Elantra|SE|6200|151491|Olathe, KS|39|clean||
1390137059737797|2013|Honda Odyssey||6999|193153|Belton, MO|39|clean|dealer|
4463742457226030|2017|Ford Focus|SE|5750|100800|Kansas City, MO|40|clean||
1587513492749189|2017|Jeep Compass|Latitude|6500|136304|Olathe, KS|42|unknown||
1381209837224217|2015|Ford Focus||5999|108365|Belton, MO|44|clean|dealer|
3572575142889633|2010|BMW 3 Series|328i xDrive|6500|178000|Independence, MO|46|unknown||
2635397386931229|2011|Chevrolet Avalanche|LS|5500|186000|Kansas City, KS|50|unknown||
1838605894246563|2011|Mercedes-Benz E-Class|E 350|6500|181889|Kansas City, MO|52|clean||
1354593570095334|2017|Nissan Murano|SL (2017.5)|6990|149000|Kansas City, MO|54|clean||
1594011382387305|2015|Volvo XC60|T5|5950|160000|Overland Park, KS|55|clean||
1915479255805914|2015|Hyundai Tucson|GL|6900|119000|Kansas City, MO|59|unknown||
1328496845712336|2014|Chrysler Town & Country|Touring|6800|140398|Grain Valley, MO|61|unknown||
2104959957099767|2013|Chevrolet Cruze|LT|5500|95000|Shawnee, KS|63|salvage||엔진 경고등 기재
1018871394092000|2013|Ford Fusion|Luxury|6000|101254|Olathe, KS|64|clean||
1695099875096105|2021|Chevrolet Trax||6500|123284|Kansas City, MO|64|clean||
2388893091520670|2008|BMW iX|528 ix|5800|106799|Kansas City, KS|64|clean||
2787288098321709|2016|Chevrolet Traverse||6500|172985|Grandview, MO|77|clean|dealer|
1673434263774449|2016|Ford Escape||5990|126207|Kansas City, KS|83|unknown||
2553277771803867|2013|Dodge Dart|SXT|5500|109600|Kansas City, MO|100|clean||
1656492608949714|2013|Hyundai Sonata|Limited|6950|111000|Kansas City, MO|103|clean||
1512594413782454|2018|Ford Escape|S|5500|113000|Independence, MO|104|unknown||
2248889715863035|2010|Nissan Murano|SL|5950|127282|Grandview, MO|110|clean||
3491731014325285|2011|BMW Series||5900|149615|Kansas City, KS|117|clean||
2414976395638630|2016|Kia Forte|LX|6500|101000|Odessa, MO|131|unknown||
2924520761243665|2009|Ford Edge|Limited|3000|158626|Kansas City, MO|0|clean||
1110211035027786|2011|Chevrolet Malibu|Lt|3000|185946|Kansas City, KS|0|unknown||
2561971250964940|2013|Scion tC||2500|157000|Kansas City, MO|0|clean||엔진 경고등 기재 · 변속기 이상 기재
1114187544391603|2008|Volkswagen Jetta|2.0L|2400|235000|Kansas City, MO|0|clean||
1460855409233640|2008|BMW 5 Series|535i xDrive|2600|145000|Raytown, MO|0|clean||
1103418142103164|2013|Ford Fiesta|S|2300|17600|Raytown, MO|0|unknown||
2185147845762073|2008|Jeep Liberty|Limited Jet Edition|3600|155650|Kansas City, KS|0|unknown||같은 차 2건 게시
1070121092529297|2010|Ford Escape|XLT|3795|161704|Smithville, MO|1|unknown||
1749138833011526|2012|Chevrolet Cruze|2LT|3500|191000|Kansas City, KS|1|clean||우박 이력
2350868372114811|2015|GMC Terrain||3900|166550|Olathe, KS|1|rebuilt||
1641049994237803|2008|Honda Odyssey|EX|2700|246000|Lawrence, KS|1|unknown||
1031242979957497|2013|Chevrolet Equinox|LT|3300|150000|Raytown, MO|1|clean||
1081366127982004|2009|Honda CR-V||3700|240000|Kansas City, MO|2|unknown||
1623582415828675|2019|Nissan Sentra|SR|3500|218920|Kansas City, MO|2|unknown||
1646793196868825|2011|Chrysler 200|200C|2200|263216|Kansas City, MO|2|unknown||
2138072400078554|2011|Ford Fusion||3300|180000|Kansas City, MO|2|unknown||
1065119496426823|2019|Nissan Versa|SV|2999|136532|Kansas City, MO|2|clean||
953449267806288|2008|Nissan Altima|2.5 S|2000|242839|Belton, MO|2|unknown|avoid|운행·시동 불가 기재
2549852222105367|2012|Mazda CX-9||3500|163296|Lenexa, KS|3|unknown|avoid|변속기 수리 필요 기재
1577466187492632|2015|Chevrolet Cruze|LT|3800|168000|Blue Springs, MO|3|clean||
2054238031964349|2014|Hyundai Sonata||3500|165827|Kansas City, KS|4|salvage||
1600855744863949|2009|Hyundai Sonata|GLS|2450|258000|Kansas City, MO|4|clean||
1394814132822679|2011|Honda Accord|EX-L|3200|250000|Raymore, MO|4|clean||
1791132615350865|2008|Chevrolet Colorado|LT|2500|183000|Kansas City, MO|4|clean||
933923699782030|2009|Lincoln MKS||3500|207000|Grain Valley, MO|4|unknown||
1669365404698711|2016|Dodge Grand Caravan|SXT|3995|195239|Kansas City, MO|5|unknown|dealer|
2348204075587545|2012|Chevrolet Impala|Ls|3299|202000|Platte City, MO|5|unknown||AS IS 판매
937010945622699|2016|Chrysler 200|200S Alloy Edition|3500|180000|Raytown, MO|5|clean||
2805317719855183|2008|Ford F-150|XLT|2250|224492|Lee's Summit, MO|5|unknown||
1072702378948832|2013|Dodge Avenger|SXT|3200|135550|Lee's Summit, MO|5|clean||
2102617541132941|2014|Ford Focus|SE|3700|91523|Shawnee, KS|6|rebuilt||
1115947778053702|2012|Buick Verano||2500|162844|Independence, MO|6|clean||
1770794027158023|2010|Chevrolet Cobalt|LT|3000|213000|Harrisonville, MO|7|unknown||
1293729842763148|2011|Hyundai Sonata|SE|2400|219000|Kansas City, MO|8|clean||
1773058144023429|2011|Ford Focus|SEL|3000|164000|Grain Valley, MO|8|rebuilt||
1061915663330353|2010|Ford Fusion|17r|2500|229000|Grandview, MO|9|clean||
1671541807676574|2010|Nissan Altima|2.5 SL|2000|160000|Raymore, MO|9|unknown||
2498429380633920|2008|Chevrolet Impala||2800|206125|Harrisonville, MO|10|clean||
2158730938044139|2014|Ford Focus|SE|3600|116000|Kansas City, MO|10|salvage||
1100941802384836|2008|Chrysler Town & Country||2500|159000|Rantoul, KS|10|unknown||
4469638676632035|2012|Ford Edge|SEL|3900|199999|Belton, MO|10|clean||설명 없음
1802619737838559|2014|Chevrolet Cruze|Premier|3375|204675|Independence, MO|10|unknown||
1398424891660899|2014|Dodge Grand Caravan||3500|170000|Princeton, KS|11|unknown||
1223211923343779|2010|Dodge Journey||2500|217000|Kansas City, KS|11|unknown||
1723868575376573|2017|Nissan Versa||3495|148387|Kansas City, KS|12|clean||
1611180940634566|2015|Nissan Pathfinder||2800|173000|Kansas City, MO|12|clean||
1462562605937533|2013|Chrysler 200|Touring|3750|179755|Kansas City, MO|13|clean||
2067317677323669|2012|Ford Focus||2800|180000|Independence, MO|13|clean||
1482697833684763|2027|Hyundai Sonata|Eco|2600|210000|Kansas City, MO|13|clean||
1756427649018497|2013|Chrysler 200|200C|3599|190852|Independence, MO|13|clean||
939681601947085|2010|Nissan Altima|2.5 SL|2800|219221|Grain Valley, MO|14|clean||
1694647624972311|2013|Chevrolet Equinox||3000|180000|Overland Park, KS|14|unknown||
1609055034200696|2008|Lexus ES|ES 350 Luxury|3500|180000|Grandview, MO|14|clean||
1067201799632107|2011|Toyota Prius||3500|285000|Overland Park, KS|15|clean||
2284112435711943|2009|Ford Escape||2950|181000|Kansas City, MO|15|clean||
1720251545943776|2012|Toyota Corolla|SE|3900|217000|Lee's Summit, MO|15|unknown||
1117614900688377|2008|Hyundai Tiburon|GT Limited|3500|220000|Lee's Summit, MO|16|clean||과열 기재
1534657502034606|2009|Toyota Corolla|LE Eco|3000|273000|Kansas City, KS|17|clean||
1128714376774238|2010|Hyundai Elantra|Blue|2000|145029|Olathe, KS|17|clean||
2426372851219183|2008|Volkswagen Jetta|Wolfsburg Edition|2500|186000|Kansas City, KS|18|unknown||
1079554327956171|2012|Chevrolet Malibu|1LT|2300|190000|Kansas City, MO|18|unknown||
1380917247590698|2009|Nissan Murano|SL|2850|165328|Independence, MO|19|clean|dealer|
1617938246580730|2009|Nissan Sentra|SE|3000|181000|Leawood, KS|19|clean||
2183670639230097|2008|Toyota Prius||3500|213000|Olathe, KS|19|clean||
27675859818780600|2027|Chevrolet Equinox|ACTIV|2000|300|Kansas City, MO|21|unknown||
1618185936560845|2012|Ford Fusion|SE|2400|167140|Kansas City, MO|21|unknown||AS IS 판매
3514109285439504|2009|Nissan Sentra|1.8 S|2800|181000|Leawood, KS|23|clean||
1571946281142080|2016|Dodge Grand Caravan||2800|160000|Ottawa, KS|23|unknown||
1917671369192636|2008|Infiniti QX56||2900|305000|Kansas City, MO|23|unknown||
2192895241493033|2014|Ford Escape|SE|3500|205000|Lee's Summit, MO|24|unknown||
2192499525484431|2014|Ford Explorer|XLT|3000|211000|Kansas City, MO|25|clean||
2185189518693037|2017|Ford Escape|SE|3500|141000|Oak Grove, MO|25|unknown||누유·누수 기재
1082541817653875|2011|BMW 5 Series|550i xDrive|3000|106000|Kansas City, MO|27|unknown||
1836206617759276|2010|Chevrolet Malibu|LS|3250|54825|Independence, MO|27|unknown||
1626747368950203|2008|Honda Odyssey|EX|2800|180000|Roeland Park, KS|28|unknown||
1774542827025523|2009|Hyundai Elantra|GLS|2750|179233|Mission, KS|28|salvage||AS IS 판매
1085260183962368|2012|Ford Fusion||3900|177142|Lee's Summit, MO|30|clean||
3974147346221344|2017|Ford Focus|SE|3400|86963|Tonganoxie, KS|30|clean||AS IS 판매
1562270902218723|2017|Nissan Versa|S (2018.5)|3700|116000|Gardner, KS|32|rebuilt||
1441740741189091|2016|Ford Fusion||3999|151000|Independence, MO|32|clean||
1022436690777577|2014|Volkswagen CC||2000|200000|Spring Hill, KS|35|clean||AS IS 판매
1778551203327093|2010|Kia Forte|EX|3200|171000|Shawnee, KS|38|unknown||
1407238337992618|2012|Ford F-350|XL|2500|300|Kansas City, MO|40|unknown||
1747864659748560|2010|Dodge Charger|R/T|3000|212000|Raytown, MO|41|clean||AS IS 판매
2640603569690932|2014|Ford Fusion|Platinum|3500|119000|Kansas City, MO|42|salvage||
877844481876053|2009|Toyota Camry|LE|2000|268000|Lee's Summit, MO|42|salvage||
2257788918316576|2017|Nissan Murano|S (2017.5)|3200|230000|Kansas City, MO|43|unknown||
1375517030606720|2013|Ford Edge|SEL|3700|214567|Kansas City, KS|45|clean||
4409147432659664|2011|Hyundai Sonata|Limited|3000|195000|Raytown, MO|46|clean||AS IS 판매
975560102156644|2014|Jeep Grand Cherokee|Limited|3900|227000|Shawnee, KS|46|clean||누유·누수 기재
1048320527687483|2010|Toyota Camry|SE|3500|160000|Kansas City, MO|48|rebuilt||
839949185750711|2013|GMC Terrain|SLT|2300|181683|Peculiar, MO|48|clean||변속기 이상 기재
1364904359161988|2011|Nissan Versa|SR|3500|113000|Kansas City, MO|49|clean||
28431509686435549|2012|Ford Focus|SE|3400|122651|Sugar Creek, MO|51|clean||
1660974501643799|2011|Toyota Avalon||3900|206000|Overland Park, KS|53|unknown||
1566575878182177|2011|Hyundai Elantra|Blue|3800|189487|Harrisonville, MO|56|clean||
1649604330499255|2013|Kia Optima|LX|3999|173468|Kansas City, MO|59|unknown||
1750552779723866|2009|Ford Fusion|SE|2950|191000|Liberty, MO|63|unknown||
2693815391012676|2008|Ford Fusion|SE|2500|256054|Liberty, MO|65|clean||
3133831870145132|2014|Chevrolet Cruze|LT|2650|150000|Baldwin City, KS|66|rebuilt||
1554987672697711|2009|Chrysler Town & Country|Anniversary Edition|2500|247700|Kansas City, MO|68|unknown||
786279717908892|2014|Ford Fusion|SE|3800|221354|Kansas City, MO|69|clean||
928146636984611|2011|Hyundai Sonata|GL|3000|175200|Kansas City, KS|69|salvage||AS IS 판매
1335047615487066|2011|Volkswagen Routan|SE|2000|219855|Ottawa, KS|69|clean||
904187158742380|2014|Volkswagen Passat|2.5L S|3600|213000|Overland Park, KS|70|unknown||
1385803267028904|2014|Ford Fiesta|SE|3500|134320|Kansas City, MO|73|clean||
1007401148594354|2018|Ford Escape|SE|3300|102389|Kansas City, MO|74|clean||AS IS 판매 · 우박 이력
1974471803355122|2014|Nissan Altima|3.5 S|3800|189000|Kansas City, KS|80|unknown||
1331986208904311|2011|Chrysler 200|LX|3499|124199|Olathe, KS|84|clean|dealer|
2660669437667979|2014|Lincoln MKS||3950|200190|Harrisonville, MO|85|clean||
2197682337694161|2010|Honda Accord|LX|3500|188000|Kansas City, MO|86|unknown||
1002564658853680|2016|Chevrolet Sonic|LS|3000|152000|Kansas City, KS|118|unknown||
825293230273925|2011|Volkswagen Jetta|2.5L SE|3400|170000|Kansas City, KS|130|clean||
796461229787419|2010|Ford F-150|FX4|3350|182000|Kansas City, MO|173|unknown||
1076176631669213|2011|Jeep Compass|Latitude|1650|170000|Kansas City, KS|0|unknown||
1658381959240363|2009|Chevrolet Impala|LT|1800|190000|Raytown, MO|1|clean||
1616535916487443|2014|Volkswagen Passat|1.8T Wolfsburg Edition|1000|123000|Kansas City, KS|1|unknown|avoid|운행·시동 불가 기재
1623872792701381|2008|Hyundai Santa Fe|SE|1500|192000|Lenexa, KS|2|unknown||
1699697922158989|2010|Ford Fusion||1800|200000|Raytown, MO|2|clean||
1741725710443542|2013|Kia Rio||700|132591|Independence, MO|2|clean||
1021872537576255|2012|Land Rover Range Rover Evoque|Pure Premium|1200|194874|Kansas City, MO|3|unknown|avoid|타이틀 없음·분실 기재 · 과열 기재 · AS IS 판매
1651950403158956|2008|Toyota Sienna|LE|1900|207765|Kansas City, KS|3|clean||AS IS 판매
28718261114464603|2013|Kia Sorento|LX|1500|239000|Belton, MO|3|salvage|avoid|엔진 수리 필요 기재 · 엔진 소음 기재
1108208951759663|2014|Chevrolet Traverse||1500|155000|Kansas City, KS|4|clean|avoid|운행·시동 불가 기재 · 우박 이력
1681912253356099|2010|Chevrolet Impala|LT|1900|212233|Kansas City, MO|4|clean||
1678383870617711|2010|Chevrolet Impala|LT|1900|210000|Kansas City, MO|7|unknown||
2041062516540921|2010|Hyundai Sonata|Sport|1600|144000|Kansas City, MO|7|clean||엔진 경고등 기재 · 엔진 소음 기재
1382040210751499|2014|Nissan Altima|3.5 SL|1600|149140|Kansas City, MO|7|unknown|avoid|변속기 수리 필요 기재
2101804307210666|2012|Jeep Patriot||1000|140000|Olathe, KS|8|unknown||
1400943015552107|2012|Nissan Maxima|SL|1200|200000|Olathe, KS|9|unknown||
1084159384610899|2008|Chevrolet Suburban|LTZ|1500|330000|Kansas City, KS|9|unknown||
1425830999424441|2015|Ford Focus|Titanium|1800|222872|Grain Valley, MO|10|clean||누유·누수 기재
2096028674456940|2012|Kia Forte|EX|1900|199361|Kansas City, KS|10|salvage||엔진 경고등 기재
2622167718241754|2016|Mitsubishi Outlander|SEL Black Edition|600|127000|Kansas City, MO|11|unknown||
2163259037920764|2008|Kia Optima|LX|1500|12345|Leavenworth, KS|11|unknown||
1043637128440436|2010|Mazda3|2.5 S|1000|181000|Smithville, MO|11|unknown|avoid|타이틀 없음·분실 기재
1026172460453997|2011|Nissan Sentra|SL|1500|198000|De Soto, KS|12|clean|avoid|수리용 차량 · AS IS 판매
2162072364689467|2008|Chevrolet Malibu||1500|178000|Kansas City, MO|12|unknown||
1667495835095030|2008|Ford Taurus|SEL|1500|213212|Independence, MO|13|unknown||
1620845332922884|2009|Honda Civic|CX|1400|200123|Kansas City, MO|13|unknown||
1045875821778046|2014|GMC Terrain|SLE|1100|101600|Lee's Summit, MO|13|unknown||
4487733041484737|2011|Jeep Patriot|Latitude|1200|148266|Bates City, MO|13|unknown||엔진 경고등 기재 · AS IS 판매
1445785897392990|2012|GMC Acadia||1000|275741|Baldwin City, KS|13|unknown||AS IS 판매
1767424404382823|2011|Chevrolet Impala|LT|1500|275000|Grain Valley, MO|14|unknown||
28045078191827578|2013|Nissan Altima|2.5 Platinum|1850|211531|Grain Valley, MO|15|clean||설명 없음
1063208060033552|2008|Ford Escape|XLT|1000|209831|Lansing, KS|17|clean||
1727323745195830|2008|Ford Crown Victoria|Police Interceptor (P71)|1650|197000|Kansas City, MO|17|unknown||
940846582397091|2014|Lincoln MKT||1900|200258|Kansas City, MO|18|unknown|avoid|타이틀 없음·분실 기재 · AS IS 판매
1079989291418829|2014|Ford Escape|SE|1850|172568|Independence, MO|19|clean|avoid,dealer|운행·시동 불가 기재
1043143395368898|2008|Mercedes-Benz C-Class||1500|180000|Kansas City, MO|19|unknown||
4424184987835320|2016|Jeep Patriot|Latitude|1900|116000|Lansing, KS|20|clean||
2935099650201931|2008|Nissan Pathfinder|LE|1000|210000|Louisburg, KS|21|clean||AS IS 판매
3735820459900759|2008|Pontiac Grand Prix|GT|1500|151000|Kansas City, MO|21|clean||누유·누수 기재
1539800181279214|2010|Honda Civic|DX|1900|245000|Kansas City, MO|21|salvage||
28108361235485367|2008|Dodge Avenger|SXT|1500|200000|Eudora, KS|23|clean||AS IS 판매
1023192277414502|2012|Ford Taurus|SHO|1500|200000|Independence, MO|23|unknown||
1086008843899665|2011|Buick Regal|CXL|1500|200000|Lenexa, KS|24|salvage||AS IS 판매
2565060750675397|2008|BMW Series||1700|160000|Kansas City, KS|31|clean||
4699948296905968|2012|GMC Sierra 1500||1800|160000|Overland Park, KS|31|clean|avoid|운행·시동 불가 기재 · AS IS 판매
1042897388378373|2015|Cadillac Escalade||800|300|Kansas City, MO|31|unknown||
2292448244900294|2010|Subaru Outback|2.5i Basic|1500|232000|Kearney, MO|30|unknown|avoid|헤드개스킷 문제 기재
3939238223038910|2011|Infiniti G37|S|1111|156000|Kansas City, MO|32|rebuilt||
1363930365850072|2017|Ford Explorer|Explorer|1234|162000|Kansas City, MO|34|clean||
1063438119610118|2012|Jeep Cherokee|Briarwood|1500|180856|Kansas City, KS|35|unknown||
2608962672867645|2012|Chevrolet Equinox||1800|243221|Leawood, KS|36|clean|avoid|운행·시동 불가 기재 · 에어컨 고장 기재
1896858317938592|2009|Chevrolet Impala|LTZ|1799|200000|Kansas City, KS|37|clean||엔진 경고등 기재 · AS IS 판매
3407615949411592|2013|Kia Optima||1000|143746|Kansas City, MO|41|unknown||
1177612512112533|2013|Ford Taurus|SEL|1000|285000|Liberty, MO|44|clean||
2970579773274508|2008|Kia Optima||1500|211309|Kansas City, MO|45|unknown||
1595785998555997|2016|Ford Fusion|Sel|1234|160200|Grain Valley, MO|46|unknown||
1065018872537393|2013|GMC Terrain|SLT|1500|220000|Ottawa, KS|47|unknown||상세 미조회
2859276854445602|2011|BMW 3 Series|series 328i|1200|165000|Kansas City, MO|48|unknown||상세 미조회
887159170742577|2010|Chevrolet Malibu|LT|1300|187000|Kansas City, MO|49|unknown||상세 미조회
892863436779961|2016|Chrysler 200|S|1500|127000|Kansas City, KS|50|unknown||상세 미조회
1304133128461854|2012|Chevrolet Traverse|LT|800|134000|Ottawa, KS|51|unknown||상세 미조회
1372294068200440|2009|Kia Borrego|LX|1000|271000|Overland Park, KS|59|unknown||상세 미조회
1556009269263090|2009|Chevrolet Impala|LTZ|1700|224000|Overland Park, KS|63|unknown||상세 미조회
1578019247236217|2010|Audi Q5|3.2 Quattro Premium Plus|1200|182000|Odessa, MO|63|unknown||상세 미조회
2531813317248122|2009|Hyundai Sonata||1100|247000|Olathe, KS|71|unknown||상세 미조회
1360854699309638|2010|Chevrolet Impala|LTZ|1900|199000|Mission, KS|74|unknown||상세 미조회
985794324447175|2014|Nissan Murano|AWD|1000|208000|Raytown, MO|82|unknown||상세 미조회
1020419160401409|2008|Ford Expedition|XLT|1500|260000|Kansas City, KS|86|unknown||상세 미조회
27331653953143129|2009|Nissan Murano||500||Kansas City, MO|99|unknown||상세 미조회
2043869333182837|2010|Ford Edge||1600|266000|Lee's Summit, MO|100|unknown||상세 미조회
936359412782035|2018|Chevrolet Malibu|LS|1500|160000|Kansas City, MO|106|unknown||상세 미조회
978742671688140|2009|Ford Edge|SE|1200|200000|Excelsior Springs, MO|127|unknown||상세 미조회
1302854661804137|2014|Nissan Sentra|SR|1800|128000|Kansas City, MO|135|unknown||상세 미조회
3474374966046049|2013|Ford F-150||1500|214000|Kansas City, KS|139|unknown||상세 미조회
1919899191993876|2014|Ford Focus|Titanium|1100|163000|Independence, MO|157|unknown||상세 미조회
2650411335418680|2008|Chevrolet Impala|Lt|800|238000|Kansas City, KS|4|unknown||상세 미조회
1116601640701019|2008|Chevrolet Malibu|1LT|850|120000|Lansing, KS|5|unknown||상세 미조회
2506969603143550|2017|Chevrolet Equinox|LTZ|750|75000|Leavenworth, KS|9|unknown||상세 미조회
1050090298025219|2009|Mazda C5||899|250000|Kansas City, KS|10|unknown||상세 미조회
2133001104297635|2019|Jeep Cherokee|Overland|700|41000|Independence, MO|21|unknown||상세 미조회
1379771256957537|2011|Jeep Liberty||950|140000|Raytown, MO|26|unknown||상세 미조회
1021928504216200|2012|Chevrolet Traverse|LT|950|111000|Kansas City, KS|29|unknown||상세 미조회
1098308316206082|2010|Chrysler Sebring|LX|950|166000|Kansas City, MO|31|unknown||상세 미조회
1807039086957056|2015|Land Rover Range Rover Sport|range rover sport SE|999|112000|Kansas City, MO|42|unknown||상세 미조회
888181120687702|2009|Honda Civic|EX-L|900|293000|Grandview, MO|42|unknown||상세 미조회
1536309037969257|2008|Chrysler Sebring||800|220000|Overland Park, KS|55|unknown||상세 미조회
4345217262402060|2011|Chevrolet Aveo|LT|500|172000|Drexel, MO|55|unknown||상세 미조회
2235682767165174|2011|Kia Forte|LX|800|230000|Kansas City, MO|59|unknown||상세 미조회
972079502526267|2013|Chrysler 200||800|195000|Kansas City, KS|61|unknown||상세 미조회
1710013043631871|2011|Cadillac CTS|3.6 Luxury|700|180000|Bates City, MO|70|unknown||상세 미조회
2110678396552623|2008|Chrysler Town & Country|& county (overheats) Town & country|950|175000|Lee's Summit, MO|92|unknown|dealer|상세 미조회
1645299583592552|2010|Ford E-Series|passenger|1500|198000|Kansas City, MO|4|unknown||상세 미조회
1627146005516730|2011|Jeep Compass|Latitude|1500|131000|Kansas City, KS|8|unknown||상세 미조회
1054318814267693|2008|Chrysler 300|Motown|1700|19000|Kansas City, KS|16|unknown||상세 미조회
3177595035763674|2008|Saturn Outlook|XE|1850|179000|Kansas City, MO|26|unknown||상세 미조회
2060938607869576|2008|Nissan Maxima|GLE|1000|285000|Shawnee, KS|27|unknown||상세 미조회
2977366162601581|2009|Chevrolet Malibu|LS|1100|125000|Oak Grove, MO|33|unknown||상세 미조회
1443343310937737|2010|Mitsubishi Galant|ES|1250|194000|Blue Springs, MO|44|unknown||상세 미조회
1706492110633986|2008|Honda Civic|SE|1000|160000|Kansas City, MO|55|unknown||상세 미조회
27586048124420785|2019|Ford Escape|SE|1200|114000|Kansas City, MO|55|unknown||상세 미조회
1833456688022014|2012|Nissan Altima|3.5 SR|1234|141000|Lenexa, KS|57|unknown||상세 미조회
1228728016985713|2013|Nissan Murano|S|1300|15000|Kansas City, KS|70|unknown||상세 미조회
28353186097615354|2010|Nissan Titan||1234|155000|Kansas City, MO|71|unknown||상세 미조회
954301137471600|2012|GMC Acadia|SLE|1200|202000|Kansas City, MO|148|unknown||상세 미조회
930679949769428|2013|Jeep Compass||1800|150000|Independence, MO|149|unknown||상세 미조회
1621316289338553|2011|Subaru Impreza||2800|200000|Shawnee, KS|0|unknown||상세 미조회
1127305819859015|2010|GMC Yukon|SLT|2800|293000|Blue Springs, MO|1|unknown||상세 미조회
2004863533466458|2011|Ford Fusion|se|2400|235000|Liberty, MO|1|unknown||상세 미조회
4659911954239023|2012|Jeep Liberty||2500|183000|Kansas City, MO|1|unknown||상세 미조회
1854663802179606|2014|Volkswagen CC|2.0T Executive|2000|214000|Belton, MO|1|unknown||상세 미조회
1060696966761244|2009|Volkswagen Tiguan|2.0T 4Motion|2500|209000|Kansas City, MO|2|unknown||상세 미조회
1821697969268905|2012|Chevrolet Traverse|6|2000|1700|Kansas City, MO|2|unknown||상세 미조회
1418120223630687|2011|Ford Escape|XLT|2900|167000|Kansas City, MO|2|unknown||상세 미조회
2358858904850347|2010|Toyota Corolla|LE|2900|270000|Grandview, MO|2|unknown||상세 미조회
1519801250165185|2011|Honda Accord|V6|2000|247000|Kansas City, MO|3|unknown||상세 미조회
1795428194827145|2013|Toyota Corolla|LE|2000|140000|Kansas City, KS|3|unknown||상세 미조회
1569663881575044|2013|Chevrolet Impala||2900|245000|De Soto, KS|3|unknown||상세 미조회
1125913079789094|2008|Chevrolet Malibu|(classic) LS|2000|244000|Blue Springs, MO|3|unknown||상세 미조회
3462875297217981|2011|Kia Soul|+|2800|226000|Kansas City, KS|3|unknown||상세 미조회
1647821373476240|2008|Ford Edge|Limited|2500|235000|Kansas City, MO|4|unknown||상세 미조회
1437499314899056|2014|Chevrolet Captiva||2850|158000|Kansas City, MO|5|unknown||상세 미조회
2069369833945747|2009|Ford Escape||2895|192000|Lee's Summit, MO|6|unknown||상세 미조회
2978998835766707|2013|Mazda CX-9|Grand Touring|2500|287000|Parkville, MO|7|unknown||상세 미조회
1422178752951218|2012|Volkswagen Jetta|Black|2100|198000|Kansas City, MO|8|unknown||상세 미조회
1791313631906278|2013|Nissan Rogue|sv awd|2600|151000|Kansas City, MO|9|unknown||상세 미조회
3502492733244131|2015|Chevrolet Sonic|LT|2500|118000|Independence, MO|9|unknown||상세 미조회
1099578485793041|2011|Buick Enclave|CXL|2500|195000|Lee's Summit, MO|9|unknown||상세 미조회
1752562399368626|2008|Ford Escape||2300|194000|Kansas City, MO|11|unknown||상세 미조회
1704228491702842|2008|Ford Escape|XLT|2500|178000|La Cygne, KS|11|unknown||상세 미조회
3516136109233906|2008|Mazda CX-5|2.5 S Select|2000|222000|Kansas City, MO|12|unknown||상세 미조회
2869420333415012|2013|Ford Escape|SE|2500|213000|Independence, MO|12|unknown||상세 미조회
1482720700360978|2012|Dodge Avenger|SXT|2500|148000|Blue Springs, MO|13|unknown||상세 미조회
2135226690754831|2009|Toyota Matrix||2000|175000|Kansas City, MO|14|unknown||상세 미조회
939869061930905|2011|Ford Explorer|sport|2700|270000|Kansas City, KS|14|unknown||상세 미조회
2115770292372632|2013|Ford Focus|S|2450|300000|Independence, MO|14|unknown||상세 미조회
1393893602168705|2012|Kia Soul||2100|133000|Gardner, KS|15|unknown||상세 미조회
1650605659996106|2008|Ford Focus|SE|2000|183000|Kansas City, KS|15|unknown||상세 미조회
1615925090066227|2013|Nissan Pathfinder|Platinum|2500|190000|Independence, MO|16|unknown||상세 미조회
1068721882564142|2011|Chevrolet Malibu|lt|2000|152000|Olathe, KS|8|unknown||상세 미조회
1695516611523354|2014|Nissan Altima|S|2000|145000|Kansas City, MO|17|unknown||상세 미조회
4032339320404137|2013|Chevrolet Impala||2500|170000|Sugar Creek, MO|18|unknown||상세 미조회
1609919630824858|2008|Pontiac G6||2600|159000|Kansas City, KS|18|unknown||상세 미조회
1404434088520563|2008|Ford Escape|Active|2400|180000|Kansas City, KS|18|unknown||상세 미조회
1688643425542050|2010|Nissan Altima|2.5 SL|2999|219000|Grain Valley, MO|19|unknown||상세 미조회
1062805033218144|2010|Mazda3||2500|202000|Gardner, KS|21|unknown||상세 미조회
1540453337369262|2013|Ford Focus|Titanium|2700|178000|Fairway, KS|21|unknown||상세 미조회
1058491120435754|2013|Chevrolet Cruze|LS|2500|200000|Kansas City, MO|22|unknown||상세 미조회
1051234594489831|2011|Ford Fiesta|SE|2200|140000|Belton, MO|22|unknown||상세 미조회
1051260284489205|2012|Ford Focus|SEL|2000|135000|Overland Park, KS|22|unknown||상세 미조회
2306213273245959|2012|Volvo S60|2.5T|2000|239000|Belton, MO|24|unknown||상세 미조회
1746971426504432|2012|Chevrolet Volt|LT|2850|244000|Raytown, MO|24|unknown||상세 미조회
1370460328623949|2013|Chevrolet Cruze|LT|2000|199000|Kansas City, MO|25|unknown||상세 미조회
1361763369450931|2009|Chevrolet Cobalt||2200|250000|Olathe, KS|25|unknown||상세 미조회
1743723623513946|2009|Nissan Pathfinder|LE|2500|200000|Harrisonville, MO|25|unknown||상세 미조회
2200967800481670|2015|Nissan Versa Note|note|2500|146000|Independence, MO|25|unknown||상세 미조회
1007728505629543|2016|Nissan Altima|2.5 SL|2000|158000|Olathe, KS|27|unknown||상세 미조회
1616146263286084|2008|Dodge Ram 1500|1500|2500|215000|Independence, MO|29|unknown||상세 미조회
1842095253622739|2013|Dodge Journey|sxt|2524|186000|Overland Park, KS|30|unknown||상세 미조회
2388411331964523|2008|Chrysler Sebring|LX|2700|205000|Lawrence, KS|31|unknown||상세 미조회
1279919370821152|2011|Nissan Sentra|1.8 S|2000|175000|Kansas City, KS|31|unknown||상세 미조회
1036016729315390|2010|Scion xB||2500|191000|Lee's Summit, MO|20|unknown||상세 미조회
4112334148902471|2008|Honda Accord|EX|2800|258000|Lenexa, KS|36|unknown||상세 미조회
1479148004233565|2014|Kia Sorento|LX|2400|242000|Kansas City, MO|37|unknown||상세 미조회
1384140960556206|2015|Chevrolet Malibu|limited LT|2500|163000|Overland Park, KS|38|unknown||상세 미조회
888944900648617|2010|Hyundai Sonata|GLS|2750|220000|Kansas City, MO|39|unknown||상세 미조회
1485566316481763|2013|Ford Focus||2000|100000|Kansas City, MO|40|unknown||상세 미조회
1431541165701923|2016|Ford Fusion|SE|2800|246000|Independence, MO|42|unknown||상세 미조회
2354761388674489|2010|Nissan Altima|2.5 S|2500|174000|Olathe, KS|43|unknown||상세 미조회
1715321952919828|2013|Ford Expedition|King Ranch|2800|201000|Kansas City, MO|43|unknown||상세 미조회
1865271414434351|2011|Nissan Altima|2.5 S|2800|186000|Kansas City, MO|44|unknown||상세 미조회
2233991884082656|2014|Dodge Journey|Limited|2500|245000|Raytown, MO|47|unknown||상세 미조회
890385220383809|2014|Jeep Patriot|Sport SE|2700|235000|Kansas City, MO|48|unknown||상세 미조회
1756409082032639|2011|Cadillac SRX|Luxury Collection|2000|150000|Oak Grove, MO|55|unknown||상세 미조회
2019579841999630|2009|Nissan Altima|2.5 S|2500|220000|Olathe, KS|56|unknown||상세 미조회
1767137390977026|2011|Nissan Altima|2.5 SL|2000|242000|Raymore, MO|58|unknown||상세 미조회
1614547973573108|2011|Infiniti G37x|Base|2000|100000|Blue Springs, MO|58|unknown||상세 미조회
27879252515020458|2008|BMW 5 Series|series 535xi|2500|214000|Overland Park, KS|62|unknown||상세 미조회
914003274345419|2012|Ford Focus||2500|146000|Independence, MO|67|unknown||상세 미조회
795302683610033|2013|Chevrolet Spark|ev|2700|140000|Kansas City, MO|68|unknown||상세 미조회
1487999536411856|2013|Nissan Altima|2.5 S|2800|192000|Kansas City, MO|71|unknown||상세 미조회 · 같은 차 2건 게시
2076115996447081|2012|Chevrolet Impala|LT|2850|160000|Kansas City, MO|73|unknown||상세 미조회
4110572795909951|2014|Dodge Avenger||2200|182000|Harrisonville, MO|75|unknown||상세 미조회
787299627744613|2013|Kia Rio|LX|2500|193000|Kansas City, MO|79|unknown||상세 미조회
3478696562280687|2016|Chevrolet Trax|Ls|2250|211000|Independence, MO|92|unknown||상세 미조회
995550666529671|2011|Chevrolet Cruze|LT|2100|161000|Lee's Summit, MO|106|unknown||상세 미조회
990820353492936|2012|Nissan Quest|Other|2899|212000|Overland Park, KS|111|unknown||상세 미조회
2136009354001364|2017|Dodge Journey|Crossroad Plus|3000|160000|Olathe, KS|0|unknown||상세 미조회
948972028261840|2015|Chevrolet Trax||3300|16000|Kansas City, MO|1|unknown||상세 미조회
2235369560367290|2008|Audi A4|2.0T|3500|230000|Osawatomie, KS|2|unknown||상세 미조회
2166356777244462|2018|Dodge Grand Caravan|ES|3000|183000|Kansas City, KS|2|unknown||상세 미조회
1714126083021404|2008|Honda Civic||3000|213000|Raytown, MO|2|unknown||상세 미조회
1851436716269844|2012|Chevrolet Traverse||3000|153000|Kansas City, KS|3|unknown||상세 미조회
1754888942469190|2016|Buick LaCrosse|Touring|3000|139000|Kansas City, MO|4|unknown||상세 미조회
2095467297843439|2011|Jeep Liberty|Limited Edition|3000|170000|Kansas City, MO|4|unknown||상세 미조회
1087734100322199|2011|Ford Escape|XLT|3000|228000|Grandview, MO|6|unknown||상세 미조회
1783567129644910|2008|Nissan Maxima||3000|172000|Kansas City, MO|6|unknown||상세 미조회
4021173091523282|2011|Nissan Rogue|S|3200|127000|Kansas City, MO|8|unknown||상세 미조회
1614590776683337|2014|Kia Sportage||3500|196000|Kansas City, KS|9|unknown||상세 미조회
1638021494601099|2014|Chrysler 200||3500|198000|Kansas City, MO|9|unknown||상세 미조회
1385520713693818|2014|Chevrolet Cruze|2LT|3200|175000|Olathe, KS|11|unknown||상세 미조회
1448599853781347|2014|Ford Escape||3000|193000|Kansas City, KS|12|unknown||상세 미조회
821828107656879|2015|Chevrolet Sonic|LS|3000|128000|Kansas City, KS|16|unknown||상세 미조회
1392325289752315|2011|Dodge Ram 1500||3500|270000|Raymore, MO|16|unknown||상세 미조회
1096932056252692|2008|Chevrolet Cobalt|Sport|3500|200000|Odessa, MO|19|unknown||상세 미조회
953449827777651|2010|Nissan Rogue||3500|185000|Greenwood, MO|20|unknown||상세 미조회
1337942681469242|2008|Dodge Durango||3000|178000|Leavenworth, KS|22|unknown||상세 미조회
985250427937382|2009|Nissan Maxima||3000|250000|Lenexa, KS|22|unknown||상세 미조회
4361952090786559|2016|Chevrolet Cruze|limited Eco|3500|190000|Kansas City, MO|23|unknown||상세 미조회
4308584859393142|2008|Nissan Altima|2.5 Platinum|3000|206000|Kansas City, KS|24|unknown||상세 미조회
3468928886608990|2015|Jeep Compass||3900|186000|Kansas City, MO|28|unknown||상세 미조회
1615338697044269|2013|Ford Explorer|Limited|3999|184000|Kansas City, MO|28|unknown||상세 미조회
1727630918358740|2012|Chevrolet Equinox|L|3200|216000|Kansas City, MO|29|unknown||상세 미조회
2108710270530379|2011|Chevrolet Aveo|LT|3950|131000|Pleasant Valley, MO|31|unknown||상세 미조회
1650128213357523|2014|Ford Explorer||3500|206000|Kansas City, KS|35|unknown||상세 미조회
1762282294920527|2009|Toyota Corolla|LE|3700|272000|Kansas City, KS|36|unknown||상세 미조회
2018586238793367|2014|GMC Terrain|AT4|3000|250000|Kansas City, KS|38|unknown||상세 미조회
1628267509000179|2014|Kia Sorento|EX|3200|242000|Mission Hills, KS|39|unknown||상세 미조회
1214619424179690|2008|Ford F-150|FX2|3000|318000|Kansas City, MO|43|unknown||상세 미조회
1220461440223739|2012|Volkswagen Eos|3.2L Hard Top|3750|125000|Kansas City, MO|43|unknown||상세 미조회
1536765257523896|2012|GMC Acadia|SLT|3000|165000|Independence, MO|47|unknown||상세 미조회
1077921547905884|2014|Chrysler 200||3500|190000|Grandview, MO|49|unknown||상세 미조회
855040357689224|2014|Kia Forte||3500|170000|Olathe, KS|49|unknown||상세 미조회
1099239476113179|2010|Volkswagen Touareg|VR6|3000|197000|Freeman, MO|24|unknown||상세 미조회
1551751859762366|2012|Ford Transit Connect|passenger|3000|288000|Overland Park, KS|56|unknown||상세 미조회
1650423816057426|2014|Chevrolet Cruze|LTZ|3000|200000|Holden, MO|58|unknown||상세 미조회
2039301713623242|2015|Dodge Dart||3800|233000|Kansas City, MO|58|unknown||상세 미조회
1269212376266055|2010|Nissan Rogue|S|3000|154000|Kansas City, MO|60|unknown||상세 미조회
4322913261352562|2008|Ford Edge|Limited|3800|175000|Olathe, KS|70|unknown||상세 미조회
1067744315816636|2010|Chevrolet Equinox|LTZ|3000|172000|Independence, MO|72|unknown||상세 미조회
1049192214354911|2013|Ford Taurus|SHO|3500|233000|Kansas City, MO|73|unknown||상세 미조회
1800882700878796|2012|Honda Pilot|LX|3500|233000|Peculiar, MO|80|unknown||상세 미조회
1036330508790137|2014|Ford Focus||3000|158000|Kansas City, MO|82|unknown||상세 미조회
1576009800850059|2014|Chevrolet Malibu|(classic)|3800|192000|Kansas City, KS|87|unknown||상세 미조회
1031910642829874|2008|Ford Edge|Limited|3000|200000|Kansas City, MO|116|unknown||상세 미조회
1673963230308426|2014|Kia Sorento|LX|3500|203000|Kansas City, MO|133|unknown||상세 미조회
26976731918609675|2015|Nissan Rogue Select||3000|194000|Olathe, KS|143|unknown||상세 미조회
2281083289352709|2008|Toyota Sienna|LE|4500|237000|Kansas City, MO|0|unknown||상세 미조회
3225682770953093|2015|Dodge Journey|R/T|4500|220000|Kansas City, KS|3|unknown||상세 미조회
2208587913053962|2015|GMC Acadia|SLT|4000|232000|Kansas City, MO|4|unknown||상세 미조회
4217961388464363|2011|Ford Escape|Limited|4500|202000|Lenexa, KS|4|unknown||상세 미조회
907857105493352|2012|Ford Escape|SEL|4200|165000|Kansas City, MO|5|unknown||상세 미조회
2881333328906800|2012|Chevrolet Cruze|LT|4000|133000|Raytown, MO|5|unknown||상세 미조회
1087211740622841|2016|Ford F-150||4700|212000|Kansas City, KS|7|unknown||상세 미조회
1635050298051828|2012|Toyota Corolla|S|4500|148000|Kansas City, KS|7|unknown||상세 미조회
1052879527373110|2011|GMC Terrain|SL|4700|152000|Kansas City, MO|7|unknown|dealer|상세 미조회
1411366084286730|2008|Lexus GS|350 F SPORT|4500|250000|Kansas City, MO|8|unknown||상세 미조회
1055732617261292|2013|Hyundai Santa Fe||4200|197000|Kansas City, MO|9|unknown||상세 미조회
1864162665023326|2011|Ford Fiesta|SE|4000|139000|Kansas City, KS|9|unknown||상세 미조회
1073079208654675|2010|Hyundai Elantra|Touring|4650|140000|Kansas City, KS|11|unknown||상세 미조회
1105569538541298|2011|Chevrolet Tahoe|LT|4000|180000|Olathe, KS|11|unknown||상세 미조회
1070859952589458|2008|GMC Acadia|limited|4500|140000|Kansas City, MO|12|unknown||상세 미조회
1058302453685640|2013|Kia Rio||4500|109000|Independence, MO|12|unknown||상세 미조회
2077909049486137|2010|Ford F-150||4500|240000|Blue Springs, MO|13|unknown||상세 미조회
2285923495577759|2008|Lexus LS|460|4500|157000|Shawnee, KS|13|unknown||상세 미조회
2158598814691410|2010|Jeep Patriot|Limited|4000|145000|Kansas City, MO|14|unknown||상세 미조회
1092638206674363|2011|Kia Sportage||4100|213000|Lenexa, KS|17|unknown||상세 미조회
1324264313117928|2015|Ford Focus|Titanium|4500|175000|Kansas City, MO|17|unknown||상세 미조회
1382656436829962|2009|Mazda3|i Touring|4500|134000|Olathe, KS|16|unknown||상세 미조회
1562552024881048|2014|Ford Edge|Limited|4500|284000|Lenexa, KS|17|unknown||상세 미조회
1464931348989063|2020|Chevrolet Spark|LS|4295|179000|Gardner, KS|19|unknown||상세 미조회
1034739209567403|2010|Chevrolet Traverse|LT|4000|222000|Kansas City, MO|20|unknown||상세 미조회
1390363882501173|2012|Honda Odyssey|EX-L w/Navigation|4500|190000|Kansas City, MO|21|unknown|dealer|상세 미조회
1059569380048411|2008|Toyota Camry|CE|4200|208000|Kansas City, KS|21|unknown||상세 미조회
1785331269126861|2014|Jeep Patriot|Latitude|4300|170000|Raymore, MO|22|unknown||상세 미조회
1495024485766997|2013|Cadillac XTS|Luxury|4600|190000|Lee's Summit, MO|23|unknown||상세 미조회
1832372061434339|2012|Ford Focus|SE|4495|141000|Kansas City, MO|23|unknown||상세 미조회
1012667551791694|2012|Audi A3|2.0T S-Line|4500|160000|Independence, MO|24|unknown||상세 미조회
1717481946199742|2013|Ford Focus|to dealership by end of the month!|4000|88000|Kansas City, MO|24|unknown||상세 미조회
2160343078165797|2009|Toyota Prius|Four Touring|4000|143000|Kansas City, MO|25|unknown||상세 미조회
2389805911824485|2015|Volkswagen Passat||4500|123000|Kansas City, MO|26|unknown||상세 미조회
850831644787083|2012|Ford Escape|Active|4000|165000|Kansas City, MO|28|unknown||상세 미조회
1038252792173913|2008|Acura TL|3.2|4250|222000|Kansas City, MO|30|unknown||상세 미조회
1261340149384528|2009|Ford F-150|King Ranch Short Bed 4D|4700|275000|Lee's Summit, MO|31|unknown||상세 미조회
1063143412922537|2014|Jeep Compass|latitude|4500|146000|Independence, MO|32|unknown||상세 미조회
1081653704443632|2010|Toyota Corolla|S|4100|270000|Independence, MO|32|unknown||상세 미조회
1043791958447567|2014|Nissan Pathfinder|Platinum|4000|180000|Kansas City, MO|33|unknown||상세 미조회
1590705682630952|2019|Chevrolet Spark||4300|108000|Independence, MO|33|unknown||상세 미조회
1039103698739845|2011|Nissan Rogue|SL|4700|154000|Kansas City, MO|35|unknown||상세 미조회
1602978674824483|2009|Ford F-150|King Ranch 4D|4500|216000|Kansas City, MO|35|unknown||상세 미조회
2576499142785553|2014|Ford Explorer|XLT|4000|170000|Independence, MO|37|unknown||상세 미조회
1560306242508334|2015|Ford Escape|S|4400|165000|Kansas City, MO|43|unknown||상세 미조회
1501032425374741|2010|Ford Edge|Sel|4600|150000|Kansas City, MO|43|unknown||상세 미조회
1036540915815221|2013|Chevrolet Traverse|LT|4500|195000|Olathe, KS|44|unknown||상세 미조회
2197432347490605|2015|Chevrolet Cruze|LT|4000|120000|Kansas City, MO|45|unknown||상세 미조회
4480257228906899|2013|Chevrolet Cruze||4500|136000|Kansas City, MO|48|unknown||상세 미조회
2528884760940701|2010|Audi Q5|3.2 Quattro Premium Plus|4500|183000|Kansas City, KS|48|unknown||상세 미조회
1581609886910974|2013|Dodge Dart|sxt|4500|173000|Kansas City, MO|51|unknown||상세 미조회
1734913627715216|2015|Chevrolet Malibu|Eco|4500|163000|Leawood, KS|52|unknown||상세 미조회
1078450628003962|2014|Kia Optima|LX|4500|111000|Kansas City, MO|54|unknown||상세 미조회
1205303535101405|2008|Smart Fortwo|Passion|4300|126000|Blue Springs, MO|56|unknown||상세 미조회
1556573039346524|2014|Nissan Juke|SL|4500|150000|Kansas City, MO|56|unknown||상세 미조회
924202907379866|2009|Nissan Pathfinder|s|4500|230000|Kansas City, MO|56|unknown||상세 미조회
27345006365192600|2011|Infiniti M37x||4500|190000|Kansas City, KS|62|unknown||상세 미조회
1585269103114910|2016|Hyundai Accent|GL|4200|183000|Kansas City, MO|63|unknown||상세 미조회
1995471111336127|2012|Hyundai Tucson|Limited|4300|220000|Kansas City, KS|63|unknown||상세 미조회
2143105609933522|2012|Chevrolet Cruze|LT|4200|184000|Kansas City, MO|65|unknown||상세 미조회
2455779931608955|2011|Audi Q5||4500|150000|Sugar Creek, MO|68|unknown||상세 미조회
987448287661923|2018|Ford Escape|Tela|4000|163000|Shawnee, KS|69|unknown||상세 미조회
1382320477104586|2014|Ford Focus||4000|127000|Kansas City, MO|70|unknown||상세 미조회
1950762328942625|2012|BMW 5 Series|series 535i|4000|125000|Kansas City, MO|77|unknown||상세 미조회
1281748880478625|2013|Volkswagen Jetta|2.0L Base|4500|19000|Kansas City, KS|83|unknown||상세 미조회
1341453377363874|2014|Nissan Rogue|S|4000|170000|Leavenworth, KS|84|unknown||상세 미조회
3921955148101059|2008|Volkswagen GTI|1.8T|4200|184000|Olathe, KS|91|unknown||상세 미조회
1514878973708293|2014|Chevrolet Traverse|LS|4000|220000|Kansas City, MO|95|unknown||상세 미조회
1731120988243685|2011|Chevrolet Impala|LS|4700|171000|Overland Park, KS|102|unknown||상세 미조회
2988825851449773|2011|Cadillac CTS|3.0 Luxury Collection|4500|140000|Kansas City, MO|121|unknown||상세 미조회
1766613167811021|2012|Mercedes-Benz C-Class|C 250 Luxury|4000|138000|Kansas City, KS|166|unknown||상세 미조회
2165029144427789|2009|BMW 3 Series|series 328i xDrive|5450|127000|Kansas City, MO|0|unknown||상세 미조회
1079938621630428|2010|Volkswagen Passat|2.0T|5250|137000|Kansas City, MO|0|unknown||상세 미조회
1036780562732441|2014|Honda Civic|LX|4800|169000|Overland Park, KS|0|unknown||상세 미조회
2007576393291015|2014|GMC Acadia|SLE-2|4800|143000|Kearney, MO|2|unknown||상세 미조회
1080656864888570|2011|Mazda3|2.0|5000|130000|Shawnee, KS|3|unknown||상세 미조회
4590405921281181|2009|Honda Accord|DX|5200|152000|Kansas City, KS|3|unknown||상세 미조회
1645424837249620|2015|Volkswagen Passat|TDI SEL Premium|4999|221000|Lee's Summit, MO|5|unknown|dealer|상세 미조회
1753113799241855|2014|Dodge Dart||4895|85000|Kansas City, MO|5|unknown||상세 미조회
2316368479160065|2013|Lincoln MKX|Premiere|5000|200000|Lee's Summit, MO|5|unknown||상세 미조회
1109418928090779|2012|Jeep Liberty|Limited|5100|203000|Kansas City, MO|5|unknown||상세 미조회
1369083941927839|2017|Kia Forte|EX|5000|160000|Kansas City, MO|6|unknown||상세 미조회
1645180657182342|2010|Mercury Mariner|Premier|5400|116000|Sugar Creek, MO|6|unknown||상세 미조회
1583979599770595|2014|Ford Escape|SE|4999|142000|Kansas City, KS|8|unknown||상세 미조회
1417907763609496|2012|Nissan Quest|SL|4800|152000|Blue Springs, MO|8|unknown||상세 미조회
1686678015770398|2015|Chevrolet Trax|LT|5499|86000|Kansas City, MO|9|unknown||상세 미조회
2478470102676362|2016|Jeep Renegade||5300|148000|Kingsville, MO|10|unknown||상세 미조회
1090077783606629|2016|Subaru Forester|2.5X|5300|171000|Kansas City, MO|12|unknown||상세 미조회
2951622831865087|2015|Jeep Renegade|latitude 4wd / manual / 190k miles|5000|190000|Kansas City, KS|13|unknown||상세 미조회
2091530474793861|2017|Dodge Grand Caravan|passenger GT|5250|175000|Olathe, KS|13|unknown||상세 미조회
2154542038461340|2015|Chevrolet Cruze|LT|4950|126000|Kansas City, MO|13|unknown||상세 미조회
1427909152523784|2009|Mercedes-Benz C-Class|4matic sport|4750|140000|Oak Grove, MO|14|unknown||상세 미조회
1861228755284461|2015|Chevrolet Sonic||4990|145000|Kansas City, MO|14|unknown||상세 미조회
1117556447272159|2008|Lexus GS|350 Crafted Line|4800|250000|Overland Park, KS|15|unknown||상세 미조회
1805558103951124|2011|Acura TSX||4800|215000|Kansas City, MO|15|unknown||상세 미조회
1554346576376878|2016|Kia Soul||4999|108000|Kansas City, MO|15|unknown||상세 미조회
1370674128483785|2015|Ford Fusion|S|4965|184000|Kansas City, MO|15|unknown||상세 미조회
1096847783302425|2014|Dodge Journey|SXT|5000|153000|Independence, MO|16|unknown||상세 미조회
991960120528890|2015|Ford Fusion||5000|160000|Kansas City, KS|17|unknown||상세 미조회
1044976168413746|2011|Hyundai Santa Fe|SE|5000|141000|Olathe, KS|17|unknown||상세 미조회
1405745084829663|2013|Infiniti JX35||5000|215000|Kansas City, KS|19|unknown||상세 미조회
28470069329347379|2014|Nissan Pathfinder|SL|5200|200000|Blue Springs, MO|19|unknown||상세 미조회
1693512822392354|2014|Jeep Compass||5000|147000|Independence, MO|19|unknown||상세 미조회
1202289682596847|2016|Chevrolet Sonic|LT|5300|87000|Blue Springs, MO|20|unknown||상세 미조회
1620925139712137|2011|Mazda3|Sport|4995|175000|Shawnee, KS|21|unknown||상세 미조회
1817775852714931|2012|Buick LaCrosse|Premium I|5499|171000|Kansas City, MO|22|unknown||상세 미조회
1583938970040693|2011|Chevrolet Equinox|Sport|4750|160000|Kansas City, MO|24|unknown||상세 미조회
1040708368773303|2015|Ford Edge|SEL|5300|160000|Grandview, MO|26|unknown||상세 미조회
2136405363957504|2015|Chevrolet Trax|- low miles - new ac compressor|5200|122000|Olathe, KS|27|unknown||상세 미조회
1181204031752755|2016|GMC Terrain|SLE|5300|186000|Kansas City, MO|28|unknown||상세 미조회
2129292334649142|2014|Buick Encore|Essence|5000|138000|Kansas City, MO|31|unknown||상세 미조회
1566502375210691|2011|GMC Yukon|sport|5200|166000|Independence, MO|32|unknown||상세 미조회
1723557608864450|2017|Dodge Journey|crossroad|5000|137000|Independence, MO|32|unknown||상세 미조회
1002560436126549|2011|Toyota Sienna|LE|4950|202000|Kansas City, MO|33|unknown||상세 미조회
1366441962286362|2012|Jeep Grand Cherokee|Overland|5000|190000|Kansas City, MO|33|unknown|dealer|상세 미조회
1799105207762716|2014|Honda Odyssey|Touring Elite|4999|253000|Lenexa, KS|33|unknown||상세 미조회
28025205173840642|2010|Dodge Avenger|SXT|5000|137000|Oak Grove, MO|34|unknown||상세 미조회
1024021563780352|2013|Chevrolet Cruze||4900|178000|Kansas City, MO|35|unknown||상세 미조회
1065709619440787|2015|Kia Soul|e|5000|188000|Overland Park, KS|36|unknown||상세 미조회
2338652430206622|2019|Dodge Journey|SE|4999|155000|Grandview, MO|38|unknown||상세 미조회
1200273245628456|2014|Dodge Grand Caravan|SXT|4999|158000|Grandview, MO|38|unknown||상세 미조회
2526921261086585|2013|Nissan Rogue|SV|5000|175000|Olathe, KS|38|unknown||상세 미조회
1056320410326530|2015|Ford Flex|SE|5000|128000|Olathe, KS|39|unknown||상세 미조회
1077713498283633|2014|GMC Acadia|Denali|5000|200000|Kansas City, MO|39|unknown||상세 미조회
937630235279498|2012|Dodge Ram 1500||5000|205000|Peculiar, MO|39|unknown||상세 미조회
1670153524058633|2008|Dodge Avenger|SE|5000|121000|Kansas City, MO|31|unknown||상세 미조회
1474770314686437|2014|Nissan Maxima|SL|5000|197000|Kansas City, MO|40|unknown||상세 미조회
1594562528892883|2011|Honda Pilot|LX|4999|195000|Kansas City, MO|41|unknown||상세 미조회
988078434260343|2013|Ford Edge|SEL|4895|144000|Oak Grove, MO|41|unknown||상세 미조회
1304789511603845|2008|Buick Enclave|CXL|4999|123000|Independence, MO|42|unknown||상세 미조회
1059733296648121|2011|Jeep Grand Cherokee|Overland|5000|193000|Kansas City, KS|45|unknown||상세 미조회
2302320253935140|2015|Ford Escape|S|4800|165000|Kansas City, MO|47|unknown||상세 미조회
1371672064419168|2014|Toyota Camry|LE|4990|248000|Kansas City, MO|48|unknown||상세 미조회
4502292070058965|2013|Cadillac ATS||5000|106000|Grandview, MO|49|unknown||상세 미조회
4310414289219300|2015|Jeep Compass||5000|150000|Kansas City, KS|52|unknown||상세 미조회
2563080764105633|2011|Subaru Impreza|2.5i Premium|5000|134000|Independence, MO|52|unknown||상세 미조회
1021452510784970|2011|Chevrolet Traverse|LT|4999|187000|Olathe, KS|54|unknown||상세 미조회
1040494481669197|2013|MINI Countryman|Classic Cooper S ALL4|5200|98000|Raytown, MO|54|unknown||상세 미조회
1678196317198957|2015|Chrysler 200||5000|158000|Kansas City, MO|55|unknown||상세 미조회
846595711718424|2013|Honda Odyssey|EX-L|5499|173000|Olathe, KS|56|unknown||상세 미조회
1026975943377606|2011|Subaru Forester||5300|158000|Independence, MO|57|unknown||상세 미조회
1324767199419594|2009|Honda CR-V||5000|235000|Kansas City, MO|58|unknown||상세 미조회
1062164412859404|2014|Volkswagen Passat|2.0T S|5200|230000|Lawrence, KS|59|unknown||상세 미조회
2284380065697748|2014|BMW X1|xDrive28i|4900|152000|Kansas City, KS|61|unknown||상세 미조회
1429055179032551|2013|Nissan Juke|S|4900|114000|Shawnee, KS|61|unknown||상세 미조회
1593882118979971|2013|Ford Flex|SEL|5250|159000|Kansas City, MO|64|unknown||상세 미조회
1551422146529476|2013|Nissan Pathfinder|S|4999|145000|Independence, MO|68|unknown||상세 미조회
1705870507400278|2010|GMC Sierra 1500||5000|217000|Kansas City, KS|70|unknown||상세 미조회
1480271057206084|2009|Chevrolet Silverado 1500|(classic) 1500|4800|154000|Lansing, KS|79|unknown||상세 미조회
1509974950516675|2016|Chevrolet Camaro|LT|5000|16000|Overland Park, KS|110|unknown||상세 미조회
1638452510770603|2012|GMC Acadia|Denali|5000|192000|Raytown, MO|123|unknown||상세 미조회
1291001925968083|2017|Ford Flex|Limited|4999|179000|Lenexa, KS|130|unknown||상세 미조회
981801921376871|2011|Ford Ranger|Xlt|5000|138000|Stilwell, KS|130|unknown||상세 미조회
4479243859007300|2012|Volkswagen CC|2.0T Sport|5000|130000|Blue Springs, MO|131|unknown||상세 미조회
1355226603330040|2008|Land Rover Range Rover Sport|range rover sport Autobiography|4800|119000|Parkville, MO|140|unknown||상세 미조회
1833265437657867|2014|Nissan Murano|Cross-Cabriolet|5500|123000|Raytown, MO|0|unknown||상세 미조회
1498580762142715|2014|Dodge Ram 1500|classic|6000|290000|Kansas City, MO|0|unknown||상세 미조회
1758350562115300|2010|Nissan Maxima||6000|174000|Belton, MO|1|unknown||상세 미조회
2150055882527177|2010|Toyota Prius|I|5950|215000|Independence, MO|1|unknown|dealer|상세 미조회
1038215275939120|2017|GMC Terrain|SLE|5999|176000|Independence, MO|1|unknown||상세 미조회
1266571475572575|2011|Honda Odyssey|EX-L w/Navigation & RES|6000|150000|Kansas City, MO|2|unknown||상세 미조회
2162270047659958|2012|Hyundai Santa Fe|SE|5500|155000|Riverside, MO|2|unknown||상세 미조회
1644805993825623|2010|Subaru Forester|2.5x premium|6000|192000|Kansas City, MO|3|unknown||상세 미조회
1109949561564187|2014|Hyundai Tucson||5500|125000|Overland Park, KS|3|unknown||상세 미조회 · 같은 차 2건 게시
1613329863659357|2008|Pontiac Solstice|GXP|5900|100000|Kansas City, MO|4|unknown||상세 미조회
2659358217834659|2014|Chevrolet Equinox||5500|1300|Kansas City, MO|4|unknown||상세 미조회
38616685391279602|2015|Smart Fortwo||5500|109000|Kansas City, KS|4|unknown||상세 미조회
4384940381760834|2011|GMC Terrain||5500|152000|Independence, MO|5|unknown||상세 미조회
28854092660862070|2009|BMW 3 Series|series 328i xDrive|5900|148000|Shawnee, KS|5|unknown||상세 미조회
3313884498795552|2014|Toyota Prius|III|5700|175000|Olathe, KS|5|unknown||상세 미조회
1332833678796220|2011|Toyota Prius||5500|191000|Gardner, KS|6|unknown||상세 미조회
1790590198952276|2013|Ford Explorer|XLT 4x4|6200|195000|Overland Park, KS|6|unknown||상세 미조회
1100964542322147|2014|Hyundai Sonata|GLS|5750|134000|Kansas City, MO|7|unknown||상세 미조회
1632743191843806|2018|Jeep Latitude||5985|195000|Independence, MO|8|unknown||상세 미조회
1617214946626962|2012|Nissan Rogue|sv awd|5950|118000|Olathe, KS|8|unknown|dealer|상세 미조회
2042267499791962|2019|Dodge Journey|Crossroad|6200|95000|Linwood, KS|9|unknown||상세 미조회
1798846294866211|2013|Chevrolet Cruze||5995|108000|Kansas City, KS|9|unknown||상세 미조회
1089501150291510|2009|Pontiac G6|(2009.5) GXP|5500|155000|Overland Park, KS|9|unknown||상세 미조회
2180258839557638|2014|Chevrolet Cruze|1LT|5500|124000|Kansas City, KS|9|unknown||상세 미조회
1598292605122652|2015|Kia Forte||6000|90000|Independence, MO|11|unknown||상세 미조회
4634609383479838|2014|Ford Mustang|Premium|5500|152000|Overland Park, KS|12|unknown||상세 미조회
1109711591616515|2011|Volkswagen GTI|2.0T|6000|120000|Kansas City, MO|13|unknown||상세 미조회
1027139056813774|2011|GMC Yukon XL|xl 1500 SL|5500|200000|Grain Valley, MO|16|unknown||상세 미조회
950501091430806|2014|Mitsubishi Lancer||5700|221000|Overland Park, KS|16|unknown||상세 미조회
1381877020186333|2011|Honda Pilot|Touring|5800|205000|Grandview, MO|18|unknown||상세 미조회
2204898720072170|2015|Honda Civic|Touring|6000|157000|Kansas City, MO|18|unknown||상세 미조회
1063568706438241|2012|Toyota Camry|XLE|5700|246000|Kansas City, MO|20|unknown||상세 미조회
1593238722209680|2015|Buick Encore||5950|140000|Pleasant Valley, MO|20|unknown||상세 미조회
28223644943961458|2010|Jeep Patriot||5700|109000|Kansas City, MO|21|unknown||상세 미조회
1025246220514742|2012|Jeep Liberty|Latitude|5500|159000|Kansas City, MO|22|unknown||상세 미조회
1417121590265112|2015|Volkswagen Jetta|1.8T SEL|6000|166000|Independence, MO|24|unknown||상세 미조회
1389054950772050|2014|Chevrolet Traverse|LS|5500|170000|Belton, MO|24|unknown||상세 미조회
2232753957515022|2014|Kia Sportage|EX|5999|160000|Independence, MO|27|unknown||상세 미조회
2144055726141587|2013|Lincoln MKX||5550|111000|Olathe, KS|28|unknown||상세 미조회
1026777613515603|2013|Toyota RAV4|LE|5800|284000|Gardner, KS|31|unknown||상세 미조회
1682712576131558|2008|Ford F-150||5500|88000|Kansas City, MO|33|unknown||상세 미조회
2329531724250643|2009|Toyota Camry|LE|5500|176000|Independence, MO|34|unknown||상세 미조회
1040201815452847|2010|Lincoln MKX||6000|148000|Independence, MO|34|unknown||상세 미조회
2771191469920464|2010|Toyota Highlander||5995|184000|Mission, KS|36|unknown||상세 미조회
1455756279918984|2011|Jeep Grand Cherokee L|Limited|5500|187000|Kansas City, KS|37|unknown||상세 미조회
1731254244590295|2014|Ford Edge||5700|184000|Excelsior Springs, MO|39|unknown||상세 미조회
1633642125093530|2014|Ford Edge|SEL Plus|5500|170000|Belton, MO|41|unknown||상세 미조회
1603245971347112|2013|Cadillac SRX|Luxury Collection|5500|137000|Kansas City, MO|43|unknown||상세 미조회
1877521676750871|2015|Ford Taurus|SHO|6100|130000|Lawrence, KS|43|unknown||상세 미조회
1371704107680705|2016|Nissan Versa||6000|121000|Leavenworth, KS|43|unknown||상세 미조회
1510081214224414|2012|Honda Odyssey||5995|236000|Kansas City, MO|44|unknown||상세 미조회
1747931539561466|2016|Buick Enclave||6000|136000|Kansas City, KS|47|unknown||상세 미조회
1482505267254832|2016|Kia Rio|S|6000|121000|Roeland Park, KS|49|unknown||상세 미조회
1610436760728461|2017|Chrysler Pacifica|Touring L|5889|187000|Kansas City, MO|50|unknown||상세 미조회
2147840042790076|2012|Toyota Highlander|base|5999|222000|Belton, MO|51|unknown||상세 미조회
1456220836269004|2013|Ford Escape|Titanium Hybrid|5500|140000|Pleasant Hill, MO|52|unknown||상세 미조회
1040673962037615|2014|Chevrolet Silverado 1500||5999|20000|Kansas City, MO|54|unknown||상세 미조회
1041743164994826|2014|Ford Edge||5850|148000|Kansas City, MO|56|unknown||상세 미조회
1570876844448885|2013|Buick Regal|Turbo Premium 1|6000|102000|Lee's Summit, MO|56|unknown||상세 미조회
1566051798397075|2012|Ford Edge|SEL|5950|235000|Spring Hill, KS|56|unknown||상세 미조회
3259909224188790|2019|Chevrolet Equinox||5500|199000|Kansas City, MO|59|unknown||상세 미조회
1554405376227012|2014|Jeep Compass||6000|162000|Kansas City, MO|60|unknown||상세 미조회
1689423118983456|2017|Jeep Compass|75th Anniversary|5500|160000|Shawnee, KS|61|unknown||상세 미조회
845138655351164|2014|GMC Terrain||5500|155000|Olathe, KS|62|unknown||상세 미조회
1371093041647097|2015|Ford Taurus|SEL|5500|191000|Grandview, MO|65|unknown||상세 미조회
1007732131891115|2009|Chevrolet Traverse|LT|5950|167000|Gardner, KS|65|unknown||상세 미조회
1693468841923818|2008|Chevrolet Silverado 1500||6000|123000|Bates City, MO|66|unknown||상세 미조회
1647136676394085|2015|Nissan Rogue||5500|238000|Kansas City, KS|66|unknown||상세 미조회
1458503936657689|2015|Chevrolet Malibu|LT|5950|180000|Kansas City, MO|72|unknown||상세 미조회
2511849302585739|2015|Ford Explorer|XLS|6000|167000|Independence, MO|76|unknown||상세 미조회 · 같은 차 2건 게시
1677084373410926|2010|Mazda3|i touring|5995|142000|Liberty, MO|78|unknown||상세 미조회
2092906678319241|2017|Kia Forte|GT-Line|6000|85000|Kansas City, KS|79|unknown||상세 미조회
865483556185690|2011|Dodge Charger|R/T Max|6000|140000|Independence, MO|87|unknown||상세 미조회
26797146876630519|2014|Chevrolet Silverado 1500||5999|207000|Kansas City, MO|89|unknown||상세 미조회
1537163021403138|2010|Cadillac SRX||5900|149000|Overland Park, KS|89|unknown||상세 미조회
1568057125113106|2013|Buick Enclave|Leather|5500|134000|Lawrence, KS|91|unknown||상세 미조회
993386516568530|2011|Volkswagen Golf|gti|6000|13000|Roeland Park, KS|108|unknown||상세 미조회
1318493973584626|2019|Kia Sportage|LX|6000|161000|Kansas City, MO|111|unknown||상세 미조회
1504821741111415|2015|Lincoln MKZ|Hybrid|5500|217000|Independence, MO|111|unknown||상세 미조회
1298875965185027|2017|Ford Escape|Titanium|6000|137000|Overland Park, KS|79|unknown||상세 미조회
811204251542869|2017|Subaru Forester|2.5i|5500|288000|Kansas City, MO|169|unknown||상세 미조회
1051828934346119|2013|Chevrolet Traverse|2LT|6500|166000|Olathe, KS|0|unknown||상세 미조회
1402339501315497|2011|Toyota Corolla||6400|145000|Kansas City, KS|0|unknown||상세 미조회
1800425167766245|2009|Toyota Avalon|XLS|6546|205000|Kansas City, MO|2|unknown||상세 미조회
1065088863020690|2015|Jeep Patriot|Latitude|6500|152000|Lee's Summit, MO|3|unknown||상세 미조회
1450016180322001|2010|Ford Explorer||6950|171000|Spring Hill, KS|3|unknown||상세 미조회
1664441985291614|2015|Chrysler Town & Country|Touring|6999|127000|Lenexa, KS|4|unknown||상세 미조회
1095331826288539|2013|Dodge Durango|SXT|6300|193000|Kansas City, KS|4|unknown||상세 미조회
1608736377590972|2018|Ford Fiesta|S|6600|58000|Shawnee, KS|5|unknown||상세 미조회
2159618334981936|2009|Acura TSX||6999|153000|Kansas City, MO|5|unknown|dealer|상세 미조회
1022473150818527|2018|Ford Focus|SE|6500|115000|Lee's Summit, MO|5|unknown||상세 미조회
1600131104827201|2016|Chevrolet Trax|Lt AWD|6350|96000|Olathe, KS|5|unknown||상세 미조회
995647720244646|2014|Volkswagen Jetta|2.0L TDI S|6700|151000|Gardner, KS|6|unknown||상세 미조회
4041065526198898|2015|Buick Regal|Turbo Premium 1|6500|128000|Independence, MO|6|unknown||상세 미조회
1087878550308770|2017|Ford F-150||6500|214000|Kansas City, MO|6|unknown||상세 미조회
1344310821112431|2015|Acura RDX|FWD w/Technology Pkg|6995|202000|Mission, KS|7|unknown|dealer|상세 미조회
1156651350365442|2014|Mazda3|Sport|6900|90000|Kansas City, MO|7|unknown||상세 미조회
1393491118934604|2011|Land Rover Range Rover Sport|range rover sport HSE Lux|6800|167000|Kansas City, MO|7|unknown||상세 미조회
1763966011470143|2016|Kia Rio||6300|122000|Kansas City, MO|7|unknown||상세 미조회
1049835821216065|2015|Subaru Crosstrek|limited 2.0 awd|6950|195000|Olathe, KS|7|unknown|dealer|상세 미조회
1835361904119757|2019|Dodge Journey|SE|6500|150000|Independence, MO|8|unknown||상세 미조회
2062491927710406|2012|Volvo S80|3.2|6900|110000|Kansas City, MO|9|unknown||상세 미조회
1366333345569740|2016|Nissan Versa||6995|104000|Lee's Summit, MO|10|unknown||상세 미조회
1631203348594100|2016|Kia Soul||6500|110000|Overland Park, KS|10|unknown||상세 미조회
1764706401232556|2014|Chevrolet Camaro|LS|6500|163000|Kansas City, KS|10|unknown||상세 미조회
1619280766456816|2011|Acura TL|3.2 Type S|6400|185000|Kansas City, MO|10|unknown||상세 미조회
1802994724360753|2011|Ford F-150||6500|200000|Kansas City, MO|11|unknown||상세 미조회
1795199951797624|2018|Chevrolet Trax|LS|6950|98000|Olathe, KS|12|unknown||상세 미조회
1611422037227202|2010|Mercedes-Benz GLK-Class||6900|171000|Kansas City, KS|12|unknown||상세 미조회
1760739818413183|2014|Subaru Forester||6999|198000|Kansas City, MO|12|unknown||상세 미조회
1433577385290002|2014|Ford Focus|SE|6500|25000|Lenexa, KS|15|unknown||상세 미조회
27440183472322004|2016|Chevrolet Trax||6999|140000|Kansas City, MO|15|unknown||상세 미조회
1398229078307233|2008|Hummer H3||6500|207000|Overland Park, KS|16|unknown||상세 미조회
2915419982157043|2014|Ford Explorer|Police Interceptor|6500|208000|Independence, MO|16|unknown||상세 미조회
2593812644382672|2012|Jeep Cherokee|Limited|6800|204000|Kansas City, KS|17|unknown||상세 미조회
927857447044677|2014|Nissan Maxima|SV|6500|188000|Olathe, KS|18|unknown||상세 미조회
892102490446935|2013|Honda Civic|EX|6500|166000|Overland Park, KS|18|unknown||상세 미조회
1721513192296159|2016|Volkswagen Jetta|1.8T Sport|6800|116000|Shawnee, KS|19|unknown||상세 미조회
2790658737972292|2014|Ford Flex|SEL|6500|170000|Kansas City, MO|20|unknown||상세 미조회
2495706944242146|2016|Ford Edge||6500|160000|Independence, MO|20|unknown||상세 미조회
1392565025565197|2016|Kia Sedona|Limited|6500|155000|Kansas City, MO|21|unknown||상세 미조회
1067921822702266|2015|Chevrolet Colorado|Es 4 cilindros no es 4x4|6600|23000|Kansas City, KS|22|unknown||상세 미조회
2136083690335766|2017|Chevrolet Equinox||6600|132000|Kansas City, MO|22|unknown||상세 미조회
1389829869937657|2018|Lincoln MKT|Premiere|6500|387000|Kansas City, KS|24|unknown||상세 미조회
1717035309597979|2011|Volkswagen GTI|2.0T|6400|135000|Kansas City, KS|24|unknown||상세 미조회
2323626634837684|2009|Toyota Venza||6800|177000|Kansas City, MO|25|unknown||상세 미조회
1780156769674643|2014|Jeep Patriot||6800|120000|Belton, MO|25|unknown||상세 미조회
1746632173239780|2011|Hyundai Genesis|4.6|6500|86000|Independence, MO|25|unknown||상세 미조회
4468722826684324|2008|Hyundai Veracruz||6700|14000|Kansas City, MO|26|unknown||상세 미조회
1059174097082615|2014|Jeep Compass|Freedom|6500|126000|Overland Park, KS|26|unknown||상세 미조회
4326274010971637|2016|Nissan Pathfinder|SV|6950|124000|Pleasant Valley, MO|26|unknown||상세 미조회
1370308988597788|2015|Buick Encore||6550|163000|Kansas City, MO|27|unknown||상세 미조회
1297827882312797|2012|Infiniti QX56||6800|200000|Bonner Springs, KS|28|unknown||상세 미조회
2167862890800076|2014|Chevrolet Equinox|LTZ|6700|152000|Overland Park, KS|29|unknown||상세 미조회
1378885737101569|2010|Toyota Corolla|CE|6800|151000|Overland Park, KS|30|unknown||상세 미조회
1243684544550526|2013|Acura ILX|Hybrid|6500|94000|Kansas City, KS|31|unknown||상세 미조회
1363388418842055|2017|Chevrolet Equinox||6500|145000|Kansas City, MO|31|unknown||상세 미조회
1553940686479635|2012|Toyota Prius|4|6500|161000|Lee's Summit, MO|31|unknown||상세 미조회
1043463225104239|2017|Nissan Rogue Sport||6350|125000|Kansas City, MO|32|unknown||상세 미조회
1084565240779310|2014|Nissan Pathfinder|SL|6500|135000|Kansas City, KS|32|unknown||상세 미조회
1961477387852428|2012|Infiniti QX56|4WD|6900|198000|Kansas City, MO|33|unknown||상세 미조회
27793955783630739|2015|Dodge Dart|SE|6500|74000|Kansas City, MO|34|unknown||상세 미조회
1693542138390294|2015|GMC Acadia|Denali|6995|175000|Kansas City, MO|36|unknown||상세 미조회
1785780399118106|2012|Honda Pilot|EX-L w/Honda Sensing|6950|200000|Kansas City, KS|37|unknown||상세 미조회
1371756191541531|2013|Chevrolet Cruze|2LT|6500|94000|Grain Valley, MO|39|unknown||상세 미조회
1815133353231547|2014|Nissan Pathfinder|SL|6500|143000|Kansas City, MO|41|unknown||상세 미조회
1078213057892328|2018|Chevrolet Malibu|LT|6500|155000|Kansas City, KS|41|unknown||상세 미조회
1640049461162394|2016|Chevrolet Trax|LS|6500|111000|Harrisonville, MO|41|unknown||상세 미조회
1048597564250752|2014|Ford Escape|SE|6500|155000|Kansas City, MO|43|unknown||상세 미조회
903353189503449|2011|Cadillac DTS||6750|158000|Independence, MO|43|unknown||상세 미조회
2287872792008071|2016|Ford Explorer|XLT|6500|156000|Pleasant Hill, MO|43|unknown||상세 미조회
1428412829162411|2017|Ford Fusion|SE|6995|161000|Independence, MO|44|unknown||상세 미조회
1265915572211198|2017|Chrysler Pacifica||6499|188000|Kansas City, MO|45|unknown||상세 미조회
1762615098488150|2008|Land Rover Range Rover|range rover Supercharged|6250|148000|Mission, KS|51|unknown||상세 미조회
1043283558165460|2010|Lexus HS|250h|6950|164000|Belton, MO|53|unknown|dealer|상세 미조회
1864015481651128|2014|Nissan Pathfinder|Platinum|6500|177000|Olathe, KS|56|unknown||상세 미조회
1386509673577768|2020|Chevrolet Sonic|LT|6500|137000|Independence, MO|57|unknown||상세 미조회
2001641657183110|2008|Chevrolet Suburban|1500 LTZ|6500|200000|Kansas City, MO|58|unknown||상세 미조회
1408716004599175|2017|Ford Escape|SE|6850|110000|Pleasant Hill, MO|59|unknown||상세 미조회
1276227234442944|2009|Toyota Venza||6500|198000|Kansas City, MO|63|unknown||상세 미조회
1420164503281742|2013|Nissan Versa|SL|6950|98000|Overland Park, KS|65|unknown||상세 미조회
1532160241922070|2014|GMC Acadia|SLE|6450|184000|Kansas City, MO|66|unknown||상세 미조회
4470401736551113|2016|BMW 5 Series|series 528i xDrive|6900|158000|Kansas City, MO|68|unknown||상세 미조회
1022444830194341|2015|MINI Cooper||6500|128000|Independence, MO|74|unknown||상세 미조회
1358120955741806|2015|Nissan Murano||6900|201000|Independence, MO|75|unknown|dealer|상세 미조회
1348036497474692|2016|Chevrolet Equinox|LT|6500|167000|Kansas City, MO|76|unknown||상세 미조회
27689564840682878|2018|Ford EcoSport|SE|6500|109000|Independence, MO|79|unknown||상세 미조회
1966603547465768|2013|Nissan Murano|Platinum|6295|173000|Overland Park, KS|81|unknown||상세 미조회
2279061819563024|2011|Nissan Altima|2.5 s|6800|87000|Overland Park, KS|87|unknown||상세 미조회
2242212559848115|2014|Ford Mustang|V6|6500|145000|Kansas City, MO|89|unknown||상세 미조회
1368223485196395|2012|Dodge Journey|SXT|6499|82000|Kansas City, MO|90|unknown||상세 미조회
986509610745738|2013|Ford Explorer|XLT|6500|161000|Kansas City, MO|111|unknown||상세 미조회
852935947854621|2012|MINI Jcw||6800|117000|Lawrence, KS|132|unknown||상세 미조회
1396762359148590|2019|Kia Soul||6300|112000|Fairway, KS|153|unknown||상세 미조회
1559662235843010|2008|Ford F-350|super duty|550|258000|Kansas City, KS|6|unknown||상세 미조회
910744165049705|2008|Ford Edge|Limited|600|180000|Olathe, KS|20|unknown||상세 미조회
1063851929874836|2012|Ford Edge||800|200000|Mission, KS|24|unknown||상세 미조회
1758970331960073|2013|Genesis 4dor|X|950|222000|Blue Springs, MO|54|unknown|dealer|상세 미조회
1067651122881417|2013|Dodge Dart||800|194000|Belton, MO|66|unknown||상세 미조회
1326772619231111|2011|Toyota Corolla|S|700|152000|Kansas City, MO|68|unknown||상세 미조회
1008964318250235|2009|Ford F-150|FX2|650|200000|Mission, KS|116|unknown||상세 미조회
1664785841195031|2022|Volkswagen Taos|SEL 4MOTION|850|40000|Kansas City, MO|155|unknown||상세 미조회
1797344408309734|2016|Ford Escape|S|700|12000|Kansas City, MO|81|unknown||상세 미조회
1580247326925211|2010|Chevrolet Camaro|SS|650|12000|Kansas City, MO|83|unknown||상세 미조회
3254219361427732|2013|Chevrolet Malibu||550|175000|Linn Valley, KS|117|unknown||상세 미조회
2270412703734467|2008|Ford Edge||850|180000|Olathe, KS|19|unknown||상세 미조회
1321608839958617|2020|Jeep Wrangler||750|20000|Lee's Summit, MO|69|unknown||상세 미조회
787738097697585|2025|Ford F-150||850||Kansas City, MO|81|unknown||상세 미조회
1486074673065031|2009|Mercury Mountaineer||800|179000|Kansas City, MO|126|unknown||상세 미조회
1653030616538665|2010|Honda Accord|EX|1100|168000|Raytown, MO|0|unknown||상세 미조회
3071320196582154|2008|Ford Fusion|SE|1000|123000|Lone Jack, MO|1|unknown||상세 미조회
1102763949279681|2011|Chevrolet Silverado 1500||1300|98000|Kansas City, KS|3|unknown||상세 미조회
4725399614355782|2009|Lincoln MKZ||1234|221000|Drexel, MO|3|unknown||상세 미조회
2311310782936745|2014|Jeep Cherokee|TrailHawk|1234|144000|Kansas City, MO|7|unknown||상세 미조회
1446536114289858|2011|Dodge Dakota||1100|198000|Greenwood, MO|7|unknown||상세 미조회
1703542144052932|2008|Honda Accord|EX|1000|158000|Kansas City, MO|10|unknown||상세 미조회
1012233405198093|2010|Kia Rondo||1000|190000|Kansas City, MO|16|unknown||상세 미조회
28037569689228801|2008|Infiniti G37|Sport|1234|113000|Kansas City, MO|19|unknown||상세 미조회
980063957765345|2013|Ford F-150||1000|304000|Kansas City, KS|20|unknown||상세 미조회
1378986563756764|2012|Nissan Maxima||1200|155000|Blue Springs, MO|26|unknown||상세 미조회
915743584481092|2011|Jeep Liberty|Renegade|1000|255000|Oak Grove, MO|26|unknown||상세 미조회
1073077065658326|2011|Dodge Journey||1200|176000|Smithville, MO|27|unknown||상세 미조회
3725175594297074|2008|Honda Pilot||1000|180000|Kansas City, KS|31|unknown||상세 미조회
1440593554647013|2015|Chevrolet Silverado 1500||1234|166000|Kingsville, MO|31|unknown||상세 미조회
2277023073070461|2010|Nissan Versa||1200|124000|Grandview, MO|35|unknown||상세 미조회
1052499877701211|2011|Dodge Grand Caravan|passenger Express|1000|205000|Kansas City, MO|40|unknown||상세 미조회
1356802756104940|2013|Mercedes-Benz Sprinter|High Roof Extended w/170" WB|1234|180000|Kansas City, MO|41|unknown||상세 미조회
1378910264344671|2013|Dodge Grand Caravan||1000|150000|Kansas City, MO|42|unknown||상세 미조회
916320284284249|2011|Chevrolet Suburban|1500 LS|1234|8000|Kearney, MO|44|unknown||상세 미조회
2158430325556784|2008|Honda Accord|v6|1200|265000|Kansas City, KS|47|unknown||상세 미조회
1772885377223703|2008|Chevrolet Silverado 1500|1500|1234|103000|Independence, MO|47|unknown||상세 미조회
1530789242183995|2012|Chevrolet Malibu|LT|1234|250000|Lenexa, KS|51|unknown||상세 미조회
2146145629283528|2008|Audi A4|2.0T Avant Quattro|1234|243000|Kansas City, MO|51|unknown||상세 미조회
1807659156887216|2009|Ford Escape|Limited|1400|162000|Kansas City, KS|53|unknown||상세 미조회
1046912561486618|2011|Nissan Altima|2.5 S|1234|20000|Overland Park, KS|55|unknown||상세 미조회
1743880676742796|2009|Chevrolet Impala|SS|1400|250000|Independence, MO|56|unknown||상세 미조회
1378380534360554|2010|Chevrolet Express||1400|244000|Kansas City, KS|57|unknown||상세 미조회
1647689334024315|2016|Ford Focus|S|1234|116000|Kansas City, KS|57|unknown||상세 미조회
973990082354404|2008|Chevrolet Malibu|limited LT|1200|170000|Kansas City, MO|62|unknown||상세 미조회
2143449492887227|2008|Honda Odyssey||1450|223000|Kansas City, MO|64|unknown||상세 미조회
1482104613955546|2011|Ford Fusion|SEL|1200|190000|Kansas City, MO|72|unknown||상세 미조회
1746750150008554|2014|Chrysler Town & Country|LX|1234|12000|Odessa, MO|80|unknown||상세 미조회
1324899739749346|2008|Ford Expedition EL|el King Ranch|1200|200000|Bucyrus, KS|82|unknown||상세 미조회
1040316218521178|2012|Nissan Rogue||1250|169000|Kansas City, MO|97|unknown||상세 미조회
1447484530758468|2015|GMC Acadia||1000|190000|Kansas City, MO|104|unknown||상세 미조회
1788516702134823|2010|Hyundai Genesis||1200|220000|Kansas City, MO|113|unknown||상세 미조회
1773553640719660|2012|Kia Sorento|EX|1200|200000|Raymore, MO|120|unknown||상세 미조회
1727865415051278|2014|Ford Escape|S|1100|1200|Kansas City, MO|134|unknown||상세 미조회
833362569812949|2010|Chevrolet Malibu|LT|1000|185000|Kansas City, MO|146|unknown||상세 미조회
1034743099461591|2013|Ford Focus|SE|1234|289000|Kansas City, KS|18|unknown||상세 미조회
1848340093215425|2011|BMW 3 Series|series 328i xDrive|1200|120000|Kansas City, MO|19|unknown||상세 미조회
1042860938486423|2014|Dodge Ram 2500||1234|230000|Kansas City, MO|41|unknown||상세 미조회
1358105503170001|2013|Nissan Versa|S|1200|156000|Overland Park, KS|47|unknown||상세 미조회
1749605229692496|2010|GMC Terrain|SLT-2|1234|128000|Kansas City, MO|48|unknown||상세 미조회
1076751938251207|2014|BMW 5 Series|series 528i|1234|160000|Kansas City, MO|49|unknown||상세 미조회
1745076473278468|2008|Honda Accord|SE|1234|123000|Kansas City, MO|53|unknown||상세 미조회
28515885678000823|2009|Dodge Challenger||1234|100000|Kansas City, MO|76|unknown||상세 미조회
3939560749673191|2010|Chevrolet Cobalt|LT|1000|213000|Grandview, MO|4|unknown||상세 미조회
1091301910019349|2008|Mazda CX-9|Grand Touring|1000|241000|Spring Hill, KS|28|unknown||상세 미조회
1313757784256867|2011|Jeep Compass||1000|130000|Kansas City, KS|77|unknown||상세 미조회
1748655166836501|2012|Chevrolet Malibu|(classic) LS|1000|164000|Kansas City, MO|98|unknown||상세 미조회
1014257054364602|2011|Suzuki Grand|vitara|1000|214000|Kansas City, KS|128|unknown||상세 미조회
1793979595384987|2009|Toyota Camry|CE|1000|227000|Kansas City, MO|88|unknown||상세 미조회
1546054533532664|2017|Chevrolet Tahoe||1111|111000|Kansas City, MO|86|unknown||상세 미조회
2852503651801549|2010|Jeep Wrangler||1234|324000|Lone Jack, MO|4|unknown||상세 미조회
1045513528353597|2016|Nissan Rogue|S|1234|155000|Kansas City, MO|25|unknown||상세 미조회
1603225361498152|2020|Ford F-250|HD Long Bed|1234|10000|Kansas City, MO|28|unknown||상세 미조회
3078728469130646|2014|Ford Fusion|SE|1234|123000|Kansas City, MO|48|unknown||상세 미조회
1763933594642648|2011|Dodge Journey|Crew|1234|201000|Belton, MO|54|unknown||상세 미조회
2076477549632808|2014|Ford Fusion|SE Hybrid|1234|205000|Spring Hill, KS|102|unknown||상세 미조회
1649068986516239|2015|Lexus RC|350 F SPORT|1234|123000|Kansas City, MO|169|unknown||상세 미조회
951938357901638|2011|Honda Accord|EX-L|1234|209000|Kansas City, KS|71|unknown||상세 미조회
1444888157661114|2010|Toyota Prius|Four|1234|170000|Kansas City, MO|71|unknown||상세 미조회
1355383246219706|2027|Audi I8||1234|100000|Kansas City, KS|72|unknown||상세 미조회
1329866645909699|2009|Chevrolet Traverse|LT|1234|200000|Kansas City, KS|76|unknown||상세 미조회
1555756659501429|2013|Chevrolet Silverado 1500||1234|199000|Parker, KS|94|unknown||상세 미조회
1642772577010747|2010|Toyota Tacoma||1233|120000|Independence, MO|108|unknown||상세 미조회
2031335474470464|2008|Dodge Nitro|SXT|1234|230000|Harrisonville, MO|158|unknown||상세 미조회
1467369565436291|2009|Hyundai Sonata||1300||McLouth, KS|96|unknown||상세 미조회
1907068623290691|2011|Buick LaCrosse|Cxl|1299|143000|Kansas City, MO|98|unknown||상세 미조회
935992959469246|2010|Nissan Rogue||1400|149000|Kansas City, MO|119|unknown||상세 미조회
1013783891082780|2014|Nissan Murano|SE|1300|165000|Kansas City, KS|143|unknown||상세 미조회
1395441962740162|2011|Toyota Camry|Hybrid SE|1500|228000|Liberty, MO|0|unknown||상세 미조회
1592832315657453|2008|Ford Taurus|Limited|1500|220000|Kansas City, MO|2|unknown||상세 미조회
1091742283398129|2013|GMC Terrain||1700|193000|Kansas City, MO|4|unknown||상세 미조회
1801777937917285|2017|Ford Edge|Limited|1600|137000|Kansas City, MO|5|unknown||상세 미조회
1781445649671553|2016|Nissan Pathfinder|LE|1500|208000|Olathe, KS|9|unknown||상세 미조회
4484630868514208|2010|Jeep Liberty|Limited|1500|198000|Kansas City, KS|10|unknown||상세 미조회
1047532288052688|2012|Chrysler Town & Country|Limited|1500|178000|Sugar Creek, MO|11|unknown||상세 미조회
877695778614704|2013|Nissan Altima|2.5 Platinum|1500|19000|Shawnee, KS|16|unknown||상세 미조회
1860166175155675|2014|Chevrolet Traverse||1500|185000|Kansas City, MO|18|unknown||상세 미조회
1651967393215187|2012|Kia Soul|!|1500|187000|Orrick, MO|25|unknown||상세 미조회
3367627353412004|2011|Subaru Outback|2.5i Limited|1500|242000|Overland Park, KS|26|unknown||상세 미조회
1310888584291076|2014|Nissan Quest|LE|1500|160000|Kansas City, KS|26|unknown||상세 미조회
1304072768322634|2011|Cadillac STS||1900|188000|Lee's Summit, MO|29|unknown||상세 미조회
28365534699778172|2010|Nissan Rogue|SL (2018.5)|1500|200000|Kansas City, MO|36|unknown||상세 미조회
1692849585216382|2012|Subaru Impreza|2.0i Premium|1800|224000|Leavenworth, KS|37|unknown||상세 미조회
2094196967971796|2008|Ford Taurus|x SEL|1500|266000|Kansas City, MO|38|unknown||상세 미조회
1078726841247156|2008|Buick Enclave||1500|188000|Kansas City, MO|48|unknown||상세 미조회
1533461984493883|2010|Honda Odyssey|EX|1800|140000|East Lynne, MO|55|unknown||상세 미조회
1025265520255931|2008|Lincoln MKX|Black Label|1500|300000|Shawnee, KS|56|unknown||상세 미조회
1021893747493861|2015|Kia Optima|EX|1500|173000|Kansas City, MO|56|unknown||상세 미조회
1036898612084411|2008|Ford Taurus|x 4x4|1700||Kansas City, MO|60|unknown||상세 미조회
1086730510537173|2009|Chevrolet TrailBlazer||1600|2000|Overland Park, KS|61|unknown||상세 미조회
2171504470091329|2010|Nissan Maxima|GLE|1750|225000|Platte City, MO|61|unknown||상세 미조회
2086701122271479|2008|Chevrolet Malibu|L|1900|177000|Kansas City, MO|63|unknown||상세 미조회
1532439731476259|2008|Honda Odyssey|Touring|1500|233000|Kansas City, KS|83|unknown||상세 미조회
1523607292891038|2009|Honda Ridgeline||1900|170000|Spring Hill, KS|90|unknown||상세 미조회
1475040811060416|2009|Pontiac G6|GXP|1600|144000|Grandview, MO|112|unknown||상세 미조회
28549863241335228|2008|Honda Civic|EX|1500|20000|Kansas City, MO|5|unknown||상세 미조회
2256913901804133|2010|Pontiac G6||1500|203000|Gardner, KS|51|unknown||상세 미조회
808293328974838|2009|Pontiac G6||1500|250000|Osawatomie, KS|54|unknown||상세 미조회
1934532800428763|2010|Buick Enclave|CX|1500|198000|Kansas City, KS|61|unknown||상세 미조회
1336433151951639|2008|Chrysler Town & Country|Limited|1500|200000|Kansas City, MO|78|unknown||상세 미조회
1598087505435103|2009|Nissan Maxima|SL|1500|200000|Kansas City, MO|8|unknown||상세 미조회
1393426116327907|2012|Subaru Impreza|Premium|1500|261000|Kansas City, MO|23|unknown||상세 미조회
1889739738371581|2008|Subaru 30r||1700|160000|Kansas City, KS|79|unknown||상세 미조회
1101740758955057|2010|Mazda3||1900|177000|Kansas City, MO|4|unknown||상세 미조회
1066500926263737|2011|Buick Enclave|CX|1800|195000|Kansas City, MO|17|unknown||상세 미조회
1694214355663295|2012|GMC Acadia|Denali|1900|171000|Drexel, MO|38|unknown||상세 미조회
1952629055615508|2010|Toyota RAV4|"Sport"|1800|120000|Kansas City, KS|144|unknown||상세 미조회
1832444377452846|2012|Chevrolet Traverse|LT|1900|156000|Kansas City, KS|174|unknown||상세 미조회
1717783027022529|2010|Dodge Avenger|SXT|2000|255000|Kansas City, MO|1|unknown||상세 미조회
1732620724460271|2012|Chrysler Town & Country|Limited|2000|205000|Overland Park, KS|3|unknown||상세 미조회
1565089778076005|2013|Dodge Grand Caravan|passenger R/T|2400|215000|Kansas City, MO|5|unknown||상세 미조회
1402338615187030|2010|Ford Focus|SE|2300|222000|Kansas City, MO|9|unknown||상세 미조회
1347746427145240|2011|Chevrolet Cruze|LT|2000|135000|Kansas City, KS|11|unknown||상세 미조회
1080774574429239|2019|Chevrolet Silverado 1500||2000|145000|Overland Park, KS|16|unknown||상세 미조회
1565386128056394|2008|Ford Edge|Limited|2200|199000|Kansas City, MO|18|unknown||상세 미조회
1846006793447955|2013|Buick Encore|Leather|2200|200000|Olathe, KS|18|unknown||상세 미조회
1070475755353399|2026|Chevrolet Colorado|Trail Boss|2000||Kansas City, MO|21|unknown||상세 미조회
27804522192576296|2009|Honda Odyssey||2400|235000|Kansas City, MO|28|unknown||상세 미조회
1066381995883731|2013|Ford F-150||2000|194000|Kansas City, KS|29|unknown||상세 미조회
1398636265726761|2013|Hyundai Accent|GLS|2000|300000|Holden, MO|35|unknown||상세 미조회
987659904333659|2014|Subaru Forester|L|2000|200000|Olathe, KS|37|unknown||상세 미조회
1792225798457149|2008|Jeep Patriot|Limited|2000|240000|Independence, MO|38|unknown||상세 미조회
1075440428169965|2013|Cadillac SRX|Luxury Collection|2000|250000|Kansas City, MO|40|unknown||상세 미조회
2096371377625794|2010|Buick LaCrosse|CXL|2000|209000|Adrian, MO|42|unknown||상세 미조회
1528765628379694|2010|Chevrolet Suburban||2000|280000|Kansas City, MO|48|unknown||상세 미조회
1440835441228373|2009|Chevrolet Cobalt|LT|2100|250000|Garden City, MO|52|unknown||상세 미조회
1049198674263040|2009|Lincoln MKS||2000|225000|Orrick, MO|63|unknown||상세 미조회
1207505391516625|2014|Dodge Avenger|SE V6|2000|182000|Peculiar, MO|71|unknown||상세 미조회
1009102661728262|2010|Mazda CX-9|Grand Touring|2000|322000|Bonner Springs, KS|74|unknown||상세 미조회
3761424170664020|2014|GMC Acadia|SLT 1|2000|177000|Kansas City, MO|74|unknown||상세 미조회
3985130924951314|2013|GMC Acadia||2000|170000|Kansas City, MO|90|unknown||상세 미조회
1294260146210293|2012|BMW 550i|xdrive|2000|140000|Shawnee, KS|107|unknown||상세 미조회
1013198977940031|2008|Kia Optima|LX|2000|167000|Kansas City, MO|119|unknown||상세 미조회
2439863619772580|2009|Toyota RAV4|"Sport"|2200|165000|Kansas City, MO|119|unknown||상세 미조회
990888813481016|2008|Hyundai Santa Fe|SE|2000|98000|Mission, KS|127|unknown||상세 미조회
26504199852565751|2018|BMW X2|xDrive28i|2350|65000|Kansas City, MO|151|unknown||상세 미조회
1482252473581019|2012|Nissan Rogue|S|2000|206000|Kansas City, MO|156|unknown||상세 미조회
1888342702553571|2010|Mercury Milan|premier|2000|178000|Kansas City, KS|160|unknown||상세 미조회
28533461596283615|2011|Chevrolet Silverado 1500||2000|2000|Overland Park, KS|2|unknown||상세 미조회
1853697168949297|2021|Buick Lucerne|CXS|2000|255000|Kansas City, MO|24|unknown||상세 미조회
1052681357150503|2009|Dodge Caliber||2000|150000|Wellsville, KS|53|unknown||상세 미조회
1524066419733837|2014|Ford Escape||2000|139000|Kansas City, KS|54|unknown||상세 미조회
960032320431786|2011|Chevrolet Malibu|L|2000|196000|Shawnee, KS|55|unknown||상세 미조회
2398648167329303|2014|BMW X5|xDrive35i|2000|150000|Kansas City, KS|57|unknown||상세 미조회
865447062997916|2011|GMC Acadia|SLE|2000|207000|Osawatomie, KS|67|unknown||상세 미조회
2816333698751259|2011|Dodge Journey|Mainstreet|2000|218000|Overland Park, KS|69|unknown||상세 미조회
1978489789461470|2008|Chrysler Sebring|Touring|2000|159000|Overland Park, KS|94|unknown||상세 미조회
994603246730919|2015|Buick Encore||2000|182000|Kansas City, MO|63|unknown||상세 미조회
1798227374495302|2009|Nissan Murano||2000|214000|Olathe, KS|85|unknown||상세 미조회
1550947136447617|2010|Chevrolet Equinox|LT|2000|102000|Gardner, KS|116|unknown||상세 미조회
2265017110948063|2011|Ford F-150||2250|238000|Kansas City, MO|8|unknown||상세 미조회
1074261358408415|2008|Mercury Grand Marquis|LS Premium|2300|241000|Leavenworth, KS|44|unknown||상세 미조회
1703841380902526|2016|Chevrolet Cruze||2300||Kansas City, MO|60|unknown||상세 미조회
3232978340237263|2008|Toyota Yaris|S|2300|200000|Kansas City, KS|62|unknown||상세 미조회
1354215886879667|2013|Nissan Altima|2.5 S|2300|196000|Kansas City, MO|64|unknown||상세 미조회
1350922743261534|2016|Kia Rio||2300|119000|Kansas City, MO|75|unknown||상세 미조회
1309395170822762|2009|Honda CR-V|EX|2345|123000|Lone Jack, MO|102|unknown||상세 미조회
843897955031764|2012|Dodge Journey||2495|200000|Kansas City, MO|110|unknown||상세 미조회
1588141863009416|2009|Toyota Prius|Other|2997|284000|Kansas City, KS|4|unknown||상세 미조회
38637379575877915|2010|Ford Edge|SE|2500|328000|Kansas City, MO|6|unknown||상세 미조회
3243354515848935|2008|BMW X3|2.5i|2800|190000|Kansas City, KS|6|unknown||상세 미조회
1609185997522005|2009|Chevrolet Aveo||2799|169000|Olathe, KS|6|unknown||상세 미조회
1889672681997753|2012|Nissan Murano||2500|206000|Kansas City, KS|9|unknown||상세 미조회
1082359101194915|2010|Dodge Journey||2800|211000|Kansas City, KS|10|unknown||상세 미조회
1399257958262952|2011|Jeep Cherokee|Classic|2500|235000|Kansas City, MO|10|unknown||상세 미조회
1422316106443381|2009|Toyota Yaris||2900|220000|Shawnee, KS|13|unknown||상세 미조회
1826793561784231|2014|Jeep Patriot||2500|225000|Kansas City, MO|14|unknown||상세 미조회
1513744920791630|2008|Pontiac G6||2800|148000|Kansas City, KS|15|unknown||상세 미조회
1377437574567830|2008|Ford Focus||2500|158000|La Cygne, KS|17|unknown||상세 미조회
1642053620772417|2009|Nissan Cube|Krom|2500|177000|Kansas City, MO|28|unknown||상세 미조회
1537347865071959|2013|Volkswagen Jetta|2.5 se|2500|152000|Lee's Summit, MO|31|unknown||상세 미조회
1625069769231006|2009|Jaguar XF|Premium Luxury|2500|225000|Kansas City, MO|32|unknown||상세 미조회
1629789068707222|2012|Dodge Grand Caravan|passenger Crew|2900|219000|Kansas City, KS|32|unknown|dealer|상세 미조회
2337034957189012|2015|Mitsubishi Outlander Sport|S|2600|167000|Kansas City, KS|39|unknown||상세 미조회
1713662686345467|2008|Ford F-150||2500|217000|Overland Park, KS|44|unknown||상세 미조회
885608194318559|2012|Ford Fusion|SE|2800|200000|Garden City, MO|46|unknown||상세 미조회
1089306593520366|2017|Ford Expedition EL|el Limited|2500|230000|Freeman, MO|48|unknown||상세 미조회
4397974390349123|2008|Chevrolet Cobalt||2500|200000|Bates City, MO|58|unknown||상세 미조회
1761833214813197|2010|Volvo XC90|3.2|2500|160000|Grandview, MO|61|unknown||상세 미조회
1373185914764114|2008|Mercury Mariner||2800|174000|Kingsville, MO|67|unknown||상세 미조회
3215740705272171|2011|Nissan Versa|S|2800|171000|Kansas City, MO|84|unknown||상세 미조회
1648498262894344|2008|Ford Edge|Limited|2500|198000|Parker, KS|91|unknown||상세 미조회
1028931819478355|2012|Ford Fiesta|SE|2500|204000|Kansas City, KS|99|unknown||상세 미조회
1653073309299335|2014|Jeep Cherokee|Limited|2500|188000|Independence, MO|132|unknown||상세 미조회
2151332219000521|2015|Subaru Outback|2.5i Premium|2800|170000|Lawrence, KS|147|unknown||상세 미조회
2731481467236931|2008|Cadillac CTS|3.6 Luxury|2500|200000|Independence, MO|149|unknown||상세 미조회
2116937195819245|2011|Jeep Grand Cherokee|All New Overland|2500|233000|Kansas City, KS|163|unknown||상세 미조회
39318249304428929|2010|Chevrolet Silverado 1500|(classic) 1500 hd|2500|277000|Adrian, MO|22|unknown||상세 미조회
1583935419805569|2013|Ford F-150||2500|328000|Lee's Summit, MO|25|unknown||상세 미조회
2414404779048336|2010|Chevrolet Suburban|1500 LT|2700|254000|Kansas City, MO|32|unknown||상세 미조회
1583233460180170|2009|Chevrolet Cobalt||2500|209000|Adrian, MO|52|unknown||상세 미조회
1534409291201198|2010|Ford F-150||2500|250000|Kansas City, MO|61|unknown||상세 미조회
2519451031891739|2012|BMW X5|xDrive35i Premium|2500|244000|Gardner, KS|65|unknown||상세 미조회
1571946217641652|2015|Subaru Forester|2.5X|2500|217000|Raymore, MO|73|unknown||상세 미조회
1339226880906972|2011|Dodge Journey|AVP|2600|190000|Kansas City, MO|89|unknown||상세 미조회
1776641356648271|2012|Ford Fusion|Sport|2500|233000|Gardner, KS|146|unknown||상세 미조회
1574573744395286|2013|Jeep Grand Cherokee L|l Limited|2500|187000|Independence, MO|42|unknown||상세 미조회
1509077270968533|2008|Chevrolet Uplander||2500|202000|Kansas City, MO|59|unknown||상세 미조회
3613988998779455|2009|Dodge Durango|SLT|2500|200000|Kansas City, MO|73|unknown||상세 미조회
1036613005975286|2008|Dodge Durango|SLT|2500|158000|Kansas City, MO|88|unknown||상세 미조회
1328116652605640|2012|Chevrolet Traverse|LT|2500|230000|Independence, MO|159|unknown||상세 미조회
1353066400312393|2015|Nissan Rogue Select||2500|139000|Overland Park, KS|63|unknown||상세 미조회
1734230557721472|2013|Ford Fusion|Hybrid|2700|130000|Kansas City, MO|49|unknown||상세 미조회
1351836003422004|2012|Mazda5|Grand Touring|2800|197000|Kansas City, MO|2|unknown||상세 미조회
1064423996210175|2013|Dodge Grand Caravan|passenger SXT Plus|2995|255000|Kansas City, MO|15|unknown||상세 미조회
1392056106456116|2011|Buick Enclave|CXL|2800|200000|Leawood, KS|31|unknown||상세 미조회
1572530924427553|2008|Chevrolet Cobalt|LS|2800|181000|Kansas City, MO|46|unknown||상세 미조회
1325026502727632|2010|Pontiac G6|GT|2900|24000|Kansas City, MO|53|unknown||상세 미조회
1362918979352838|2016|Dodge Grand Caravan|SE|2800|254000|Kansas City, MO|65|unknown||상세 미조회
2367274047114944|2010|Ford Focus|Ses|2950|149000|Independence, MO|97|unknown||상세 미조회
931138966621274|2010|Kia Sorento|EX|2995|245000|Kansas City, MO|114|unknown||상세 미조회
2161129618065400|2012|Nissan Murano||2800|212000|Kansas City, MO|121|unknown||상세 미조회
1690481909042290|2008|Cadillac CTS|2.0 Performance Collection|2900|193000|Kansas City, MO|147|unknown||상세 미조회
1374373407856708|2013|GMC Terrain|SLE-1|2800|218000|Kansas City, MO|117|unknown||상세 미조회
961078176749587|2013|GMC Terrain|SLE-1|2950|218000|Kansas City, MO|118|unknown||상세 미조회
2933847593649863|2012|Ford Fusion|SEL|3000|218000|Roeland Park, KS|1|unknown||상세 미조회
2804353456626047|2008|Chevrolet Silverado 1500||3000|60000|Olathe, KS|1|unknown||상세 미조회
1074182408760744|2009|Jeep Patriot||3200|179000|Kansas City, MO|2|unknown||상세 미조회
1833258627680478|2010|Lincoln MKS|EcoBoost|3000|202000|Belton, MO|3|unknown||상세 미조회
1487964413162663|2013|Ford Fusion|Sport|3000|204000|Raytown, MO|8|unknown||상세 미조회
1624517559232273|2013|Chevrolet Silverado 1500|(classic) 1500|3000|150000|Kansas City, MO|8|unknown||상세 미조회
2190759801653145|2008|GMC Acadia||3300|170000|Independence, MO|10|unknown||상세 미조회
2337738293665227|2016|Hyundai Santa Fe Sport|2.0T|3000|161000|Kansas City, MO|11|unknown||상세 미조회
2084940505446539|2010|Mazda CX-5|2.5 S Preferred|3425|232000|Independence, MO|11|unknown||상세 미조회
1803154974199381|2008|Chevrolet Silverado 1500|1500|3400|280000|Overland Park, KS|11|unknown||상세 미조회
2300987720656485|2010|Ford Escape|Active|3200|19000|Kansas City, MO|12|unknown||상세 미조회
1101208435801717|2011|Chevrolet Equinox|LS|3000|132000|Spring Hill, KS|13|unknown||상세 미조회
2107414593315744|2009|Lincoln MKS||3000|180000|Kansas City, KS|14|unknown||상세 미조회
2134899417237350|2011|Chevrolet Traverse|LT|3450|206000|Kansas City, MO|16|unknown||상세 미조회
1766442181065850|2011|Ford Expedition|King Ranch|3200|220000|Overland Park, KS|16|unknown||상세 미조회
2238170953426013|2010|Pontiac G6|W/1AS|3499|159000|Raytown, MO|16|unknown||상세 미조회
2111432539746378|2014|Nissan Versa||3000|160000|Grandview, MO|16|unknown||상세 미조회
2013063402956579|2010|Chevrolet Impala||3000|144000|Kansas City, MO|17|unknown||상세 미조회
1084968484110083|2012|Subaru Outback|2.5i Premium|3400|130000|Kansas City, MO|18|unknown||상세 미조회
2356630745166620|2015|Chevrolet Equinox||3000|18000|Kansas City, KS|19|unknown||상세 미조회
1049429618064404|2008|BMW X3|m|3400|120000|Harrisonville, MO|22|unknown||상세 미조회
1552707372787760|2012|Chevrolet Cruze|LS|3000|166000|Independence, MO|24|unknown||상세 미조회
4372368973076324|2011|Ford Escape||3000|213000|Kansas City, KS|24|unknown||상세 미조회
1013839291687043|2013|GMC Terrain|SLT|3000|219000|Independence, MO|24|unknown||상세 미조회
1382509653854802|2016|Chevrolet Impala|LT|3000|235000|Kansas City, MO|25|unknown||상세 미조회
1102911768776287|2015|Chevrolet Equinox|LT|3000|272000|Kansas City, KS|26|unknown||상세 미조회
1045938174736403|2011|Chevrolet Malibu|LS|3000|145000|Shawnee, KS|26|unknown||상세 미조회
1619318563089192|2009|Toyota Camry|hybrid XLE|3000|200000|Kansas City, KS|34|unknown||상세 미조회
1595300962227327|2010|Nissan Altima|3.5 SE|3150|200000|Kansas City, MO|35|unknown||상세 미조회
1068364462309094|2010|Honda Accord|EX|3000|275000|Smithville, MO|38|unknown||상세 미조회
1396389665919817|2012|Chevrolet Cruze|LTZ|3400|187000|Olathe, KS|41|unknown||상세 미조회
37517610001219867|2009|Dodge Charger|Black|3000|151000|Kansas City, MO|41|unknown||상세 미조회
920831621062789|2012|Volkswagen Tiguan|2.0T S|3000|173000|Raytown, MO|45|unknown||상세 미조회
1026282563371731|2009|Nissan Murano|SL 3.5|3300|216000|Leavenworth, KS|47|unknown||상세 미조회
1023861270266046|2014|Ford Focus|Titanium|3400|170000|Kansas City, MO|48|unknown||상세 미조회
1656535438779974|2010|Honda Pilot||3000|190000|Olathe, KS|49|unknown||상세 미조회
2505836493258188|2010|Chevrolet Impala|LT|3200|196000|Kansas City, KS|50|unknown||상세 미조회
1680316899929607|2014|Chevrolet Cruze|LT|3200|178000|Sugar Creek, MO|51|unknown||상세 미조회
1935885163652540|2011|Chevrolet Equinox||3000|210000|Kansas City, MO|51|unknown||상세 미조회
1797174221638725|2015|Hyundai Elantra||3299|147000|Kansas City, MO|52|unknown||상세 미조회
1771764000840982|2010|Nissan Rogue||3000|205000|Raytown, MO|54|unknown||상세 미조회
1633061454910938|2008|Jeep Compass|All New Limited|3000|99000|Leavenworth, KS|58|unknown||
1037028632059162|2011|Hyundai Tucson|GLS|3000|199100|Kansas City, MO|61|unknown||엔진 경고등 기재
1069103882327589|2011|Ford Focus|SEL|3000|180000|Kansas City, MO|63|unknown||상세 미조회
1296973549177240|2011|Hyundai Sonata|Eco|3300|237000|Kansas City, MO|65|clean||
1023027133666048|2013|Chevrolet Malibu|Other|3000|279597|Olathe, KS|67|unknown||
2483787348755922|2012|Nissan Sentra||3000|199624|Kansas City, KS|67|unknown||
965480809836895|2011|GMC Terrain|SLT-1|3000|160000|Independence, MO|69|clean||
1761218644872724|2011|Ford Fusion|SE|3000|240000|Olathe, KS|72|clean||
4289291138001180|2015|Nissan Versa||3000|98000|Kansas City, MO|75|clean||변속기 이상 기재
820535047716494|2010|Mazda3|2.0|3200|227000|Kansas City, MO|80|clean||
2163357231186363|2015|Chevrolet Sonic|LS|3250|200000|Kansas City, MO|85|clean||
2239503046952500|2012|Kia Forte|EX|3250|136914|Parkville, MO|87|salvage||
1479566497274941|2012|Chevrolet Cruze|LS|3000|125000|Liberty, MO|87|clean||
1371157178205581|2016|Chevrolet Impala|LT|3000|135000|Pleasant Hill, MO|88|unknown|avoid|타이틀 없음·분실 기재
1686436955733093|2014|GMC Terrain|SLT-2|3400|174000|Osawatomie, KS|88|unknown||
1306180021722766|2008|Chevrolet Impala|LS|3000|155000|Independence, MO|106|clean||
1011879128042095|2008|BMW 5 Series|535xi|3000|180000|Shawnee, KS|119|unknown||
1656629915540146|2008|Hyundai Elantra|GLS|3300|177168|Kansas City, MO|139|clean||
1566137878175241|2010|GMC Acadia|AT4|3300|110000|Lawrence, KS|147|clean||
1431948998202957|2012|Ford Fusion|S|3200|178836|Olathe, KS|158|unknown||
3213845925454080|2008|Toyota Grand Highlander|Automático|3000|2000|Kansas City, MO|9|unknown||
1085685294052938|2009|Chevrolet Equinox|LT|3000|52820|Louisburg, KS|10|unknown|avoid|헤드개스킷 문제 기재
1753796682537846|2011|Chevrolet Traverse|LS|3000|280000|Kearney, MO|11|clean||
1557313865643673|2014|Chevrolet Silverado 1500|Z71 LTZ|3200|190000|Kansas City, MO|13|unknown|avoid|타이틀 없음·분실 기재
28566697449684012|2010|Infiniti EX35||3000|225000|Olathe, KS|17|unknown||
1432717608673649|2010|Cadillac Escalade|Platinum Edition|3200|253000|Blue Springs, MO|23|unknown||
1615243359965613|2010|Ford Escape|Active|3000|194000|Kansas City, MO|27|clean||
1833559360958020|2012|Ford F-150|XLT|3000|264000|Independence, MO|38|unknown||엔진 소음 기재
2264249567672982|2011|Chevrolet Equinox||3000|20000|Kansas City, MO|50|unknown||
1081100754247658|2011|Volvo XC90|2.5T|3000|127062|Shawnee, KS|65|unknown||AS IS 판매
1579514803522999|2008|Chevrolet Silverado 1500||3000|226000|Wellsville, KS|71|unknown||
1379459620725585|2011|Kia Forte|FE|3000|137000|Lawrence, KS|83|unknown||
1026436143268747|2011|Chevrolet Malibu||3000|200000|Kansas City, MO|86|clean||
1841110407046438|2013|Kia Sorento|Camioneta|3100|199070|Kansas City, MO|5|clean||
1088268210229704|2013|Kia Sorento|Camioneta|3100|199007|Kansas City, MO|5|clean||
1406992458203563|2008|Ford F-150|FX4|3000|241000|Independence, MO|7|unknown||
4091771584460581|2014|Toyota Camry|SE|3000|180000|Kansas City, KS|14|clean|avoid|엔진 수리 필요 기재
1048167888132181|2014|Chevrolet Impala||3000|200000|Kansas City, MO|21|clean||
1075266851963954|2008|Cadillac DTS||3000|206497|Independence, MO|29|unknown||엔진 경고등 기재 · AS IS 판매
1038048322373084|2009|GMC Yukon XL|Denali|3100|243231|Independence, MO|42|clean|avoid|엔진 수리 필요 기재
1326630669529025|2008|Honda Civic|DX|3000|234115|Kansas City, MO|59|unknown||
2952605041745846|2014|Ford Escape||3000|229362|Olathe, KS|49|unknown||누유·누수 기재
1588115979681121|2011|Ford Edge|SE|3000|208000|Grandview, MO|14|unknown||
1653126096371765|2008|Toyota Avalon|Limited|3000|306000|Independence, MO|19|clean||
1550786096394644|2014|Nissan Versa|Note S|3050|191000|Independence, MO|107|clean||
970919099035113|2008|Scion tC||3095|199996|Kansas City, KS|121|rebuilt||
1656280499501196|2012|Toyota Prius|Advanced|3200|213000|Kansas City, MO|8|unknown||
1740038790576980|2008|Ford F-150|FX4|3200|237000|Independence, MO|40|unknown||
2074370870135693|2014|Chevrolet Spark|Spark|3200|106000|Kansas City, KS|50|clean||
928628320203079|2009|Subaru Forester|2.5X Premium|3200|200000|Olathe, KS|120|unknown||
812852644909985|2008|BMW 3 Series|335i xDrive|3200|196000|Harrisonville, MO|137|salvage||
28567984486173261|2010|Toyota Corolla|S|3350|250000|Kansas City, KS|17|unknown||
1051449431028988|2010|Chevrolet Traverse|LT|3300|154536|Kansas City, MO|17|unknown||
2324418368327636|2010|Chevrolet Impala|LS|3450|198000|Overland Park, KS|26|salvage||
1400260278715841|2010|Dodge Charger|Police Pursuit|3300|88705|Olathe, KS|27|rebuilt||
1554525246351732|2008|Jeep Liberty|Sport|3450|175000|Kansas City, MO|50|unknown||
1499658145263835|2015|Dodge Journey||3300|202325|Kansas City, KS|64|clean||
1400917915219555|2012|Kia Soul||3300|178937|Kansas City, MO|65|clean||
1734502964394125|2008|Ford Focus|SE|3299|145000|Independence, MO|90|unknown||
3145892438947589|2011|Volvo XC90|3.2 Platinum|3995|163479|Raytown, MO|1|rebuilt||엔진 경고등 기재
1531009145381444|2011|Hyundai Sonata||3995|217137|Kansas City, MO|2|unknown|dealer|
1903521307699370|2017|Chevrolet Equinox|LT|3800|198000|Kansas City, MO|2|clean||
4660165450887172|2012|Acura MDX|SH-AWD|3900|225000|Kansas City, MO|2|clean||
1089414250167182|2010|Nissan Titan|SE|3500|223773|Pleasant Hill, MO|2|unknown||
1125535853379752|2013|Honda CR-V|EX|3500|164150|Kansas City, KS|2|unknown||
1046667248368934|2012|Nissan Maxima|S|3800|145000|Kansas City, KS|3|unknown||
1452149293468732|2010|Nissan Altima|2.5 S|3500|208239|Kansas City, MO|4|unknown||
1618956706352720|2013|Hyundai Accent|GL|3500|160000|Independence, MO|9|clean||
2033523490662451|2015|Chevrolet Malibu|L|3500|180000|Parkville, MO|10|unknown||설명 없음
28396497236654806|2015|Jeep Patriot||3600|162000|Olathe, KS|11|clean||
1598378685116403|2008|Honda Civic|DX|3500|213000|Raytown, MO|12|unknown||
2557444448061345|2011|Suzuki Kizashi||3500|220124|Grandview, MO|13|unknown||
1797809418018022|2013|Ford Focus|SE|3599|163000|Independence, MO|13|clean||
2481116435742729|2010|Ford Escape|SE|3500|231000|Adrian, MO|15|salvage||우박 이력
2146509829557560|2014|Toyota Yaris||3800|206000|Kansas City, MO|15|unknown||설명 없음
4460579684230133|2012|Dodge Charger|SXT|3800|217029|Kansas City, KS|15|clean||엔진 경고등 기재 · 에어컨 고장 기재
28115418421486486|2014|Nissan Rogue|SV|3500|230000|Kansas City, KS|17|unknown||
1079652534432611|2013|Chevrolet Equinox|L|3800|180000|Kansas City, MO|17|clean||
1422242730042477|2013|Cadillac XTS|Luxury|3900|205220|Kansas City, MO|18|salvage||
2836857886694537|2009|Nissan Altima|2.5 S|3500|217000|Independence, MO|18|unknown|dealer|
1772790360391566|2011|Ford Expedition||3800|200000|Kansas City, MO|23|clean||AS IS 판매
901674802688414|2011|Jeep Grand Cherokee L|Limited|3500|160000|Independence, MO|23|unknown||
1494289696060814|2009|Honda Accord|EX-L|3500|246000|Raymore, MO|28|clean||
1002993882785864|2012|Nissan Altima|2.5|3800|187230|Kansas City, MO|29|clean||
1091433840119631|2014|Dodge Journey|Sxt 2wd|3500|249000|Kansas City, KS|31|clean||과열 기재 · 우박 이력
2787256871674900|2008|Nissan Altima|3.5 SE|3500|173000|Independence, MO|37|unknown||
1512586527564022|2011|Kia Sportage|EX|3800|155000|Independence, MO|37|unknown||
2056460559077584|2013|Ford Edge|SE|3700|183000|Kansas City, MO|39|clean||
2526739581161780|2010|GMC Terrain||3770|175000|Kansas City, KS|39|unknown||
2335067910565898|2014|Chevrolet Equinox|LT|3950|242000|Gardner, KS|44|unknown||설명 없음
1393437829652288|2008|Chevrolet Malibu|LS|3500|143615|Kansas City, MO|44|clean||
1057232720144715|2013|Kia Sorento|LX|3999|126000|Grandview, MO|47|clean|dealer|엔진 경고등 기재
28018889691056725|2008|GMC Acadia|SLT-2|3800|178322|Kansas City, MO|50|clean||
1389426893281800|2012|Chevrolet Impala|LT|3800|157000|Kansas City, MO|52|unknown||
1610272694034979|2017|Dodge Grand Caravan||3500|550000|Platte City, MO|52|clean||
877698558741257|2009|BMW 3 Series|328i|3500|131326|McLouth, KS|56|clean||
1688252739121598|2008|Chrysler Sebring||3700|129509|Kansas City, KS|56|clean||
1325356133080119|2014|BMW X1|sDrive28i|3500|146000|Independence, MO|58|unknown|avoid|헤드개스킷 문제 기재
2550153745404784|2015|Chevrolet Impala|LTZ|3500|200000|Kansas City, MO|64|clean||
973950129027551|2012|GMC Terrain|SLT|3500|145339|Kansas City, MO|65|clean||
1527652352134603|2012|GMC Terrain|SLT|3500|145328|Kansas City, MO|65|clean||
1045102841544612|2012|Nissan Altima|2.5 S|3800|159000|Kansas City, MO|66|clean||
1661869644881990|2018|Nissan Sentra|SL|3500|130000|Grain Valley, MO|68|unknown||
1813061213192789|2011|Kia Sportage|LX|3900|160000|Lenexa, KS|69|rebuilt||
1072827805175632|2009|Ford F-150|XLT|3900|184000|Kansas City, MO|72|unknown||
864592379705084|2012|Buick LaCrosse|1SV|3500|168000|Raytown, MO|75|clean||엔진 경고등 기재
1347786514122065|2009|Ford Edge|Limited|3500|198785|Kansas City, MO|81|unknown||
27783779001215612|2012|Cadillac SRX|Standard|3600|362350|Kansas City, MO|82|clean||
1780239529801912|2009|Chevrolet Impala|LTZ|3500|250000|Kansas City, MO|93|clean||
1335430587940111|2012|Cadillac SRX||3500|245432|Independence, MO|97|unknown||
3208363902699222|2013|Nissan Juke|SL|3750|168000|Kansas City, MO|118|clean||
2283578809100489|2016|Land Rover Range Rover Sport|GT Limited Edition|3500|106675|Kansas City, KS|3|unknown||
2366112724126524|2013|Chevrolet Equinox|Loaded|3500|250000|Kansas City, MO|12|unknown||
2209119393339700|2011|Chevrolet Equinox|LT|3500|182000|Kansas City, MO|14|rebuilt||
1728784018391206|2013|Chevrolet Equinox||3500|252267|Kansas City, MO|16|clean||
1060095333593668|2009|Toyota Corolla|CE|3500|231252|Blue Springs, MO|18|clean||
1708310500254952|2008|Chrysler Town & Country|Limited|3700|193142|Kansas City, MO|20|unknown||
1729875511568064|2010|Mitsubishi Lancer||3500|200000|Grandview, MO|23|unknown||
1090212763745277|2013|Chevrolet Spark|2013|3500|117000|Kansas City, MO|25|unknown||
27930542416610840|2013|Volkswagen Jetta|2.0L TDI|3500|173000|Shawnee, KS|34|unknown||
2109774759930505|2010|Dodge Grand Caravan|ES|3500|160000|Kansas City, KS|34|clean||
1998966727417787|2010|GMC Yukon XL|Denali|3500|282449|Oak Grove, MO|34|rebuilt||
1060743856318422|2014|Chrysler Town & Country|Touring|3500|174571|Osawatomie, KS|34|unknown||
4734056630181546|2010|Infiniti EX35||3500|22000|Overland Park, KS|39|unknown||설명 없음
1622075005950488|2008|Saturn Astra|XR|3500|169000|Kansas City, MO|50|clean||
1349885986661753|2009|Audi A8|L W12 Quattro|3500|167000|Kansas City, MO|70|rebuilt||
1008782935373806|2014|Ford Fiesta|Se|3500|186000|Raytown, MO|71|clean||
2518708221890653|2013|GMC Equinox||3500|22500|Kansas City, KS|76|clean||
27632859466343566|2011|Kia Sorento|EX|3500|136436|Overland Park, KS|77|clean||
1986456682004192|2017|Chevrolet Equinox||3500|231158|Olathe, KS|80|unknown||
996253613028629|2008|Ford F-350|FX4|3500|255000|Raymore, MO|85|unknown||
1722660928936724|2008|Mercury Milan|Premier|3500|260000|Adrian, MO|92|unknown||엔진 경고등 기재
1674676110245153|2019|Ford F-350|King Ranch|3500|60000|Platte City, MO|98|unknown||
1516057386668480|2010|Ford F-150|Lariat Limited|3500|336000|Blue Springs, MO|104|unknown||AS IS 판매
1023948693288221|2011|Nissan Murano|SL|3600|177160|Kansas City, MO|136|clean||
1660903838953145|2012|Ford Edge|SEL|3600|199000|Belton, MO|18|clean||
1039902221708988|2008|GMC Sierra 1500|Long Bed|3500|240000|Kansas City, MO|86|unknown||
1342991953918973|2008|Hyundai Santa Fe Sport|2.0T|3500|248814|Kansas City, MO|94|clean||설명 없음
1587951949409641|2008|Toyota Camry|LE|3500|180000|Kansas City, KS|64|clean||
989134520425938|2014|Dodge Avenger|R/T|3500|99391|Smithville, MO|99|clean||
1046558744632595|2016|Kia Forte||3500|192000|Kansas City, KS|40|clean||
1080307491515467|2009|Scion xB||3800|150000|Overland Park, KS|0|unknown||
1810893356990825|2012|Nissan Versa|SL|3800|145000|Kansas City, KS|6|rebuilt||
2227452974771253|2012|Ford Focus||3800|130000|Kansas City, MO|7|unknown||
2451221762035273|2014|Dodge Grand Caravan||3999|200000|Overland Park, KS|14|unknown||설명 없음
1805769603745778|2009|Chevrolet Silverado 2500HD|Work Truck|3800|286999|Olathe, KS|26|clean||
1451110246898287|2013|Ford Focus|SE|3950|163000|Independence, MO|27|clean||
1355745783398910|2010|Honda Odyssey|EX|3999|191900|Kansas City, MO|30|clean||
1035274295809950|2012|Ford Fusion||3800|205350|Kansas City, MO|35|clean||AS IS 판매
1416241343978446|2011|Ford Expedition EL|4×4|3999|243565|Kansas City, MO|43|unknown||
2337957379944539|2014|Dodge Grand Caravan|ES|3900|210000|Overland Park, KS|46|unknown||
3122720731251572|2015|Chrysler Town & Country|Touring|3999|261000|Olathe, KS|54|clean||
820157877754252|2012|Jeep Grand Cherokee|Laredo A|3800|190000|Kansas City, MO|57|unknown||
1030444229670486|2014|Dodge Journey|Limited|3850|212000|Independence, MO|84|unknown||
28056537163949410|2013|Infiniti G37x|X awd|3800|185462|Independence, MO|85|clean||
2122085938732447|2008|Chevrolet Equinox|LT|3995|101109|Kansas City, MO|96|clean|dealer|
1845062606130034|2008|Ford Escape|Limited|3800|192000|Kansas City, KS|150|clean||
1693779302058832|2009|Chrysler Aspen|Limited|3900|256000|Kansas City, KS|173|clean|dealer|
931106396302376|2012|Honda Odyssey|Ex|3900|197665|Kansas City, MO|177|clean||
36327148363600464|2013|Nissan Rogue|Other|3800|142000|Overland Park, KS|97|salvage||
1646084266593433|2014|Hyundai Elantra|SE|3900|198312|Kansas City, MO|134|clean||
1390426023218969|2013|GMC Sierra 1500|SLE|4000|243000|Louisburg, KS|3|rebuilt||
1612695063572736|2011|Jeep Patriot||4100|153000|Olathe, KS|3|clean||
1034597079599577|2015|MINI Cooper|Cooper|4300|164000|Lee's Summit, MO|5|rebuilt||
1418121756939856|2009|Nissan Murano|SL|4000|165000|Kansas City, MO|6|clean||
1401192621366018|2014|Nissan Altima|2.5 S|4000|179000|Fairway, KS|7|clean||
4700574893562338|2012|Dodge Charger|SE|4100|22000|Kansas City, MO|8|clean||
1741534313800523|2012|Ford F-150||4000|250000|Lee's Summit, MO|13|unknown|avoid|타이틀 없음·분실 기재
1341592185696941|2012|Kia Soul|!|4350|174000|Kansas City, MO|13|clean||
1054635680722807|2010|Honda Pilot||4000|226000|Kansas City, KS|15|clean||AS IS 판매
1098843499157825|2009|Honda Civic|EX|4100|210000|Blue Springs, MO|16|clean||우박 이력
4215602388730752|2011|Chevrolet Equinox|LS|4350|177783|Kansas City, MO|16|unknown||
28484427017840321|2008|Dodge Ram 3500||4000|470000|Kansas City, MO|17|unknown|avoid|변속기 수리 필요 기재
1377612303976065|2008|MINI Cooper||4300|87322|Lansing, KS|18|unknown||우박 이력
1577444660742516|2008|Toyota RAV4|LE|4200|218326|Kansas City, MO|19|clean||
1374035258053307|2014|Buick LaCrosse||4000|215146|Kansas City, MO|19|clean||
1085866450576758|2008|Chevrolet HHR||4000|175000|Independence, MO|19|unknown||
900435082861197|2009|Ford Escape||4300|199220|Kansas City, MO|19|unknown||
1795207381654151|2010|Chevrolet Silverado 2500HD|Short Bed|4000|123456|Independence, MO|23|unknown|avoid|변속기 수리 필요 기재
1051467544151980|2013|Ford Focus|SE|4000|98000|Kansas City, KS|23|unknown||
954296041032804|2011|Land Rover LR4|HSE LUX|4250|199000|Pleasant Hill, MO|23|unknown||
1747719979872705|2011|Kia Sedona|EX|4000|208000|Raytown, MO|23|clean||
1752282739317728|2010|Jeep Liberty|Sport|4000|180000|Kansas City, KS|25|clean||AS IS 판매
1102304202122587|2010|Chevrolet Cobalt|Sport|4000|138550|Independence, MO|26|clean||
1047777751394847|2011|Ford F-150|XLT|4000|233000|Kansas City, MO|28|clean||
1373737077585760|2011|Chevrolet Equinox|LT|4000|172944|Kansas City, MO|33|clean||엔진 경고등 기재
1089914400231037|2010|Honda Insight|LX|4000|243675|Lee's Summit, MO|37|clean||
1084380247377980|2011|Mitsubishi Lancer|ES|4000|176000|Kansas City, KS|38|unknown||
1037643282201335|2012|Chevrolet Cruze|eco|4200|119500|Bonner Springs, KS|39|unknown||
1611002620361129|2012|Kia Sorento|L|4000|17500|Overland Park, KS|40|clean||
1038596459084973|2013|Ford Explorer||4250|214000|Buckner, MO|40|clean||
2179399995955359|2009|Ford F-150|Lariat Limited|4100|167000|Kansas City, KS|45|salvage||AS IS 판매
1349844050609284|2013|Nissan LEAF|SL|4000|91147|Kansas City, MO|52|clean||
1032377696072401|2012|GMC Acadia|SLE|4100|157000|Leawood, KS|53|unknown||
3300363180352206|2010|GMC Terrain|SLE|4200|219560|Kansas City, MO|59|clean||
1016947297843552|2011|Jeep Grand Cherokee|Overland|4000|182700|De Soto, KS|59|clean||
1519258132836523|2013|Infiniti QX60||4000|216102|Overland Park, KS|62|clean||
1941822933445861|2011|Acura TL|SH-AWD|4250|190000|Kansas City, KS|62|salvage||
1419927846658641|2009|Jeep Patriot||4000|180000|Kansas City, MO|65|clean||
1022617390563011|2010|Chevrolet Traverse|LT|4000|221410|Kansas City, MO|69|unknown||
2251707075599888|2011|Chevrolet Malibu|1LT|4200|141000|Kansas City, MO|72|unknown||
1062705076187272|2013|Nissan Sentra|1.8 S|4000|151395|Kansas City, KS|72|clean||
28214162951500778|2012|Toyota Prius|Advanced|4000|226000|Kansas City, MO|72|unknown||
1540061204519212|2015|Subaru Forester|2.0XT Premium|4000|276000|Bonner Springs, KS|78|clean||
1336918815086316|2011|Volkswagen Jetta|2.5L SE|4000|148000|Kansas City, MO|80|clean||
1017805900737812|2013|Dodge Journey||4000|173244|Kansas City, KS|86|clean||
1480891873360632|2010|Saturn VUE||4000|170000|Olathe, KS|90|unknown||
1326181739035702|2008|Ford Taurus||4300|85000|Shawnee, KS|90|clean||
1523338542504180|2008|BMW 3 Series|335i|4000|148591|Kansas City, MO|99|salvage||
1903554463675625|2013|Chevrolet Equinox||4300|184373|Shawnee, KS|99|unknown||
2116078352296165|2013|Nissan Juke|S|4000|152000|Roeland Park, KS|101|clean||
2208764209898636|2014|GMC Terrain|SLT-2|4000|200771|Bonner Springs, KS|106|clean||
1683454966299117|2008|Ford Edge|Limited|4000|197110|Independence, MO|114|clean||
2967680560237814|2011|Jeep Grand Cherokee|Laredo|4000|181148|Liberty, MO|135|unknown|avoid|수리용 차량 · 엔진 소음 기재
928417773531856|2010|Chevrolet Traverse|LTZ|4400|231351|Independence, MO|148|clean||
722429484230715|2010|Chevrolet Equinox|LT|4000|172592|Kansas City, MO|163|unknown||
1036202325982308|2012|Mitsubishi Lancer|GT|4000|212431|Sugar Creek, MO|29|clean||
1035528916132719|2008|Ford F-150|XL|4000|183006|Olathe, KS|47|unknown||
1769425004098109|2011|Jeep Patriot|Latitude|4100|180000|Shawnee, KS|47|salvage||
1751354935857925|2011|Dodge Nitro|Heat|4000|87683|Olathe, KS|64|unknown||
2213169209446130|2011|Kia Soul||4000|142000|Gardner, KS|116|clean||
2117684502513679|2010|Nissan Armada|Platinum Reserve|4000|265000|Overland Park, KS|120|unknown||
27727208143540296|2014|Subaru Outback|2.5i|4000|196000|Grandview, MO|65|unknown||
1537016834027201|2012|Dodge Ram 1500|HEMI|4300|271000|Kansas City, KS|58|unknown||
2189091778607692|2008|Dodge Durango|SLT|4321|148000|Buckner, MO|62|rebuilt||
1548007073389776|2014|Volkswagen Jetta|2.0L S|4400|167650|Kansas City, MO|65|unknown||설명 없음
1487994069303534|2015|Nissan Rogue||4490|230707|Independence, MO|90|clean|dealer|
878091908673155|2012|GMC Savana||4250|334242|Olathe, KS|91|unknown||
1757840485512807|2014|Buick Enclave|Leather|4500|135537|Kansas City, MO|1|clean||
2122645638646103|2010|Ford Crown Victoria||4600|17200|Harrisonville, MO|4|rebuilt||
1055294620604713|2014|Chevrolet Sonic|LT|4800|150100|Kansas City, MO|6|clean||누유·누수 기재 · 우박 이력
1129337672760716|2012|Hyundai IONIQ|Limited|4500|196127|Kansas City, MO|7|unknown||
1082399354527953|2014|Chevrolet Cruze|LS|4500|108000|Independence, MO|8|clean|dealer|
1435372611818327|2016|Dodge Grand Caravan|SE|4500|138000|Overland Park, KS|11|clean||
1400224098415882|2010|Jeep Grand Cherokee|Laredo|4600|223300|Edwardsville, KS|11|clean||
1706998470386453|2012|Buick Enclave|Leather|4500|145000|Liberty, MO|12|clean||
1377341381145684|2016|Chevrolet Cruze|LT|4950|232000|Kansas City, MO|16|clean||
1413564337528927|2008|Nissan Altima|2.5 SL|4500|193000|Kansas City, MO|18|clean||
1159614873393722|2016|Ford Fusion|Titanium|4950|183000|Independence, MO|19|clean||
1501361968377524|2012|Scion tC|Release Series 7.0|4950|253000|Kansas City, MO|20|clean||
1129385073370029|2013|Ford F-150|XL|4500|271255|Kansas City, MO|21|unknown||
1063731986060778|2015|Nissan Altima|2.5 Platinum|4500|175000|Kansas City, MO|22|clean||
2260859168035617|2014|Nissan Murano|CrossCabriolet|4500|85680|Shawnee, KS|37|clean||
2272119596936510|2012|Hyundai Accent|GS|4500|145173|Kansas City, KS|39|clean||
931039210034701|2013|Kia Soul||4500|130000|Kansas City, MO|40|unknown||
2107731416484129|2013|Nissan Pathfinder|LE|4500|121000|Kansas City, MO|41|salvage||
1352506810372796|2012|Volkswagen Passat|2.5L SE|4999|169000|Grandview, MO|47|clean|dealer|
1852295665747875|2009|GMC Acadia|SLT-1|4500|123000|Kansas City, KS|61|clean||
1375396250664256|2014|Nissan Juke|S|4500|154000|Smithville, MO|63|unknown||
2096423877899309|2011|Chevrolet Equinox||4500|162187|Kansas City, MO|100|clean||
1503228214806876|2008|Toyota Corolla||4500|214000|Kansas City, MO|131|clean||엔진 경고등 기재
929275566658609|2008|Chevrolet Silverado 1500|Z71 LT|4500|145000|Leavenworth, KS|150|unknown||
1389326689888555|2009|Chevrolet Traverse|LS|4500|198000|Grain Valley, MO|162|unknown||
1943127556297496|2012|Mazda CX-7|i Touring|4750|176000|Kansas City, MO|172|clean||우박 이력
1773567590803478|2008|GMC Acadia||4500|131000|Independence, MO|13|clean||
941877694988427|2014|Ford Mustang|V6|4500|153000|Independence, MO|20|unknown||엔진 경고등 기재
1452821260017895|2013|Dodge Grand Caravan||4500|172000|Kansas City, KS|25|clean||
1995271384458961|2008|Toyota Highlander||4500|224380|Liberty, MO|27|clean||엔진 경고등 기재
1084665380767340|2013|Kia Soul|!|4500|130300|Kansas City, MO|29|unknown||
2104917570063402|2008|Toyota Matrix|L Sport|4500|175000|Kansas City, MO|49|unknown||
2229403644564626|2008|Pontiac G6||4500|172310|Kansas City, MO|61|clean||AS IS 판매
1717573812901012|2010|Chevrolet Camaro||4500|157000|Kansas City, MO|65|unknown||엔진 소음 기재 · AS IS 판매
3283958138462607|2011|GMC Acadia||4500|160948|Kansas City, KS|75|clean||
2520542885061349|2010|Chevrolet Traverse|LT|4500|221410|Kansas City, MO|79|clean||
2110492936209348|2009|Mazda5|Touring|4500|145000|Kansas City, MO|78|clean||
1166728869864285|2010|Ford Escape|Active|4650|215849|Kansas City, KS|89|unknown||
1048925017752431|2017|Chevrolet Camaro|RS|4500|175000|Overland Park, KS|26|unknown||
1108914351827492|2008|GMC Yukon XL|SLT|4550|228000|Independence, MO|28|clean||
2275125183296753|2013|Ford Focus||4500|122000|Kansas City, KS|71|unknown||
1005000525844329|2014|Volkswagen Passat|1.8T Wolfsburg Edition|4700|174000|Kansas City, MO|92|clean||
1744883540124611|2012|Chevrolet Yukon||4999|203000|Kansas City, MO|6|unknown||
1542888067776818|2008|MINI Clubman|Cooper S|4999|142669|Lee's Summit, MO|9|clean|dealer|
1611143870655296|2015|Buick Enclave|Premium|4995|196000|Independence, MO|13|clean||
1072519831941144|2015|Lincoln MKC||4900|183000|Grandview, MO|23|clean||
2263771734425527|2010|Dodge Ram 1500|ST|4950|244771|Grandview, MO|55|unknown||
1042769178303345|2010|Volvo S80|3.2|4999|156553|Lee's Summit, MO|57|clean|dealer|
1073697801749535|2011|Volkswagen GTI|2.0T|4800|121528|Kansas City, MO|57|clean||
1717687366154619|2012|Chevrolet Equinox||4950|183972|Kansas City, MO|58|clean||
884570500875698|2015|Nissan Rogue||4995|230707|Independence, MO|75|clean|dealer|
1580755783470622|2019|Nissan Sentra|LE|4900|170000|Shawnee, KS|93|clean||
4305635276317056|2013|Dodge Dart|· SXT|4900|109600|Kansas City, MO|97|unknown||
1246383454047127|2012|Chevrolet Cruze|LS|4950|121000|Pleasant Hill, MO|113|clean||
1653966962508154|2008|Toyota RAV4||4800|256015|Kansas City, KS|134|unknown||
2235193040563838|2014|Ford Focus||4950|137000|Belton, MO|90|clean|dealer|우박 이력
1867724167527053|2018|Dodge Ram 1500|Laramie|5000|191000|Overland Park, KS|2|unknown||
1586726939364252|2015|Dodge Ram 1500||5000|346934|Spring Hill, KS|6|clean||
1354321786475527|2009|Ford Explorer|Eddie Bauer|5000|162000|Independence, MO|6|clean|dealer|
4620991428187507|2012|Dodge Ram 1500|SLT|5000|170000|Independence, MO|7|unknown||
1619911896454994|2012|Jeep Liberty|Limited Edition|5300|174800|Kansas City, KS|7|clean||
3939636749665219|2013|Chevrolet Silverado 1500|Short Bed|5000|123456|Olathe, KS|7|clean|avoid|엔진 수리 필요 기재
1554521716356553|2018|Dodge Grand Caravan|SE|5000|181250|Kansas City, MO|8|clean||
1767819321165621|2016|Dodge Ram 1500|SLT|5000|208000|Kansas City, MO|10|unknown||
1069803612468627|2014|Dodge Durango|R/T|5000|245000|Kansas City, MO|11|unknown||
1140932152011274|2009|Honda Pilot|TOURING|5200|210000|Basehor, KS|13|clean||
931049713401106|2017|Hyundai Accent|Other|5495|121740|Kansas City, KS|14|clean||
911492701680453|2014|Cadillac ATS|2.0L Turbo Premium|5000|146963|Kansas City, MO|16|rebuilt||엔진 경고등 기재
27806826385687131|2012|Chevrolet Silverado 2500HD||5000|174000|Belton, MO|16|unknown||
1404158924991873|2013|Chevrolet Malibu|1LT|5400|116000|Lee's Summit, MO|18|unknown||
28555473370759284|2008|Chevrolet Suburban|LS|5000|246746|Harrisonville, MO|22|clean||
2203422346866497|2012|Hyundai Sonata|Limited|5000|226923|Kansas City, MO|22|unknown||
941360804943943|2016|Dodge Grand Caravan|R/T|5000|160000|Kansas City, MO|31|clean||
1053959907431545|2012|GMC Acadia|Denali|5000|190000|Kansas City, KS|34|unknown||
1537711698104425|2012|BMW X5|xDrive35i Premium|5000|227750|Independence, MO|37|clean||
1474204357797551|2012|Cadillac CTS|3.0 Luxury Collection|5000|186837|Independence, MO|50|clean||
1015792221218084|2009|Ford Crown Victoria||5000|180000|Overland Park, KS|53|unknown||
1542483083985002|2014|Audi A4|2.0T Quattro Premium|5000|190000|Bonner Springs, KS|64|clean|avoid|엔진 수리 필요 기재
4473404292977079|2010|Nissan Armada|SE|5000|236512|Drexel, MO|66|rebuilt||
1711386513336203|2010|Chevrolet Silverado 1500|Long Bed|5000|190000|Kansas City, MO|70|clean||
2568705920254365|2011|Acura MDX|Technology+and+entertainment+package+4wd|5000|188000|Kansas City, MO|70|unknown||
2502812603546902|2011|Dodge Ram 1500|SLT|5000|209000|Kansas City, MO|71|clean||
877105244916078|2013|Chevrolet Spark||5000|178000|Grandview, MO|89|unknown||
28111116271822413|2010|Volkswagen Touareg|TDI|5000|165000|Bonner Springs, KS|93|clean||
1360885212569819|2010|Ford Taurus|SHO|5000|184959|Kansas City, MO|100|unknown||AS IS 판매
1052083561149303|2010|Ford F-150|FX2|5000|1490|Kansas City, KS|38|unknown||
1039103328839738|2008|Chevrolet Tahoe|LT|5000|180000|Kansas City, MO|64|unknown||
1343630710637377|2014|Infiniti QX60|SENSORY|5000|177693|Kansas City, MO|71|clean||
1063039749388959|2016|Chevrolet Camaro||5000|170000|Overland Park, KS|110|unknown||
1573015077861953|2011|Acura MDX|SH-AWD w/Technology & A-Spec Pkgs|5000|180000|Kansas City, KS|70|unknown||
1110649711826240|2010|Honda CR-V||5000|259000|Kansas City, MO|87|clean||
1393992499259151|2017|Ford Focus|SE|5100|112000|Kansas City, MO|98|clean||
2095767221019847|2016|Nissan Versa Note|SV|5300|118000|Kansas City, MO|41|clean||
1751040379402956|2013|Ford Explorer||5300|229111|Kansas City, KS|88|unknown||
1314929234078049|2011|Toyota Prius||5300|154000|Lenexa, KS|106|rebuilt||
1105585958791561|2016|Chevrolet Traverse|LT|5800|154000|Kansas City, MO|3|clean|dealer|같은 차 2건 게시
1582707713333258|2008|Mercedes-Benz GL-Class|GL 450 4MATIC|5500|122701|Kansas City, KS|4|clean|dealer|
1837237627293070|2012|Land Rover LR4|HSE|5950|146000|Kansas City, MO|4|clean||
1111547845164357|2013|Honda Odyssey|EX-L|5900|230000|Kansas City, MO|7|clean||
1386191757011111|2012|GMC Acadia|SLE|5700|172000|Kansas City, MO|9|clean||
2356781518397734|2016|Chevrolet Traverse|LT|5900|173077|Lee's Summit, MO|16|clean||
1300174338709121|2014|Ford Focus||5950|130000|Belton, MO|26|unknown|dealer|
2529850130868882|2015|Chevrolet Cruze||5950|132000|Belton, MO|26|clean|dealer|우박 이력
1727403451894823|2014|Kia Sorento|LX|5800|163000|Grandview, MO|27|clean||
868604706190670|2013|Lincoln MKX||5550|111423|Lenexa, KS|28|salvage||
2492174264638576|2012|Chevrolet Traverse|LT|5500|175000|Olathe, KS|29|unknown||
2110906046522652|2014|Jeep Grand Cherokee|Limited|5500|194000|Olathe, KS|30|clean||엔진 경고등 기재
1331302125747768|2012|MINI Cooper|Cooper S|5500|148448|Kansas City, MO|30|clean||
2287214372116685|2013|Buick Enclave||5800|222460|Raymore, MO|32|rebuilt||
4577057489243152|2009|Ford Explorer|Clothes|5500|161620|Pleasant Hill, MO|37|clean||
945148578057369|2014|Buick Enclave|Leather|5950|156840|Greenwood, MO|40|salvage||
2298566420548465|2008|GMC Sierra 1500|SLE|5900|250000|Olathe, KS|41|unknown||설명 없음
1798635224472095|2012|Chevrolet Equinox||5995|161900|Kansas City, MO|44|unknown||
1311743414108941|2010|Honda Civic|LX|5500|95600|Grandview, MO|46|unknown||
1025126696818809|2008|Ford Mustang||5500|166000|Liberty, MO|46|clean||
2847558828963254|2013|Mercedes-Benz GL-Class|GL 450 4MATIC|5500|155000|Raytown, MO|46|unknown||
1650920986549890|2019|Dodge Grand Caravan||5500|20014|Independence, MO|47|unknown||
1489747676254775|2015|Dodge Journey|Limited|5750|132000|Pleasant Hill, MO|61|clean||
872359952614439|2016|GMC Acadia|SLT|5500|150000|Kansas City, MO|62|clean||
1795759538078023|2014|Mitsubishi Outlander Sport|SEL|5950|125000|Kansas City, MO|63|unknown||
1044480228540900|2011|Dodge Charger|SE|5500|235266|Baldwin City, KS|66|unknown||
1056469487070437|2010|Honda Odyssey||5500|203000|Olathe, KS|73|unknown||설명 없음
2138384126718964|2014|Dodge Journey|SXT|5555|149048|Kansas City, MO|75|unknown||
1170670218597940|2010|Ford Fusion||5500|225275|Independence, MO|75|clean|dealer|
4207981369492473|2013|Chevrolet Traverse||5500|149042|Kansas City, MO|78|unknown||설명 없음
1016019194162961|2014|Toyota Corolla||5900|190000|De Soto, KS|87|unknown||
2027967264527370|2013|Hyundai Santa Fe|Limited|5900|160000|Kansas City, KS|89|clean||
2088193262079157|2016|Nissan Rogue|SV|5900|191000|Kansas City, KS|104|clean|dealer|
970368622403286|2014|Kia Sorento|S|5950|100000|Pleasant Hill, MO|123|clean||
2167567024000785|2008|Infiniti G35x||5900|208709|Kansas City, KS|128|clean||
1489298979243581|2015|Kia Sorento||5500|170000|Belton, MO|131|clean|dealer|
1349670740349670|2016|Subaru Impreza||5900|190058|Kansas City, KS|160|clean||
1463605938713299|2014|Chevrolet Impala|LT|5500|130000|Kansas City, KS|177|clean||
28333121949683693|2013|Subaru Impreza|2.5i Premium|5650|186520|Kansas City, MO|4|clean||
1617671553034585|2014|Dodge Grand Caravan|Sxt|5500|160000|Lee's Summit, MO|8|unknown||
1738849134046354|2011|Volkswagen GTI|2.0T|5500|121656|Kansas City, MO|11|clean||
1722722648940464|2008|GMC Yukon||5500|201000|Kansas City, MO|40|clean||누유·누수 기재
1034775915964001|2014|Nissan Murano|CrossCabriolet|5700|85215|Kansas City, MO|47|clean||
927624546304762|2010|Jeep Patriot||5700|109835|Kansas City, MO|55|clean||
2096018867938967|2020|Chevrolet Spark||5500|155800|Kansas City, MO|56|clean||
2239578476794706|2008|GMC Yukon|SLE|5500|233000|Kansas City, MO|66|unknown||
1384491510173773|2011|Ford Crown Victoria|LX|5500|166000|Kansas City, MO|105|unknown||엔진 경고등 기재
1596971638054640|2015|Jeep Compass||5500|144000|Belton, MO|130|clean|dealer|
1704584684097545|2014|Chevrolet Silverado 1500||5500|215353|Raymore, MO|30|unknown||
1429236745820990|2009|Dodge Grand Caravan|Extended|5500|20014|Independence, MO|47|clean||
1917239018950769|2017|Buick Encore|Encore|5500|101000|Independence, MO|67|clean||
1606866990372005|2014|Nissan Altima||5500|171000|Belton, MO|130|clean|dealer|
1330891668841439|2015|Ford Escape|Titanium|5600|116000|Independence, MO|97|salvage||
1580058116813987|2012|Toyota Camry|XLE|5700|236159|Kansas City, MO|67|unknown||
3381483395363865|2013|Ford Escape|SEL|5699|151000|Kansas City, MO|74|clean||
1074855261944526|2009|Subaru Forester|Other|5997|173288|Kansas City, KS|1|unknown|dealer|
28569542295991418|2013|Dodge Durango|SXT|5900|203000|Kansas City, KS|6|clean|dealer|
1631387251662687|2018|Jeep Grand Cherokee||5985|195300|Kansas City, MO|7|clean|dealer|
1880709209965488|2013|Nissan Rogue|S|5800|134000|Lee's Summit, MO|8|clean||
1588231299456176|2015|Honda Pilot|EX-L|5950|191000|Independence, MO|22|unknown||
1447160574137995|2013|Toyota Prius||5800|193112|Kansas City, MO|24|clean||
1051468364191990|2014|Nissan Sentra|SR|5999|99010|Kansas City, MO|28|clean||
1299564342130860|2008|GMC Sierra 1500||5995|165000|Independence, MO|35|rebuilt||우박 이력
1967671690566171|2008|Toyota Highlander|LE|5900|241113|Kansas City, MO|43|clean||
2270833907075237|2013|Mazda5|Touring|5995|135205|Kansas City, MO|54|clean||
1699740251252932|2016|Ford Escape|SE|5750|125000|Pleasant Hill, MO|61|clean||
894961720321642|2010|Kia Soul||5950|110542|Belton, MO|65|unknown|dealer|
1936426020351989|2014|Dodge Grand Caravan||5995|184473|Liberty, MO|79|clean|dealer|
4415677592035000|2009|Chevrolet Malibu|LT|5950|168962|Pleasant Valley, MO|93|unknown||
1817346885905537|2014|Chevrolet Silverado 1500|Short Bed|5999|207937|Overland Park, KS|102|unknown||
1190026649915987|2009|GMC Sierra 1500|SLE|5800|178000|Independence, MO|104|unknown||
1431388458304697|2016|Nissan Altima|2.5 S|5995|208128|Lee's Summit, MO|158|unknown||
2944251949272921|2016|Ford Explorer||5800|173000|Kansas City, KS|73|clean||
2027813997888621|2016|Ford Taurus|SE|5895|130791|Kansas City, MO|7|clean|dealer|
1127497916278758|2012|Chevrolet Tahoe|LT XFE|6000|212000|Leavenworth, KS|1|unknown||설명 없음
1069748092506372|2012|Dodge Ram 1500|SLT|6250|227475|Lone Jack, MO|3|clean||
2845450199164007|2017|Kia Sportage|109000|6475|109000|Kansas City, MO|5|clean||
4604643283153100|2011|Lincoln MKX||6000|176000|Kansas City, MO|6|clean||
1102563158776426|2008|Scion tC||6046|184000|Kansas City, MO|6|clean|dealer|
1580738023519205|2017|Jeep Renegade||6000|153539|Kansas City, KS|6|unknown||
1776134316969349|2008|Ford Expedition EL||6300|140230|Kansas City, MO|7|unknown||
1063783969750771|2013|Chevrolet Silverado 1500||6000|191000|Olathe, KS|7|clean||
1101048222365211|2013|Volkswagen GTI|Wolfsburg Edition|6000|156675|Olathe, KS|9|rebuilt||
909055878640256|2011|Subaru Outback||6487|182431|Kansas City, MO|11|unknown|dealer|
1820284445810158|2011|Ford F-150|FX4|6200|149000|Kansas City, MO|11|clean||
2315032122596247|2012|Chrysler Town & Country|Touring-L|6000|66121|Kansas City, MO|14|clean||
2598155990632558|2010|BMW i5|M60|6000|143000|Kansas City, MO|14|clean||
1430975708894085|2015|Ford Expedition EL|XL|6000|202000|Kansas City, KS|14|rebuilt||우박 이력
3329343117248814|2011|BMW 3 Series|330xi AWD|6000|102000|Kansas City, MO|16|clean||
1391585562397631|2015|Jeep Grand Cherokee||6200|196000|Olathe, KS|16|clean||
1118798570717989|2015|Kia Soul|4 door|6000|163000|Independence, MO|19|clean||설명 없음
1743375173472840|2010|Ford F-150|Platinum|6450|236555|Leavenworth, KS|26|clean||
1793807878422296|2015|Buick Enclave||6100|148000|Kansas City, KS|28|unknown||
1531425841629902|2009|Ford F-150|XL STX|6000|179000|Kansas City, MO|31|clean||
1786353599223264|2011|Chevrolet Tahoe|LT|6000|247700|Kansas City, KS|34|unknown||
1594231655446225|2009|Audi A5|2.0T Premium|6000|171100|Kansas City, MO|38|unknown||
2584974151975196|2011|Dodge Charger|SE|6000|127000|Raytown, MO|40|unknown||
1614900906877214|2014|Chrysler 300|300 Touring|6000|124819|Kansas City, MO|43|rebuilt||
2642970422825039|2013|Ford F-150|FX4|6000|220000|Pleasant Valley, MO|51|clean||
4548345002158336|2014|Chevrolet Captiva Sport|LT|6400|114334|Oak Grove, MO|53|clean||
885580987566607|2009|Audi A3|2.0T Premium|6000|100000|Pleasant Hill, MO|54|unknown||
923229676811843|2013|Lincoln MKT||6200|128000|Kansas City, MO|55|clean||누유·누수 기재
1404876968180378|2010|Ford F-150|Platinum|6400|240000|Independence, MO|60|clean||변속기 이상 기재
1547409773325634|2012|Toyota Corolla|LE|6300|195000|Grandview, MO|71|clean||
1353410413595234|2015|Honda Civic|Si|6200|190000|Raymore, MO|72|unknown||
2046371259605359|2013|Chevrolet Silverado 1500|LT|6000|222000|Independence, MO|78|clean||
1326998902940998|2015|Buick Enclave||6225|323030|Independence, MO|83|unknown|dealer|
4514698068761814|2011|Nissan Rogue|SV|6200|108574|Liberty, MO|85|clean||
2122347541681719|2011|Dodge Ram 1500|SLT|6200|222963|Kansas City, KS|85|clean||
1337123714535105|2010|Chevrolet Tahoe|Hybrid|6300|150000|Kansas City, KS|85|clean||
1051969603933137|2010|Mazda3|MAZDASPEED3 Touring|6300|166000|Belton, MO|86|clean||
840885812112041|2015|Nissan Frontier||6199|202450|Kansas City, MO|101|unknown||
1682872449702709|2012|Nissan Altima|2.5|6000|171000|Kansas City, MO|116|rebuilt||
1371002828116775|2018|Ford Focus|ST|6400|130000|Fairway, KS|153|unknown||
1567190858449501|2013|Ford Focus|SE FLEX FUEL|6000|127000|Independence, MO|61|clean||설명 없음
976380618315300|2013|BMW 3 Series|328i xDrive|6000|187000|Kansas City, KS|122|unknown||
1299999231543194|2015|Nissan Pathfinder|SV|6000|148995|Lee's Summit, MO|134|clean||
1369144955075386|2017|Chevrolet Traverse|LT|6100|142500|Peculiar, MO|84|clean||
1500190428810020|2014|Ford Escape|SEL|6000|220000|Kansas City, MO|106|clean||
918161697273977|2017|Ford Escape|SE|6350|110000|Pleasant Hill, MO|59|clean||다운페이·할부 광고
1182635677325334|2012|Ford F-150|XL|6300|240000|Kansas City, KS|102|unknown||
929475849861743|2008|Ford F-150|FX4|6300|141000|Kansas City, KS|163|unknown||
3652922401526783|2014|Nissan Juke|RS NISMO(All Wheel Drive)|6500|111250|Raytown, MO|0|clean||
885146901211475|2011|Ford F-250|HD Long Bed|6750|218000|Blue Springs, MO|1|clean||
939674402083100|2012|Ford Focus||6946|76840|Kansas City, MO|2|unknown||
1782903329512368|2018|Nissan Murano|SV|6999|138000|Kansas City, MO|3|clean||
1065397022974377|2014|Chrysler Town & Country|Touring|6500|159241|Kansas City, MO|5|unknown||
1781488836524578|2012|GMC Yukon|ready to leave|6700|147000|Kansas City, MO|5|clean||
1106356238432791|2014|Jeep Grand Cherokee|Laredo|6950|190000|Independence, MO|6|clean||
2268558627052065|2009|Lexus RX|RX 350 F SPORT Handling|6799|195489|Independence, MO|6|clean||
1306102664832745|2012|Jeep Cherokee|Limited|6500|170000|Kansas City, MO|7|clean||
1581937086739747|2009|Infiniti G37x||6500|181000|Raymore, MO|8|clean||
2115218495744505|2012|BMW 7 Series|750Li|6950|105426|Kansas City, MO|13|clean||
1100566285769618|2008|Ford F-250|XLT|6500|298000|Bates City, MO|14|clean||
1784076062830434|2016|Chrysler Town & Country|Touring|6999|141000|Sugar Creek, MO|16|unknown||
1089730856875204|2013|Kia Optima||6900|145377|Grandview, MO|23|clean||
1062693373143705|2011|Ford Explorer|Limited|6500|182000|Kansas City, MO|25|clean||
2281730325976694|2010|Ford F-150|Platinum|6850|236555|Leavenworth, KS|26|clean||
1063932279698253|2011|Honda Odyssey|EX-L w/Navigation|6800|180000|Kansas City, MO|27|clean||
1072884935098154|2016|Ford F-150||6900|174475|Lenexa, KS|28|clean||누유·누수 기재 · AS IS 판매
1409456897815174|2014|Ford Escape||6950|149000|Belton, MO|28|clean|dealer|
1937404950257869|2017|Subaru Forester|2.5i Premium|6500|251262|Kansas City, MO|41|unknown||
1336096115275356|2013|Mitsubishi Sport||6500|127000|Kansas City, KS|42|unknown||
2560110884414371|2014|Toyota RAV4||6900|83111|Kansas City, MO|43|clean||
1059723533319371|2010|Chevrolet Silverado 1500|Z71 LT|6500|184321|Kansas City, MO|50|unknown||같은 차 2건 게시
2273357743440382|2014|Ford Flex|SEL|6500|170449|Kansas City, MO|55|clean||
1063550436107837|2008|Dodge Ram 2500|Laramie|6500|254000|Kansas City, MO|58|unknown||
1386396210130394|2012|Honda Odyssey|EX|6750|190600|Independence, MO|64|unknown||설명 없음
1008365512115471|2014|GMC Acadia|SLE-2|6950|184900|Pleasant Valley, MO|65|unknown|dealer|
917540338045967|2015|Ford Edge||6999|153123|Kansas City, MO|68|unknown||설명 없음
1690561778914863|2015|Chrysler Town & Country||6950|152000|Belton, MO|74|clean|dealer|
984400530907137|2019|Kia Soul||6950|98000|Belton, MO|130|clean|dealer|
1451209936936966|2011|BMW 3 Series|330xi AWD|6500|102000|Kansas City, MO|2|clean||
1609800830548374|2014|Ford Focus||6500|146628|Belton, MO|14|clean|dealer|
1042306115231163|2011|GMC Yukon||6500|250879|Kansas City, MO|55|clean||
37325558877092114|2014|Kia Sorento|EX|6650|120000|Pleasant Hill, MO|59|clean|dealer|
1700898354479956|2013|Ford Explorer|Limited|6500|195000|Cleveland, MO|60|unknown||
2092328058030204|2011|Chevrolet Silverado 1500|Long Bed|6500|112900|Grain Valley, MO|62|clean||엔진 경고등 기재
1929137401117623|2008|Dodge Ram 1500|SLT|6600|183000|Edwardsville, KS|63|clean||
1052204604036765|2011|Dodge Challenger|SE|6500|150000|Kansas City, MO|102|rebuilt||
1680970603109286|2017|Hyundai Elantra|Limited|6500|152000|Leavenworth, KS|134|clean||
963847766667265|2013|Honda CR-V||6599|25000|Kansas City, MO|47|unknown||설명 없음
1038071402057657|2016|Kia Sedona|LX|6500|155535|Kansas City, MO|68|unknown||
1753706535612010|2014|GMC Acadia|SL|6500|1780|Kansas City, KS|114|unknown||
2245612272960732|2020|Mitsubishi Mirage||6995|71670|Kansas City, MO|5|unknown|dealer|
2380523816090750|2008|Honda Fit|Sport|6900|166000|Kansas City, MO|11|unknown|dealer|
1462216259299887|2012|Chrysler Town & Country|Touring-L|6900|66321|Kansas City, MO|14|clean||
1076662088181915|2013|GMC Terrain||6999|145763|Belton, MO|15|clean|dealer|
1053740320983404|2016|Nissan Altima|2.5 S|6850|132000|Independence, MO|19|clean||
1636849311119475|2013|Chrysler Town & Country|Touring|6950|169000|Kansas City, MO|20|clean||
1044591151680128|2014|Buick Encore||6950|145000|Belton, MO|36|clean|dealer|
1052311054162538|2010|Dodge Ram 1500|Laramie|6900|238000|Kansas City, MO|53|clean||
2119864308948997|2012|Ford F-150|XLT|6950|2666|Pleasant Hill, MO|63|clean||
27424168183909141|2010|Nissan Maxima||6900|135494|Kansas City, MO|89|clean||
966647679504581|2008|Honda Odyssey|LX|6999|95000|Kansas City, MO|130|unknown||
1948937945985184|2019|Kia Niro|LX|6999|161758|Kansas City, KS|132|clean|dealer|
1547653673620499|2010|BMW 28i|28i|6800|12000|Kansas City, KS|85|unknown||
2243492376220329|2018|Jeep Grand Cherokee||6985|172741|Kansas City, MO|4|clean|dealer|
1587182423186556|2015|Kia Sedona||7000|180000|Kansas City, KS|0|clean||
1437826061660956|2017|Kia Soul|Soul|7200|87000|Kansas City, MO|4|unknown||
2937491316584169|2010|Nissan Xterra|S|7400|150693|Overland Park, KS|5|clean||
1397157025222737|2017|Ford Edge|Titanium|7300|167274|Grandview, MO|8|clean||
3545971005550620|2012|Volvo S60|T6|7000|16000|Kansas City, MO|8|unknown||
1082853531283216|2013|Chevrolet Suburban||7000|1460|Kansas City, MO|10|unknown||
4464694017105882|2008|Ford Mustang|GT|7000|102000|Bates City, MO|25|rebuilt||
4582775842009539|2009|Ford Explorer||7000|105588|Overland Park, KS|33|clean||
1355032473464627|2011|Dodge Ram 1500|Sport|7200|178000|Kansas City, MO|33|rebuilt||AS IS 판매
1051245184272928|2012|Dodge Durango|Citadel|7000|200000|Lawrence, KS|33|unknown||
1692073475347336|2015|Jeep Grand Cherokee|Limited|7000|148340|Kansas City, MO|34|unknown||
973413502409665|2009|Honda Pilot|EX|7300|164347|Kansas City, MO|55|clean||같은 차 2건 게시
27651660534500246|2009|Honda Pilot|fwd-|7000|194720|Kansas City, MO|58|unknown|dealer|
2130135754551902|2016|Nissan Altima|2.5 S|7485|120557|Olathe, KS|66|clean||같은 차 2건 게시
4154037281593815|2008|Infiniti G35||7000|180000|Kansas City, KS|67|unknown||
1343454857853614|2013|GMC Terrain|SLE-1|7400|112500|Kansas City, MO|69|clean||
1570810344563621|2013|Honda Civic|LX|7000|131531|Kansas City, MO|79|rebuilt||
1001458082631398|2010|Cadillac Escalade|Luxury|7000|243000|Kansas City, KS|98|unknown||
1565427555202310|2012|Toyota Yaris|L|7000|146000|Kansas City, MO|125|unknown|dealer|
1354916763245257|2008|Nissan Armada|LE|7000|17084|Kansas City, KS|91|clean||
1664298031449687|2015|Audi A3|Premium|7000|112436|Raytown, MO|118|clean||
1124061750047124|2014|Volkswagen Jetta||7199|144634|Kansas City, MO|7|unknown|dealer|
1332894182148423|2014|Subaru Forester||7400|198121|Independence, MO|106|clean|dealer|
1249606936816118|2017|Kia Forte|LX|7350|152000|Kansas City, KS|179|clean||
1761013611807288|2010|Chevrolet Camaro|LS|7800|120131|Kansas City, KS|0|clean||
1436197458422486|2011|Chevrolet Equinox|LTZ|7600|101322|Lenexa, KS|1|unknown||
1655840652784685|2016|Chrysler 300|300 Limited|7995|123000|Independence, MO|2|clean||
1435018238529561|2017|Buick Enclave|Premium|7750|185000|Smithville, MO|2|clean||
4382930831970334|2009|Lexus IS|IS 250|7500|156515|Kansas City, MO|2|clean||
2085223299051984|2015|Audi A5|2.0T Quattro Premium|7500|93000|Liberty, MO|2|clean||누유·누수 기재 · AS IS 판매
1595493805555725|2020|Chevrolet Trax|LS|7999|63500|Olathe, KS|6|clean||
2215540815684860|2013|Chevrolet Silverado 1500|Work Truck|7500|204024|Kansas City, MO|8|clean||
2237590397089022|2012|Dodge Challenger|Challenger+2d+cupe|7900|105000|Olathe, KS|8|rebuilt||
1559500812596535|2008|Chevrolet Silverado 1500|Short Bed|7500|152547|Belton, MO|10|unknown||
2001712217197540|2015|Subaru Legacy|2.5i Premium|7800|90580|Olathe, KS|11|rebuilt||
2804607309940222|2015|Dodge D150|Short Bed|7995|150250|Kansas City, MO|14|clean||
1960813587930196|2012|Honda Civic|EX-L|7900|39927|Kansas City, MO|16|clean||
2096736427609628|2012|Subaru Impreza||7995|149567|Lee's Summit, MO|20|unknown||
4318254458438482|2017|Kia Sportage|LX|7700|125000|Kansas City, MO|26|clean|dealer|
27876305548716896|2011|Lincoln MKX||7995|147794|Lee's Summit, MO|27|unknown||
2495006214245347|2011|Mercedes-Benz M-Class||7999|110004|Belton, MO|28|clean|dealer|
1350593540395011|2008|Chevrolet Tahoe|LTZ|7500|1111|Kansas City, KS|29|unknown||
1625197409282427|2010|Infiniti G37|X|7500|123541|Lee's Summit, MO|30|clean||
1551746976731291|2012|Honda Odyssey|EX-L w/DVD Res|7995|164000|Independence, MO|44|clean||
1406440018069302|2011|Cadillac Escalade|Prem Lux Platinum|7800|164825|Odessa, MO|45|unknown||
1518516486200866|2008|GMC Sierra 2500HD|Sierra HD|7550|200000|Olathe, KS|48|clean||
1069514798833841|2010|BMW 1 Series|128i|7999|150900|Wellsville, KS|48|clean||
1033920102736342|2010|Mercedes-Benz E-Class|E 550 4MATIC|7500|150000|Smithville, MO|51|unknown||
1385444497067003|2010|GMC Yukon XL|Commercial|7500|267000|Independence, MO|52|clean||
1618121706415584|2008|Toyota Camry|4dr|7780|152797|Independence, MO|61|unknown||다운페이·할부 광고
1528280421473242|2010|Chevrolet Silverado 1500|Short Bed|7500|180000|Archie, MO|73|unknown||누유·누수 기재
1568715768157081|2017|Kia Soul|Soul|7950|111000|Belton, MO|123|clean|dealer|
1465095722075266|2014|Chevrolet Equinox|LS|7950|144484|Kansas City, MO|160|unknown||
1496958178688389|2016|Cadillac SRX||7900|160082|Kansas City, KS|167|clean||
1641958406945602|2016|Chevrolet Cruze||7999|117499|Belton, MO|168|clean|dealer|
842842072188660|2011|Hyundai Accent||7699|61229|Kansas City, MO|7|unknown|dealer|
1077666981293649|2008|Honda Ridgeline|RTX|7500|169000|Overland Park, KS|32|clean||
1024118200016674|2013|Chevrolet Tahoe|Commercial|7500|95124|Belton, MO|79|clean||
2210388076460452|2014|Toyota Tundra||7500|244000|Kansas City, KS|84|unknown||
967372339233807|2018|Nissan Altima||7500|161000|Belton, MO|130|clean|dealer|
2246948715835035|2012|BMW 7 Series|750Li|7500|104250|Kansas City, MO|130|clean||
1478455000491120|2010|BMW 3 Series|328i xDrive|7500|150000|Prairie Village, KS|142|clean||
985391654153135|2014|Dodge Ram 1500|Express|7500|160000|Lee's Summit, MO|170|clean||엔진 경고등 기재
994069766856296|2017|Ford Escape|SE|7500|131000|Kansas City, KS|107|clean||
1085706363822335|2014|Volkswagen Golf|2.5L|7950|75000|Raytown, MO|1|clean||
28135479179414020|2014|Ford Escape|Titanium|7950|80073|Kansas City, MO|7|salvage||
1553939502637057|2010|Nissan Rogue||7800|73888|Excelsior Springs, MO|12|unknown||
1632069655016477|2015|Hyundai Elantra||7950|98000|Belton, MO|23|clean|dealer|
2459808541169994|2009|Acura RDX||7950|114000|Kansas City, MO|34|clean||
1055463846865609|2017|Chevrolet Traverse||7750||Mission, KS|41|unknown|dealer|
2884142375269488|2008|Ford F-350|Super Duty 6.4 Powerstroke|7900|200000|Kansas City, KS|65|clean|dealer|
1509321600667484|2013|Ford Fusion||7950|153907|Independence, MO|88|clean|dealer|
1274224778118730|2014|Cadillac SRX|Premium Collection|7750|163000|Kansas City, MO|99|clean|dealer|
958066957230206|2009|Audi A4||7950|108174|Belton, MO|102|clean||
25698710676472278|2011|BMW 5 Series|535i xDrive|7800|131000|Kansas City, MO|146|unknown||
821368207577800|2016|Infiniti Q50|3.0t SPORT|7900|92000|Kansas City, KS|89|rebuilt||
39659113567021135|2008|Honda Civic||7899|129171|Kansas City, MO|7|unknown|dealer|'''

have = {x['id'] for x in d['listings']}
same_car = {(x['year'], x['model'], x['price'], x['miles']) for x in d['listings']}
def implausible(year, price):
    # ponytail: fixed year/price floors, not a valuation model; tune if real cheap cars get dropped
    return (year >= 2026 or price in (1234, 12345) or (year >= 2022 and price < 5000) or (year >= 2019 and price < 4000)
            or (year >= 2016 and price < 2500) or (year >= 2014 and price < 1000) or (year >= 2010 and price < 800))

rows, repeats, scams = [], 0, 0
for line in raw.splitlines():
    i, year, model, trim, price, miles, city, days, title, flags, note = line.split('|')
    flags = set(filter(None, flags.split(',')))
    assert i not in have and title in {'clean', 'rebuilt', 'salvage', 'unknown'} and flags <= {'avoid', 'dealer'}, line
    assert 500 <= int(price) <= 7999 and int(year) >= 2008 and int(days) <= 180, line
    miles = int(miles) if miles else None
    if implausible(int(year), int(price)):
        scams += 1
        continue
    if miles is not None and int(year) <= 2023 and miles < 2000 * (2026 - int(year)):
        note = ' · '.join(filter(None, [note, f'주행거리 표기 이상(원문 {miles:,} mi)']))
        miles = None
    if miles is not None and (int(year), model, int(price), miles) in same_car:
        repeats += 1  # the same car re-posted under a new listing id
        continue
    rows.append(dict(id=i, year=int(year), model=model, vehicle=f'{year} {model} {trim}'.strip(), price=int(price), miles=miles,
                     city=city, days=int(days), title=title, pick=False, avoid='avoid' in flags, dealer='dealer' in flags, note=note))
assert len({r['id'] for r in rows}) == len(rows)

d['listings'] += rows
d['search'].update(priceMin=0, scanned=5384)
d['search']['passes'].append(dict(price='$0–$7,999', scanned=5384, kept='1·2차에 없던 승용차·SUV·밴·픽업 전체'))
path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print(f"added {len(rows)} (skipped {repeats} re-posts, {scams} implausible prices); total {len(d['listings'])}; avoid {sum(r['avoid'] for r in rows)}")
