def gretest_common_factor(a, b):
    
    # while a > 0 and b > 0:
    #     if a > b:
    #         a = a % b
    #     else:
    #         b = b % a
        
    # # if a == 0:
    # #     return b
    # # else:
    # #     return a
    # return b if a==0 else a
        
# print(gretest_common_factor(52, 10)) 

############# Simple way #############
    gcd = 0
    for i in range(1, min(a, b)+ 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

print(gretest_common_factor(5,10))