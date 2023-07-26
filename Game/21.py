#this code is made by MRayan Asim
import time

print("This 21 game is made by MRayan Asim hope you will like this! 😊")
time.sleep(3)

def nearestMultiple(num):
    return num + (4 - (num % 4)) if num >= 4 else 4


def lose1():
    print("\n\nYOU LOSE!")
    print("Better luck next time!")
    exit(0)


def check(xyz):
    return all(xyz[i] - xyz[i - 1] == 1 for i in range(1, len(xyz)))


def start1():
    xyz = []
    last = 0
    while True:
        print("Enter 'F' to take the first chance.")
        print("Enter 'S' to take the second chance.")
        chance = input('> ')

        # player takes the first chance
        if chance == "F":
            while True:
                if last == 20:
                    lose1()
                else:
                    print("\nYour Turn.")
                    print("\nHow many numbers do you wish to enter?")
                    inp = int(input('> '))

                    if inp > 0 and inp <= 3:
                        comp = 4 - inp
                    else:
                        print("Wrong input. You are disqualified from the game.")
                        lose1()

                    i, j = 1, 1

                    print("Now enter the values")
                    while i <= inp:
                        a = input('> ')
                        a = int(a)
                        xyz.append(a)
                        i += 1

                    last = xyz[-1]

                    if check(xyz) == True:
                        if last == 21:
                            lose1()
                        elif inp > 10:
                            print("You entered more than 10 numbers. You are disqualified from the game.")
                            lose1()
                        else:
                            while j <= comp:
                                xyz.append(last + j)
                                j += 1
                            print("Order of inputs after computer's turn is: ")
                            print(xyz)
                            last = xyz[-1]
                    else:
                        print("\nYou did not input consecutive integers.")
                        lose1()

        elif chance == "S":
            comp = 1
            last = 0
            while last < 20:
                j = 1
                while j <= comp:
                    xyz.append(last + j)
                    j += 1
                print("Order of inputs after computer's turn is:")
                print(xyz)
                if xyz[-1] == 20:
                    lose1()
                else:
                    print("\nYour turn.")
                    print("\nHow many numbers do you wish to enter?")
                    inp = input('> ')
                    inp = int(inp)
                    if inp > 10:
                        print("You entered more than 10 numbers. You are disqualified from the game.")
                        lose1()
                    print("Enter your values")
                    xyz.extend(int(input('> ')) for _ in range(1, inp + 1))
                    last = xyz[-1]
                    if check(xyz) == True:
                        near = nearestMultiple(last)
                        comp = near - last
                        comp = 3 if comp == 4 else comp
                    else:
                        print("\nYou did not input consecutive integers.")
                        lose1()
            print("\n\nCONGRATULATIONS!!!")
            print("YOU WON!")
            exit(0)

        else:
            print("Wrong choice")


game = True
while game:
    print("Player 2 is Computer.")
    print("Do you want to play the 21 number game? (Yes / No)")
    ans = input('> ')
    if 'y' in  ans.lower() :
        start1()
    else:
        print("Do you want quit the game?(yes / no)")
        nex = input('> ')
        if  'y' in  ans.lower():
            print("You are quitting the game...")
            exit(0)
        elif 'n' in nex.lower() :
            print("Continuing...")
        else:
            print("Wrong choice")

