# def find_one_occurance_number(arr):
#     n = len(arr)

#     for i in range(n):
#         num = arr[i]
#         count = 0
#         for j in range(n):
#             if arr[j] == num:
#                 count += 1
#         if count < 2:
#             return num

# print(find_one_occurance_number([1,1,2,3,3,4,4]))


##### Better solution with dict

# def find_one_occurance_number(arr):
#     n = len(arr)

#     mydict = {}

#     for num in arr:
#         if num in mydict:
#             mydict[num] += 1
#         else:
#             mydict[num] = 1
    
#     for key, value in mydict.items():
#         if value == 1:
#             return key

# print(find_one_occurance_number([1,1,2,3,3,4,4]))

######## Optimal solution with XOR

def find_one_occurance_number(arr):
    XOR = 0

    for i in range(len(arr)):
        XOR = XOR ^ arr[i]
    return XOR

print(find_one_occurance_number([1,1,2,3,3,4,4]))