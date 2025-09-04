# python
# Imports 
import os 
import sys

# Importing functions from stats.py for better organization
from stats import get_book_text, book_word_counter, book_char_frequencies, book_final_report

# Checking if at least two arguments are provided (script name and filepath)
sys.argv[0] = "main.py" # Script name
filepath = sys.argv[1] # Filepath argument


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    print("Example: python3 main.py books/moby_dick.txt")
    sys.exit(1)








    
def main():
    print ("Reading book from :" , filepath)
    text = get_book_text()
    word_count = book_word_counter()
    char_count = book_char_frequencies()
    report = book_final_report()
    print(text)
    print(word_count)
    print(char_count)
    print(report)


main()
