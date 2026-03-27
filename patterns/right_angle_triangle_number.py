def right_angle_triangle_number(n):
    for i in range( n):
        num = 1
        for j in range(i+1):
            print(num, end=" ")
            num += 1
        print()

right_angle_triangle_number(5)


################# OR #############

def right_angle_triangle_number(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
