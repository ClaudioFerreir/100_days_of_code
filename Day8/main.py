# def greet():
#     print("Hello World!")
#     print("name")
#     print("age")

# greet()

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")
#
# greet_with(location="Nowhere", name="John")

# print("name" + "oi")

def calculate_love_score(name1, name2):
    true_letters = ["T", "R", "U", "E"]
    love_letters = ["L", "O", "V", "E"]

    names = (name1 + name2).upper()
    true_points = 0
    love_points = 0

    for letter in names:
        if letter in true_letters:
            true_points += 10

        if letter in love_letters:
            love_points += 1

    love_score = true_points + love_points

    print(love_score)


calculate_love_score("Kanye West", "Kim Kardashian")