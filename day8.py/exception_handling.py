# while True:
#     try:
#         a=int(input("Enter a number:"))
#         b=int(input("Enter 2nd number:"))
#         if a==5:
#             raise Exception("input cannot be 5")
#         print(a/b)
#     except ZeroDivisionError:
#         print("a number cannot divided by zero")
#     except ValueError:
#         print("input field requirement only integer")
#     except Exception as e:
#         print(f"something went wrong {e}")


""" TASK """
# number=[1,4,5,8,3,9,2]
# total_index=len(number)-1
# while True:
#     try:
#         index=int(input(f"Enter the number between o to {total_index}"))
#         print(number[index])
#     except IndexError:
#         print(f"Invalid input number must be lesser or equal to {total_index}")
#     except ValueError:
#         print("input must be only integer number")
#     except Exception as e:
#         print("something went wrong",{e})







