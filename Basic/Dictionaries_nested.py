teams = [
    {
        'astros': {
            '2B': 'Altuve',
            'SS': 'Correa',
            '3B': 'Bregman',
        }
    },
    {
        'angels': {
            'OF': 'Trout',
            'DH': 'Pujols',
        }
    }
]

# print(teams[0])

angels = teams[1].get('angels', 'Team not found')

print(list(angels.values())[1])

# astros = teams[0].get('2B', 'player not found')

# print(astros)
