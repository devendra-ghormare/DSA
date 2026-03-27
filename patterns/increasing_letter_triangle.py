
def increasing_letter_triangle(n):
    for i in range(n):
        for j in range(i):
            print(chr(ord('A') + j), end=" ")
        print()

increasing_letter_triangle(6)


##############################3
# import string
# def increasing_letter_triangle(n):
#     for i in range(n):
#         for j in range(i):
#             print(string.ascii_uppercase[j], end=" ")
#         print()

# increasing_letter_triangle(6)