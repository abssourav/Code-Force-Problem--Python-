n = int(input())
x = list(map(int, input().split(" ")))
count = 0
for i in x:
    if i == 1:
        count += 1
        break

if count > 0:
    print("HARD")
else:
    print("EASY")
