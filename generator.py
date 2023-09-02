from generatorlib import GeneratorLib
import pyperclip
import sys
from validator import Validate
import settings


def main():

    if len(sys.argv) < 2:
        inp = input("Enter secret key (ex., cypher@example.com):\n")
    else:
        inp = sys.argv[1]
        print("Password Generation for {}:".format(inp))

    params_dict = {}
    # algo_index = input("\nChoose the algorithm (default - 1): \n  1 - SHA256\n  2 - SHA384\n  3 - SHA512\n")
    flag = False
    while flag is not True:
        try:
            algo_index = int(input("\nChoose the algorithm (default - 1): \n  {} \n".format("\n  ".join(
                [f"{str(key)} - {val.upper()}" for key, val in settings.ALGO.items()]
            ))))
            flag = Validate.validate_algo_index(algo_index)
            if not flag:
                raise ValueError
        except ValueError:
            print("Incorrect format. Value should be >0 and <4. Try again!")
            continue

    flag = False
    while flag is not True:
        try:
            pwd_length = int(input(f"\nEnter password Length (default - {settings.PASSWORD_MAX_LENGTH}):\n"))
            flag = Validate.validate_pwd_length(pwd_length)
            if not flag:
                raise ValueError
        except ValueError:
            print("Incorrect format. Password length should be a number and >4. Try again!")
            continue

    genlib = GeneratorLib(inp, pwd_length, algo_index)
    pwd_result = genlib.getpassword()
    print("\n\nYour password:\n" + pwd_result)

    print("\n\nPress \"Enter\" to copy password & Exit...\n")
    input()

    pyperclip.copy(pwd_result)


if __name__ == "__main__":
    main()
