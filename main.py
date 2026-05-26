from stats import get_word_count, get_char_count

path_to_file = "/home/frentr/Projects/requests-stuff/books/frankenstein.txt"



def get_book_text(file_path):
    with open(path_to_file) as f:
        file_content = f.read()

        return file_content
    

myBook = get_book_text(path_to_file)
print(myBook)

word_count = get_word_count(myBook)
print(f"The number of words in the book is: {word_count}")

book_char_count = get_char_count(myBook)
print(book_char_count)

print("=========BookBot=========")
print(f"Analyzing books found at {path_to_file}")
print("----------Word Count----------")
print(f"Found {word_count} total words")
print("----------Character Count----------")
print(book_char_count.sort(key = book_char_count.values))