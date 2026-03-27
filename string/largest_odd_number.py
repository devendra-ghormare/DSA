def largestOddNumber(num):

    for i in range(len(num) - 1, -1, -1):
        if num[i] in "13579":
            return num[:i+1]
    
    return ""


print(largestOddNumber("52"))