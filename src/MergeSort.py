'''
                            [1, 2, 3, 7 , 2, 1, 3]
                [1, 2, 3]                             [7, 2, 1, 3]
            [1]3       [2, 3]4                       [7, 2]         [1, 3]
                    [2]1     [3]2                 [7]      [2]    [1]     [3]
'''
def merge_sort(unsorted:list[int]):
    if len(unsorted) <=1 : return unsorted 
    mid = len(unsorted)//2
    left = unsorted[:mid]
    right = unsorted[mid:]

    # anything that returns out of merge_sort function is either returned if it is the only
    # value in the list or as a result of the merged function which sorts two sorted lists
    left_sorted = merge_sort(left) 
    right_sorted = merge_sort(right)
    return merge(left_sorted, right_sorted)
    

def merge(sorted_left:list[int], sorted_right:list[int]):
    merged_list = []
    left_index , right_index = 0 , 0
    while(left_index < len(sorted_left) and right_index < len(sorted_right)):
        if sorted_left[left_index] <= sorted_right[right_index]:
            merged_list.append(sorted_left[left_index])
            left_index +=1
        else:
            merged_list.append(sorted_right[right_index])
            right_index +=1
    merged_list = merged_list+sorted_left[left_index:] + sorted_right[right_index:]
    return merged_list
