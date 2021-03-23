a={101:10000,102:20000,103:45000}
def check_amount_in_list(b):
    if b in a.keys():
        print(a[b])
    else:
        f=int(input("enter amount: "))
        if b not in a.keys():
            a[b]=f
            print("updated list:",a) 
j=int(input("enter id no:"))
check_amount_in_list(j)