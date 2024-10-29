# cowsay.py

import sys
from heifer_generator import get_cows


def list_cows(cows):
    print("Cows available:", " ".join(cow.get_name() for cow in cows))


def find_cow(name, cows):
    for cow in cows:
        if cow.get_name() == name:
            return cow
    return None


def main():
    cows = get_cows()

    if len(sys.argv) < 2:
        print("Usage: python cowsay.py [-l | MESSAGE | -n COW MESSAGE]")
        return

    # '-l' 옵션: 사용 가능한 소 목록 출력
    if sys.argv[1] == "-l":
        list_cows(cows)

    # 기본 소를 사용하여 메시지 출력
    elif len(sys.argv) == 2:
        message = sys.argv[1]
        cow = find_cow(cows)  # 기본 소 이름을 "heifer"로 사용
        if cow:
            print(f"{message}\n{cow.get_image()}")
        else:
            print("Default cow not found!")

    # 특정 소를 사용하여 메시지 출력
    elif sys.argv[1] == "-n" and len(sys.argv) >= 4:
        cow_name = sys.argv[2]
        message = " ".join(sys.argv[3:])
        cow = find_cow(cow_name, cows)
        if cow:
            print(f"{message}\n{cow.get_image()}")
        else:
            print(f"Could not find {cow_name} cow!")

    else:
        print("Invalid usage. Check command format.")


if __name__ == "__main__":
    main()
