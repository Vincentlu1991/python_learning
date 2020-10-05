
try:
#   value = 10/0
    number = int(input("Enter a number "))
    print(number)

#只抓ZeroDivisionError
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)