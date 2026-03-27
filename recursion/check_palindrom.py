# def is_palindrom(s:str):

#     def check(left, right):

#         if left >= right:
#             return True
#         if s[left] != s[right]:
#             return False
        
#         return check(left+1, right-1)
#     return check(0, len(s) - 1)

# print(is_palindrom("MSDAM"))


####################

# def is_palindrom(s:str):
#     return s == s[::-1]


# print(is_palindrom("MADAM"))

##############3333

def is_palindrom_two_pointers(s:str) -> bool:
    left = 0
    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
print(is_palindrom_two_pointers("MDM"))