import math
PI = math.pi
# Write your Wheel class here
class Wheel: 
    def __init__(self, radius):
        self.radius = radius
    def wheel_area(self):
        self.area = PI * (self.radius * self.radius)
        return self.area
    def wheel_perimeter(self):
        self.perimeter = 2 * PI * self.radius
        return self.perimeter
    def swap_radius(self,new_radius):
        self.radius = new_radius
        return self.radius

if __name__ == "__main__":
    wheel = Wheel(float(input("Radius of wheel: ")))
    print("Surface area of wheel: ", wheel.wheel_area())
    print("Perimeter of wheel: ", wheel.wheel_perimeter())
    yesno = input("More wheels? Y/N")
    morewheels = yesno == 'y' or yesno == 'Y'
    while morewheels:
        radius = float(input("Radius of wheel: "))
        wheel.swap_radius(radius)
        print("Surface area of wheel: ", wheel.wheel_area())
        print("Perimeter of wheel: ", wheel.wheel_perimeter())
        yn = input("More wheels? Y/N")
        morewheels = yn == 'y' or yn == 'Y'

