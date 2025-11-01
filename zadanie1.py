liczba_pkt = int(input("Podaj liczbę zdobytych punktów na egzaminie: "))

if liczba_pkt > 80:
    print("Zaliczyłeś egzamin w terminie 0")
elif liczba_pkt >= 50 and liczba_pkt <= 80:
    print("Możesz poprawić wynik swojego egzaminu")
else: #czyli liczba_pkt < 50
    print("Musisz poprawić egzamin")