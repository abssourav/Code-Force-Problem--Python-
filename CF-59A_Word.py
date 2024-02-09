word = input()
upperCase = 0
lowerCase = 0
for i in word:
    if i == i.upper():
        upperCase += 1
    else:
        lowerCase += 1

if upperCase < lowerCase or upperCase == lowerCase :
    word = word.lower()
else:
    word = word.upper()

print(word)
