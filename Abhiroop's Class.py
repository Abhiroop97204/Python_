class Abhiroop():
    def __init__(self, name, mobile, age, company):
        self.name=name
        self.mobile=mobile
        self.age=age
        self.company=company
    def show_name(self):
        print("the name of employee is: ",self.name)
    def show_mobile(self):
        print("the mobile number is :",self.mobile)
    def show_age(self):
        print("the age is :",self.age)
    def show_company(self):
        print("the company is: ",self.company)
n=input("enter your name:")
m=int(input("enter mobile:"))
b=int(input("enter age: "))
c=input("enter company:")
a=Abhiroop(n,m,b,c)
a.show_age()
a.show_name()
a.show_mobile()
a.show_company()