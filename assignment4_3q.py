def square_function(n):
    return n * n
number = list(map(int,input().split()))
square_number = map(square_function,number)
print(list(square_number))