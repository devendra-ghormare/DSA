def inverted_triangle(n):
############### Brute Force #############

    # for i in range(n):
    #     for _ in range(n-i):
    #         print("*", end=" ")
    #     print()

############ Optimized version ###########
    for i in range(n):
        print("*" * (n-i))

    # Time = O(n²)
    # Space = O(1)

inverted_triangle(5)