n = int(input())
drinks = list(map(int, input().split(' ')))

sum_Drinks = 0
for i in drinks:
    sum_Drinks = sum_Drinks + i

result  = sum_Drinks/n
print("{:4f}".format(result))
