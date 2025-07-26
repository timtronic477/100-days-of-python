def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1*n2

def div(n1, n2):
    return n1/n2

op = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator():
    should_accumulate = True
    n1 = input("What's the first number?")
    while should_accumulate:
        ope = input("What operation?")
        n2 = input("What's the second number?")
        ans = op[ope](int(n1), int(n2))
        print(f'{n1} {ope} {n2} = {ans}')
        cont = input("Do you want to continue using this number?")
        if cont == 'y':
            n1 =ans
        else:
            should_accumulate = False
            print("\n"*20)
            calculator()


calculator()
