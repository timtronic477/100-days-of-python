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

def d_hit():
    d.append(deck[r()])

def board():
    print(f"Your cards: {p}, current score: {sum(p)}")

def bust():
    print(f"Your final hand: {p}, final score: {sum(p)}")
    print(f"Computer's final hand: {d}, final score {sum(d)}.")
    print("You went over, you lose :(")

def d_bust():
    print(f"Your final hand: {p}, final score: {sum(p)}")
    print(f"Computer's final hand: {d}, final score {sum(d)}.")
    print("Computer went over, you win :)")

def tie():
    print(f"Your final hand: {p}, final score: {sum(p)}")
    print(f"Computer's final hand: {d}, final score {sum(d)}.")
    print("You scored the same, Tie")

def win():
    print(f"Your final hand: {p}, final score: {sum(p)}")
    print(f"Computer's final hand: {d}, final score {sum(d)}.")
    print("You scored the higher, you win :)")

def lose():
    print(f"Your final hand: {p}, final score: {sum(p)}")
    print(f"Computer's final hand: {d}, final score {sum(d)}.")
    print("Computer scored the higher, you lose :(")

def play():
    pl = input("you want to play a game of Blackjack? Type 'y' or 'n': ")
    if pl == 'y':
        blackjack()
    else:
        return

def clear():
    p.clear()
    d.clear()

def check():
    if sum(p) > 21 and 11 in p:
       p[p.index(11)] = 1

def d_check():
    if sum(d) > 17 and 11 in d:
       d[d.index(11)] = 1
    soft_17()

def soft_17():
    while sum(d) < 17:
        d_hit()

def compare():
    if sum(d) == sum(p):
        tie()
    if sum(p) > sum(d):
        win()
    if sum(p) < sum(d):
        lose()

def aces():
    soft_17()
    d_check()

def blackjack():
    money_on_table = True
    deal()
    board()
    print(f"Computer's first card: {d}")
    while money_on_table:
        h = input("Type 'y' to get another card, type 'n' to pass: ")
        if h == 'y':
            hit()
            check()
            if sum(p) > 21:
                bust()
                money_on_table = False
                clear()
                play()
            else:
                board()
        else:
            aces()
            if sum(d) > 21:
                d_bust()
                money_on_table = False
                clear()
                play()
            else:
                compare()
                money_on_table = False
                clear()
                play()


blackjack()