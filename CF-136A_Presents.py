n = int(input())
frnds = list(map(int,input().split()))

result = [0] * n


for i in range(n):
    result[frnds[i]-1] = i+1

print(*result)