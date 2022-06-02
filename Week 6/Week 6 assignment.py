# Week 6 normal assignment
# import requests
#
# search_term = input("Please enter a search term: ")
# r = requests.get(f"https://itunes.apple.com/search?term={search_term}")
# json = r.json()
#
# resultcount = json["resultCount"]
# print(f"The search returned {resultcount} results.")
#
# for result in json["results"]:
#     artist_name = result["artistName"]
#     album_name = result["collectionName"]
#     track_count = result["trackCount"]
#     print(f"Artist: {artist_name} - Album: {album_name} - Track_count: {track_count}")


# Week 6 Bonus assignment
import random
import math

points_in_circle = 0
for _ in range(10000):
    x = random.random()
    y = random.random()
    xy = [x, y]
    if (x ** 2 + y ** 2) < 1:
        points_in_circle += 1


calculated_pi = points_in_circle*4/10000
pi_from_math = math.p
print(f"Calculated value of π: {calculated_pi}")
print(f"Value of π from math library: {math.pi}")
print(f"Difference: {calculated_pi - pi_from_math}")



