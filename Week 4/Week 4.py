# list1 = []
# with open("numbers.txt", "r") as file:
#     for line in file:
#         line = line.strip()
#         line = int(line)
#         list1.append(line)
#     list1.sort(reverse=True)
#     for n in range(3):
#         print(list1[n])
#

# with open("lorem_ipsum", "w") as file:
#     for n in range(97, 123):
#         line = ""
#         char = chr(n)
#         line = line + str(char)
#         file.write(line + "\n")

# with open("even_numbers.txt", "w") as file1:
#     with open("numbers.txt", "r") as file2:
#         for number in file2:
#             number = int(number)
#             if number % 2 == 0:
#                 line = ""
#                 line = line + str(number)
#                 file1.write(line + "\n")
# print("List of even numbers created!")

# with open("invoice_data.txt", "r") as file:
#     for line in file:
#         list_of_items = []
#         line = line.split()
#         for item in line:
#             list_of_items.append(item)
#         print(f"{str(list_of_items[0]):15s}"
#               f"{int(list_of_items[1]):3d}"
#               f"{float(list_of_items[2]):7.2f}"
#               f"{float(list_of_items[2])*float(list_of_items[1]):8.2f}")
#
# secret_list = []
# secret_string = ""
# key_list = []
#
# with open("secret.txt", "r") as secret_file:
#     for secret_line in secret_file:
#         secret_line = secret_line.strip()
#         secret_list.append(secret_line)
#     secret_string.join(secret_list)
# secret_string = "".join(secret_list)
#
# with open("key.txt", "r") as key_file:
#     for key_line in key_file:
#         key_line = key_line.strip()
#         key_list.append(key_line)
#
# key_column = int(key_list[0])
# key_row = int(key_list[1])
# column_start = 0
# column_end = key_column
# row_number = 1
#
# with open("public.txt", "w") as public_file:
#     while row_number <= key_row:
#         row_number += 1
#         public_line = secret_string[column_start:column_end]
#         public_file.write(public_line + "\n")
#         column_start += key_column
#         column_end += key_column

# player_one_scores = []
# player_two_scores = []
# draw = 0
# player1_wins = 0
# player2_wins = 0
# total_sum = draw + player1_wins + player2_wins
#
# with open("player1.txt", "r") as player1_file:
#     for player1_line in player1_file:
#         player1_line = player1_line.strip()
#         player_one_scores.append(player1_line)
#
# with open("player2.txt", "r") as player2_file:
#     for player2_line in player2_file:
#         player2_line = player2_line.strip()
#         player_two_scores.append(player2_line)
#
# for number in range(100):
#     if player_one_scores[number] == player_two_scores[number]:
#         draw += 1
#     else:
#         if player_one_scores[number] == "R":
#             if player_two_scores[number] == "S":
#                 player1_wins += 1
#             else:
#                 player2_wins += 1
#         elif player_one_scores[number] == "P":
#             if player_two_scores[number] == "R":
#                 player1_wins += 1
#             else:
#                 player2_wins += 1
#         else:
#             if player_two_scores[number] == "P":
#                 player1_wins += 1
#             else:
#                 player2_wins += 1
#
# with open("results.txt", "w") as results_file:
#     results_line_player1 = ""
#     results_line_player1 += str(player1_wins)
#     results_line_player2 = ""
#     results_line_player2 += str(player2_wins)
#     results_line_draw = ""
#     results_line_draw += str(draw)
#     results_file.write(f"Player1_wins: {results_line_player1}" + "\n")
#     results_file.write(f"Player2_wins: {results_line_player2}" + "\n")
#     results_file.write(f"Draws: {results_line_draw}" + "\n")




