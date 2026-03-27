def myAtoi(s:str):
    n = len(s)
    i = 0

    if not s:
        return 0
    
    INT_MAX = 2**31 - 1 
    INT_MIN = -2**31

    # skip white spaces
    while i < n and s[i] == " ":
        i += 1
    
    # sign
    sign = 1
    if i < n and s[i] in "+-":
        if s[i] == "-":
            sign = -1
        i += 1
    
    # digit
    result = 0
    while i < n and s[i].isdigit():
        digit = int(s[i])

        # overflow check
        if result > (INT_MAX - digit) // 10:
            return INT_MAX if sign == 1 else INT_MIN
        
        result = result * 10 + digit 
        i += 1

    return sign * result

print(myAtoi("-42"))