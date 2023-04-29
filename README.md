# Projekt numer 1 z informatyki.
 Wykonali: Piotr Zawistowski, Julia Surała, Maja Wiśniewska

## CEL PROJEKTU
  * Utworzenie programu do transformacji współrzędnych między układami.

## CO ZAWIERA NASZ PROGRAM
  * Program zawiera następujące funkcje na zamiany współrzędnych między układami oraz transformacje: z układu geocentrycznego do geodezyjnego (hirvonen), z układu geodezyjnego do geocentrycznego (flh2XYZ), z układu geocentrycznego do topocentrycznego (xyz2neu), oraz transformacje fi i lam do układów 2000 i 1992. Transformacji można dokonać wykorzystując elipsoidy: GRS80, WGS84, Krasowski. Aby dokonać transformacji na odpowidniej elipsoidze należy wpisać jej nazwę w odpowiednim miejscu w skrypcie. 

## 


## SPIS TREŚCI 
 * do czego służy program i jaką funkcjonalność oferuje (transformacja XYZ -> BLH, transformacja BLH -> XYZ, jakie elipsidy są obsługiwane, ...)
 * jakie wymagania trzeba spełnić, by program działał na danym komputerze (np. trzeba mieć pythona w wesji takiej-a-takiej, 
      zainstalowaną bibliotekę taką-a-taką, ...)
 * dla jakiego systemu operacyjnego został napisany program 
 * jak go używać wraz z kilkoma przykładami wywołań obrazującymi jak z niego korzystać (w tym opis struktury danych wejściowych i wyjściowych) 
      oraz rezultatami tych wywołań (przykładowe wywołania powinny za input brać plik z przykładowymi danymi)
 * znane błędy i nietypowe zachowania programu, które nie zostały jeszcze naprawione


## DO CZEGO SŁUŻY PROGRAM?
  * Program do zamiany współrzędnych między układami oraz transformacji służy do konwertowania punktów opisanych w jednym układzie odniesienia na punkty opisane w innym układzie odniesienia.
  * Program ten pozwala przeliczać współrzędne geodezyjne, takie jak szerokość, długość geograficzna wraz z wysokością pomiędzy różnymi układami odniesienia geodezyjnego: WGS84, GRS80, Krasowski.
  
## WYMAGANIA, KTÓRE TRZEBA SPEŁNIAĆ, ŻEBY PROGRAM DZIAŁAŁ NA DANYM KOMPUTERZE
  * Program Python w wersji odpowiedniej dla danego systemu operacyjnego.
  * Zainstalowane biblioteki:  math, numpy, argparse np. przy pomocy menadżera pakietów pip.
 
## SYSTEM OPERACYJNY 
  * 
 
## JAK UŻYWAĆ PROGRAMU 
Posługując się git bash należy otorzyć nasz folder (w którym zrobiliśmy skrypt oraz znajdują się dane), po wpisaniu 'python nazwaskryptu.py -h' ukaże się wskazówka, w jaki sposób zamiścić plik z danymi oraz jakie są dostępne transformacje.
Dane w pliku do wczytania odzielamy przecinkami, odpowiedni w kolejności: dla hirvonena: x,y,z; flh2XYZ: f,l,h; xyz2neu: x,y,z,x0,y0,z0,f,l; h u2000: f,l; u1992: f,l.
Aby skorzystać z wybranej przez nas transformacji należy wpisać: python nazwaskryptu.py 'wybrana transformacja' 'plik z danymi txt' 'plik wyjściowy (np. txt)'. 
  
## KORZYSTANIE Z PROGRAMU 
  * 

## ZNANE BŁĘDY I NIETYPOWE ZACHOWANIA, KTÓRE NIE ZOSTAŁY JESZCZE NAPRAWIONE
  * 

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


## TRANSFORMACJE
### Transformacja XYZ -> BLH
- Program realizujący transformację XYZ -> BLH służy do przeliczania współrzędnych geodezyjnych  punktu na Ziemi z jego współrzędnych kartezjańskich (XYZ). Oferuje funkcjonalność umożliwiającą dokładne określenie położenia punktu w przestrzeni. Program umożliwia wprowadzenie danych w formacie XYZ i przeliczenie ich na wartości BLH, przy użyciu odpowiednich wzorów. 
- Aby dokonać przekształcenia XYZ na BLH, należy zastosować poniższe etapy:
 1. Obliczenie długości i szerokości geogaficznej: 
   ```
     B=atan(Y/X)
     L=atan(Z/sqrt(X^2 +Y^2))
   ```
 2. Wyznaczenie punktu do punktu osi obrotu Ziemi:
    ```
     R=sqrt(X^2 + Y^2 + Z^2)
    ```
 3. Obliczenie wysokości geoidy, obliczając różnicę pomiędzy odległością od osi obrotu Ziemi,       a odległością od punktu do geoidy (N):
    ```
    a = 6378137.0 [m] (promień równika Ziemi)
    b = 6356752.3142 [m] (promień biegunowy Ziemi)
    e^2 = (a^2 - b^2) / a^2 (kwadrat pierwszego spłaszczenia Ziemi)
    N = a / sqrt(1 - e^2 * sin(B)^2) (promień krzywizny normalnej do powierzchni geoidy)
    H = R - N
    ```
- Po dokonaniu przekształcenia współrzędnych z układu kartezjańskiego XYZ na układ geodezyjny BLH, otrzymujemy szukane wartości.
 
### Transformacja BLH -> XYZ
- Program służący do transformacji BLH na XYZ umożliwia przeliczanie współrzędnych geograficznych BLH na współrzędne kartezjańskie w układzie XYZ. Dzięki temu programowi możliwe jest łatwe i precyzyjne określenie położenia punktu na Ziemi w przestrzeni kartezjańskiej. Program ten oferuje funkcjonalność przeliczania współrzędnych BLH na XYZ na podstawie podanych przez użytkownika parametrów geometrycznych Ziemi (promienia równika, promienia biegunowego, pierwszego i drugiego spłaszczenia Ziemi).   
- Aby dokonać przekształceniaBLH na XYZ, należy zastosować poniższe etapy:
1. Obliczenie promienia krzywizny normalnej do powierzchni geoidy (N) na podstawie wartości długości geograficznej
  ```
  a = 6378137.0 [m] (promień równika Ziemi)
  b = 6356752.3142 [m] (promień biegunowy Ziemi)
  e^2 = (a^2 - b^2) / a^2 (kwadrat pierwszego spłaszczenia Ziemi)
  N = a / sqrt(1 - e^2 * sin(B)^2) (promień krzywizny normalnej do powierzchni geoidy)
  ```
2. Obliczenie współrzędnych X, Y i Z punktu na Ziemi na podstawie znanych wartości B, L, H:
  ```
  X = (N + H) * cos(B) * cos(L)
  Y = (N + H) * cos(B) * sin(L)
  Z = (N * (1 - e^2) + H) * sin(B)
  ```
- Wynikiem przekształcenia BLH na XYZ są współrzędne punktu na Ziemi w układzie kartezjańskim XYZ, które opisują jego położenie w przestrzeni trójwymiarowej.

### Transformacja XYZ -> NEU
- Program do transformacji współrzędnych XYZ na NEU pozwala na przeliczenie położenia punktu z układu kartezjańskiego na układ lokalny (północ-wschód-wysokość). Funkcjonalność programu polega na przeliczeniu wartości współrzędnych punktu z układu XYZ na odpowiadające im wartości współrzędnych w układzie NEU. Dzięki temu, użytkownik programu może łatwo i precyzyjnie określić położenie punktu na mapie lub w terenie.
- Aby dokonać przekształcenia XYZ na NEU, należy zastosować poniższe etapy:
1. Przekształcenie współrzędnych XYZ na BLH.
2. Wyznaczenie współrzędnych punktu odniesienia (N, E, U) w układzie NEU.
```
N = -sin(B) * cos(L) * X - sin(B) * sin(L) * Y + cos(B) * Z
E = -sin(L) * X + cos(L) * Y
U = cos(B) * cos(L) * X + cos(B) * sin(L) * Y + sin(B) * Z
```
3. Odejmowanie współrzędnych punktu odniesienia (N, E, U) od współrzędnych punktu, którego chcemy przekształcić (X, Y, Z), uzyskując różnicę dX, dY, dZ.
```
!!!WZORY!!!!
```
4. Wykonanie obrotów układu XYZ tak, aby oś Z była skierowana w kierunku pionu geodezyjnego punktu odniesienia.
```
!!!WZORY!!!!
```
5. Wykonanie przekształcenia liniowego macierzowego, aby uzyskać współrzędne NEU z różnicy dX, dY, dZ.
```
!!!WZORY!!!!
```
6. Wynikiem są współrzędne N, E, U punktu, którego przekształcenie wykonaliśmy.
- Wartości N, E i U są wyrażane w tych samych jednostkach co X, Y i Z. Przekształcenie to jest wykorzystywane do określania położenia punktu na powierzchni Ziemi w lokalnym układzie współrzędnych NEU.

### Transformacja BL -> 2000
-  Program do transformacji BL na układ współrzędnych 2000 służy do przeliczania współrzędnych geograficznych na współrzędne w układzie 2000. Transformacja ta jest często stosowana, ponieważ pozwala na dokładne określenie położenia punktu na Ziemi z uwzględnieniem zmiany układu odniesienia. Funkcjonalność programu polega na przeliczeniu współrzędnych BL na współrzędne XYZ w układzie WGS84, a następnie na przeliczeniu współrzędnych XYZ z WGS84 na współrzędne XYZ w układzie 2000. Wynikiem działania programu jest para liczb reprezentujących długość i szerokość geograficzną punktu w układzie 2000 oraz jego wysokość nad elipsoidą w tym samym układzie. 
 
### Transformacja BL -> 1992
- Program do transformacji współrzędnych BL na układ 1992 służy do przeliczania współrzędnych geograficznych pomiędzy różnymi układami odniesienia. W tym przypadku, program dokonuje przekształcenia z układu BL na układ 1992, co pozwala na jednoznaczne określenie położenia punktu na powierzchni Ziemi z większą dokładnością i precyzją. Funkcjonalność programu polega na wprowadzeniu wartości współrzędnych geograficznych w układzie BL oraz wyborze docelowego układu współrzędnych tj. 1992. Program przelicza podane współrzędne na odpowiednie wartości w wybranym układzie i wyświetla wynik. W ten sposób użytkownik może łatwo i szybko dokonać przekształcenia współrzędnych geograficznych z jednego układu na inny.

 
 
