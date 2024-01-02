def bubble_sort(unsorted_list: list[int])-> list[int]:
    for i in range(len(unsorted_list)):
        for j in range(i+1, len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[i]:
                local = unsorted_list[i]
                unsorted_list[i] = unsorted_list[j]
                unsorted_list[j] = local
    return unsorted_list

def bubble_sort_real(unsorted_list: list[int]) -> list[int]:
    length = len(unsorted_list)
    for i in range( length-1 ):
        for j in range( length-1-i ):
            if unsorted_list[j+1] < unsorted_list[j]:
                unsorted_list[j] , unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
    return unsorted_list

