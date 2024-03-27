""" string datatype  """
#"""  for emoji(window+.) """
# 😊
# name="😊hello world"
# print(name)
# print(name[2])
# print(type(name))
# print(name[0:6])
# print(name[2::])


""" # cannot change string """
# name[0]=d 


""" # research(homework) """
# name="Hello world"
# print(name[::-1])

# output:dlrow olleh

""" # # interger datatype """
# number=1
# print(type(number))

# percentage=2.7
# print(type(percentage))


""" # # list """
# fruits=["apple",
#  "banana",
#   "mango",
#   1,
#   4.4
#   ]
  
# print(fruits)
# fruits[0]="chocolate"
# print(fruits)
# print(type(fruits))
# print(fruits[0][-1])


""" # tupple """
# fruits=("apple",
#  "banana",
#   "mango",
#   1,
#   4.4
# )
# print(type(fruits)) 
# print(fruits)
# print(fruits[1])
# print(fruits[0][-1])
""" tuple object doesnot change or assign """
# fruits[0]="chocolate"


""" # sets """
# a={1,2,33,2,"avd",56,1.2}
# print(a)
# a.add(5)
# print(a)
# print(type(a))


# dictionary
person={
    'name':'yug',
    'age':20,
    'city':'ktm',
    'hobbies':[
        'football',
        'basketball',
        'dancing'
    ],
    'family':(
        'jone',
        'geena',
        'rajesh'
    ),
    'friends':[
        {
        'name':'ram',
        'age':25,
        'city':'pokhara',
        'hobbies':[
        'football',
        'singing',
        'dancing'
    ],
    'family':(
        'jone',
        'geena',
        'rajesh'
    ),
}
    ]
}
# print(person['name'])
# print(person['hobbies'])

print(person['friends'[0]]['hobbies'])