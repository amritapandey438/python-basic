# class house:
#     window=10
#     color="red"
#     door=5

# def get_color(self):
#     return self.color

# def set_color(self, color):
#     self.color=color  
# ram_ko_ghar=house()
# ram_ko_ghar.set_color("green")
# print(ram_ko_ghar.get_color())
# # print(ram_ko_ghar.door)    


""" method chaining """
# class pizza:
#     def dough(self):
#         print("dough")
#         return self

#     def sauce(self):
#         print("sauce")
#         return self

#     def cheese(self):
#         print("cheese")
#         return self 

#     def sausage(self):
#         print("sausage")
#         return self 

# pizza=pizza()
# pizza.dough().sausage().cheese().sauce() 



# class House:

#     def __init__(self,window,color,door):
#         self. window=window
#         self.color=color
#         self.door=door

#     def __str__(self):
#         # return self.color
#         return f"colour of house is {self.color}"    

#     def get_color(self):
#         return self.color

#     def set_color(self,color):
#         self.color=color  

# ram_ko_ghar=House(
#     window=16,
#     color="blue",
#     door=3)
# print(ram_ko_ghar)
# # ram_ko_ghar.set_color("green")
# print(ram_ko_ghar.get_color())
# # print(ram_ko_ghar.door)    




# class employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary

#     def __eq__(self, other):
#         return self.salary==other.salary

#     def __ne__(self, other):
#         return self.salary!=other.salary

#     def __le__(self, other):
#         return self.salary<=other.salary
       
#     def __ge__(self, other):
#         return self.salary>=other.salary

#     def __gt__(self, other):
#         return self.salary>other.salary  

#     def __lt__(self, other):
#         return self.salary<other.salary    

# Ram=employee("Ram", 15)    
# Durga=employee("Durga",11)    

# print(Ram.salary==Durga.salary)
# print(Ram==Durga)
# print(Ram!=Durga)
# print(Ram>Durga)
# print(Ram<Durga)
# print(Ram>=Durga)
# print(Ram<=Durga)