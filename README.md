# Projekt numer 1 z informatyki.
 Wykonali: Piotr Zawistowski, Julia Surała, Maja Wiśniewska

## CEL PROJEKTU
  * Utworzenie programu do transformacji współrzędnych między układami.

## SPIS TREŚCI 
 * Do czego służy program i jaką funkcjonalność oferuje
 * Jakie wymagania trzeba spełnić, by program działał na danym komputerze 
 * Dla jakiego systemu operacyjnego został napisany program
 * Jak używać programu
 * Przykładowe wywołania programu wraz z wynikami 
 * Błędy i nietypowe zachowania programu, które nie zostały jeszcze naprawione
 
## Do czego służy program i jaką funkcjonalność oferuje:
  - Program do zamiany współrzędnych między układami oraz transformacji służy do konwertowania punktów opisanych w jednym układzie odniesienia na punkty opisane w innym układzie odniesienia.

  - Program zawiera następujące funkcje na zamiany współrzędnych między układami oraz transformacje: z układu geocentrycznego do geodezyjnego (hirvonen), z układu geodezyjnego do geocentrycznego (flh2XYZ), z układu geocentrycznego do topocentrycznego (xyz2neu), oraz transformacje fi i lam do układów 2000 i 1992. Transformacji można dokonać wykorzystując elipsoidy: GRS80, WGS84, Krasowski. Aby dokonać transformacji na odpowidniej elipsoidze należy wpisać jej nazwę w odpowiednim miejscu w skrypcie. 

  
## Jakie wymagania trzeba spełnić, by program działał na danym komputerze: 

  - Program Python został napisany w wersji 3.9 a więc dla tej wersji będzie działał, biblioteka numpy, która jest wykorzystana jest dostępna od wersji pythona 1.4, a więc dla straszych wersji kod nie będzie działał.
   
  - Zainstalowane biblioteki: numpy, argparse np. przy pomocy menadżera pakietów pip.
 
## Dla jakiego systemu operacyjnego został napisany program: 
Kod Pythona będzie obowiązywał na wielu systemach operacyjnych (m.in. Windows, Linuks, Mac), platformy te obsługują Pythona w różnych wersjach, a więc najważniesze jest aby skontrolować czy dana wymagana biblioteka jest zainstalowana.
 
## Jak używać programu: 
Posługując się git bash należy otorzyć folder (w którym zrobiliśmy skrypt oraz znajdują się dane), po wpisaniu 'python nazwaskryptu.py -h' ukaże się wskazówka, w jaki sposób zamieścić plik z danymi oraz jakie są dostępne transformacje. Jeżeli wpiszę się nazwę transformacji, której nie ma lub popełni się błąd w nazwie, ukaże się komunikat aby skorzystać z jednej z transformacji, których nazwy się wyświetlą. 
Dane w pliku do wczytania odzielamy przecinkami, odpowiedni w kolejności: dla hirvonena: x,y,z; flh2XYZ: f,l,h; xyz2neu: x,y,z,x0,y0,z0,f,l,h; u2000: f,l; u1992: f,l.
Aby skorzystać z wybranej przez nas transformacji należy wpisać: python nazwaskryptu.py 'wybrana transformacja' 'plik z danymi txt' 'plik wyjściowy (np. txt)'.
  
## Przykładowe wywołania programu wraz z wynikami oraz komendami wywołania:
Na elipsoidzie wgs84:
  - hirvonen: dane wejściowe z pliku txt (x,y,z)[m]:  
3745115.219,1668527.508,4869859.368  
3738500.415,1672151.169,4873749.983  
3731878.893,1675771.950,4877631.999  
3726355.841,1678787.064,4880860.434    
komenda: ' python skrypt.py hirvonen dane_xyz.txt wyniki_hirvonen.txt '  
wyniki z powstałego pliku (f,l,h)[rad][m]:  
0.8743248033899605,0.4191229564769907,360.00001946184784  
0.8752656281942796,0.42058849040821594,420.0001845471561  
0.8762053804053673,0.42205732114026634,479.9998778253794  
0.8769876835154149,0.42328387194116407,529.9997042985633  

  - flh2XYZ: dane wejściowe z pliku txt (f,l,h)[rad][m]:  
0.90759684600,0.27934967325,274.154  
0.90292450888,0.27184674487,277.635  
0.90759462173,0.27934939683,175.337  
0.90569821555,0.27595518859,176.862  
komenda: ' python skrypt.py flh2XYZ dane_flh.txt wyniki_flh.txt '  
wyniki z powstałego pliku (x,y,z)[m]:  
3782459.9998788894,1084999.999984002,5003120.000011584  
3813066.1506870356,1062882.0896164104,4984729.575443349  
3782412.5636472907,1084985.2613198122,5003033.399512065  
3795234.3825005945,1074734.9385740883,4995582.386563064  

  - u2000 i u1992: dane wejściowe z pliku txt (f,l)[rad]:  
0.90759684600,0.27934967326  
0.90292450888,0.27184674487  
0.90984841548,0.27958488448  
0.90358589949,0.27995262262    
komenda: ' python skrypt.py u2000 dane_u2000_u1992.txt  wyniki_2000.txt '  
         ' python skrypt.py u1992 dane_u2000_u1992.txt  wyniki_1992.txt '  
wyniki z powstałych plików (x2000,y2000)[m], (x1992,y1992)[m]:  
u2000:  
5763540.701333446,5569051.247375576  
5733436.160445737,5539766.844731892  
5777906.183646557,5569775.301797976  
5738007.15574452,5571788.684727578  
u1992:  
463705.50410325825,294520.884347805  
435255.92246309575,263629.6249726071  
478006.9485056922,296034.4053810106  
438064.4873036621,295851.7827999486  

Na elipsoidze grs80:
Wszystkie dane wejściowe są takie same jak na elipsoidzie wgs84
  - hirvonen:  
komenda: 'python skrypt.py hirvonen dane_xyz.txt grs80_hirvonen.txt'  
wyniki z powstałego pliku (f,l,h)[rad][m]:  
0.874324803406157,0.4191229564769907,360.0000810595229  
0.8752656282104705,0.42058849040821594,420.00024624262005  
0.8762053804215524,0.42205732114026634,479.9999396177009  
0.8769876835315953,0.42328387194116407,529.9997661709785  

  - flh2XYZ:  
komenda: 'python skrypt.py flh2XYZ dane_flh.txt grs80_flh2XYZ.txt'  
wyniki z powstałego pliku (x,y,z)[m]:  
3782459.999917521,1084999.9999950835,5003119.9998976905  
3813066.1507256944,1062882.0896271865,4984729.5753295  
3782412.563685922,1084985.2613308935,5003033.39939817  
3795234.382539241,1074734.9385850322,4995582.386449187  

  - u2000 i u1992:  
komenda: 'python skrypt.py u2000 dane_u2000_u1992.txt  grs80_2000.txt'  
python 'skrypt.py u1992 dane_u2000_u1992.txt  grs80_1992.txt'  
wyniki z powstałych plików (x2000,y2000)[m], (x1992,y1992)[m]:  
u2000:  
5763540.701209578,5569051.247376281  
5733436.160321937,5539766.844732296  
5777906.183522654,5569775.301798691  
5738007.155620714,5571788.684728308  
u1992:  
463705.50397950504,294520.88434570585  
435255.9223394282,263629.62497020984  
478006.9483819045,296034.40537891956  
438064.48717996944,295851.7827978761  

Na elipsoidze Krasowskiego:
 - hirvonen:  
komenda: 'python skrypt.py hirvonen dane_xyz.txt kr_hirvonen.txt'  
wyniki z powstałego pliku (f,l,h)[rad][m]:  
0.8743243854405441,0.4191229564769907,250.41072719730437  
0.8752652103920222,0.42058849040821594,310.40838652383536  
0.8762049627515784,0.42205732114026634,370.4055777443573  
0.8769872659863452,0.42328387194116407,420.4033220047131  

  - flh2XYZ:  
komenda: 'python skrypt.py flh2XYZ dane_flh.txt kr_flh2XYZ.txt'  
wyniki z powstałego pliku (x,y,z)[m]:  
3782522.914652955,1085018.047109381,5003208.0457295915  
3813129.5828701165,1062899.7711694278,4984817.308407567  
3782475.478608956,1085003.3084801827,5003121.445081654  
3795297.514095697,1074752.8161869433,4995670.305429225  

  - Wyniki zostały skontrolowane na podstawie funkcji wykorzystywanych na przedmiocie Geodezja Wyższa z semsetru 3.
  
  - xyz2neu (na elipsoidzie wgs84): dane wejściowe z pliku txt (x,y,z,x0,y0,z0,f,l,h)[m][rad]:   3782460.000,1085000.000,5003120.000,3813144.749,1062905.755,4984836.387,0.90759684600,0.27934967325,274.154   3882460.000,1285000.000,5503120.000,3913144.750,4892905.769,4989162.387,0.90499949444,0.27151967324,254.155   4082460.000,1585000.000,5403120.000,3713144.751,4982905.748,4484810.387,0.90559498449,0.21849884415,192.156   3716910.000,1048400.000,5003120.000,3813144.736,1452905.765,4984848.387,0.99298191188,0.28151511215,126.154  
wyniki z powstałego pliku (n,e,u):  
-29698.484581531888,-8940.87415696065,6365140.022492256  
3467498.597825916,-1080891.8724055937,6153415.4626685595  
3397171.358170043,-841861.1334792367,6855538.382545167  
361847.5382611249,-161970.16071317875,6266697.91499167  

## Błędy i nietypowe zachowania programu, które nie zostały jeszcze naprawione:
Zamiana układu geocentrycznego na topocentryczny (xyz2neu) budzi lekkie wątpliwości co do poprawności użycia wzoru, jak i uzyskanych wyników, które jako jedyne nie zostały skontrolowane.  
   

## UKŁADY WSPÓŁRZĘDNYCH WYKORZYSTANE W ZADANIU
  * Układ współrzędnyuch BLH to układ współrzędnych geodezyjnych, w którym:
     - długość geograficzna (B) to kąt między płaszczyzną południka zielonego (czyli płaszczyzną zawierającą oś obrotu Ziemi) a płaszczyzną, która przechodzi przez dany punkt oraz przez południk zerowy;
     - szerokość geograficzna (L) to kąt między płaszczyzną równika a płaszczyzną zawierającą dany punkt;
     - wysokość geoidy (H) to odległość punktu od geoidy (powierzchni odniesienia).
     
  * Układ współrzędnych XYZ to system, w którym położenie punktu w przestrzeni opisywane jest trzema wartościami: X, Y i Z. 
     - oś X jest określana przez przecięcie południka zerowego z równikiem, 
     - oś Y jest prostopadła do osi X i wskazuje kierunek wschodni, 
     - oś Z jest prostopadła do płaszczyzny utworzonej przez osie X i Y i wskazuje kierunek północny. 
     Dzięki współrzędnym X, Y i Z w układzie XYZ możliwe jest jednoznaczne określenie położenia punktu w przestrzeni.
     
  * Układ współrzędnych NEU to układ kartezjański. W tym układzie współrzędne są określane jako N, E i U. 
     - oś N wskazuje kierunek północny, 
     - oś E wskazuje kierunek wschodni,  
     - oś U wskazuje kierunek wertykalny - wysokość (odpowiadający kierunkowi pionowemu).
     
  * Układ współrzędnych 2000 to globalny układ odniesienia wykorzystywany w pomiarach geodezyjnych, oparty na ITRS. Układ ten jest związany z modelem geocentrycznym Ziemi, a jego początkiem jest środek masy Ziemi. Współrzędne w układzie 2000 określają położenie punktu na powierzchni Ziemi w trzech wymiarach: długość geocentryczna, szerokość geocentryczna oraz wysokość geocentryczna, wyrażone w radianach lub stopniach. 
  
  * Układ współrzędnych 1992 




 
 
