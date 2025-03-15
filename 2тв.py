from msilib import make_id


class Person:

    def  __init__(self, name='Marsel' , surname='Sharapov' , age=17 , gender='male' ):


        self.name = name
        self.surename = name
        self.  age = age
        self.gender = gender

    def  walk(self):
        print("'Person'self.name, 'is walking'")
    def info(self):
        print(f"person{self.name} {self.surname} is {self.  age} years old.")