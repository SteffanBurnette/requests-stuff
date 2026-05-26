from typing import TypedDict

class CharacterCount(TypedDict):
    char: str
    num: int

def get_word_count(text):
    count = len(text.split())

    return count

def get_char_count(text):
    myDict = {}
    text = text.strip().lower()
    print(text)
    for c in text:
        if c not in myDict:
           myDict[c] = 1

        else:
            myDict[c] += 1

    return myDict