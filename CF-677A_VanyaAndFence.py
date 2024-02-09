n , h = map(int, input().split(" "))
k = list(map(int,input().split(" ")))
count = 0
for i in k:
    if i > h:
        count += 2
    else:
        count += 1
print(count)