def is_prime_number(n):
    count = 0
#     for i in range(1, n+1):
#         print(i)
#         if n%i == 0:
#             count += 1
    
#     if count == 2:
#         return True
#     else:
#         return False

# print(is_prime_number(7))

##############3

    for i in range(1,int(n ** 0.5) + 1):
        if n%i == 0:
            count += 1
            if (n//i) != i:
                count += 1

        return count == 2
    
print(is_prime_number(52))