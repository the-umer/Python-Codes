def quick_sort(arr):
    # base case
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

numbers = []
n = int(input("Enter number of elements: "))
i = 0
while i < n:
    inp = int(input(f"Enter {i+1} number: "))
    numbers.append(inp)
    i +=1

sorted_list = quick_sort(numbers)
print(sorted_list)
