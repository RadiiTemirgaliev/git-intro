# create class
class Rectangle:

    # create a constructor method
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width


    # create an object method
    def get_area(self):
        return self.height * self.width

rectangle_1 = Rectangle(2, 4)
rectangle_2 = Rectangle(2, 6)

print(rectangle_1.get_area())
print(rectangle_2.get_area())