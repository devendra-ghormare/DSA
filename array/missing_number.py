# def missing_num(arr):

#     for i in range(1, len(arr)):
#         if i not in arr:
#             return i
    
# print(missing_num([1,2,4,5]))


########## Optimal with sum 

def missing_num(arr, n):
     
    num_sum = n * (n+1)//2

    s = 0

    for i in range(len(arr)):
        s += arr[i]
    
    return num_sum - s

print(missing_num([1,2,3,4,6], 6))