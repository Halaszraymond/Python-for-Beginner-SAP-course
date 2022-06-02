# first_name = str(input("Please enter the given name of the student: "))
# surname = str(input("Please enter the surname of the student: "))
# field = str(input("Please enter the field of study of the student: "))
#
# student = (first_name, surname, field)
# print(student)
#
# emoji_dict = {
#     "happy": "😃",
#     "heart": "😍",
#     "rotfl": "🤣",
#     "smile": "😊",
#     "crying": "😭",
#     "kiss": "😘",
#     "clap": "👏",
#     "grin": "😁",
#     "fire": "🔥",
#     "broken": "💔",
#     "think": "🤔",
#     "excited": "🤩",
#     "boring": "🙄",
#     "winking": "😉",
#     "ok": "👌",
#     "hug": "🤗",
#     "cool": "😎",
#     "angry": "😠",
#     "python": "🐍",
# }
# sentence = input("Please enter a sentence: ")
# words = sentence.split()
# new_list = []
# for word in words:
#     if word in emoji_dict:
#         word = emoji_dict[word]
#         new_list.append(word)
#     else:
#         new_list.append(word)
# new_sentence = " "
# print(new_sentence.join(new_list))

# caesar = True
# while caesar:
#     list_of_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#                     'u', 'v', 'w', 'x', 'y', 'z']
#     shifts = input("Please enter the number of places to shift: ")
#     if not shifts.isdecimal():
#         print("You need to enter a number between 0 and 25!")
#         break
#     sentence = str(input("Please enter a sentence: ")).lower()
#     sentence_list = list(sentence)
#     new_sentence = []
#     if 25 >= int(shifts) >= 0:
#         for char in sentence_list:
#             if char in list_of_char:
#                 char_num = list_of_char.index(char)
#                 char_num += int(shifts)
#                 if char_num % 26 >= 1:
#                     char_num -= 26
#                 new_char = list_of_char[char_num]
#                 new_sentence.append(new_char)
#             else:
#                 new_sentence.append(char)
#         new_string = "".join(new_sentence)
#         print(f"The encrypted sentence is: {new_string}")
#     else:
#         print("You need to enter a number between 0 and 25!")
