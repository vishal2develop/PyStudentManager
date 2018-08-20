students=[]
class Student:
    school_name="SDA"
    # Replace pass with your code
    # self is used to call a function from inside the same function
    #def add_student(self, name, student_id=332):
     #   student = {"name": name, "student_id": student_id}
      #  students.append(student)

    def __init__(self, name, student_id=323):
        #student = {"name": name, "student_id": student_id}
        #Replacing student dictionary
        self.name=name
        self.student_id=student_id
        #students.append(student)
        #Appending to students list
        students.append(self)

    # Override method to avoid errors when printing class instance - mark
    def __str__(self):
        return "Student "+self.name

    def get_name_capitalize(self):
        return self.name.capitalize()


# mark = Student("mark")
    def get_school_name(self):
        return self.school_name

#Inheritance
class HighSchoolStudent(Student):
    school_name = "High School SDA"
    def get_school_name(self):
        return "This is a highschool student"

    def get_name_capitalize(self):
        original_value=super().get_name_capitalize()
        return original_value+ " -HS"

james=HighSchoolStudent("james")
print(james.get_name_capitalize())
print(james.get_school_name())







