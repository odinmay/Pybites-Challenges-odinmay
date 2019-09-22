games_won = dict(sara=0, bob=1, tim=5, julian=3, jim=1)


def print_game_stats(games_won=games_won):
    for key, value in games_won.items():

        if value == 1:
            print(f'{key} has won {games_won[key]} game')

        if value == 0 or value >= 2:
            print(f'{key} has won {games_won[key]} games')

print_game_stats()
