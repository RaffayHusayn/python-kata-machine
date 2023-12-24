import math
def two_crystal_balls(breaks: list[bool])-> int:
    length = len(breaks) 
    jump = math.floor(math.sqrt(length))
    result = -1
    for i in range(0, length, jump):
        if(breaks[i]):
            for j in range(i-jump+1, length):
                if(breaks[j]):
                    return j
    return result
    