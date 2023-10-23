def generowanie_histogramu(text):
    text_zmieniony = ''.join(filter(str.isalpha, text)).lower()

    litery = []
    ilosc = []

    for char in text_zmieniony:
        if char not in litery:
            litery.append(char)