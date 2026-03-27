def number_spuare_decrease(n):
    for i in range(2*n - 1):
        for j in range(2*n - 1):
            top = i
            left = j
            right = (2*n-2) - j
            bottom = (2*n - 2) - i
            print(n- min(top, left, right, bottom), end=" ")
        print()

number_spuare_decrease(4)