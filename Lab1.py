
# taking three inputs at a time
x= int(input("Enter X value: "))
y= int(input("Enter Y value: "))
z = int(input("Enter Z value:"))
print("Value of X= ", x)
print("Value of Y= ", y)
print("Value of Z= ", z)

def minus():
    print ("Which Operation you would like to perform")
    print ("1: X-Y 2: Y-X 3: Z-X 4: Z-Y 5: X-Z 6: Y-Z")
    p= int(input("Operation: "))
    if (p==1):
        return x-y
    if (p==2):
        return y-x
    if (p==3):
        return z-x
    if (p==4):
        return z-y
    if (p==5):
        return x-z
    else:
        return y-z
def add():
    print ("Which Operation you would like to perform")
    print("1 X+Y 2: Z+X 3: Z+Y ")
    p=int(input("Operation: "))
    if (p==1):
        return x+y
    if (p==2):
        return z+x
    else:
        return z+y
def mult():
    print("Which Operation would you like to perform")
    print("1: X*Y 2: Z*X 3: Z*Y")
    p=int(input("Operation: "))
    if (p==1):
      return x*y
    if (p==2):
      return z*x
    else:
      return z*y
def power():
    print ("Which Operation you would like to perform")
    print ("1: X**Y 2: Y**X 3: Z**X 4: Z**Y 5: X**Z 6: Y**Z")
    p= int(input("Operation: "))
    if (p==1):
        return x**y
    if (p==2):
        return y**x
    if (p==3):
        return z**x
    if (p==4):
        return z**y
    if (p==5):
        return x**z
    else:
        return y**z
def divide():
    print ("Which Operation you would like to perform")
    print ("1: X/Y 2: Y/X 3: Z/X 4: Z/Y 5: X/Z 6: Y/Z")
    p= int(input("Operation: "))
    if (p==1):
        return x/y
    if (p==2):
        return y/x
    if (p==3):
        return z/x
    if (p==4):
        return z/y
    if (p==5):
        return x/z
    else:
        return y/z
def default():
    x+y+z
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
z1= int(input("Enter Operation Number: "))
print (operation(z1))
