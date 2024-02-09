numbers = input().split("+")
numbers.sort()
result = ""

for i in numbers:
    result = result + i + "+"

print(result[:-1])

