import json
from random import randint

'''Tämä on pekingin mysteerin mysteerivalitsin. Tällä ohjelmalla
voit arpoa seuraavan pelattavan mysteerin. Onnea matkaan!'''

# ensin avataan lista, jolle on tallennettu pelatut pelit
try:
    with open('luvut.txt', 'r') as filehandle:
        pelatut = json.load(filehandle)
# mikäli listaa ei ole, sellainen luodaan
except IOError:
    pelatut = []

# arvotaan seuraava mysteeri
# jos mysteeri on jo pelattu, arvotaan uusi
while True:
    luku = randint(1, 50)
    if luku not in pelatut:
        pelatut.append(luku)
        print(f'Seuraavaksi pelataan mysteeri numero {luku}!')
        break

# tyhjennetään lista:
# pelatut.clear()

# tallennetaan tiedostoon:
with open('luvut.txt', 'w') as filehandle:
    json.dump(pelatut, filehandle)