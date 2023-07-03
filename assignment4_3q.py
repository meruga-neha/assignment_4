def square_function(n):
    return n * n
number = list(map(int,input('enter the list of numbers:').split()))
square_number = map(square_function,number)
print('list of square numbers:',(list(square_number)))
