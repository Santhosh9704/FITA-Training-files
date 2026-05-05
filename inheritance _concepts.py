'''
# single level inheritance :(single parent and child)
class company:

    staff=100

    def details(self):
        print("Top most compant")
        
class BNT(company):
    student=150

company1=BNT()
print(company1.staff)
print(company1.student)
company1.details()
'''
# multiple level inheritance :("single parent and multiple child class")

class company: # parent class
    
    staff=100

    def about(self):
        print("Top most company")

class FITA(company): # child class 1
    students=200

class wipro(company): #child class 2
    students=300

company1=FITA
company2=wipro

print(company1.students)
print(company2.students)

