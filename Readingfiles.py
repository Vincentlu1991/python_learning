# open("filename")
# open("filename"."r") read only
# open("filename"."w") write
# open("filename"."a") append 添加

#只读
employee_file = open("employee.txt", "r")
print(employee_file.readlines()[0])
employee_file.close()

#添加数据
employee_file = open("employee.txt", "a")
employee_file.write("\nLu - LuWeiXiong")
employee_file.close()

#Override the file
employee_file = open("employee.txt", "w")
employee_file.write("\nLu - LuWeiXiong")
employee_file.close()