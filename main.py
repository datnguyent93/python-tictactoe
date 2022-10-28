board = [' ' for _ in range(9)]
print(board)
for row in [board[i*3:(i+1)*3] for i in range(3)]:
    print('| ' + ' | '.join(row) + ' |')