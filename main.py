from stats import get_num_words
from stats import get_num_char
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_num_words(book_text)
    print(f"{word_count} words found in the document")
    print(get_num_char(book_text))


main()
