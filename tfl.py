from random import randint as ri
from time import sleep
import ranks

elo = 0
mmr = 20
previous_limit = 0
next_limit = 100
shield = True
passperm = True

while True:
    placement = ri(1,8)
    change = (4.5-placement)*mmr
    if elo + change > 0:
        elo += change
        if passperm == False:
            pass
        elif elo >= next_limit:
            print('KADEME ATLANDI!')
            elo = next_limit
            previous_limit += 100
            next_limit += 100
            mmr += 1
            shield = True
        elif elo < previous_limit:
            if shield:
                print('Düşme Kalkanı Kullanıldı.')
                elo = previous_limit
                shield = False
            else:
                print('KADEME DÜŞÜRÜLDÜ!')
                elo = previous_limit-25
                previous_limit -= 100
                next_limit -= 100
                shield = True
                mmr -= 1
    else:
        elo = 0
        if mmr > 5:
            mmr -= 1

    print(f"Sıra: {placement} / LP+-: {int(change)} / DERECE: {ranks.rank(elo)} {int(elo-(elo//100*100))}LP")
    press_to_continue = input('')
    if press_to_continue == 'mmr':
        print(f'(mmr: {mmr})\n')