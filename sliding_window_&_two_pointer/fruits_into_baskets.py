from collections import defaultdict

def totalFruits(fruits):
    n = len(fruits)

################## Brute force ################
    # maxlen = 0
    
    # for i in range(n):
    #     seen = set()
    #     for j in range(i, n):
    #         seen.add(fruits[j])

    #         if len(seen) <= 2:
    #             maxlen = max(maxlen, j-i+1)
    #         else:
    #             break
    
    # return maxlen

    # Time: O(n²)
    # Space: O(1)
    
################ Optimal-1 ####################

    maxlen = 0
    left = right = 0
    basket = defaultdict(int)

    while right < n:
        basket[fruits[right]] += 1

        while len(basket) > 2:
            basket[fruits[left]] -= 1
            if basket[fruits[left]] == 0:
                del basket[fruits[left]]
            left += 1

        # if len(basket) > 2:
        #     basket[fruits[left]] -= 1
        #     if basket[fruits[left]] == 0:
        #         del basket[fruits[left]]
        #     left += 1
        
        maxlen = max(maxlen, right - left + 1)
        right += 1
    
    return maxlen

    # Time = O(n)
    # Space = O(1)

print(totalFruits([1, 2, 3, 2, 2]))