import matplotlib.pyplot as plt


def GeNeRoWaNiE_HiStOgRaMu_Z_oGrAnIcZoNyM_zAkReSeM(TeXt, zAkReS):
    TeXt_ZmIeNiOnY = list(TeXt.lower())

    ScOpE = list(zAkReS.lower())
    LiTeRy = []
    IlOsC = []
    for ChAr in TeXt_ZmIeNiOnY:
        if (ChAr in ScOpE) and (ChAr in TeXt_ZmIeNiOnY):
            x = TeXt_ZmIeNiOnY.count(ChAr)
            LiTeRy.append(ChAr)
            IlOsC.append(x)

    plt.bar(LiTeRy, IlOsC)
    plt.xlabel("Litry")
    plt.ylabel("Ilosc")
    plt.title("Histogram częstości liter")

    plt.savefig('histogram_z_zakresem.png')


print("Menu: ")
print("1 - Odczyt tekstu z pliku tekstowego")
print("2 - Odczyt tekstu wpisanego z klawiatury")
OpCjA = int(input("Wybierz opcje z menu: "))

while OpCjA < 1 or OpCjA > 2:
    print("Wybrano nieprawidłową opcje !!!")
    OpCjA = int(input("Wybierz opcje z menu: "))

if (OpCjA == 1):
    ScOpE = input("Wpisz litery których czestotliwość ma być przedstawiona na histogramie: ")
    with open('tekst.txt', 'r') as file:
        TeKsT = file.read()

    GeNeRoWaNiE_HiStOgRaMu_Z_oGrAnIcZoNyM_zAkReSeM(TeKsT, ScOpE)

else:
    print("Wprowadź tekst z klawiatury: ")
    TeKsT = input("Twój tekst: ")
    ScOpE = input("Wpisz litery których czestotliwość ma być przedstawiona na histogramie: ")
    GeNeRoWaNiE_HiStOgRaMu_Z_oGrAnIcZoNyM_zAkReSeM(TeKsT, ScOpE)

print("Operacja została wykonana. Histogram został utworzony")

