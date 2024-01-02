#--------- Quick Sort Implementation 1 ------------
def quick_sort_inplace(unsorted:list[int], start:int, end:int)-> list[int]:
    if start >= end : return unsorted
    pivot_index = partition(unsorted, start, end)
    quick_sort_inplace(unsorted, start, pivot_index -1)
    quick_sort_inplace(unsorted,  pivot_index +1, end)
    return unsorted


def partition(unsorted:list[int], start:int, end:int) -> int:
    # left most element within the start/end bound is our pivot
    pivot = unsorted[end]
    # partition_index is the index where on the left will be smaller than the pivot and the right will be larger than the pivot
    partition_index = start
    for i in range(start, end):
        if unsorted[i] <= pivot:
            unsorted[i], unsorted[partition_index] = unsorted[partition_index] , unsorted[i]
            # incrementing partition_index because previous location def is less/equal than pivot 
            partition_index +=1
    #coming out of the loop, the partition_index will either already be the same as end if everything was smaller than pivot or 
    # it will be in a position where swapping with pivot would make everything on the left smaller and right larger
    unsorted[partition_index], unsorted[end] = unsorted[end],unsorted[partition_index] 
    return partition_index


#--------- Quick Sort Implementation 2 ------------
def quick_sort_split_array(unsorted:list[int], start:int , end :int) -> list[int]:
    if start >= end : return unsorted
    # calculating the pivot which will be the last element of the unsorted array 
    pivot = unsorted[end]
    smaller = [i for i in unsorted[:-1] if i <= pivot ]
    greater = [i for i in unsorted[:-1] if i > pivot ]
    return quick_sort_split_array(smaller, 0, len(smaller)-1 ) + [pivot] + quick_sort_split_array(greater, 0, len(greater)-1) 

#--------- Quick Sort Implementation 3 ------------
def quick_sort_split_array_one_param(unsorted: list[int]) -> list[int]:
    if len(unsorted) <= 1 : return unsorted
    pivot = unsorted[len(unsorted) -1]
    smaller= [i for i in unsorted[:-1] if i <= pivot]
    greater= [i for i in unsorted[:-1] if i > pivot]
    return quick_sort_split_array_one_param(smaller) + [pivot] + quick_sort_split_array_one_param(greater)