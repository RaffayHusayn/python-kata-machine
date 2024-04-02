def fib_for_position(pos):
    if(pos < 2):
        return pos
    return fib_for_position(pos-1) + fib_for_position(pos -2) 

def fib(num):
    seq = []
    for i in range(num+1):
        seq.append(fib_for_position(i))
    return seq

print(fib(5))

