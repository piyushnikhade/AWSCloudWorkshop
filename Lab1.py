# taking two inputs at a time
x= int(input("Enter X value: "))
y= int(input("Enter Y value: "))
print("Value of X= ", x)
print("Value of Y= ", y)

def minus():
    print ("Which Operation you would like to perform")
    print ("1: X-Y 2: Y-X")
    p= int(input("Operation: "))
    if (p==1):
        return x-y
    else:
        return y-x
def add():
    return x+y
def mult():
    return x*y
def power():
    print ("Which Operation you would like to perform")
    print ("1: X**Y 2: Y**X")
    p= int(input("Operation: "))
    if (p==1):
        return x**y
    else:
        return y**x
def divide():
    print ("Which Operation you would like to perform")
    print ("1: X/Y 2: Y/X")
    p= int(input("Operation: "))
    if (p==1):
        return x/y
    else:
        return y/x
    
def default():
    return x+y
switcher ={
    0:minus,
    1:add,
    2:mult,
    3:power,
    4:divide
    }

def operation(op):
    return switcher.get(op,default)()

print ("0: Minus, 1:Addition, 2:Multiplication, 3:Power, 4:Divide")
z= int(input("Enter Operation Number: "))
print (operation(z))
