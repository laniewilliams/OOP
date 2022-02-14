from datetime import date

class Student:

    def __init__(self,id,name,dob,grade):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__grade = grade
    

    def age(self):
        todays_date = date.today()
        self.__dob = self.__dob.split('/')
        self.__dob = todays_date.year - int(self.__dob[2])
    
    def get_age(self):
        return self.__dob


    def register(self):
        if self.__grade == 'F':
            print("Registration dates: 11/10 - 11/12")
        elif self.__grade == 'S':
            print("Registration dates: 11/7 - 11/9")
        elif self.__grade == 'Jr':
            print("Registration dates: 11/4 - 11/6")
        else:
            print("Registration dates: 11/1 - 11/3")

