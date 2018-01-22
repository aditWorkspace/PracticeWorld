
class Teacher(object):


    species= "human"
    def __init__(self, nice, grade, gender):
        self.nice = nice
        self.grade = grade
        self.gender = gender

    def print_name(self):
        print(self.gender)


downing = Teacher(nice= "1", grade = '1', gender = 'she')
lafferty = Teacher(nice = '1/2', grade='2', gender= 'she')
iwata = Teacher(nice='1', grade = '3', gender = 'she')
pande = Teacher(nice = '1/4', grade = '4', gender = "she")
lee= Teacher(nice = '3/4', grade = '5', gender = "he")
padania = Teacher(nice = '1', grade = '6', gender = "he")
print(padania.grade)



padania.print_name()