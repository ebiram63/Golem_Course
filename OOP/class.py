class Rectangle:
    pass

r1 = Rectangle()
r2 = Rectangle()

print(type(Rectangle))
print(type(r1))
print(type(r2))
print(id(r1), id(r2))

# Object 
x = 5
print(type(x))
#help(int) 
print(isinstance(r1, Rectangle))