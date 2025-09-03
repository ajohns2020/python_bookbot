# python

def get_book_text(filepath): # Stores all characters in memory.
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f: # Tries to ignore Window's Windows-1252 encoding, might not need it. 
        return f.read()

    
def book_word_counter(filepath):  
    text = get_book_text(filepath)  # Use the parameter, not hardcoded path
    words = text.split() 
    word_count = f"{len(words)} words found in the document." 
    return word_count


def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = book_word_counter("books/frankenstein.txt")
    print(text)
    print(word_count)


main()