import math


def calculate_circle_area(diameter):
    radius = diameter / 2
    area_cm2 = math.pi * radius * radius
    return area_cm2


def calculate_rectangle_area(length, width):
    area_cm2 = length * width
    return area_cm2


def calculate_triangle_area(base, height):
    area_mm2 = (base * height) / 2
    return area_mm2


def convert_area_to_m2_cm2_mm2(area_cm2):
    area_m2 = area_cm2 / 10000
    area_mm2 = area_cm2 * 100
    return area_m2, area_cm2, area_mm2


def main():
    # Input for the circle
    diameter = int(input("Input the diameter of the circle (cm): "))
    circle_area_cm2 = calculate_circle_area(diameter)

    # Input for the rectangle
    length = float(input("Input the length of the rectangle (cm): "))
    width = float(input("Input the width of the rectangle (cm): "))
    rectangle_area_cm2 = calculate_rectangle_area(length, width)

    # Input for the triangle
    base = float(input("Input the base of the triangle (mm): "))
    height = float(input("Input the height of the triangle (mm): "))
    triangle_area_mm2 = calculate_triangle_area(base, height)

    # Convert areas
    circle_area_m2, circle_area_cm2, circle_area_mm2 = convert_area_to_m2_cm2_mm2(circle_area_cm2)
    rectangle_area_m2, rectangle_area_cm2, rectangle_area_mm2 = convert_area_to_m2_cm2_mm2(rectangle_area_cm2)
    triangle_area_m2 = triangle_area_mm2 / 1000000  # Convert mm^2 to m^2
    triangle_area_cm2 = triangle_area_mm2 / 100  # Convert mm^2 to cm^2

    # Print the results
    print(
        f"The area of the circle is {int(circle_area_m2)}m^2, {int(circle_area_cm2)}cm^2 and {circle_area_mm2:.2f}mm^2.")
    print(
        f"The area of the rectangle is {int(rectangle_area_m2)}m^2, {int(rectangle_area_cm2)}cm^2 and {rectangle_area_mm2:.2f}mm^2.")
    print(
        f"The area of the triangle is {int(triangle_area_m2)}m^2, {int(triangle_area_cm2)}cm^2 and {triangle_area_mm2:.2f}mm^2.")


if __name__ == "__main__":
    main()

    #The task involves creating a shape calculator that prompts for user inputs to compute and convert areas of a circle,
    # rectangle, and triangle while ensuring clear output formatting.

    # the chat history with GenAI

    # You have been tasked to create a shape calculator to compute the areas of three shapes; a
    # circle, a rectangle, and a triangle. For each shape, the user will be providing the following input:
    # • For the circle, the user will enter the diameter as an integer in centimetres.
    # • For the rectangle, the user will enter the length and the width as real numbers in centimetres.
    # • For the triangle, the user will enter the base and the height as real numbers in millimetres.
    # Create a Python file named calc_shapes.py in which you will need to prompt the user for input and
    # calculate the area of each shape. The formulae for calculating the areas are:
    # • For the circle, Pi * r * r
    # • For the rectangle, length * width
    # • For the triangle, (base * height) / 2
    # When collecting the input, please prompt the user with the following messages:
    # "Input the diameter of the circle (cm): "
    # "Input the length of the rectangle (cm): "
    # "Input the width of the rectangle (cm): "
    # "Input the base of the triangle (mm): "
    # "Input the height of the triangle (mm): "
    # Once the areas are calculated, you will need to print the area of each shape in the format of m^2,
    # cm^2 and mm^2. For example, if the area of a particular shape is 10356.4902cm^2, it can also be
    # represented as 1m^2, 356cm^2 and 49.02mm^2. An example of the expected output is:
    # The area of the circle is 1m^2, 356cm^2 and 49.02mm^2.
    # The area of the rectangle is 21m^2, 86cm^2 and 46.00mm^2.
    # The area of the triangle is 8m^2, 3163cm^2 and 5.73mm^2.

# Here's a Python program that calculates the areas of a circle, rectangle, and triangle based on the user input.
# You can save this code in a file named `calc_shapes.py`.
#
# import math
#
# Function Definitions
# def calculate_circle_area(diameter):
#     radius = diameter / 2
#     area_cm2 = math.pi * radius * radius
#     return area_cm2
#
# Function to calculate rectangle area
# def calculate_rectangle_area(length, width):
#     area_cm2 = length * width
#     return area_cm2
#
# Function to calculate triangle area
# def calculate_triangle_area(base, height):
#     area_mm2 = (base * height) / 2
#     return area_mm2
#
# Function to convert areas
# def convert_area_to_m2_cm2_mm2(area_cm2):
#     area_m2 = area_cm2 / 10000
#     area_mm2 = area_cm2 * 100
#     return area_m2, area_cm2, area_mm2
#
# Main function
# def main():
#     # Input for the circle
#     diameter = int(input("Input the diameter of the circle (cm): "))
#     circle_area_cm2 = calculate_circle_area(diameter)
#
#     # Input for the rectangle
#     length = float(input("Input the length of the rectangle (cm): "))
#     width = float(input("Input the width of the rectangle (cm): "))
#     rectangle_area_cm2 = calculate_rectangle_area(length, width)
#
#     # Input for the triangle
#     base = float(input("Input the base of the triangle (mm): "))
#     height = float(input("Input the height of the triangle (mm): "))
#     triangle_area_mm2 = calculate_triangle_area(base, height)
#
#     # Convert areas
#     circle_area_m2, circle_area_cm2, circle_area_mm2 = convert_area_to_m2_cm2_mm2(circle_area_cm2)
#     rectangle_area_m2, rectangle_area_cm2, rectangle_area_mm2 = convert_area_to_m2_cm2_mm2(rectangle_area_cm2)
#     triangle_area_m2 = triangle_area_mm2 / 1000000  # Convert mm^2 to m^2
#     triangle_area_cm2 = triangle_area_mm2 / 100  # Convert mm^2 to cm^2
#
#     # Print the results
#     print(f"The area of the circle is {int(circle_area_m2)}m^2, {int(circle_area_cm2)}cm^2 and {circle_area_mm2:.2f}mm^2.")
#     print(f"The area of the rectangle is {int(rectangle_area_m2)}m^2, {int(rectangle_area_cm2)}cm^2 and {rectangle_area_mm2:.2f}mm^2.")
#     print(f"The area of the triangle is {int(triangle_area_m2)}m^2, {int(triangle_area_cm2)}cm^2 and {triangle_area_mm2:.2f}mm^2.")
#
# Entry point of the program
# if __name__ == "__main__":
#     main()

