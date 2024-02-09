lang1 = input()
lang2 = input()
lang3 = lang1[::-1]

# for i in range(len(lang1)-1,-1,-1):
#     lang3 = lang3+lang1[i]

if lang2 == lang3:
    print("YES")
else:
    print("NO")