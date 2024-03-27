""" USING DECORATORS """
# def star(func):
#     def wrapper():
#         print("*"*10) 
#         func()
#         print("*"*10)
#     return wrapper
# @star
# def hello():
#     print("hello")

# @star
# def bye():
#     print("bye")
   
# hello()
# bye()


""" Or """
# def star(func):
#     def wrapper():
#         print("*"*10) 
#         func()
#         print("*"*10)
#     return wrapper

# def hello():
#     print("hello")


# def bye():
#     print("bye")
   
# star(hello)()
# star(bye)()


""" without using decorstors """
# def hello():
#     print("*"*10)
#     print("hello")
#     print("*"*10)

# def bye():
#     print("*"*10)
#     print("bye")
#     print("*"*10)

# hello()
# bye()


""" USING HASH AND STAR(CW) """
# def star(func):
#     def wrapper():
#         print("*"*10) 
#         func()
#         print("*"*10)
#     return wrapper

# def hash(func):
#     def wrapper():
#         print("#"*10) 
#         func()
#         print("#"*10)
#     return wrapper
# @hash
# @star
# def hello():
#     print("hello")

# @hash
# @star
# def bye():
#     print("bye")
   
# hello()
# bye()









