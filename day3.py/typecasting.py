# changing one type to another
pie=3.14
pie="3.12"
pie=int(pie)
print(pie)
pie=int(pie)
print(pie)
print(type(pie))

# it doesnot change string character to integer
a="acf23"
a=int(a)


""" Boolen """
# true or false


"""HW  """
# islogin=False
# print(type(islogin))


# task
# convert bool to integer....

fruits=[
    'apple',
    'kiwi',
    'banana'
]
print(fruits)
print(type(fruits))
fruits[0]='mango'

fruits=tuple(fruits)





fruits=(
    'apple',
    'kiwi',
    'banana'
)
print(before)
print(fruits)
fruits=list(fruits)
print(after)
print(fruits)
