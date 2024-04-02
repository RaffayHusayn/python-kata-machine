def flatten(nested_list: list[int])->list[int]:
    output = []
    recurse_item(nested_list, output)
    return output

def recurse_item(nested_list, output):
    for i in nested_list:
        if isinstance(i, list):
            recurse_item(i, output)
        else:
            output.append(i)
inputList = [1, 2, None,  3, [4,[1,2,4],6],7]