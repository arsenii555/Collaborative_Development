import cowsay
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--first_cow", default="cow")
parser.add_argument("first_msg")
parser.add_argument("-F", "--second_cow", default="cow")
parser.add_argument("-E", "second_yeys", default="oo")
parser.add_argument('-N', '--no-wrap', action='store_true')
parser.add_argument("second_msg")


