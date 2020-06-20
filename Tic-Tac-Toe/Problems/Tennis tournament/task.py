n = int(input())
data = [input().split() for _i in range(n)]
win_players = [player[0] for player in data if player[1].lower() == 'win']
print(win_players, len(win_players), sep='\n')
