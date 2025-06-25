class Employee: 
    language = "Python"  # Class attribute
    salary = 1200000     # Class attribute

    def __init__(self, name="Unknown", salary=salary, language=language):  # Constructor with defaults
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")
 
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


john = Employee("john", 1300000, "JavaScript") 
print(john.name, john.salary, john.language)

arthur = Employee()  # Now works without arguments
print(arthur.name, arthur.salary, arthur.language)
