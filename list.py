#list 学习

friends =["kevin","lu","Jim","Toby","Oscar"]
#            0      1    2     3      4
print(friends[0])

#列出从1到2 去尾
print(friends[1:3])
#结果： ['lu', 'Jim']

#添加element 在末尾
friends.append("creed")
print(friends)

#添加element到特定位置
friends.insert(1,"killer")
print(friends)

#删除
friends.remove("killer")
#使用del 删除
del friends[0]

#全删除
#firends.clear()

#pop 删除最后一个element
friends.pop()
print(friends)

#取element的index
print(friends.index("kevin"))

#count() element重复多少次
print(friends.count("killer"))

#sort() Acending order
#reverse()列表顺序倒过来
#copy() 复制
friends2=friends.copy()
print(friends2)

#list index放-1 会返回列表最后一个元素
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[-1])
#print out 'specialized'

