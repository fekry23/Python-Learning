#Similar to try catch block at java
#Python use try except


try:
    value = 10/0                                     #we cant divide 0                         
    number = int(input("Enter a number : "))
    print(number)
except ZeroDivisionError as err:
    print("Error type : " + str(err))
    print("Divided by zero")
except ValueError as err:
    print("Error type : " + str(err))
    print("Invalid input")