def romanToInt(s:str):
############### Brute Force #################
    # roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    # special = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
    # total = 0
    # i=0

    # while i < len(s):
    #     if i+1 < len(s) and s[i] + s[i+1] in special:
    #         total += special[s[i] + s[i+1]]
    #         i+= 2
    #     else:
    #         total += roman[s[i]]
    #         i+=1
    # return total
    
############### Optimal  #################

    roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    total = 0

    for i in range(len(s)):
        if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
            total -= roman[s[i]]
        else:
            total += roman[s[i]]
    
    return total

print(romanToInt("IV"))
print(romanToInt("XI"))

