
def half_diamond_star(n):

    # for i in range(n):
    #     for j in range(i+1):
    #         print("*", end="")
    #     print()
    # for i in range(n-1):
    #     for j in range(n-i-1):
    #         print("*", end="")
    #     print()
###################

    for i in range(2*n):
        stars = i

        if i > n:
            stars = 2*n-i

        for j in range(stars):
            print("*", end=" ")
        print()

### Optimize way ########

    # for i in range(1, n+1):
    #     print("*" * i)
    # for i in range(n-1, 0, -1):
    #     print("*" * i)

half_diamond_star(5)