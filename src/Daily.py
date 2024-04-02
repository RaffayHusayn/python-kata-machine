'''
Daily Problems:
1. Binary Search 
2. Bubble Sort
3. Quick Sort 1 and 2
4. Merge Sort
5. Flatten
'''
# def bubble_sort(unsorted:list[int]):
#     length = len(unsorted)
#     for i in range(length):
#         for j in range(1, length -i):
#             if unsorted[j-1]> unsorted[j]:
#                 unsorted[j-1], unsorted[j] =unsorted[j], unsorted[j-1]
#     return unsorted

# def binary_search(haystack:list[int], needle:int):
#     low=0
#     high = len(haystack)
#     while low < high:
#         mid = low + (high-low)//2
#         if haystack[mid] == needle:
#             return mid 
#         elif haystack[mid] > needle:
#             high = mid
#         else:
#             low = mid+1
#     return -1

# def quick_sort_2(unsorted:list[int], start:int, end:int):
#     if start >= end-1: return
#     partition_index = partition(unsorted, start, end)
#     quick_sort_2(unsorted, start, partition_index)
#     quick_sort_2(unsorted, partition_index+1, end)
#     return unsorted

# def partition(unsorted:list[int], start:int, end:int):
#     moving_index = start
#     pivot = unsorted[end-1]
#     for i in range(start, end-1):
#         if unsorted[i] <= pivot:
#             unsorted[i], unsorted[moving_index] = unsorted[moving_index], unsorted[i]
#             moving_index +=1
#     unsorted[moving_index], unsorted[end-1]=unsorted[end-1], unsorted[moving_index]
#     return moving_index

'''
Notes about quick sort:
We are creating a recursive algorithm and this is how it works:
1. The start is inclusive and the end is exclusive for the indexes so in the function that we will recurse we want to see when we are left with an array
of a single element, we want to just return that and not do any more processing. 
2. In the case of inclusive starting element and exclusive ending element, if start_index = end_index then it means that there's only 1 element. See the example below
A, B, C, D 
0, 1, 2, 3  ->  start=2 and end =3 
so the condition to check to make sure there's only one elemnt left is to just make sure that start = end -1 . This means that there should only be one element in the array
Imagine if unsorted provided was literally 1 element. The start would be 0 and the end =1. Since it is only one element and start = end -1 it just proves that our condition is correct
'''

# def quick_sort_1(unsorted:list[int]):
#     if len(unsorted) <= 1 : return unsorted

#     pivot = unsorted[len(unsorted)-1]
#     lower= [i for i in unsorted[:-1] if i<= pivot]
#     higher = [ j for j in unsorted[:-1] if j > pivot]

#     return quick_sort_1(lower)+ [pivot] + quick_sort_1(higher)

# def merge_sort(unsorted: list[int])-> list[int]:
#     # if len = 1 then it means that it is already sorted. Length = 0 mean it has nothing to be sorted
#     if len(unsorted) <= 1 : return unsorted 
#     mid = len(unsorted)//2
#     left_split = unsorted[:mid] 
#     right_split = unsorted[mid:]

#     sorted_left_split = merge_sort(left_split)
#     sorted_right_split = merge_sort(right_split)
#     return merge(sorted_left_split, sorted_right_split)

# def merge(sorted_left:list[int], sorted_right: list[int])-> list[int]:
#     merged_list =[]
#     left_index, right_index = 0,0
#     while (left_index < len(sorted_left) and right_index < len(sorted_right)):
#         if sorted_left[left_index] <= sorted_right[right_index]:
#             merged_list.append(sorted_left[left_index])
#             left_index +=1
#         else:
#             merged_list.append(sorted_right[right_index])
#             right_index +=1
#     merged_list = merged_list + sorted_right[right_index:] + sorted_left[left_index:]
#     return merged_list

# def merge_sort(unsorted: list[int])->list[int]:
#     if len(unsorted) <= 1 : return unsorted
#     mid = len(unsorted) //2

#     left_split = unsorted[:mid]
#     right_split = unsorted[mid:]

#     left_split_sorted = merge_sort(left_split)
#     right_split_sorted = merge_sort(right_split)

#     return merge(left_split_sorted, right_split_sorted)

# def merge(left, right)-> list[int]:
#     merged_list = []
#     left_ind, right_ind = 0,0
#     while left_ind < len(left) and right_ind < len(right):
#         if left[left_ind] <= right[right_ind]:
#             merged_list.append(left[left_ind])
#             left_ind +=1
#         else:
#             merged_list.append(right[right_ind])
#             right_ind +=1
#     merged_list = merged_list+left[left_ind:] + right[right_ind:]
#     return merged_list


# def binary_search( haystack: list[int], needle: int)-> int :
#     low = 0
#     high = len(haystack)
#     while low<high:
#         mid = low + (high-low)//2
#         if haystack[mid] == needle:
#             return mid
#         elif haystack[mid] > needle:
#             high = mid
#         else: 
#             low = mid+1
#     return -1


# def bubble_sort(unsorted:list[int])-> list[int]:
#     for i in range(len(unsorted)):
#         for j in range(1, len(unsorted)-i):
#             if unsorted[j-1] > unsorted[j]:
#                 unsorted[j-1], unsorted[j] = unsorted[j], unsorted[j-1]
#     return unsorted


# def quick_sort_1(unsorted:list[int])-> list[int]:
#     if len(unsorted) <= 1: return unsorted

#     pivot = unsorted[len(unsorted)-1]
#     less_split = [i for i in unsorted[:-1] if i <= pivot]
#     greater_split = [j for j in unsorted[:-1] if j > pivot]

#     return quick_sort_1(less_split) + [pivot] + quick_sort_1(greater_split) 

# def quick_sort_2(unsorted:list[int], start: int, end:int):
#     if start >= end: return 

#     pivot_index = partition(unsorted, start, end)
#     quick_sort_2(unsorted, start, pivot_index)
#     quick_sort_2(unsorted, pivot_index+1, end  )

#     return unsorted


# def partition(unsorted: list[int], start:int, end:int):
#     # we need to sort the passed list within bounds for the pivot index
#     # return pivot index 
#     pivot = unsorted[end-1]
#     moving_index = start
#     for i in range(start, end-1):
#         if unsorted[i] <= pivot:
#             unsorted[i], unsorted[moving_index] = unsorted[moving_index], unsorted[i]
#             moving_index +=1
#     unsorted[moving_index], unsorted[end-1] = unsorted[end-1], unsorted[moving_index]
#     return moving_index


# def flatten(nested_list)-> list[int]:
#     output_list = []
#     def recurse_element(nested_list):
#         for i in nested_list:
#             if isinstance(i, list):
#                 recurse_element(i)
#             else:
#                 output_list.append(i)
#     recurse_element(nested_list)
#     return output_list

# def merge_sort(unsorted: list[int]) -> list[int]:
#     if len(unsorted) <= 1: return unsorted
#     mid = len(unsorted) //2
#     left_part = unsorted[:mid]
#     right_part = unsorted[mid:]

#     left_part_sorted = merge_sort(left_part)
#     right_part_sorted = merge_sort(right_part)
#     return merge(left_part_sorted, right_part_sorted)

# def merge(left: list[int], right:list[int])-> list[int]:
#     merged_list = []
#     left_index , right_index = 0,0

#     while left_index < len(left) and right_index < len(right):
#         if left[left_index] <= right[right_index]:
#             merged_list.append(left[left_index])
#             left_index +=1
#         else:
#             merged_list.append(right[right_index])
#             right_index +=1
#     merged_list = merged_list + left[left_index:] + right[right_index :]
#     return merged_list

def binary_search(haystack: list[int], needle: int)->int:
    start = 0 
    end = len(haystack)
    while start < end:
        mid = start + (end-start)//2
        if haystack[mid] == needle:
            return mid
        elif haystack[mid] > needle:
            end = mid
        else:
            start = mid +1
    return -1

def bubble_sort(unsorted: list[int])-> list[int]:
    for i in range(len(unsorted)):
        for j in range(1, len(unsorted)-i):
            if unsorted[j] < unsorted[j-1]:
                unsorted[j], unsorted[j-1] = unsorted[j-1], unsorted[j]
    return unsorted

def quick_sort_1(unsorted: list[int]):
    if len(unsorted) <= 1: return unsorted
    pivot = unsorted[-1]
    smaller = [i for i in unsorted[:-1] if i <= pivot]
    greater = [i for i in unsorted[:-1] if i>pivot ]
    return quick_sort_1(smaller) + [pivot] + quick_sort_1(greater)

# start is inclusive, end is exclusive
def quick_sort_2(unsorted:list[int], start: int, end : int):
    if start >= end-1 : return 

    partition_index = partition(unsorted, start, end)
    quick_sort_2(unsorted, start, partition_index)
    quick_sort_2(unsorted, partition_index+1, end)

    return unsorted

# return the partition index
def partition(unsorted:list[int], start:int, end:int):
    pivot=unsorted[end-1]
    moving_index = start
    for i in range(start, end-1):
        if unsorted[i]<=pivot:
            unsorted[i], unsorted[moving_index] = unsorted[moving_index], unsorted[i]
            moving_index +=1
    # move the pivot element the moving_index location
    unsorted[end-1], unsorted[moving_index] = unsorted[moving_index], unsorted[end-1]
    return moving_index

# def merge_sort(unsorted:list[int]):
#     if len(unsorted) <=1: return unsorted

#     #splitting the array
#     mid = len(unsorted) //2
#     left = unsorted[:mid]
#     right = unsorted[mid:]

#     lsplit = merge_sort(left)
#     rsplit = merge_sort(right)
#     return merge(lsplit, rsplit)

# def merge(sorted_lsplit, sorted_rsplit):
#     lindex = 0
#     rindex = 0
#     sorted_merged = []
#     while lindex < len(sorted_lsplit) and rindex < len(sorted_rsplit):
#         if (sorted_lsplit[lindex] <= sorted_rsplit[rindex]):
#             sorted_merged.append(sorted_lsplit[lindex])
#             lindex+=1
#         else:
#             sorted_merged.append(sorted_rsplit[rindex])
#             rindex+=1
#     sorted_merged = sorted_merged + sorted_lsplit[lindex:]+sorted_rsplit[rindex:]
#     return sorted_merged 

def merge_sort(unsorted:list[int])->list[int]:
    if len(unsorted) <= 1: return unsorted

    # splitting 
    mid = len(unsorted)//2
    left = unsorted[:mid]
    right = unsorted[mid:]

    #drilling down
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)


# basically merge two sorted lists and keep the merge list sorted
def merge(left_sorted:list[int], right_sorted:list[int])->list[int]:
    l_index = 0
    r_index = 0
    merged= []
    while l_index < len(left_sorted) and r_index < len(right_sorted):
        if left_sorted[l_index] <= right_sorted[r_index]:
            merged.append(left_sorted[l_index])
            l_index +=1
        else:
            merged.append(right_sorted[r_index])
            r_index +=1
    merged = merged + left_sorted[l_index:] + right_sorted[r_index:]
    return merged


def flatten(nested_list):
    flattened_list = []
    def recurse_flat(nested_list, flattened_list):
        for i in nested_list:
            if isinstance(i, list):
                recurse_flat(i, flattened_list)
            else:
                flattened_list.append(i)
    recurse_flat(nested_list, flattened_list)
    return flattened_list

