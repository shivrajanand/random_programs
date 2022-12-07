import random

def rps(mpoint, upoint, turns):
    val = random.randint(1, 4)
    if val == 1:
        machine = 'rock'
    elif val == '2':
        machine = 'paper'
    else:
        machine = 'scissor'

    print(f"machine: {mpoint} <---> user: {upoint} ::::: turns: {turns}")
    user = int(input("Choose\n1.rock\n2.paper\n3.scissor\n>>> "))

    if machine == 'rock' and user == 1:
        print("TIE")
        mpoint = mpoint + 0.5
        upoint = upoint + 0.5
    elif machine == 'rock' and user == 2:
        print("You won!")
        upoint = upoint + 1
    elif machine == 'rock' and user == 3:
        print("You lost")
        mpoint = mpoint + 1
    elif machine == 'paper' and user == 1:
        print("You lost")
        mpoint = mpoint + 1
    elif machine == 'paper' and user == 2:
        print("TIE")
        mpoint = mpoint + 0.5
        upoint = upoint + 0.5
    elif machine == 'paper' and user == 3:
        print("You won!")
        upoint = upoint + 1
    elif machine == 'scissor' and user == 1:
        print("You WON!")
        upoint = upoint + 1
    elif machine == 'scissor' and user == 2:
        print("You Lost")
        mpoint = mpoint + 1
    elif machine == 'scissor' and user == 3:
        print("TIE")
        mpoint = mpoint + 0.5
        upoint = upoint + 0.5
    else:
        print()
    print(f"machine: {machine}")

    return [mpoint, upoint]


def clear():
    print("\n"*100)


if __name__ == '__main__':
    mpoint = 0
    upoint = 0
    turns = 0
    while True:
        clear()
        turns += 1
        val = rps(mpoint, upoint, turns)
        mpoint = val[0]
        upoint = val[1]
        choice = input("Press Enter to continue or Q to quit: ")
        choice = choice.lower()
        if choice == '\n':
            continue
        elif choice == 'q':
            clear()
            print(f"machine: {val[0]} <---> user: {val[1]}")
            if val[0] > val[1]:
                print("MACHINE WON!")
            else:
                print("USER WON!")
            break
        else:
            print()
