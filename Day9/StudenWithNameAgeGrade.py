
class Student:
    def __init__(self, name, age, grade) -> None:
        self.name = name
        self.age = age
        self.grade = grade

    def __repr__(self) -> str:
        return f"Name is {self.name}, Age is {self.age}, Grade is {self.grade}"


st1 = Student("akash", 30, "A")
st2 = Student("Palash", 27, "A+")

print(st1)
print(st2)


