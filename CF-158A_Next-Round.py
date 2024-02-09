participent, position = map(int, input().split(' '))
scores = list(map(int, input().split(' ')))

count = 0

for i in scores:
    if (scores[position-1] <= i) and (i != 0):
        count = count+1
print(count)