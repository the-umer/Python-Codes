"""
Linear Search searches an item in the list by traversing the whole array
and comparing with every item.
if Item is present in the array then we return the index else return -1.
"""

def linearSearch(array,size,item):
    for index in range(0,size):
        if array[index] == item:
            return index
    return -1

numbers = [5,2,1,7,3,4,9,3,6]
search = linearSearch(numbers,len(numbers),9)
if(search != -1):
    print(f"The item is present in the array at index {search}.")
else:
    print("The item is not present in the array.")