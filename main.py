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
def generowanie_histogramu_z_ograniczonym_zakresem(text,zakres):

    text_zmieniony =list(text)

    scope = list(zakres)
    litery=[]
    ilosc = []
    for char in scope:
        litery.append(char)
        ilosc.append(1)
    for char in text_zmieniony:
        if char in litery:
            index = litery.index(char)
            ilosc[index] += 1

    plt.bar(litery, ilosc)
    plt.xlabel("Litry")
    plt.ylabel("Ilosc")
    plt.title("Histogram częstości liter")

    plt.savefig('histogram_z_zakresem.png')



with open('tekst.txt', 'r') as file:
   tekst = file.read()
wpisany_tekst=input("Wpisz tekst: ")
scope=input("Wpisz litery których czestotliwość ma być przedstawiona na histogramie: ")
generowanie_histogramu_z_ograniczonym_zakresem(wpisany_tekst,scope)
