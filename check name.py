def check_name(a):
    s=" " in a
    if s is True:
        return(f"Your name is saved as {a}")
    else:
        return(f"Your name format is invalid")    
def check_password(b):
    c=b.islower
    d=b.isupper
    e=b.isalnum
    if c and d and e is True:
        return(f"your password saves successfully")
    else:
        return("Invalid password format")

f=input("Enter your name: ")
g=input("Enter your password: ")
print(check_name(f))
print(check_password(g))


