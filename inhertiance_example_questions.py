
# multiple level inhertitance example

class job:
    role="Advance python"
    
    def detail(self):
        print("Employee  details")
        
class emp1(job):
    name="rio"
    age=22
    salary=100000
    
class emp2(job):
    name="santoo"
    age=21
    salary=80000

e1=emp1
e2=emp2


print("Employee name:",e1.name,"AGE:",e1.age,"salary:",e1.salary , e1.role)
print("Employee name:",e2.name,"AGE:",e2.age,"salary:",e2.salary, e2.role)
