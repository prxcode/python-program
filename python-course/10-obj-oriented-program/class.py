class Employee: 
    language = "Python" # This is a class attribute
    salary = 1500000


john = Employee()
john.name = "john" # This is an instance attribute
print(john.name, john.language, john.salary)

arthur = Employee()
arthur.name = "arthur"
print(arthur.name, arthur.salary, arthur.language)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class