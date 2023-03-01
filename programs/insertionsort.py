''' This sorting algorithm builds a sorted list ome elements at a time from the sorted list.
It virtually divides the list of elements in two sub-list 
i.e sorted sub-list and unsorted sub-list.'''

n = int(input("Enter the number of elements: "))
a = []
for i in range(n):
    a.append(int(input()))
print("Unsorted list: ",a)
k = 1
for k in range(k,n):
    temp = a[k]
    j = k-1
    while temp<a[j] and j>=0:
        a[j+1] = a[j]
        j = j-1
    a[j+1] = temp
    
print("Sorted list:",a)
        