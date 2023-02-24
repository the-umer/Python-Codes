def fab(n):
    '''To Display Fabonacci Series'''
    a = 0
    b = 1
    sum = 0
    print(a, end=' ')
    print(b, end=' ')
    while n - 2 > 0:
        sum = a + b
        print(sum, end=' ')
        a = b
        b = sum
        n -= 1


print()
a = int(input("Enter a number upto which you want to print print Fabonacci Series: "))
fab(a)
print('...')