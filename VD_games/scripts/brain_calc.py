import random

def main():
    print("Welcome to the VD games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    for _ in range(3):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        op = random.choice(['+', '-', '*'])
        expr = f"{a} {op} {b}"
        correct = eval(expr)
        print(f"Question: {expr}")
        answer = input("Your answer: ")
        if answer == str(correct):
            print("Correct!")
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct}.\nLet's try again, {name}!")
            break

if __name__ == "__main__":
    main()
