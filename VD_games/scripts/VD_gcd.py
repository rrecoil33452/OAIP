import random
import math

def main():
    print("Welcome to the VD Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    for _ in range(3):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        print(f"Find the greatest common divisor of given numbers.\nQuestion: {a} {b}")
        correct = math.gcd(a, b)
        answer = input("Your answer: ")
        if answer == str(correct):
            print("Correct!")
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct}.\nLet's try again, {name}!")
            break

if __name__ == "__main__":
    main()
