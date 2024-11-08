# File: cowsay.py
import sys
from heifer_generator import get_cows
from dragon import Dragon

def list_cows():
    cows = get_cows()
    print("Cows available:", end=" ")
    print(" ".join(cow.get_name() for cow in cows))

def main():
    if len(sys.argv) == 1:
        print("Usage: cowsay [-l] [-n cow] message")
        sys.exit(1)

    if sys.argv[1] == "-l":
        list_cows()
        sys.exit(0)

    if sys.argv[1] == "-n":
        if len(sys.argv) < 4:
            print("Usage: cowsay [-l] [-n cow] message")
            sys.exit(1)
        cow_name = sys.argv[2]
        message = " ".join(sys.argv[3:])
    else:
        cow_name = "heifer"
        message = " ".join(sys.argv[1:])

    # Get all cows and find the one we want
    cows = get_cows()
    cow = None
    for available_cow in cows:
        if available_cow.get_name() == cow_name:
            cow = available_cow
            break

    if cow is None:
        print(f"Could not find {cow_name} cow!")
        sys.exit(1)

    print(message)
    print(cow.get_image())
    
    if isinstance(cow, Dragon):
        if cow.can_breath_fire():
            print("This dragon can breathe fire.")
        else:
            print("This dragon cannot breathe fire.")

if __name__ == "__main__":
    main()