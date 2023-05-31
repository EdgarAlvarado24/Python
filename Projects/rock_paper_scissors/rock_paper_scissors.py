import random

def play():
    user = input("Cual es tu eleccion?, 'r' para roca, 'p' para papel y 't' para tijeras: ")
    computer = random.choice(['r', 'p', 't'])

    if(user == computer):
        return 'Empate'
    if is_win(user, computer):
        return 'Ganaste'
    return 'Perdiste'

def is_win(player, oponent):
    if(player == 'r' and oponent == 't') or (player == 'p' and oponent == 'r') or (player == 't' and oponent == 'p'):
        return True
print(play())