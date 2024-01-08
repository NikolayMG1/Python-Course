# def f():
#     for i in range(1,10):
#         print(i)

# f()   

# print(x // 3 for i in [1,2,3,4,5,6,7,8,9][-1] if i % 2)

 # Define the value of x (for example)
result = [i // 3 for i in [1, 2, 3, 4, 5, 6, 7, 8, 9][::-1] if i % 2]
print(result)

