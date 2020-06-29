total_people = int(input())
starting_infected = int(input())
spread_rate = int(input())
total_happy_people = starting_infected
day = 0

while total_happy_people <= total_people:
   total_happy_people += starting_infected*spread_rate
   starting_infected = (starting_infected * spread_rate)
   day += 1

print(day)
