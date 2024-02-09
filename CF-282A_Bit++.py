n = int(input())
count = 0
for i in range(n):
    stringValue = input()

    if stringValue[0] == '+' or stringValue[len(stringValue)-1] == '+':
        count += 1
    elif stringValue[0] == '-' or stringValue[len(stringValue)-1] == '-':
        count -= 1
print(count)
