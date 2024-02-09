n = int(input())
passenger = 0
min_passenger = 0

for i in range(n):
    a,b = map(int, input().split(" "))
    passenger = passenger - a + b
    if passenger > min_passenger :
        min_passenger = passenger

print(min_passenger)