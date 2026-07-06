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

def sort_on(d: CharacterCount) -> int:
    return d["num"]

def chars_dict_on_sorted_list(num_chars_dict: dict[str, int]) -> list[CharacterCount]:
    sorted_list: list[CharacterCount] = []

    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})

    sorted_list.sort(reverse = True, key = sort_on)
    return sorted_list