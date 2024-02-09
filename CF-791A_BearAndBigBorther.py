a, b = map(int, input().split(" "))
count = 0
while True:
    count += 1
    if a * 3 > b * 2:
        break
    else:
        a = a * 3
        b = b * 2
print(count)
