from Student import Student #from student file, it will import student class

student1 = Student("Jim", "Business", 3.1, False)   #creating an object
student2 = Student("Pam", "Art", 2.5, True)         #we pass the values to __init__ function

print(student1.name)                                #acess the variables inside Student class
print(student2.name)
