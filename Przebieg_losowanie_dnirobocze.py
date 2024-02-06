#########################################################################################
#########################################################################################

#PL
#Program pozwala użytkownikowi na podanie aktualnego przebiegu pojazdu 
#oraz rok i miesiac zakupu
#Program losuje ile kilometrow auto musialo pokonac w dni robocze od tego czasu
#oraz sporzadza liste z tymi wartosciami

#ENG
#The program allows the user to enter the current mileage of the vehicle 
#and the year and month of purchase
#The program draws at random how many kilometres the car must have travelled on working days since then
#and produces a list with these values


#########################################################################################
#########################################################################################
#########################################################################################
import csv
import random
from datetime import datetime, timedelta

def licz_dni_robocze(miesiac, rok):
    dzien = datetime(rok, miesiac, 1)
    dni_robocze = 0

    while dzien.month == miesiac:
        if dzien.weekday() < 5:  # 0-4 to poniedziałek-piątek
            dni_robocze += 1
        dzien += timedelta(days=1)

    return dni_robocze

def losuj_liczby(liczba_liczb, suma_docelowa):
    try:

        # Sprawdzenie, czy suma_docelowa jest osiągalna
        if suma_docelowa < liczba_liczb * 12 or suma_docelowa > liczba_liczb * 400:
            raise ValueError("Nie można uzyskać sumy docelowej dla podanych warunków.")
        
        #liczby = 0
        if suma_docelowa > 2500:
            # Losowanie liczb
            liczby = random.sample(range(12, 401), liczba_liczb)
        else:
             # Losowanie liczb
            liczby = random.sample(range(12, 201), liczba_liczb)           
        
        # Dopóki suma nie jest równa sumie docelowej, losuj ponownie
        while sum(liczby) < suma_docelowa - 500:
            if suma_docelowa > 2500:
                # Losowanie liczb
                liczby = random.sample(range(12, 401), liczba_liczb)
            else:
                # Losowanie liczb
                liczby = random.sample(range(12, 201), liczba_liczb)    
        
        suma_liczb = sum(liczby)
        #print(suma_docelowa)
        #print(suma_liczb)
        i = 1
        #print(liczby[liczba_liczb-i])

        #Pętla
        while suma_docelowa != suma_liczb:
            suma_liczb = suma_liczb - liczby[liczba_liczb-i]
            if suma_docelowa < suma_liczb:
                liczby[liczba_liczb-i] = 0
                i = i + 1
            if suma_docelowa > suma_liczb:
                liczby[liczba_liczb-i] = suma_docelowa - suma_liczb
                break

        print ("Przebieg = {przebieg}, Wylosowany przebieg - {suma}".format(przebieg = suma_docelowa,suma = sum(liczby)) )
        
        #Przemieszanie wartości w liście liczby
        random.shuffle(liczby)
        return liczby
    except ValueError as e:
        print(f"Błąd: {e}")
        return None
    
def wypisz_miesiace_do_csv(od_rok, od_miesiac, Wybor_przebieg):
    obecna_data = datetime.now()
    data_poczatkowa = datetime(od_rok, od_miesiac, 1)

    with open('wyniki.csv', mode='w', newline='') as plik_csv:
        writer = csv.writer(plik_csv)
        writer.writerow(['Rok', 'Miesiąc', 'Ilość dni roboczych', 'Przebieg', 'Przebieg na dzień'])

        while data_poczatkowa < obecna_data:
            rok_miesiac = data_poczatkowa.strftime("%Y-%m")
            rok, miesiac = map(int, rok_miesiac.split('-'))
            
            ilosc_dni_roboczych = licz_dni_robocze(miesiac, rok)
            try:
                if Wybor_przebieg == 1:
                    # Pytanie użytkownika o liczbę i sumę docelową
                    suma_docelowa = int(input("Podaj sumę docelową (od 216 do 8400): "))
                else:
                    # Pytanie użytkownika o liczbę i sumę docelową
                    suma_docelowa = ilosc_dni_roboczych * 200
                # Wywołanie funkcji losującej
                wynik = losuj_liczby(ilosc_dni_roboczych, suma_docelowa)

                # Wyświetlenie wyniku
                #if wynik:
                #    print("Wylosowane liczby:", wynik)
            except ValueError:
                print("Błąd: Wprowadź poprawne liczby.")
            writer.writerow([rok, miesiac, ilosc_dni_roboczych,suma_docelowa, wynik])

            if data_poczatkowa.month == 12:
                data_poczatkowa = datetime(data_poczatkowa.year + 1, 1, 1)
            else:
                data_poczatkowa += timedelta(days=30)



# Pobierz dane od użytkownika
od_rok = int(input("Podaj rok początkowy: "))
od_miesiac = int(input("Podaj miesiąc początkowy: "))
Wybor_przebieg = int(input("Czy chcesz sam wpisać przebieg na każdy miesiąc? (Tak - 1, Nie - 0): "))

# Wywołaj funkcję
wypisz_miesiace_do_csv(od_rok, od_miesiac,Wybor_przebieg)





