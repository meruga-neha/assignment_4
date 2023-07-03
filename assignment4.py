def my_function(num):
    return num + num + num
number = list(map(int,input('enter the list of numbers:').split()))
triple_number = map(my_function,number)
print('list of triple numbers:',(list(triple_number)))