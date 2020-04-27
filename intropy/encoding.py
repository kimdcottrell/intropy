import sys
from typing import TextIO

script, input_encoding, error = sys.argv

print("This is my file to test Python's execution methods.")
print("The variable __name__ tells me which context this file is running in.")
print("The value of __name__ is:", repr(__name__))


def main(language_file: TextIO, encoding: str, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line: int, encoding: str, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(f"{raw_bytes} <===> {cooked_string}")

languages = open("languages.txt", encoding="utf-8")

if __name__ == "__main__":
    main(languages, input_encoding, error)
