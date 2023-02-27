name = "Karla"
age = 27
favourite_games = ["Hogwarts Legacy", "The cult of thr lamb"]
has_pets = True

# print(name, age, favourite_games, has_pets)

def hello(name: 'list[str]'):
    print(name)

hello(["karla", "ana"])