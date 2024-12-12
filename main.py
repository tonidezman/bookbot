import string
from collections import Counter
from typing import List

def count_words(text: string) -> int:
    counter = 0
    for _ in text.split():
        counter += 1
    return counter

def count_characters(text: str) -> Counter:
    text = text.lower()
    counter = Counter()
    alphabet =  string.ascii_lowercase

    for char in text:
        if char in alphabet:
            counter[char.lower()] += 1
    return counter

def display_characters(l: List[tuple[str, int]]) -> None:
    for char, count in l:
        print(f"The '{char}' character was found {count} times")

def main():
    filename = "books/frankenstein.txt"

    print(f"--- Begin report of {filename} ---")

    with open(filename) as f:
        text = f.read()
        print(f"{count_words(text)} words found in the document")
        print("")

        counter = count_characters(text)
        l = list(counter.items())
        l.sort(key=lambda x: x[1], reverse=True)
        display_characters(l)
        print("--- End report ---")


if __name__ == '__main__':
    main()
