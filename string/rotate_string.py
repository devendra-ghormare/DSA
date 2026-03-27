def rotateString(s:str, goal:str):
    if len(s) != len(goal):
        return False

############ Brute Force ###########
   
    # for _ in range(len(s)):
    #     if s == goal:
    #         return True
        
    #     s = s[1:] + s[0]
    
    # return False

########### Optimal Approach ########

    doube_s = s + s 

    if goal in doube_s:
        return True
    else:
        return False
print(rotateString(s = "abcde", goal = "cdeab"))
print(rotateString(s = "abcde", goal = "abced"))

