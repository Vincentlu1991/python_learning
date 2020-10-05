#Functions

#define a function
def say_hi(name,age):
    print("hello user "+name, ", you are " + str(age))

#call the function
say_hi("mike",35)

#Ruturn 一个值
def cube(num):
    return num*num*num

result = cube(4)
print(result)
print(cube(3))