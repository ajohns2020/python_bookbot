# python 
# Moving functions to stats.py for better organization @ajohns2020 


def get_book_text(filepath): # Stores all characters in memory.
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f: # Tries to ignore Window's Windows-1252 encoding, might not need it. 
        return f.read()



def book_word_counter(filepath):  
    text = get_book_text(filepath)  # Use the parameter, not hardcoded path
    words = text.split() 
    word_count = {len(words)} 
    return word_count

def book_char_frequencies(filepath):  
    freq = {}
    text = get_book_text(filepath)   # <-- read file contents here

    for ch in text:
        if ch.isalpha():  # only alphabet letters
            ch = ch.lower() # normalize to lowercase
            freq[ch] = freq.get(ch, 0) + 1 # count frequency

    return freq

def book_final_report(filepath):
    text = get_book_text(filepath)
    word_count = book_word_counter(filepath)
    char_freq = book_char_frequencies(filepath)
    report = f"Looking at file: {filepath}\n"
    report = f"Text Length: {len(text)} characters\n"
    report += f"Found {word_count} total words\n"
    report += "Character Count:\n"
    for ch, count in sorted(char_freq.items()):
        report += f"  {ch}: {count}\n"

    return report

