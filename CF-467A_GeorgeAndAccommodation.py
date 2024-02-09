n = int(input())
count = 0

for i in range(n):

    x = list(map(int, input().split(" ")))

    if x[0] <= x[1] - 2:
        # print(x[1])
        # print(x[1]+2)
        count += 1
print(count)

