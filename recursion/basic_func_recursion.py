def basic_recursion(count):
    print(count)
    if count == 3:
        return 
    basic_recursion(count + 1)

basic_recursion(0)