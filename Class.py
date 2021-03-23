class d:
    def __init__(self, name, id, roll):
        self.name = name
        self.id = id
        self.roll = roll
    def student_name(self):
        print(self.name)
std = d("abhiroop","std01",1)
print(std.name, std.roll, std.id)
std.student_name()
std1=d("nayan","std02",2)
print(std1.name, std1.roll, std1.id)
std1.student_name()
