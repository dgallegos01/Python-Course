# we will learn about constructors
# this class from previous code should have a constructor
class Point: 
    # this 'init' method will intialize our objects. also known as a constructor
    def __init__(self, x, y): # 'init' stands for initialize. this is the method that gets called when we get a new 'Point' object
        self.x = x # 'self' is a reference to the current object
        self.y = y

    def move(self): 
        print("move")
    def draw(self):
        print("draw")

# 10 and 20 will be set to x and y in the costructor
point = Point(10, 20) # when we create a new point object, 'self' references that object in memory
point.x = 11 # this updates x to 11
print(point.x)
