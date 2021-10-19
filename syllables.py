#!/usr/bin/env python3


VOWELS = ["a", "an", "e", "en", "i", "in", "o", "on", "u", "un"]
CONSONANTS = ["j", "k", "l", "m", "n", "p", "s", "t", "w"]
FORBIDDEN = {"wu", "wo", "ji", "ti"}

SPACING = 5


def main():
    for consonant in CONSONANTS:
        for vowel in VOWELS:
            syllable = consonant + vowel
            if syllable[:2] in FORBIDDEN:
                # illegal part can only occur in first two chars
                print(" " * SPACING, end="")
                continue

            print(("{:<%s}" % SPACING).format(syllable), end="")
            # this is the crunchiest workaround
        print()


if __name__ == "__main__":
    main()
