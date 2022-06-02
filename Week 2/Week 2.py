# star_wars_movies = [
#     ["The Phantom Menace", "Attack of the Clones", "Revenge of the Sith"],
#     ["A New Hope", "The Empire Strikes Back", "Return of the Jedi"],
#     ["The Force Awakens", "The Last Jedi", "The Rise of Skywalker"],
#     ]
#
# trilogy_choice = int(input("From which trilogy would you like to choose a movie (choose 1, 2 or 3): "))
# movie_choice = int(input(f"Which movie would you like to choose? {star_wars_movies[trilogy_choice - 1]} "
#                          f"(choose 1, 2 or 3): "))
#
# print(f"You chose {star_wars_movies[trilogy_choice - 1][movie_choice - 1]}")

# stocks = [["SAP", 106, -3.0], ["AAPL", 165, 1.25], ["TSLA", 860, 54.2], ["ORCL", 76, -0.25], ["ZM", 114, 6.2]]
# sell_list = []
#
# for i in stocks:
#     if i[2] >= 5.0:
#         sell_list.append(i[0])
#
# print(sell_list)

# rows = int(input("Please enter the number of rows in the matrix: "))
# columns = int(input("Please enter the number of columns in the matrix: "))
# list1 = []
#
# for i in range(rows):
#     list1.append([])
#     for item in range(columns):
#         value = int(input("Value: "))
#         list1[i].append(value)
#
# for i in range(rows):
#     print(f"Sum of row: {sum(list1[i])}")

