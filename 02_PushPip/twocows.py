import cowsay
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--first_cow", default="cow")
parser.add_argument("first_msg")
parser.add_argument("-e", "--first_eyes", default="oo")
parser.add_argument("-F", "--second_cow", default="cow")
parser.add_argument("-E", "--second_eyes", default="oo")
parser.add_argument('-N', '--no-wrap', action='store_true')
parser.add_argument("second_msg")


args = parser.parse_args()
possible = cowsay.list_cows()
if args.first_cow in possible and args.second_cow in possible:
    cow1 = cowsay.cowsay(message=args.first_msg, cow=args.first_cow, eyes=args.first_eyes)
    cow2 = cowsay.cowsay(message=args.second_msg, cow=args.second_cow, eyes=args.second_eyes)

    cow1_splitted = cow1.split("\n")
    cow2_splitted = cow2.split("\n")

    max_len = max(len(cow1_splitted), len(cow2_splitted))
    cow1_splitted[:0] = [""] * (max_len - len(cow1_splitted))
    cow2_splitted[:0] = [""] * (max_len - len(cow2_splitted))
    max_width = max(len(line) for line in cow1_splitted)
    zip_lines = zip(cow1_splitted, cow2_splitted)
    for line1, line2 in zip_lines:
        print(f"{line1.ljust(max_width)} {line2}")
else:
    raise Exception("Wrong cow type")