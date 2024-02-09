n = int(input())
k = []
for i in range(n):
    x = int(input())
    k.append(x)

count = 1

for i in range(n - 1):
    if k[i] == k[i + 1]:
        continue
    else:
        count += 1

print(count)