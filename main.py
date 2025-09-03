# python
# Importing functions from stats.py for better organization
from stats import get_book_text, book_word_counter

    
def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = book_word_counter("books/frankenstein.txt")
    print(text)
    print(word_count)


main()
