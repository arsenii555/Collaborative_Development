import random
import sys
import certifi
import requests
import cowsay

def bullscows(guess: str, riddle: str) -> (int, int):
    bulls = 0
    cows = 0
    bulls_letters = set()
    for i in range(len(riddle)):
        if guess[i] == riddle[i]:
            bulls += 1
            bulls_letters.add(guess[i])
        elif guess[i] in riddle and not guess[i] in bulls_letters:
            cows += 1
    return bulls, cows


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    riddle = random.choice(words)
    count = 1
    while (guess := ask("Введите слово: ")) != riddle:
        bulls, cows = bullscows(guess, riddle)
        inform("Быки: {}, Коровы: {}", bulls, cows)
        count += 1
    print(f"Правильно! Вы использовали {count} attempts.")


def custom_cowsay(message):
    bubble = f"""
  {'_' * (len(message) + 2)}
< {message} >
  {'-' * (len(message) + 2)}"""

    cow = r"""
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
    """
    return bubble + "\n" + cow


def ask(prompt: str, valid: list[str] = None) -> str:
    print(custom_cowsay(prompt))
    word = input()
    if valid is not None:
        while word not in valid:
            print(custom_cowsay(prompt))
            word = input()
    return word


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(cowsay.cowsay(format_string.format(bulls, cows)))


def load_words(source: str, length: int) -> list[str]:
    if source.startswith("http://") or source.startswith("https://"):
        words = requests.get(source, verify=certifi.where()).text.splitlines()
    else:
        with open(source, "r") as f:
            words = f.read().splitlines()
    return [word.strip() for word in words if len(word.strip()) == length]


def main():
    if len(sys.argv) < 2:
        print("Incorrect. Usage: `python -m bullscows dictionary [length]`")
    else:
        source = sys.argv[1]
        length = int(sys.argv[2]) if len(sys.argv) > 2 else 5
        words = load_words(source, length)
        gameplay(ask, inform, words)


if __name__ == "__main__":
    main()