firstBananaCost, availableDolers, wantsBanana = map(int, input().split(" "))
totalCost = 0

for i in range(1, wantsBanana + 1):
    if wantsBanana > 1:
        totalCost = totalCost + firstBananaCost * i

need = totalCost - availableDolers
if need < 0 :
    need = 0
print(need)
