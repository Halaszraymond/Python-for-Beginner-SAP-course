# def get_student_data():
#     last_name = input("Please enter your last name: ")
#     first_name = input("Please enter your first name: ")
#     student_id = input("Please enter your student-id: ")
#     data = (last_name, first_name, student_id)
#     return data
#
#
# print(get_student_data())

# def is_even(number):
#     output = number % 2 == 0
#     return output
#
#
# for num in range(100):
#     outcome = is_even(num)
#     if outcome:
#         print(f"{num} is even")
#     else:
#         print(f"{num} is not even")

# speed_in_kmh = float(input("What is your speed in km/h: "))
#
#
# def reaction_path(speed):
#     output = speed * (3 / 10)
#     return output
#
#
# def brake_distance(speed):
#     output = (speed / 10) ** 2
#     return output
#
#
# def stopping_distance(speed):
#     reaction = reaction_path(speed)
#     brake = brake_distance(speed)
#     output = reaction + brake
#     return output
#
#
# stop_distance = stopping_distance(speed_in_kmh)
# print(stopping_distance)
#
#
# word = input("Which text should be encrypted: ")
# keyword = input("Which keyword should be used: ")
#
#
# def encrypt_letter(character, key_index):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     if character.isalpha():
#         character_index = alphabet.find(character)
#         encrypted_character_index = character_index + key_index
#         if encrypted_character_index >= 26:
#             encrypted_character_index -= 26
#         return alphabet[encrypted_character_index]
#     return character
#
#
# def calculate_shifts(letter):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     return alphabet.find(letter)
#
#
# def encrypt_text(text, a_keyword):
#     list_text = list(text.lower())
#     list_keyword = list(a_keyword.lower())
#     new_list_encrypted = []
#     counter = 0
#     for char in list_text:
#         if counter >= len(a_keyword):
#             counter = 0
#             new_list_encrypted.append(encrypt_letter(char, calculate_shifts(list_keyword[counter])))
#             counter += 1
#         else:
#             new_list_encrypted.append(encrypt_letter(char, calculate_shifts(list_keyword[counter])))
#             counter += 1
#     seperator = ""
#     return seperator.join(new_list_encrypted)
#
#
# print(encrypt_text(word, keyword))
# #
# input_integer = int(input("Up to which number do you want all prime numbers: "))
#
#
# def is_prime(integer):
#     if integer <= 1:
#         return False
#     for number in range(2, integer):
#         if integer % number == 0:
#             return False
#     return True
#
#
# def prime_list(integer):
#     list_of_prime = []
#     for number in range(integer):
#         if is_prime(number):
#             list_of_prime.append(number)
#     return list_of_prime
#
#
# list_prime_numbers = prime_list(input_integer)
# print(list_prime_numbers)
