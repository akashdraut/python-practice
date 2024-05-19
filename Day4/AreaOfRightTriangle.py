
def area_of_right_triangle(base, height):
    area = 0.5 * base * height
    return area


base = int(input("Enter base value: "))
height = int(input("Enter height value: "))
print("Area of triangle is: ", area_of_right_triangle(base, height))
