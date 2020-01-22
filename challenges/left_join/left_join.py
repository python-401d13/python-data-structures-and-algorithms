
def left_join(hash_one, hash_two):
    hash_copy = {}
    for key in hash_one:
        hash_copy[key] = [hash_one[key]]

        if hash_two.get(key):
            hash_copy[key].append(hash_two[key])
        else:
            hash_copy[key].append(None)

    return hash_copy
