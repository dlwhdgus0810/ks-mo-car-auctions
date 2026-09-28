"""Add Facebook Marketplace listings posted after the 2026-09-23 snapshot: $5,000-$7,999, Overland Park 40 mi.

On 2026-09-28 the Cars & Trucks search ($5,000-$7,999, newest first) was opened once per price band until each band
reached listings older than the 9/23 scan (about 2026-09-24 03:30 UTC); 342 unique listings were seen. Only search-result
data was read (year, model, price, odometer, city, posting time). Detail pages were not opened, so title status and seller
notes are unknown ('상세 미조회'). The $5,500, $6,000 and $6,500 price points each had more new listings than one results
page shows, so a few listings posted on 9/24 at exactly those prices may be missing.
Rules follow the third pass (scripts/add-marketplace-under8k-sep23.py): model year 2008+, passenger cars, SUVs, vans and
pickups only (an empty model means a motorcycle, UTV, RV or golf cart), implausible prices dropped, odometers under 2,000 mi
per year of age treated as unknown, repeat posts of one car dropped. Existing rows get 5 more days since posting so every
row counts days from 2026-09-28. Ten of the newest, lowest-mileage cars were opened on their listing pages to read the title
status and the seller's description (DETAILS); the three clean-title ones join the recommended picks.
"""
import json
from pathlib import Path

p = Path(__file__).resolve().parents[1] / 'dist'
path = p / 'marketplace-2026-09-23.json'
d = json.loads(path.read_text())
assert d['checkedAt'] == '2026-09-23', 'One-time migration'

# id|year|model|trim|price|odometer|city|days since posted on 2026-09-28|flags (empty model = not a car)
raw = '''2354421035360760|2017|Chevrolet Malibu|LT|6999|139000|Overland Park, KS|0|
1764033761547068|2014|Ford Escape|SE|5500|100000|Linwood, KS|0|
1138146168737294|2013|Honda Accord|LX|6900|166000|Kansas City, KS|0|
2272164480241447|2013|Subaru Forester||5500|179000|Mission, KS|0|
1728166141609824|2002|Chevrolet Silverado 2500HD||5500|254000|Belton, MO|0|
1813808679611589|2014|Dodge Ram 1500|SLT|6500|198000|Bates City, MO|0|
1844361160343900|2012|Subaru Outback||5900|288000|Shawnee, KS|0|
1408843274047615|2004|Ford Explorer||6000|152000|Adrian, MO|0|
1073590798706235|2008|Jeep Liberty||5000|91000|Overland Park, KS|0|
1073473595447754|2014|Chevrolet Cruze|LT|5500|82000|Kansas City, MO|0|
1516692120503749|2015|Ford Escape|Active|6000|92000|Lawrence, KS|0|
1078717788075795|2006|Lincoln Navigator|Premier|5000|207000|Osawatomie, KS|0|
1293055042886808|2011|Toyota RAV4||5000|215000|Shawnee, KS|0|
4096900460613471|1999|Jeep Cherokee|Sport 4D|6000|175000|Lawrence, KS|0|
2042570783217913|2006|Ford F-150|Lariat|6500|197000|Raytown, MO|0|
1068956472707056|2014|Volkswagen Passat|TDI SE|5800|186000|Louisburg, KS|0|
2923010374749644|2015|Kia Sorento|LX|5500|139000|Olathe, KS|0|
2559261214539713|1987|Volkswagen Cabriolet|Classic|6900|100000|Kansas City, MO|0|
1671180414799603|2011|Honda Civic||5399|186000|Kansas City, KS|0|
1704542223967712|2013|Ford Fusion|SE|5500|177000|Kansas City, MO|0|
1094198033076297|2011|Honda Accord|EX|6200|149000|Olathe, KS|0|
1794057671789621|2012|Toyota Sequoia|Platinum|6400|292000|Fontana, KS|0|
983186531476538|2010|Toyota Prius||5500|202000|Lenexa, KS|0|
1123419466704933|2016|GMC Acadia|SLT|6995|144000|Kansas City, MO|0|
2030397821696339|2011|Honda Pilot|EX-L|7200|151000|Raymore, MO|0|
976592578027490|2013|Ford Escape|SE|6200|97000|Independence, MO|0|
1356482222982085|2006|Lexus RX|RX 330|7500|193000|Olathe, KS|0|
1081494611281046|2018|Dodge Grand Caravan|SE|7500|93000|Shawnee, KS|0|
2257591301699533|2018|Chevrolet Cruze||7999|113000|Kansas City, MO|0|
1118580454013468|2007|Subaru Forester|2.5X Premium|5500|190000|Kansas City, KS|0|
1091363370296111|2013|Dodge Ram 1500||6000|250000|Independence, MO|0|
1706218407135306|2016|Lincoln MKZ||7500|139000|Kansas City, MO|0|
2197191008345120|2017|Nissan Rogue||7999|127000|Kansas City, MO|0|
2084967935471393|2012|Ford Explorer||7999|138000|Kansas City, KS|0|
2537835290048774|2024|||7500|1800|Independence, MO|0|
1412534537686758|2015|Ford F-150|FX4|7800|222000|Leavenworth, KS|0|
2536322746873706|2019|Ford Fusion|SEL Hybrid|5500|188000|Overland Park, KS|0|
1067704809429914|2014|Kia Soul||6450|103000|Olathe, KS|0|
4529964267325098|2013|Ford E-Series||5500|230000|Shawnee, KS|0|
949575821540346|2012|Nissan Quest||7000|201000|Kansas City, MO|0|
2785950061790726|2013|Buick Enclave|Leather|5100|163000|Kansas City, MO|0|
1427724442644192|2014|Ford Escape|Titanium|5500|154000|Kansas City, MO|0|
1321281989943374|2013|Mazda3||6000|108000|Kansas City, KS|0|
1077040711715432|2010|Nissan Maxima|SV|5500|164000|Kansas City, MO|0|
29131705016437551|2014|Buick Verano|Convenience|7500|126000|Kansas City, KS|0|
1054361190761869|2010|Ford F-150|STX|6400|96000|Kansas City, MO|0|
1776577906922194|2017|Nissan Murano|SL (2017.5)|6990|148000|Kansas City, MO|0|
1619840933106246|2012|Chevrolet Silverado 1500|4x4|7500|15000|Olathe, KS|0|
1079217454719285|2014|Nissan Rogue|S|6750|106000|Kansas City, MO|0|
2152821665589392|2004|Dodge Ram 2500|Laramie|5000|246000|La Cygne, KS|0|
1071691762298498|2015|Audi A6|2.0T Premium Plus|6450|143000|Kansas City, MO|0|
2027990614528106|2004|Chevrolet Silverado 1500|Short Bed|6500|195000|Independence, MO|0|
1018084774580139|2012|Ford Mustang||7000|115000|Kansas City, KS|0|
3047069268978127|2013|Nissan Rogue||5985|103000|Kansas City, KS|0|
1109515815348132|2015|Ford Edge|SE|6500|136000|Lenexa, KS|0|
1997532267624736|2026|||7900||Grain Valley, MO|0|
1804775724277323|2014|Mazda3|Grand Touring|6400|141000|Kansas City, KS|0|
1103653102378739|2007|Toyota Prius||6000|108000|Kansas City, MO|1|
3469200416591025|2012|Infiniti G37||7000|135000|Prairie Village, KS|1|
1106237731885382|2011|Toyota Sienna|XLE|6500|214000|Kansas City, MO|1|
1414781480613757|2016|Kia Optima|EX|6200|145000|Kansas City, MO|1|
1095691180053538|2018|Ford Escape|SEL|7500|121000|Lee's Summit, MO|1|
1788813388982068|2014|Audi A4|2.0T Quattro|5950|122000|Shawnee, KS|1|
1630104208666320|2012|Buick Enclave|Leather|6500|162000|Kansas City, MO|1|
1695083598708488|2007|Ford F-150|FX4|5000|204000|Kansas City, MO|1|
29702052049384543|2002|Dodge Ram 2500|SLT|6000|92000|Lawrence, KS|1|
2213913775834629|2019|Dodge Grand Caravan|SXT|7350|101000|Kansas City, MO|1|
2164227454518691|2002|Ford Mustang|GT|5300|125000|Lenexa, KS|1|
1352306163399459|2010|Toyota RAV4||6600|145000|Kansas City, KS|1|
2875567026144793|2012|Volkswagen Jetta|S|5499|200000|Kansas City, MO|1|
1127969523086629|2018|Kia Optima|SX|5500|170000|Kansas City, KS|1|
1601897938009638|2004|GMC Sierra 2500HD||6800|361000|Belton, MO|1|
4368416686802883|2014|GMC Terrain|SLE|6200|150000|Smithville, MO|1|
2015376245820400|2004|Ford F-150|FX4|5500|127000|Kansas City, MO|1|
2157919744819924|2014|Honda CR-V|LX|5200|300|Olathe, KS|1|
1303518239516413|2004|Ford F-250|Lariat|7000|165000|Independence, MO|1|
1898646118183603|1993|Honda Del|So|5000|178000|Lenexa, KS|1|
1390965499334784|2007|Toyota Camry|LE|6700|117000|Olathe, KS|1|
1422740619824624|1967|Chevrolet Silverado 1500|Long Bed|6000|100000|Olathe, KS|1|
28530263159990958|2013|Infiniti G37x||5500|133000|Kansas City, MO|1|
1789491655621942|2011|Dodge Charger|R/T|5500|205000|Kansas City, KS|1|
28270726635912331|2015|GMC Savana||7800|248000|Raytown, MO|1|
1070158325909951|2013|Dodge Challenger|R/T|6500|80000|Kansas City, MO|1|
2316504115850632|2013|Audi Q7|3.0 TDI Quattro Premium|6500|159000|Kansas City, MO|1|
1394146856202613|2010|Chevrolet Silverado 1500|LT|6500|237000|Lawrence, KS|1|
2342889362916365|2010|Toyota Corolla|LE|5000|191000|Olathe, KS|1|
1733131337989042|2013|Chevrolet Malibu||5399|93000|Kansas City, MO|1|
1835244064307657|1996|Ford Ranger|XLT|6000|136000|Kansas City, MO|1|
1388829026745370|2012|FIAT 500|Sport|5300|106000|Lee's Summit, MO|1|
1466168905572793|2007|||6000|8000|Bates City, MO|1|
1395265439463187|1990|Chevrolet Suburban||6500|4000|Kingsville, MO|1|
1636709101160465|2019|Dodge Ram 1500|Tradesman|5575|241000|Kansas City, MO|1|
28589491217368919|2023|||6900|300|Kansas City, MO|1|
4729058937418194|2012|Toyota Camry|CE|5500|199000|Kansas City, MO|1|
2266175390902127|2013|Kia Rio|EX|5000|144000|Roeland Park, KS|1|
1452617060090877|2015|Volkswagen Jetta|S|5990|139000|Independence, MO|1|
2951632978568687|2006|Ford E-Series||6500|144000|Grain Valley, MO|1|
1380672910945857|2018|Ford Fusion|SE|7900|112000|Kansas City, KS|1|
1023222157435213|2007|Honda Element|SC|5900|221000|Kansas City, KS|1|
1400880722170908|2020|Ford Explorer||7500|109000|Kansas City, MO|1|
955691287579129|2012|Buick LaCrosse|Premium Cleanest Buick on Market|7950|99000|Kansas City, MO|1|
2107669989959211|2015|Ford Flex|SE|5900|128000|Olathe, KS|1|
1532683792227651|2017|Nissan Rogue|SL|7900|97000|Olathe, KS|1|
1250689320554186|2005|Toyota Highlander||5400|298000|Platte City, MO|1|
1086952687551603|2017|Ford Edge|SEL Plus|5990|158000|Overland Park, KS|1|
4540385709532169|2007|Pontiac G5||6000|141000|Kansas City, KS|1|
3527330694114666|2004|Infiniti I35|No Accidents or Damage Reported|7999|84000|Kansas City, MO|1|dealer
1444448931112381|2005|Chevrolet Uplander||5880|145000|Lawrence, KS|1|
1790684659726990|2008|Ford F-150|XLT|5650|129000|Basehor, KS|1|
1099878489208122|2018|Ford Escape||5600|169000|Kansas City, MO|1|
2439107019916491|2016|Volkswagen Jetta|1.4T S|6000|148000|Kansas City, KS|1|
1490018276401312|2017|Kia Soul||6800|87000|Kansas City, MO|1|
2916554592024787|2015|Nissan Murano|Platinum|7950|161000|Kansas City, MO|1|
1848178146551060|2013|Honda Civic|Hybrid|6800|159000|Blue Springs, MO|1|
3202041546658034|1998|Jeep Wrangler|"Sport"|6200|190000|Paola, KS|1|
1574005278105032|2016|Subaru Outback|2.5i Premium|6450|206000|Overland Park, KS|1|
2028611551185917|2015|Nissan Altima|2.5 S|5490|141000|Lenexa, KS|1|
1632734548373807|2010|Audi A6|2.7T S-Line Quattro|6000|142000|Independence, MO|1|dealer
2173237739889103|2013|Ford Fusion|SE|5200|163000|Kansas City, MO|1|
2134939483797901|2017|Dodge Grand Caravan|SE Plus|6500|176000|Kansas City, MO|1|
1077413665265135|2003|Chevrolet Tahoe||6400|201000|Kansas City, MO|1|
1878825139766921|2008|Toyota FJ||7500|250000|Kansas City, KS|1|
1104874095350424|2013|Nissan Altima||6250|136000|Overland Park, KS|1|
2152991552286854|2004|Mercury Marauder||5999|336000|Lenexa, KS|1|
1022257687538861|2012|Mercedes-Benz Sprinter|High Roof Extended w/170" WB Extended|6500|575000|Leavenworth, KS|1|
1629907151979447|2015|||6500|4900|Tonganoxie, KS|1|
3007754979576708|2008|BMW 3 Series|328i|6900|141000|Shawnee, KS|1|
1483242616962375|2022|Chevrolet Express||7500|213000|Overland Park, KS|1|
1700756027650640|2008|Jeep Grand Cherokee||6000|176000|Lawrence, KS|2|
998415469936739|2007|Ford Edge||6780|152000|Kansas City, MO|2|
1092742856740007|2015|Ford Taurus|Limited|5950|145000|Shawnee, KS|2|
2711653559290416|2016|Buick Enclave|Premium|6500|151000|Independence, MO|2|
1078160474927032|2016|Chevrolet Spark|Ls|6500|70000|Kansas City, MO|2|
1884320972977591|2015|Dodge Journey|Crossroad|5999|105000|Kansas City, MO|2|
1684973889819313|1987|Jaguar Le||5000|47000|Kansas City, KS|2|
2569000306935841|2016|Chevrolet Spark|LS|6500|70000|Kansas City, MO|2|
1588128013056899|2012|BMW 5 Series|535i|5450|161000|Overland Park, KS|2|
2951609518532638|1993|Lincoln Town|Executive|7500|157000|Blue Springs, MO|2|
933689066467140|2017|Kia Forte|S|6400|178000|Grain Valley, MO|2|
1945660436101995|2012|Subaru Outback|2.5i Premium|6999|147000|Belton, MO|2|dealer
1151233747607035|2007|Hummer H3|4x4|6900|186000|Kansas City, KS|2|
2136408076979994|2019|||5500|2900|Overland Park, KS|2|
1664374948536984|2008|Cadillac Escalade|Luxury|7000|220000|Kansas City, KS|2|
1401509665433185|1997|Jeep Wrangler||5000|186000|Oak Grove, MO|2|
2514826592320435|2016|Kia Sedona|LX|5950|124000|Kansas City, MO|2|
1837371240754026|2016|||6000|300|Shawnee, KS|2|
1400446331620723|2021|||6900||Smithville, MO|2|
1616422929865838|2016|Nissan Rogue|SV|6900|126000|Kansas City, MO|2|
986566111164952|2013|Honda Civic|EX|5500|168000|Overland Park, KS|2|
2310946212998470|2014|Chevrolet Traverse||7599|159000|Kansas City, KS|2|
1090252493715341|2015|Nissan Rogue||6900|135000|Kansas City, KS|2|
1122703290322828|2013|Kia Rio|LX|6100|75000|Kansas City, KS|2|
2344828243001508|2015|Ford Fusion||7995|156000|Kansas City, KS|2|
1624015399113906|2000|Toyota 4Runner|Limited|7000|175000|Olathe, KS|2|
4711868492405080|2017|Chevrolet Traverse||6000|119000|Kansas City, MO|2|
1388258596809867|2012|Audi A4|Quattro premium plus|6000|148000|Kansas City, MO|2|
2530616520781121|2012|BMW X5|xDrive35i Premium|6500|200000|Pleasant Hill, MO|2|
1819318082541158|2014|Infiniti Q50|S Hybrid|5400|167000|Greenwood, MO|2|
3278045745731823|2014|Honda Odyssey||5999|240000|Kansas City, KS|2|
1921338982172306|2017|Hyundai Elantra|Limited|7800|99000|Raytown, MO|2|
1635551417952895|2015|Nissan Sentra|SV|5500|139000|Osawatomie, KS|2|
1788489062155015|2015|Chevrolet Malibu|LT|5500|175000|Belton, MO|2|
1411450523776633|2014|Ford Escape|Titanium|5950|146000|Kansas City, KS|2|
2609082616216569|2018|Buick Encore|Encore|6800|125000|Lee's Summit, MO|2|
2817772931937512|2013|Ford Edge|SEL|6000|149000|Lawrence, KS|2|
1027919080255061|2017|Nissan Altima|2.5 S|5000|17000|Independence, MO|2|
2243644099538555|2015|Chevrolet Express|Regular|6450|232000|Kansas City, MO|2|
1777230926847708|2012|Kia Optima|EX|6950|111000|Overland Park, KS|2|
2871572709895240|2014|Volkswagen CC|2.0T Executive|6900|115000|Kansas City, KS|2|
942823438890549|2015|GMC Terrain||7500|127000|Belton, MO|2|
1758754585175923|2017|Dodge Journey|SXT|6300|149000|Belton, MO|2|
1628492102154846|2014|Ford Flex||6999|168000|Belton, MO|2|
1067224909532322|2014|Volkswagen Touareg|V6 Executive|7000|139000|Kansas City, MO|2|
1822391182442291|2015|Smart Fortwo|Passion|7300|87000|Greenwood, MO|2|
2569817943460820|2006|Audi A4|2.0T Avant Quattro Premium|6499|259000|Pleasant Hill, MO|2|
1718634639197913|2013|Mazda CX-9|Grand Touring|7800|155000|Leawood, KS|2|
1639497274436069|2015|Chevrolet Cruze|LT|5000|136000|Belton, MO|2|
2190735854808600|2007|Lexus IS|IS 250|6800|195000|Kansas City, MO|2|
1979791332978032|2008|Chevrolet Silverado 1500||7200|230000|Kansas City, KS|3|
1108688711891828|2016|Chevrolet Equinox|LT|7500|130000|Independence, MO|3|
1410357867908620|2018|Jeep Renegade|Latitude|6600|118000|Kansas City, MO|3|
1453116640065386|2017|Hyundai Elantra|SE|7999|103000|Stilwell, KS|3|
2248195359083609|2011|Lexus RX||7995||Lee's Summit, MO|3|
1099695822443790|2018|Chevrolet Malibu||7950|147000|Lenexa, KS|3|
1713656453057963|2016|Hyundai Elantra||6000|136000|Overland Park, KS|3|
4533845410212954|2014|Jeep Patriot||7800|124000|Kansas City, MO|3|
1046120121815513|2017|Volkswagen Jetta|1.4T SEL|7000|130000|Overland Park, KS|3|
1600764251577628|2011|Mazda CX-7||5250|99000|Kansas City, KS|3|
1059186923591419|2010|Kia Optima||5200|139000|Overland Park, KS|3|
1619398876256311|2016|Ford Explorer|Limited|6995|169000|Independence, MO|3|
2487045961780534|2015|Kia Optima|Limited-SXL|5450|133000|Kansas City, MO|3|
1088788173918083|2014|Jeep Compass|Latitude|5300|163000|Kansas City, MO|3|
1792172172110721|2015|Nissan Pathfinder|SV|5500|150000|Overland Park, KS|3|
1398377085161418|2008|Ford F-150|FX2|7500|200000|Kansas City, KS|3|
973172172492330|2015|Volvo XC60|3.2 Premier|6500|170000|Overland Park, KS|3|
1848780909614023|2009|GMC Sierra 1500|SL|6500|213000|Independence, MO|3|
1609529547295073|2012|Ford Focus|SE|5000|145000|Independence, MO|3|
1769361234313037|2011|Audi A4|2.0T Quattro|6500|152000|Independence, MO|3|
1577085500087316|2012|||6000||Olathe, KS|3|
29588563354077760|2015|Volkswagen CC|(Only 88K Miles)|6750|88000|Raytown, MO|3|
1738397857384060|2011|Jeep Grand Cherokee|Laredo 4x4|7500|118000|Kansas City, MO|3|
940302972481857|2017|Kia Sorento||6200|165000|Lenexa, KS|3|
1416972713213396|2016|Hyundai Elantra|SE Value Edition|6000|136000|Overland Park, KS|3|
3255067178027614|2016|Hyundai Elantra|SE Value Edition|5500|136000|Overland Park, KS|3|
1121964687364126|2016|Nissan Rogue|SV|5850|141000|Smithville, MO|3|
1112336697977156|2016|Nissan Murano|S|5850|187000|Smithville, MO|3|
967030605692404|2014|BMW 3 Series||5500|195000|Kansas City, KS|3|
3125811787766308|2014|Kia Optima|EX|7900|91000|Grandview, MO|3|
1083636187719226|2012|||7250|22000|Olathe, KS|3|
1783362836209280|2013|Ford F-150|Lariat|5600|294000|Leawood, KS|3|
930271700153381|2015|GMC Acadia|SLE-1|7000|129000|Shawnee, KS|3|
1821950932384049|1981|Chevrolet C10||5000|2500|Overland Park, KS|3|
1831785404513360|2018|Nissan Sentra|1.8 S|5000|123000|Kansas City, MO|3|
1402574871305832|2011|Subaru Forester|2.5X Limited|5500|171000|Kansas City, MO|3|
917381014500612|2025|||7000||Oak Grove, MO|3|
2145044269730436|2014|Chevrolet Equinox||5900|128000|Lawrence, KS|3|
2312889829547732|2015|Chevrolet Malibu|LT|5300|141000|Kansas City, MO|3|
1063181959918262|2017|Ford Escape|SE|5950|119000|Blue Springs, MO|3|
2231256407606354|2004|Ford Explorer||6000|97000|Kansas City, MO|3|
1657673192813782|2013|||5988||Liberty, MO|3|
1663855635343954|2014|Ford Fusion||5699|150000|Kansas City, MO|3|
3774079539397458|2010|Dodge Ram 2500|Laramie|5000|156000|Kansas City, MO|3|
1082617894629136|2014|Jeep Cherokee|Latitude|5750|148000|Kansas City, MO|3|
906323232350056|2016|Jeep Cherokee|Latitude|5750|172000|Kansas City, MO|3|
1353987830140123|2013|Mercedes-Benz E-Class|E 350 4MATIC|5850|177000|Kansas City, MO|3|
1792254175448237|2019|Chevrolet Equinox|LS|5999|165000|Kansas City, MO|3|
1752904372650499|2017|Ford Fusion|SE|5650|176000|Kansas City, MO|3|
955652196967868|2016|Ford Taurus|SE|5800|135000|Independence, MO|3|
2243962236188167|1984|Chevrolet Monte||6000|6500|Raymore, MO|3|
1105163551977197|2011|Hyundai Genesis|4.6|6500|86000|Independence, MO|3|
2183028622647247|2016|Nissan Maxima|Platinum|7250|149000|Olathe, KS|3|
28347852161536740|2020|Kia Soul||7499|152000|Kansas City, MO|3|dealer
1586880956409039|1987|Ford F-350|Long Bed|5000|154000|Kansas City, MO|3|
1095905309701497|2003|Chevrolet Silverado 1500|LT|5000|220000|Shawnee, KS|3|
4464937847112661|2014|Ford F-150|FX4|7500|234000|Independence, MO|3|
1373287024956817|2018|Nissan Rogue|SV(AWD,Low Miles,Loaded)|7999|107000|Leawood, KS|3|
4060622697570869|2016|Kia Soul|Plus|7500|130000|Overland Park, KS|3|
968074692983351|2007|Honda Civic|Si|5000|114000|Kansas City, MO|3|
1075580208423653|2015|Jeep Compass|Latitude|6200|100000|Kansas City, MO|3|
29451891991079226|2011|Cadillac SRX|Luxury Collection|5700|164000|Blue Springs, MO|3|
2154004611990007|2017|Chevrolet Traverse||7750||Mission, KS|4|
1735417897745792|2011|Hyundai Santa Fe|Limited Ultimate|5400|123000|Kansas City, KS|4|
1632352854996634|2011|GMC Acadia||6550|124000|Kansas City, KS|4|
1071958219044900|2013|Kia Optima||7950|77000|Mission, KS|4|
1518468276705562|2017|Chevrolet Spark||6900|83000|Kansas City, MO|4|
2145111022773901|2016|Dodge Journey|Crossroad|6500|137000|Grandview, MO|4|
1409481200617252|2016|Dodge Journey|Crossroad|6500|137000|Grandview, MO|4|
1123710053329048|2006|Honda VFR||6000|41000|Lee's Summit, MO|4|
1618094303323504|2006|BMW 3 Series|330i|6500|205000|Lawrence, KS|4|
1495335159088939|1994|Ford F-350|XLT|7000|200000|Kansas City, MO|4|
1739008720658564|2010|||6800|10000|Raymore, MO|4|'''


# Read from the listing pages on 2026-09-28: exact odometer, title status, notes
DETAILS = {
    '1400880722170908': dict(miles=109000, avoid=True, note='경찰차(Police Interceptor) · ABS 교체 후 정비 모드 해제 필요·브레이크 페달 딱딱함 기재'),
    '2213913775834629': dict(miles=101722, title='rebuilt', note='우박 손상 Rebuilt 기재'),
    '1081494611281046': dict(miles=93500, title='rebuilt', note='Rebuilt · MO 고속도로순찰대 검사 통과 기재'),
    '1410357867908620': dict(miles=118000, title='rebuilt', dealer=True, note='왼쪽 펜더 교체 Rebuilt · 임시번호판 60일·파워트레인 보증 30일'),
    '1831785404513360': dict(miles=123978, note='타이틀 미기재 · 운행 가능 기재'),
    '1532683792227651': dict(miles=97000, title='rebuilt', note='설명상 SV AWD 7인승 · R 타이틀 기재'),
    '1373287024956817': dict(miles=107000, title='clean', pick=True, vehicle='2018 Nissan Rogue SV AWD', note=''),
    '1490018276401312': dict(miles=87000, note='타이틀 미기재 · 정비 최신 기재'),
    '1921338982172306': dict(miles=99140, title='clean', pick=True, note='새 배터리·점화플러그 기재'),
    '1516692120503749': dict(miles=92300, title='clean', pick=True, note='2인 소유'),
}


def implausible(year, price):
    # ponytail: same fixed year/price floors as the third pass, not a valuation model
    return (year >= 2026 or price in (1234, 12345) or (year >= 2022 and price < 5000) or (year >= 2019 and price < 4000)
            or (year >= 2016 and price < 2500) or (year >= 2014 and price < 1000) or (year >= 2010 and price < 800))


have = {x['id'] for x in d['listings']}
same_car = {(x['year'], x['model'], x['price'], x['miles']) for x in d['listings']}
rows, seen, skipped = [], {}, dict(not_car=0, before_2008=0, implausible=0, repost=0)
for line in raw.splitlines():
    i, year, model, trim, price, miles, city, days, flags = line.split('|')
    year, price, days = int(year), int(price), int(days)
    assert i not in have and 5000 <= price <= 7999 and 0 <= days <= 5 and flags in ('', 'dealer'), line
    if not model:
        skipped['not_car'] += 1
        continue
    if year < 2008:
        skipped['before_2008'] += 1
        continue
    if implausible(year, price):
        skipped['implausible'] += 1
        continue
    miles = int(miles) if miles else None
    note = '상세 미조회'
    if miles is not None and year <= 2023 and miles < 2000 * (2026 - year):
        note += f' · 주행거리 표기 이상(원문 {miles:,} mi)'
        miles = None
    if miles is not None and (year, model, price, miles) in same_car:
        skipped['repost'] += 1
        continue
    key = (year, model, price, miles if miles is not None else city)
    if key in seen:  # the same car posted twice since 9/23
        seen[key]['posts'] += 1
        skipped['repost'] += 1
        continue
    seen[key] = dict(id=i, year=year, model=model, vehicle=f'{year} {model} {trim}'.strip(), price=price, miles=miles, city=city,
                     days=days, title='unknown', pick=False, avoid=False, dealer=flags == 'dealer', note=note, posts=1)
    rows.append(seen[key])
for r in rows:
    if r.pop('posts') > 1:
        r['note'] += ' · 같은 차 2건 게시'
    r.update(DETAILS.pop(r['id'], {}))
assert not DETAILS, DETAILS

for x in d['listings']:
    x['days'] += 5
d['listings'] += rows
d['checkedAt'] = '2026-09-23·28'
d['search']['passes'].append(dict(price='$5,000–$7,999', scanned=342, kept='9/23 이후 새로 올라온 승용차·SUV·밴·픽업 (2026-09-28 조회, 상세 미조회)'))
assert len(rows) == 185 and skipped == dict(not_car=13, before_2008=48, implausible=0, repost=5), (len(rows), skipped)
path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print(f"added {len(rows)}, skipped {skipped}; total {len(d['listings'])}")
