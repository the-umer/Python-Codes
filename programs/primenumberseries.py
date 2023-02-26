#progrom to print prime numbers
#m is the upper range to which the prime numbers to be print

m=int(input())
print("Entered number is",m)
print()
print("Prime numbers are")
for j in range(2,m):
  for i in range(2,j):
    if j%i==0:
      break
  else:
    print(j)