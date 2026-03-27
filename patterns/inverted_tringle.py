def inverted_triangle(n):
    for i in range(n):
        for j in range(n-i):
            print("*", end=" ")
        print()

inverted_triangle(5)