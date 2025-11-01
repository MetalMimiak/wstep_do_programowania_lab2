litera = str(input("Podaj literę: "))

if litera.isupper():
    print("Wprowadzona litera jest duża")
elif litera.islower():
    print("Wprowadzona litera jest mała")
else:
    print("Wprowadzona wartość nie jest literą")