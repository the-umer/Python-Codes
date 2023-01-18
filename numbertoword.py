def numbers_to_word_converter(number):
    for number in numbers:
        match number: 
            case "1" : print("One",end='')
            case "2" : print("Two",end='')
            case "3" : print("Three",end='')
            case "4" : print("Four",end='')
            case "5" : print("Five",end='')
            case "6" : print("Six",end='')
            case "7" : print("Seven",end='')
            case "8" : print("Eight",end='')
            case "9" : print("Nine",end='')
            case "0" : print("Zero",end='')
            case " " : print(" ",end='')
            case _ : print("invalid characters....")

numbers = input("Enter some number: ")
numbers_to_word_converter(numbers)
