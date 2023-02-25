# to check that the entered number is prime or not

n = int(input("Enter a number: "))
t = 0
for i in range(2,n):
    if n%i == 0:
        t += 1
    else:
        continue


if t>1:
    print(n,'is not a prime number.')
else:
    print(n,'is a prime number.')