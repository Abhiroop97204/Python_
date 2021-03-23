country_name_code={'IND':'INDIA','US':'UNITED STATES','UK':'UNITED KINGOM'}
def view():
    for x in country_name_code.items():
        print(x)
def add():
    b=input("Enter country code: ")
    c = input("Enter country name: ")
    u1=b.upper()
    u2=c.upper()
    country_name_code[u1]=u2
    print(country_name_code)
def delete():
    d=input("enter code you want to del: ")
    s=d.upper()
    if s in country_name_code.keys():
        del country_name_code[s]
        print(country_name_code)
    else:
        print("Key not Present")

print("Welcome to Abhiroop's Country App")
print("1. Add  2. View  3. Delete")
while True:
    a = int(input("Enter your choise: "))
    if a == 1:
        add()
    elif a == 2:
        view()
    elif a == 3:
        delete()
