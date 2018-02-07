#! /usr/bin/env python3
"""Rudimentary pig latin translation module

Attributes:
    CONSONANT_CLUSTERS: list of all special case pig latin consonant clusters
"""

CONSONANT_CLUSTERS = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr',
                      'st', 'sl', 'cl', 'pl', 'fl']


def translate(phrase):
    """Converts input phrase into pig latin

    Args:
        phrase (str): phrase to be converted to pig latin

    Returns:
        str: pig latin converted phrase in all lowercase
    """

    words = phrase.split()
    pl_sentence = ""
    for word in words:
        word = word.lower()
        if word[0] in ['a', 'e', 'i', 'o', 'u']:
            pl_word = word +'ay'
        elif word[0:1] in CONSONANT_CLUSTERS:
            pl_word = word[2:] + word[:2] + 'ay'
        else:
            pl_word = word[2:] + word[0] +'ay'

        if len(pl_sentence) == 0:
            pl_sentence = pl_word
        else:
            pl_sentence = pl_sentence + " " + pl_word

    return pl_sentence


def main():
    """Example function the uses pig latin translator.

    Solicits input from user and outputs the pig latin translatio the specivied number of times
    """
    # The following solicits the input of the user and stores it in the variable sentence
    sentence = input('Type the mantra you would like translated into pig-latin and press ENTER: ')
    pl_sentence = translate(sentence)
    times = int(input('Type how many times you would like to repeat your mantra and press ENTER: '))

    for _ in range(times):
        print(pl_sentence)

if __name__ == "__main__":
    main()