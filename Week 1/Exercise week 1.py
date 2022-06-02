# text = "Python is the best programming language"
# text = text.upper()
# text = text.replace("best", "very best")
# print(text)
#
# name = input("What is your name?\n")
# start_city = input("In which city would you like to start?\n")
# destination_city = input("To which city would you like to go?\n")
# means_of_transportation = input("How would you like to travel?\n")
#
# print(f"{name} wants to travel from {start_city} to {destination_city} by {means_of_transportation}")
#
# first_number = int(input("Please enter the first number: "))
# second_number = int(input("Please enter the second number: "))
# third_number = int(input("Please enter the third number: "))
#
# if first_number > second_number:
#     largest_number = first_number
# elif second_number > third_number:
#     largest_number = second_number
# else:
#     largest_number = third_number
#
# print(f"The largest number is {largest_number}")

# first_triangle = int(input("Please enter the first triangle: "))
# second_triangle = int(input("Please enter the second triangle: "))
# third_triangle = int(input("Please enter the third triangle: "))
# triangle = False
#
# if first_triangle + second_triangle + third_triangle == 180:
#     if first_triangle > 0 and second_triangle > 0 and third_triangle > 0:
#         triangle = True
#     else:
#         print("Angles smaller than 0 are not valid")
# else:
#     print("The entered values are not valid")
#
# if triangle:
#     if first_triangle > 90 or second_triangle > 90 or third_triangle > 90:
#         print("Obtuse triangle")
#     elif first_triangle < 90 and second_triangle < 90 and third_triangle < 90:
#         print("Acute triangle")
#     else:
#         print("The triangle is a right triangle")

a = int(input("Please enter the value of a: "))
b = int(input("Please enter the value of b: "))
c = int(input("Please enter the value of c: "))
d = float(b**2 - 4 * a * c)

if d == 0:
    print("The quadratic equation has 1 real solution.")
elif d > 0:
    print("The quadratic equation has 2 real solutions.")
elif d < 0:
    print("The quadratic equation has 2 complex solutions.")

