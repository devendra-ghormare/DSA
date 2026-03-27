def flatten_array(arr):

    # simple using loop
    flat =  []
    for row in arr:
        for num in row:
            flat.append(num)

    # list comprehention for above

    # flat = [x for row in arr for x in row ]
    return flat

print(flatten_array([[1, 2], [3, 4], [5, 6]]))


# with recursive approch for nested array

def recursive_flatten_array(arr):
    result = []

    for ar in arr:
        if isinstance(ar, list):
            result.extend(recursive_flatten_array(ar))
        else:
            result.append(ar)

    return result

print(recursive_flatten_array([1, [2, [3, 4], 5], 6]))

# without any inbuild method used 

def flatten_without_inbuild_method(arr):

    result = []

    for ar in arr:
        if type(ar) == list:
            for y in flatten_without_inbuild_method(ar):
                result.append(y)
        else:
            result.append(ar)
    return result
print(flatten_without_inbuild_method([1, [2, [3, 4], 5], 6]))