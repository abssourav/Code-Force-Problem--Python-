digit, n = map(int, input().split(" "))


for i in range(n):
    if digit % 10 == 0:
        digit = digit/10
    else:
        digit -= 1
print(int(digit))