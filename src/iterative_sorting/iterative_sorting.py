# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements\
    for i in range(0, len(arr)-1):
        min_val = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_val]:
                min_val = j
            if min_val != i:
                arr[min_val], arr[i] = arr[i], arr[min_val]

    return arr


print(selection_sort([4, 3, 2]))

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    index_len = len(arr)-1
    sort = False
    while not sort:
        sort = True
        for i in range(0, index_len):
            if arr[i] > arr[i+1]:
                sort = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


print(bubble_sort([2, 5, 3, 4]))

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # Your code here

    return arr
