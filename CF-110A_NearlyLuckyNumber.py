digit = input()
count = 0

for i in digit:
    if(i=='4' or i=='7'):
        count += 1
        print(count)


if(count==7 or count ==4):
    print("YES")
else:
    print("NO")

