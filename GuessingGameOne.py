import random
c = 0
while True:
    c += 1
    a = random.randint(1, 9)
    b = int(input("Enter a number: "))
    print ("a = " + str(a))
    if b < a:
        print("Too low.")
    elif b > a:
        print("Too high.")
    else:
        print("You guessed it!")
    if (input("Type 'exit' to leave: ") == "exit"):
        print("Guesses:", c)
        break;