# def binary_number_triangle(n):
#     start = 1

#     for i in range(n):
#         if i % 2 == 0:
#             start = 1
#         else:
#             start= 0
        
#         for _ in range(i+1):
#             print(start, end=" ")
#             start = 1 - start
#         print()

############# Optimize ######################

def binary_number_triangle(n):
    for i in range(n):
        for j in range(i + 1):
            print((i + j) % 2, end=" ")
        print()

# Time = O(n²)
# Space = O(1)

binary_number_triangle(5)