class fita:
    
    institute="FITA_ACADEMY"
    location="palikarani"
    course="advance python"

#constructor method
    def __init__(self,name,age,deg,yog,per):
        self.name=name
        self.age=age
        self.deg = deg
        self.yog=yog
        self.per=per
       
#object method
    def studentdetails(self):
        print(self.name,end=" ")
        print(self.age,end=" ")
        print(self.deg,end=" ")
        print(self.yog,end=" ")
        print(self.per)

#class method
    @classmethod
    def institutedetails(cls):
        print(cls.institute)
        print(cls.location)
        print(cls.course)

#static method
    @staticmethod
    def reversename(name):
       
        r=""
        for i in name:
            r=i+r
        return r
        
s1=fita ("santoo",20,"b.tech",2026,79)
s1.studentdetails()
s2=fita ("rio",22,"b.tech",2025,99)
s3=fita ("deva",25,"BE",2026,89)
s2.studentdetails()
s3.studentdetails()

#class method call
fita.institutedetails()



print("name:",s2.name,s1.age,s1.deg,s1.yog,s1.per)
#static method call
print(s1.reversename(s1.name))


