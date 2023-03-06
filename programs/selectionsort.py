def selection_sort(lst):
  n = len(lst)
  for i in range(n - 1):
    min = i
    for j in range(i + 1, n):
      if (lst[j] < lst[min]):
        min = j
    lst[i], lst[min] = lst[min], lst[i]


numbers = []
n = int(input("Enter number of elements: "))
i = 0
while i < n:
    inp = int(input(f"Enter {i+1} number: "))
    numbers.append(inp)
    i +=1

selection_sort(numbers)
print(numbers)
