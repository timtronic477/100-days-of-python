import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

p = []
d = []
def r():
    return random.randint(0, 12)

def deal():
    p.append(deck[r()])
    p.append(deck[r()])
    d.append(deck[r()])

def hit():
    p.append(deck[r()])

def board():
    print(f"Your cards: {p}, current score: {sum(p)}")

def bust():
    print(f"Your final hand: {p}, final score: {sum(p)}")
    print(f"Computer's final hand: {d}, final score {sum(d)}.")
    print("You went over, you lose :(")

def play():
    pl = input("you want to play a game of Blackjack? Type 'y' or 'n': ")
    if pl == 'y':
        blackjack()
    else:
        return
def clear():
    p.clear()
    d.clear()

def blackjack():
    money_on_table = True
    deal()
    board()
    print(f"Computer's first card: {d}")
    while money_on_table:
        h = input("Type 'y' to get another card, type 'n' to pass: ")
        if h == 'y':
            hit()
            if sum(p) > 21:
                bust()
                money_on_table = False
                clear()
                play()
            else:
                board()
blackjack()