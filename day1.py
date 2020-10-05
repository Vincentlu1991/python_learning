from math import *

phrase = "Abcd123"

#输出index为0位置的字母
print(phrase[0])

#输出b所在的index的值
print(phrase.index("b"))

#将A换成O并输出,但并不会修改phrase
print(phrase.replace("A","O"))

#Numbers 学习
#先乘除后加减
print(2+6/2)
print(3*(4+5))

#取余数
print(10 % 3)

#Abs 绝对值
my_num = -5
print(abs(my_num))

#pow 幂计算
print(pow(4,6))

#Max、Min取最大值
print(max(2,6))
print(min(2,6))

#round四首五入
print(round(3.7))

print(floor(3.7))
print(ceil(3.7))
print(sqrt(36))

#input 默认是String
name = input("Please enter your name ")
print("hello" + " " + name)

num1 = input("Please enter a number ")
num2 = input("Please enter a number ")
result = float(num1) + float(num2)
print(result)

