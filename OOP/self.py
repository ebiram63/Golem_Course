class Rectangle:
    #method
    def perimeter(self):
        return f"perimeter, {id(self)}"
    def area(self):
        return f"area, {id(self)}"
    
r1 = Rectangle()
r2 = Rectangle()
print(r1.area())#, Rectangle.area(r1))
print(r2.area())
print(r2.perimeter())