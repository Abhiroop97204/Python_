class circle:
    def __init__(self, radius):
        self.radius=radius
    def circle_area(self):
        print("Area is ",3.14*self.radius**2)
    def circle_circrumference(self):
        print("Cirrumference is:",2*3.14*self.radius)
x=int(input("enter radius: "))
a=circle(x)
a.circle_area()
a.circle_circrumference()
