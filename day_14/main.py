import random
from data import data
from art import logo, vs


def gen_data():
    r = random.randint(0, 49)
    return [data[r]["name"],data[r]["follower_count"], data[r]["description"], data[r]["country"]]

def start():
    name1, followers1, description1, country1 = gen_data()
    name2, followers2, description2, country2 = gen_data()
    print(f"Compare A: {name1} a {description1}, from {country1}.")
    print(vs)
    print(f"Compare A: {name2} a {description2}, from {country2}.")

def check(a, b):
    return "A" if int(a) > int(b) else "B"


def game():
    print(logo)
    score = 0
    name1, followers1, description1, country1 = gen_data()
    name2, followers2, description2, country2 = gen_data()
    print(f"Compare A: {name1} a {description1}, from {country1}.")
    print(vs)
    print(f"Compare A: {name2} a {description2}, from {country2}.")
    ans = input("Who has more followers? Type 'A' or 'B': ")
    correct = check(followers1, followers2)
    if correct == "B":
        name1, followers1, description1, country1 = name2, followers2, description2, country2
    if ans == correct:
        score += 1
    while score > 0:
        print(f"Your score is {score}")
        name2, followers2, description2, country2 = gen_data()
        print(f"Compare A: {name1} a {description1}, from {country1}.")
        print(vs)
        print(f"Compare A: {name2} a {description2}, from {country2}.")
        correct = check(followers1, followers2)
        ans = input("Who has more followers? Type 'A' or 'B': ")
        if ans == correct:
            score += 1
        else:
            print("\n"*20)
            print(f"Incorrect. Final score is {score}")
            score = 0
        if correct == "B":
            name1, followers1, description1, country1 = name2, followers2, description2, country2


game()