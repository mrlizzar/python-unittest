width =int (input("Enter the width of the rectangle: "))
assert width >= 0, "The width must be greater than or equal to 0"
height = int(input("Enter the height of the rectangle: "))
assert height >= 0, "The height must be greater than or equal to 0"

area = width * height
print(f"The area of the rectangle is {area}")
