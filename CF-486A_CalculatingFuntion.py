import math
def f(n):

  if(n%2==0):
    n = n // 2
    even = n * ( n + 1 )
    odd = n * n
    # print("even = ", even)
    # print("odd = ", odd)
    result=even-odd
    print(math.floor(result))
  else:
    n=(n//2)+1
    odd=n*n
    n=n-1
    even=n*(n+1)
    # print("even = ", even)
    # print("odd = ", odd)
    result=even-odd
    print(math.floor(result))


n = int(input())

f(n)