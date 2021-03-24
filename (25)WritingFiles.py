
#open file
employee_file = open("employees.txt", "a") #a will append at the back of the file line
                                           #w will write a new file or overwrite the file

#write to the file
employee_file.write("\nToby - Human Resources")

#close the file
employee_file.close()