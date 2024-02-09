n , t = map(int, input().split(" "))
line = list(input())
temp = ""
for i in range(t):
    j = 0
    while j < (n-1):
        if line[j] == "B" and line[j+1] == "G":
            line[j] = "G"
            line[j+1] = "B"
            j += 1
        j += 1


for i in line:
    temp = temp+i
print(temp)
