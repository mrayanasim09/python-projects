# This code is made by MRayan Asim
from time import time


# calculate the accuracy of the input prompt
def typingErrors(prompt):
    words = prompt.split()
    errors = 0

    for i in range(len(iwords)):
        if i in (0, len(iwords) - 1):
            if iwords[i] == words[i]:
                continue
            else:
                errors += 1
        else:
            if iwords[i] == words[i]:
                if (iwords[i + 1] == words[i + 1]) & (iwords[i - 1] == words[i - 1]):
                    continue
                else:
                    errors += 1
            else:
                errors += 1
    return errors


# calculate the speed in words per minute
def typingSpeed(iprompt, stime, etime):
    global iwords

    iwords = iprompt.split()
    twords = len(iwords)
    speed = twords / time

    return speed


# calculate total time elapsed
def timeElapsed(stime, etime):
    time = etime - stime

    return time


if __name__ == "__main__":
    prompt = "Hi, this code is written by MRayan asim, a programmer"
    print("Type this:- '", prompt, "'")

    # listening to input ENTER
    input("press ENTER when you are ready!")

    # recording time for input
    stime = time()
    iprompt = input()
    etime = time()

    # gather all the information returned from functions
    time = round(timeElapsed(stime, etime), 2)
    speed = typingSpeed(iprompt, stime, etime)
    errors = typingErrors(prompt)

    # printing all the required data
    print("Total Time elapsed : ", time, "s")
    print("Your Average Typing Speed was : ", speed, "words / minute")
    print("With a total of : ", errors, "errors")
