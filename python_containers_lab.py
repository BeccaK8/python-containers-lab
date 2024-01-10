# Exercise 1
print( "\nExercise 1: \n")

students = [ 'Brynlee', 'Lexi', 'Stan', 'Colby', 'Kayla' ]
print( f"Second student is {students[1]} ")
print( f"Last student is {students[-1]} ")


# Exercise 2
print( "\nExercise 2: \n")

foods = ( 'Steak', 'Green beans', 'Liver', 'Spaghetti', 'Cookies' )
for food in foods:
    print( f"{food} is a good food" )


# Exercise 3
print( "\nExercise 3: \n")

for food in foods[3:]:
    print(food)


# Exercise 4
print( "\nExercise 4: \n")

home_town = {
    'city': 'West Burlington',
    'state': 'Iowa',
    'population': 3000
}

print( f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}" )
