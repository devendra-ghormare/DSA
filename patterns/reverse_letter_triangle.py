def reverse_letter_triangle(n):
    for i in range(n):
        for j in range(n-i):
            print(chr(ord('A') + j), end=" ")
        print()

reverse_letter_triangle(6)