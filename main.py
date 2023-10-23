import matplotlib.pyplot as plt

def generowanie_histogramu(text):

    text_zmieniony = ''.join(filter(str.isalpha, text)).lower()

    litery = []
    ilosc = []

    for char in text_zmieniony:
        if char not in litery:
            litery.append(char)
            ilosc.append(1)
        else:
            index = litery.index(char)
            ilosc[index] += 1

    plt.bar(litery, ilosc)
    plt.xlabel("Litry")
    plt.ylabel("Ilosc")
    plt.title("Histogram częstości liter")

    plt.savefig('histogram.png')


print("Menu: ")
print("1 - Odczyt tekstu z pliku tekstowego")
print("2 - Odczyt tekstu wpisanego z klawiatury")
opcja = int(input("Wybierz opcje z menu: "))

while (opcja != 1) | (opcja != 2):
    print("Wybrano nieprawidłową opcje !!!")
    opcja = int(input("Wybierz opcje z menu: "))

if (opcja == 1):
    with open('tekst.txt', 'r') as file:
        tekst = file.read()

    generowanie_histogramu(tekst)

else:
    print("Wprowadź tekst z klawiatury: ")
    tekst = input("Twój tekst: ")
    generowanie_histogramu(tekst)

print("Operacja została wykonana. Histogram został utworzony")
