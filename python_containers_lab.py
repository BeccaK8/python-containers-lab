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


# Exercise 5
print( "\nExercise 5: \n")

for key, val in home_town.items():
    print( f"{key} = {val}")


# Exercise 6
print( "\nExercise 6: \n")

cohort = []
for index, student in enumerate(students):
    student_food = {}
    student_food['student'] = student
    student_food['fav_food'] = foods[index]
    cohort.append(student_food)

for student in cohort:
    print(f"{student['student']} - {student['fav_food']}")