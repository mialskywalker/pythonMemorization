num_of_movies = int(input())

highest = 0
highest_name = ""
lowest = 10
lowest_name = ""
average = 0

for _ in range(num_of_movies):

    name = input()
    rating = float(input())

    if rating > highest:
        highest = rating
        highest_name = name
    elif rating < lowest:
        lowest = rating
        lowest_name = name
    average += rating

average /= num_of_movies

print(f"{highest_name} is with highest rating: {highest}\n"
      f"{lowest_name} is with lowest rating: {lowest}\n"
      f"Average rating: {average:.1f}")
