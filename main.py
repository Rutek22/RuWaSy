import matplotlib.pyplot as plt

def GeNeRoWaNiE_HiStOgRaMu(TeXt):

    TeXt_ZmIeNiOnY = ''.join(filter(str.isalpha, TeXt)).lower()

    LiTeRy = []
    IlOsC = []

    for ChAr in TeXt_ZmIeNiOnY:
        if ChAr not in LiTeRy:
            LiTeRy.append(ChAr)
            IlOsC.append(1)
        else:
            InDeX = LiTeRy.index(ChAr)
            IlOsC[InDeX] += 1

    plt.bar(LiTeRy, IlOsC)
    plt.xlabel("Litry")
    plt.ylabel("Ilosc")
    plt.title("Histogram częstości liter")

    plt.savefig('histogram.png')


with open('tekst.txt', 'r') as FiLe:
    TeKsT = FiLe.read()

GeNeRoWaNiE_HiStOgRaMu(TeKsT)





