# python
# Importing functions from stats.py for better organization
from stats import get_book_text, book_word_counter, book_char_frequencies, book_final_report

    
def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = book_word_counter("books/frankenstein.txt")
    char_count = book_char_frequencies("books/frankenstein.txt")
    report = book_final_report("books/frankenstein.txt")
    print(text)
    print(word_count)
    print(char_count)
    print(report)


main()
