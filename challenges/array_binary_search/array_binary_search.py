def array_binary_search(lst, val):
    if val not in lst:
        return -1
    else:
        i = 0
        while i < len(lst):
            if val == lst[i]:
                return i
            i += 1
