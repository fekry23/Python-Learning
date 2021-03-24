#https://www.w3schools.com/python/python_file_handling.asp

#open file
employee_file = open("employees.txt", "r")

#it will read line by line (only one line)
print(employee_file.readline())

#it will store the lines inside a list/array
#print(employee_file.readlines())

#.read() will read all of the things inside the file
print(employee_file.read())

#close file
employee_file.close()