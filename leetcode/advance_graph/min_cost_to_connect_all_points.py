import heapq
from collections import defaultdict
from typing import List

# T: O(n^2)
# S: O(n^2)
# https://leetcode.com/problems/min-cost-to-connect-all-points/
def min_cost_connect_points(points: List[List[int]]) -> int:
    adj_list = defaultdict(list)

    for i in range(len(points)):
        x1, y1 = points[i]
        for j in range(i + 1, len(points)):
            x2, y2 = points[j]
            distance = abs(x1 - x2) + abs(y1 - y2)
            adj_list[i].append([distance, j])
            adj_list[j].append([distance, i])

    visited = set()
    pq = [[0, 0]]

    max_cost = 0
    while len(visited) < len(points):
        cost, node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)
        max_cost += cost

        for neighbor_cost, neighbor_node in adj_list[node]:
            if neighbor_node in visited:
                continue
            heapq.heappush(pq, [neighbor_cost, neighbor_node])

    return max_cost

print(min_cost_connect_points(points = [[0,0],[2,2],[3,10],[5,2],[7,0]])) # 20
print(min_cost_connect_points(points = [[3,12],[-2,5],[-4,1]])) # 18
print(min_cost_connect_points([[23273,-66721],[23463,-42064],[25314,-94622],[-89168,36016],[-41117,44872],[72509,54160],[81319,20155],[13682,75878],[-32279,77441],[-55749,93526],[26833,36993],[52765,62596],[-95713,74010],[-40705,-38617],[56351,-49033],[-84224,-28177],[65788,-15006],[12275,32414],[9631,82997],[-78340,65275],[-35473,-9982],[-54480,-52974],[-49572,-99901],[-15012,68794],[63869,30188],[-97975,-9588],[2444,-80830],[-6606,-89873],[52097,6689],[-86990,-7396],[-14101,19854],[63165,-35456],[77140,2795],[-45442,-71242],[52679,45189],[-73337,26575],[-50026,-43860],[78247,12996],[88194,19997],[17080,-57189],[-50828,-33082],[22098,-70030],[-63267,-54310],[-70507,63783],[-20246,64304],[44148,14648],[-90820,-93182],[20043,-16880],[87685,-13802],[1203,-90329],[-20487,48833],[-3778,-47940],[68840,-17075],[-4110,28332],[-30199,5407],[90664,51546],[-34517,-81568],[26447,-89801],[-21740,35055],[-38856,-56672],[36319,-29947],[77577,70560],[26003,-4980],[12814,-45047],[87658,78060],[-18046,71383],[23053,-74429],[-84072,2092],[35174,148],[-99119,29084],[-59414,19371],[-30990,92270],[72575,14324],[1295,85753],[-25128,-50718],[45677,-39503],[-68304,-66248],[69860,42671],[69797,-90365],[94024,-61283],[45187,-7850],[-92574,51229],[9175,-21785],[44767,-93122],[-29547,-16847],[-24137,38540],[-72809,28643],[-46827,97372],[-21018,-73104],[-60794,-51510],[-27536,-19402],[46997,-62627],[-58564,4124],[19086,-46211],[-24748,-49279],[92596,-90547],[-84704,15249],[51772,25655],[70939,-46335],[25130,-86021],[-31577,32565],[-8556,-42386],[-1519,14862],[-74257,-53657],[85812,-74168],[72793,29701],[99999,13992],[47419,10108],[-2699,37468],[-22634,4487],[-58725,98347],[-98879,45584],[-15035,61931],[18336,-78837],[39333,-52238],[79654,65029],[32292,-1647],[-16612,82132],[-36157,70443],[-39504,-85921],[-4949,-37867],[-758,-64295],[-8428,-40866],[-3589,8189],[89310,19603],[-43670,-55257],[-28296,-28844],[75860,-74973],[-51704,85828],[76678,-510],[-75823,24647],[-31657,83441],[53658,-43479],[-24625,48869],[24250,-98478],[-87136,-34195],[693,18703],[-65516,-20103],[-26829,25138],[-21962,-88478],[33693,41441],[26412,10762],[-1284,34148],[30141,-17729],[-87641,70402],[-78942,-73931],[41903,8824],[74967,70783],[-61472,63085],[66963,34096],[-10015,71836],[-63109,-10110],[66650,69958],[46579,96944],[39270,-64158],[-2631,50184],[56781,-22885],[-99800,-77917],[65712,24006],[9394,30427],[48656,8450],[67424,19220],[2839,-2229],[86576,57830],[67758,22591],[84854,-24252],[54330,218],[-37662,-90269],[-18453,-46656],[-49728,-61877],[51026,-85957],[15316,56517],[-90584,66739],[63312,18529],[-39500,63520],[73392,77135],[-96996,32945],[-90038,-14770],[8847,77836],[44758,-38754],[22699,-72870],[65239,-9659],[-46741,-23577],[29680,75251],[-47726,23552],[-65992,-67996],[-55915,19567],[-24092,-10810],[-71544,33460],[-2676,-54822],[49757,15357],[-58103,58744],[18470,-10344],[-83018,-2653],[-51696,16790],[90919,61990],[13094,87481],[48174,-14799],[-18208,-92927],[-60349,-85843],[-70473,-52159],[-40303,-85394],[-96179,3220],[44803,12094],[1616,-55389],[63639,-90529],[-28894,27447],[27649,91550],[-67007,-49126],[25527,24464],[-72107,13348],[-20009,3250],[-3892,-96523],[-98319,-66071],[6828,90484],[22581,-74800],[80313,37613],[67888,51738],[28293,-37146],[-10231,-876],[44193,-90847],[14665,94950],[33826,32523],[51176,16304],[15999,72186],[28236,-69296],[-44346,75633],[79255,-12192],[21299,13086],[-73719,76278],[61387,-89815],[50634,64333],[8873,-12760],[3162,-94579],[-36499,28463],[41806,77372],[-64063,-92017],[1856,-70061],[36188,-59270],[10811,85229],[42451,49370],[-98057,-67546],[-77967,75115],[50212,18566],[-36616,-17005],[-6656,-69361],[-46847,-10425],[-20927,19792],[-72986,70039],[-13751,90272],[-87598,40939],[-23870,-23818],[44793,-11656],[6791,99984],[-64436,55962],[92227,-6569],[52639,-70260],[-83521,63174],[68228,64864],[-80308,-6384],[90980,-5132],[-82662,17167],[-64497,-6187],[75021,87694],[83304,-57607],[-37454,38989],[-99334,-31479],[2551,-67324],[-90315,74154],[53188,79768],[-72424,13160],[-80584,-77286],[22248,88373],[86121,45193],[-30799,14686],[4004,-32397],[18914,-58242],[76022,58380],[-47749,-85442],[-18268,-18634],[-31875,-59436],[74743,14010],[-62117,-53192],[15283,-68145],[90186,-34934],[-60749,14492],[-65268,-49294],[-64633,27084],[16781,-16044],[-46255,-35068],[-11885,-50213],[-96405,2949],[-29943,-58098],[14633,-37272],[40329,26405],[-22150,80922],[60141,32194],[-5221,-3028],[-19557,65451],[-39712,-45259],[-68502,-43798],[14712,17619],[-84799,-30282],[-80863,-8593],[-48377,73324],[-24851,-20336],[-17506,-19756],[14025,-21604],[18285,-64794],[-18117,45792],[73023,-64144],[-80487,3999],[-74641,22260],[29151,-70121],[20145,-76522],[81723,-16672],[57696,-82852],[-63342,35405],[38216,15057],[-89882,61324],[-10630,-97089],[15588,-42491],[-45856,-89192],[2852,-87081],[53589,-73704],[42458,-31012],[99102,37531],[82008,43893],[-82500,-52199],[-96575,60283],[16836,-33645],[85131,-26134],[-26196,-64755],[33322,-43071],[-9883,-43414],[-11397,-1539],[55888,69112],[36696,57408],[9182,34524],[54390,-2074],[-74469,18212],[-50949,41346],[76767,-4786],[95520,34231],[52028,23155],[-14244,92320],[-9240,15027],[-25749,50540],[-8743,-29372],[18031,57896],[18845,1029],[-6260,63520],[-74064,96109],[12549,26331],[-96091,88392],[-22933,-52492],[25363,21373],[41086,-45217],[-28132,-24418],[-84217,-6333],[46273,-7168],[77816,-54915],[-71475,-21197],[-36400,43490],[99313,54415],[43677,-31017],[35399,74700],[-75727,46878],[29864,6128],[-64064,98754],[71386,-86794],[-47453,-29437],[-83977,-2148],[68840,-94822],[66077,-67885],[-95335,61128],[97618,66159],[-81028,-9346],[17160,-91725],[-80533,69304],[745,-21205],[-64156,9678],[-526,8163],[-37554,-45486],[27148,79928],[-57913,-45821],[14052,49215],[22430,37703],[25387,-92764],[-29872,24554],[-58668,-32],[-45277,36068],[55073,44087],[83506,32548],[15048,11590],[7170,-66195],[70693,2389],[38642,80498],[56993,-86653],[-52679,38437],[44454,-68825],[12249,46393],[-11893,19404],[54826,-90626],[-51578,80051],[-80453,-48225],[27008,93346],[72382,-22841],[78068,-16073],[-74716,96701],[-58174,37645],[-34246,5254],[95531,-2687],[-70251,65477],[32403,62244],[-27786,-1466],[-20619,-38052],[-50914,-12233],[89639,-52069],[70989,59718],[-35597,90742],[88,80187],[-28925,89004],[-69237,92707],[42790,1736],[86641,87255],[96451,-36579],[-61195,-66643],[-13213,42995],[4122,4404],[-71084,-28950],[-59143,13567],[-26866,4827],[-22479,-46171],[-80722,-60624],[87667,40749],[-55862,-47826],[46323,-63662],[-39509,38632],[-19895,-50538],[47342,-88367],[54106,-23253],[-91716,68284],[-46006,30499],[92336,-41974],[75890,-83608],[11202,57278],[20602,46250],[54898,-19999],[23117,-37204],[20441,-19641],[-49826,-74635],[57130,-48331],[-4551,-71360],[-66114,54784],[26034,-13975],[-3948,-85797],[-7743,-95233],[-4326,50879],[-73576,-48290],[74378,-83131],[-17126,24592],[-48845,86264],[73319,75609],[58637,-83654],[309,69668],[-19378,2755],[22209,-5971],[-10584,54511],[-46033,-81390],[-82611,74686],[-60591,47025],[23651,14688],[-22689,-76535],[39546,-91717],[-2098,1936],[-75324,-66581],[-40196,18736],[-85104,68981],[-34220,-3012],[-81252,-85228],[93543,-98773],[-77428,-72651],[-93721,-82702],[-36103,39935],[-6396,12473],[20365,-8887],[44375,63328],[98935,-90204],[81399,-29300],[-43682,-77270],[-80428,-14414],[29340,-54412],[47224,41198],[2111,4949],[-16340,-11528],[-64954,-51711],[12175,-59820],[51465,-40793],[76106,-48342],[54834,-26925],[3028,-97466],[57368,-2699],[-27195,-61549],[28543,3118],[93167,45734],[-65599,92504],[47664,25193],[-2596,30129],[-20517,-3832],[-50910,47352],[-78533,-20624],[-81460,-72717],[-58246,19975],[-50490,-54388],[84589,13610],[43266,16118],[-28908,9581],[-59641,-55579],[59447,-3907],[-71878,-61240],[66386,-4334],[41378,-53601],[-36102,-80974],[77910,-80109],[44963,-98333],[9175,-84441],[27465,-28146],[-94309,-20827],[62565,58367],[-41164,54180],[39729,35123],[56455,-298],[17335,4726],[-66455,-64665],[-46262,79234],[77810,-16977],[-11735,-33854],[17862,-71242],[-25537,76953],[53864,3386],[89280,77242],[99571,43580],[53520,98120],[-39121,-40049],[-10108,-99433],[5662,63277],[-23383,59187],[-45180,21910],[-71012,-99045],[-61109,11301],[32073,14401],[-35202,94754],[-50700,14431],[82418,6652],[91567,-85555],[-21474,-48919],[73275,66652],[39636,-68052],[-68962,90048],[38572,-82838],[80502,-19311],[-85900,90260],[56593,-44172],[-25718,64876],[75194,-91715],[-86300,-14003],[11886,21926],[20848,-55345],[-71999,-81518],[84752,26715],[97348,-92571],[-58634,83565],[89049,-94123],[-83890,18706],[-37731,74554],[-1289,96344],[30551,80451],[28331,-61655],[-7979,88048],[-16023,77915],[49762,15951],[69228,59969],[47050,2279],[58456,-54254],[13239,8727],[56831,1594],[-88624,-41321],[-89412,-85639],[94151,-85212],[81042,-77879],[-54703,-93002],[80022,-7898],[63423,2964],[6706,-50308],[-11466,-17471],[77476,-67793],[4969,-61074],[-96718,1679],[91598,33827],[-50587,28706],[65230,-11028],[-22965,-26046],[-99448,54844],[-60835,99677],[81203,-79926],[-46709,-41206],[97096,49748],[-31335,-33123],[93681,-31712],[-19236,61582],[79854,-74263],[12488,45006],[-40224,-56562],[-39865,61254],[47661,43152],[-80479,97562],[87831,-33805],[53508,77507],[39698,-61908],[85576,-24491],[-45043,-83844],[-34741,70222],[62307,-27225],[-5696,71333],[-50361,-96716],[68165,-11056],[9792,-86509],[-51881,-55887],[41597,-39795],[-88149,99949],[-90623,-80115],[64279,-69076],[-83553,66878],[74349,50584],[-34028,-50730],[-90777,49716],[33210,60393],[13892,-27447],[32879,65165],[-1779,-76437],[78013,-42200],[87783,40005],[2614,41403],[63946,-80983],[56407,-53816],[-87004,91927],[29326,24296],[-50606,-10131],[24524,-37509],[-97468,-639],[-46240,72446],[-84128,552],[-16993,69058],[-45636,-31098],[-36538,21974],[-5490,6401],[45277,-7596],[34579,88247],[65338,-63736],[-63612,-19807],[4172,-22948],[73230,-18890],[63356,76157],[-57420,83635],[-84787,22434],[-72125,-51246],[-29401,-52047],[-18270,-13663],[90415,50528],[14298,-20939],[-83302,2466],[-10461,-24459],[-45672,52714],[63516,-35490],[5920,3764],[-67652,-41376],[95890,44762],[-25872,-95245],[-47552,12699],[-63634,24814],[3245,12264],[-83914,-21920],[3502,49628],[90181,24662],[-83574,-38123],[-68247,-66699],[90457,-63408],[-76592,-63545],[65408,27463],[-85624,59689],[37077,73105],[69814,-40751],[-72455,7619],[10582,76415],[-39305,83602],[-44008,-66523],[17012,-51331],[-34733,26928],[40854,17239]])) # 4278850