def isIsomorphic(s:str, t:str):
    if len(s) != len(t):
        return False
    
    mpp_st = {}
    mpp_ts = {}

    for c1, c2 in zip(s, t):
        if c1 in mpp_st and mpp_st[c1] != c2:
            return False
        
        if c2 in mpp_ts and mpp_ts[c2] != c1:
            return False
        
        mpp_st[c1] = c2
        mpp_ts[c2] = c1
    
    return True

print(isIsomorphic("egg", "add"))