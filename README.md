# Projekt numer 1 z informatyki.
 Wykonali: Piotr Zawistowski, Julia Surała, Maja Wiśniewska

## CEL PROJEKTU
  * 

## CO ZAWIERA NASZ PROGRAM
  * 

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
  * 
  
## WYMAGANIA, KTÓRE TRZEBA SPEŁNIAĆ, ŻEBY PROGRAM DZIAŁAŁ NA DANYM KOMPUTERZE
  * Program Python w wersji...
  * Zainstalowane biblioteki: numpy, math, argparse
 
## SYSTEM OPERACYJNY 
  * 
 
## JAK UŻYWAĆ PROGRAMU 
  * 
  
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
- Przeliczanie współrzędnych kartezjańskich X, Y, Z na współrzędne geodezyjne B, L, H. Jest to  sposób opisu położenia geodezyjnego punktu na Ziemi. 
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
- Transformacja BLH na XYZ to proces przekształcania pozycji punktu na Ziemi z układu geodezyjnego BLH, a układ kartezjański XYZ. 
- Aby dokonać przekształcenia XYZ na BLH, należy zastosować poniższe etapy:
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
 
 ### Transformacja BL -> 2000
 
 ### Transformacja BL -> 1992
 

 
 
