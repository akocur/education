max_column = 8
max_row = 8

column = int(input())
row = int(input())

max_moves = 8
if column in (1, max_column) and row in (1, max_row):
    max_moves = 3
elif column in (1, max_column) or row in (1, max_row):
    max_moves = 5

print(max_moves)
