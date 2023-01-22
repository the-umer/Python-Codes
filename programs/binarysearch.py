"""
1. Binary search works on divide and conquer method.
2. It works only on the sorted array.
"""

def binarySearch(array,item,start,end):
    low = start 
    high = end
    mid = int((low+high)/2)
    while low <= high:
        if item == array[mid]:
            return mid
        elif item > array[mid]:
            low = mid + 1
            binarySearch(array,item,low,high)
        elif item < array[mid]:
            high = mid - 1
            binarySearch(array,item,low,high)
        mid = int((low+high)/2)

    return -1

numbers = [1,2,3,4,5,6,7,8,9,10]
search = binarySearch(numbers,8,0,len(numbers))
print(search)