rank_names = [
    'Demir',
    'Bronz',
    'Gümüş',
    'Altın',
    'Platin',
    'Elmas',
    'Ustalık',
    'Üstatlık',
    'Şampiyonluk'
]

def rank(elo):
    rank_num = int(elo//100)
    if rank_num > 8: rank_num = 8
    rank = rank_names[rank_num]
    return rank