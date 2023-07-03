def my_function(num):
    return num + num + num
number = list(map(int,input().split()))
triple_number = map(my_function,number)
print(list(triple_number))