from math import floor

def binary_search(haystack: list[int], pin : int):
    start = 0 
    end = len(haystack)

    while start < end:
        mid = floor((end-start)/2) + start
        if haystack[mid] == pin:
            return mid
        elif haystack[mid] > pin:
            end = mid
        else: 
            start = mid +1
    return -1


def bubble_sort(unsorted: list[int])-> list[int]:
    n = len(unsorted)
    for i in range(n): # because last one is not included in range 
        for j in range(1, n - i):
            if unsorted[j-1] > unsorted[j]:
                unsorted[j], unsorted[j-1] = unsorted[j-1], unsorted[j]
    return unsorted

def quick_sort_1(unsorted: list[int])-> list[int]:
    if len(unsorted) <= 1: return unsorted
    pivot = unsorted[len(unsorted)-1]
    smaller = [i for i in unsorted[:-1] if i <= pivot ]
    greater = [i for i in unsorted[:-1] if i > pivot ]
    return quick_sort_1(smaller) + [pivot] + quick_sort_1(greater)

def quick_sort_2(unsorted: list[int], start: int, end: int)->list[int]:
    if start >= end : return unsorted
    partition_index = partition(unsorted, start, end)
    quick_sort_2(unsorted, start, partition_index-1)
    quick_sort_2(unsorted, partition_index+1, end)
    return unsorted

def partition(unsorted: list[int], start: int, end: int) ->int:
    ans = start
    pivot = unsorted[end]
    for i in range(start, end):
        if unsorted[i] <= pivot:
            unsorted[ans], unsorted[i]  = unsorted[i], unsorted[ans]
            ans +=1
    unsorted[end], unsorted[ans] = unsorted[ans], unsorted[end]
    return ans



    

