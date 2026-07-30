board = [[],[],[]],[[],[],[]],[[],[],[]]
for i in range(3):
    print(board[i])

while True:
    row = int(input("Enter your move (row):"))

    col = int(input("Enter your move (column):"))
    if board[row][col] == []: 
        board[row][col] = "x"
    for i in range(3):
        print(board[i])

    row = int(input("Enter your move (row):"))

    col = int(input("Enter your move (column):"))

    if board[row][col] == []:
        board[row][col] = "o"
    for i in range(3):
        print(board[i])

    if board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        if board[1][1] == "x":
            print("x have won")
        if board[1][1] == "o":
            print("o have won")
        break

    if board[2][0] == board[2][1] and board[2][1] == board[2][2]:
            if board[2][1] == "x":
                print("x have won")
            if board[2][1] == "o":
                print("o have won")
            break

