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
  * BLH to układ współrzędnych geodezyjnych, w którym:
     * długość geograficzna (B) to kąt między płaszczyzną południka zielonego (czyli płaszczyzną zawierającą oś obrotu Ziemi) a płaszczyzną, która przechodzi przez dany punkt oraz przez południk zerowy;
     * szerokość geograficzna (L) to kąt między płaszczyzną równika a płaszczyzną zawierającą dany punkt;
     * wysokość geoidy (H) to odległość punktu od geoidy (powierzchni odniesienia).



## TRANSFORMACJE
 ### Transformacja XYZ -> BLH
 - Przeliczanie współrzędnych kartezjańskich X, Y, Z na współrzędne geodezyjne B, L, H. Jest to  sposób opisu położenia geodezyjnego punktu na Ziemi. 
 - Aby dokonać przekształcenia XYZ na BLH, należy zastosować poniższe etapy:
    1. Obliczenie długości i szerokości geogaficznej: 
   '''
    $ B=atan(Y/X)
    $ L=atan(Z/sqrt(X^2 +Y^2))
   ''' 
    2. Wyznaczenie punktu do punktu osi obrotu Ziemi:
    '''
    $ R=sqrt(X^2 + Y^2 + Z^2)
    '''
    3. 
 
 ### Transformacja BLH -> XYZ
 
 ### Transformacja XYZ -> NEU
 
 ### Transformacja BL -> 2000
 
 ### Transformacja BL -> 1992
 
 

 
 
