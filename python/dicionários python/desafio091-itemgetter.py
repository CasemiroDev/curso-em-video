from random import randint
from time import sleep
from operator import itemgetter
united = {"jogador1": randint(1,6),
          "jogador2": randint(1,6),
          "jogador3": randint(1,6),
          "jogador4": randint(1,6)}
sort=[]
sort = sorted(united.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(sort):
    print(f" O {i+1}ª lugar foi {v[0]} com {v[1]}")