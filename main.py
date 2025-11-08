from stats import (num_words, get_num_chars, chars_dict_to_sorted_list)
import sys


def main():
    book_path = get_book_path(sys.argv)
    frankenstein = get_book_text(book_path)
    num_of_words = num_words(frankenstein)
    num_of_chars = get_num_chars(frankenstein)
    chars_sorted_list = chars_dict_to_sorted_list(num_of_chars)

    print_report(book_path, num_of_words, chars_sorted_list)

def get_book_path(syst):
    book_path = None
    if len(syst) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = syst[1]
    return book_path


def get_book_text(file_path):
    with open(file_path) as f:
        file_text = f.read()
    return file_text

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")



main()
