import matplotlib.pyplot as plt
def generowanie_histogramu_z_ograniczonym_zakresem(text,zakres):

    text_zmieniony =list(text.lower())
    
    scope = list(zakres.lower())
    litery=[]
    ilosc = []
    for char in text_zmieniony:
        if (char in scope) and (char in text_zmieniony):
            x=text_zmieniony.count(char)
            litery.append(char)
            ilosc.append(x)


    plt.bar(litery, ilosc)
    plt.xlabel("Litry")
    plt.ylabel("Ilosc")
    plt.title("Histogram częstości liter")

    plt.savefig('histogram_z_zakresem.png')

print("Menu: ")
print("1 - Odczyt tekstu z pliku tekstowego")
print("2 - Odczyt tekstu wpisanego z klawiatury")
opcja = int(input("Wybierz opcje z menu: "))

while opcja < 1 or opcja > 2:
    print("Wybrano nieprawidłową opcje !!!")
    opcja = int(input("Wybierz opcje z menu: "))

if (opcja == 1):
    scope=input("Wpisz litery których czestotliwość ma być przedstawiona na histogramie: ")
    with open('tekst.txt', 'r') as file:
        tekst = file.read()

    generowanie_histogramu_z_ograniczonym_zakresem(tekst,scope)

else:
    print("Wprowadź tekst z klawiatury: ")
    tekst = input("Twój tekst: ")
    scope=input("Wpisz litery których czestotliwość ma być przedstawiona na histogramie: ")
    generowanie_histogramu_z_ograniczonym_zakresem(tekst,scope)

print("Operacja została wykonana. Histogram został utworzony")
