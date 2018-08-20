students=[]


class Student:
    school_name="SDA"

    def __init__(self, name, student_id=323, last_name=""):

        self.name=name
        self.student_id=student_id
        self.last_name=last_name
        students.append(self)  # Appending to students list

    # Override method to avoid errors when printing class instance - mark
    def __str__(self):
        return "Student "+self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_last_name_capitalize(self):
        return self.last_name.capitalize()

    def get_school_name(self):
        return self.school_name
