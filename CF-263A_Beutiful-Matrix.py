matrix = [list(map(int, input().split())) for _ in range(5)]
moves = 0
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            r, c = abs(2 - i), abs(2 - j)
            moves = r + c
            matrix[i][j] = 0
            matrix[2][2] = 1
            break
    if moves > 0:
        break
print("Need Move for ", moves, " times")

# extra
print(" ")
print("The beutiful Matrix is: ")
for i in range(5):
    print("\n")
    for j in range(5):
        print(matrix[i][j], end=' ')

# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25
