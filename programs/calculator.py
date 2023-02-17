import math as m
from math import *

print("1. Addition\t\t9. Factorial\n2. Subtraction\t\t10. Power a^b")
print("3. Multiplication\t11. Exponentional Value\n4. Division\t\t12. Log Value")
print("5. Square\t\t13. Angular Conversion\n6. Square Root\t\t14. Trigonometric Value")
print("7. Cube\t\t\t15. Hyperbolic Functions\n8. Cube Root\t\t16.")
print("\t\t0. Exit")
print()


def logvalue(v):
    i = float(input("Enter a number: "))
    match v:
        case 1:
            print("Log(", i, "):", log(i))
        case 2:
            print("Log(", i, "):", log2(i))
        case 3:
            print("Log(", i, "):", log10(i))
        case _:
            print("Wrong Input...")


def trigonvalue(u):
    match u:
        case 1:
            tr = float(input("Enter angle: "))
            print("sin(", tr, "):", sin(tr))
        case 2:
            tr = float(input("Enter angle: "))
            print("cos(", tr, "):", cos(tr))
        case 3:
            tr = float(input("Enter angle: "))
            print("tan(", tr, "):", tan(tr))
        case 4:
            tr = float(input("Enter a number b/w -1 and 1: "))
            print("sin-1(", tr, "):", m.asin(tr))
        case 5:
            tr = float(input("Enter a number b/w -1 and 1: "))
            print("cos-1(", tr, "):", m.acos(tr))
        case 6:
            tr = float(input("Enter a number: "))
            print("tan-1(", tr, "):", m.tan(tr))
        case _:
            print("Wrong Input...")


def angconver(i):
    match i:
        case 1:
            x = float(input("Enter angle in Radians: "))
            print(x, 'rad:', m.degrees(x), '°')
        case 2:
            x = float(input("Enter angle in Degrees: "))
            print(x, '°:', m.radians(x), 'rad')
        case _:
            print("Wrong Input...")


def hypbfun(hb):
    match hb:
        case 1:
            hy = float(input("Enter angle: "))
            print("sinh(", hy, "):", sinh(hy))
        case 2:
            hy = float(input("Enter angle: "))
            print("cosh(", hy, "):", cosh(hy))
        case 3:
            hy = float(input("Enter angle: "))
            print("tanh(", hy, "):", tanh(hy))
        case 4:
            hy = float(input("Enter a number: "))
            print("sinh-1(", hy, "):", m.asinh(hy))
        case 5:
            hy = float(input("Enter a number: "))
            print("cosh-1(", hy, "):", m.acosh(hy))
        case 6:
            hy = float(input("Enter a number: "))
            print("tanh-1(", hy, "):", m.atanh(hy))
        case _:
            print("Wrong Input...")


def expval():
    print("1. e^x\n2. 2^x\n3. 10^x")
    ec = int(input("Enter your choice: "))
    if ec == 1:
        x = float(input("Enter the power: "))
        print('e^', x, ':', exp(x))
    elif ec == 2:
        x = float(input("Enter the power: "))
        print('2^', x, ':', exp2(x))
    elif ec == 3:
        x = float(input("Enter the power: "))
        print('10^', x, ':', pow(10, x))
    else:
        print("Wrong Input...")


while True:
    ch = int(input("Enter your choice: "))
    if ch > 4:
        if ch <= 10:
            b = float(input("Enter a number: "))
            match ch:
                case 5:
                    print("Square of", b, "is ", pow(b, 2))
                case 6:
                    print("Square Root of", b, "is ", sqrt(b))
                case 7:
                    print("Cube of", b, "is ", pow(b, 3))
                case 8:
                    print("Cube Root of", b, "is ", cbrt(b))
                case 9:
                    b = int(b)
                    print(b, "! :", factorial(b))
                case 10:
                    a = float(input("Enter Base Value: "))
                    print(a, '^', b, ':', pow(a, b))
        else:
            match ch:
                case 11:
                    expval()
                case 12:
                    print("1. Natural log\n2. base-2\n3. base-10")
                    a = int(input("Your Choice: "))
                    logvalue(a)
                case 13:
                    print("1. Radians to Degrees\n2. Degrees to Radians")
                    c = int(input("Your Choice: "))
                    angconver(c)
                case 14:
                    print("1. sin(x)\t4. sin-1(x)\n2. cos(x)\t5. cos-1(x)\n3. tan(x)\t6. tan-1(x)")
                    t = int(input("Your Choice: "))
                    trigonvalue(t)
                case 15:
                    print("1. Sinh(x)\t4. sinh-1(x)\n2. cosh(x)\t5. cosh-1(x)\n3. tanh(x)\t6. tanh-1(x)")
                    h = int(input("Your Choice: "))
                    hypbfun(h)
                case _:
                    print("Enter a valid choice...")

    elif ch == 0:
        print("EXIT.")
        break
    else:
        a = float(input("Enter first number:"))
        b = float(input("Enter second number:"))
        match ch:
            case 1:
                print(a, "+", b, "=", a + b)
            case 2:
                print(a, "-", b, "=", a - b)
            case 3:
                print(a, "x", b, "=", a * b)
            case 4:
                if b == 0:
                    print("Zero Division Error")
                else:
                    print(a, "/", b, "=", a / b)
