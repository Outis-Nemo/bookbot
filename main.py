from stats import get_num_words
from stats import get_num_char
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    word_count = get_num_words(book_text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_dictionary = get_num_char(book_text)
    ordered_keys = sorted(char_dictionary, reverse = False)
    for key in ordered_keys:
        print(f"{key}: {char_dictionary[key]}")
    print("============= END ===============")
main()
