"""
binary_search.py

Using recursion

𝑇(𝑛)=𝑙𝑜𝑔(𝑛)∗𝑘

The time complexity of the function is a logarithmic function of the input, 𝑛
Hence, the time complexity of the recursive algorithm for binary search is 𝑙𝑜𝑔(𝑛).
"""
def binary_search(arr, target):
    return binary_search_func(arr, 0, len(arr) - 1, target)

def binary_search_func(arr, start_index, end_index, target):
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index)//2

    if arr[mid_index] == target:
        return mid_index
    elif arr[mid_index] > target:
        return binary_search_func(arr, start_index, mid_index - 1, target)
    else:
        return binary_search_func(arr, mid_index + 1, end_index, target)

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 44, 71, 72, 73, 101, 999]
print(binary_search(arr, 71))

