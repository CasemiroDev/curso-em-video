champions = ("Sena","Cantona","Ronaldinho","Pelé","Cafú","Rashford","Maradona","Neymar","Messi","Shaw","De Gea","Casemiro","Vini Malvadeza","Benzema","Luke","Di Bala","Tafareo","Jael","rogerio","Di Maria")
index = 0
print(champions[:5])
print(champions[-4:])
print(sorted(champions))

for index, champions in enumerate(champions):
    if champions == 'Pelé':
        print(index)