n = int(input())
games = input()
anton = 0
danik = 0
for i in games:
    if i == 'A':
        anton += 1
    elif i == 'D':
        danik += 1
if anton > danik:
    print("Anton")
elif anton < danik:
    print("Danik")
else:
    print("Friendship")
