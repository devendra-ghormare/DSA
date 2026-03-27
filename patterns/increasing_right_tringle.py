def increasing_right_tringle(n):
    num = 1
    for i in range(n):
        for j in range(1, i+1):
            print(num, end=" ")
            num+=1

        print()

increasing_right_tringle(6)