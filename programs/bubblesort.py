"""
Bubble sort works in passes. In this each element is compared with the next
element in the array and if the first element is smaller than the next element
then they are swapped. This process is repeated until the entire array is 
sorted.
"""

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    
    return array


numbers = []
n = int(input("Enter the number of elements in the array: "))
for i in range(0,n):
    number = int(input(f"Enter {i+1} number: "))
    numbers.append(number)
print(bubbleSort(numbers))