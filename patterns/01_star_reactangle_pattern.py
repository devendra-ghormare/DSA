def star_rectangle(n):

########### Brute Force ##################
    # for i in range(n):
    #     for i in range(n):
    #         print("*", end=" ")
    #     print()

########## Optimized version #############
    for _ in range(n):
        print("*" * n)

star_rectangle(6)