def inverted_number_tringle(n):

    for i in range(n):
        for j in range(n-i):
            print(j+1, end=" ")
        print()

inverted_number_tringle(5)

