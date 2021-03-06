
def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError
    else:
        if len(int_list) == 0:
            return None
        else:
            largest = int_list[0]
            for i in int_list:
                if largest < i:
                    largest = i
            return largest


def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError
    if len(int_list) == 0:
        return []
    return [int_list[-1]] + reverse_rec(int_list[:-1])


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    if int_list is None:
        raise ValueError
    else:
        if int_list == []:
            return None
        mid = (high + low) // 2
        if int_list[mid] == target:
            return mid
        elif int_list[mid] > target and target >= int_list[low]:
            return bin_search(target, low, mid, int_list)
        elif int_list[mid] < target and target <= int_list[high]:
            return bin_search(target, mid + 1, high, int_list)
        else:
            return None
