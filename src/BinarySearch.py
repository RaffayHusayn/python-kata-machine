import math

def binary_search(haystack: list[int], needle: int) -> bool: 
    start = 0 
    end = len(haystack)
    while start < end:
        mid = math.floor(start + (end - start)/2)
        if haystack[mid] == needle:
            return True
        elif haystack[mid] < needle:
            start = mid+1
        else:
            end = mid
    return False

