nowa_spolka = "ALR, 113"

with open("notowania_gieldowe.txt", "a") as plik:
    plik.write(f"\n{nowa_spolka}")

with open("notowania_gieldowe.txt", "r") as plik:
    for linia in plik:
        print(linia.strip())