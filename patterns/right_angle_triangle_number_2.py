def right_angle_triangle_number_2(n):

    for i in range(1, n+1):
        for j in range(1, i+1):
            print(i, end=" ")
           
        print()

right_angle_triangle_number_2(5)