import sys
from stats import get_num_words
from stats import get_chars_dict
from stats import get_sorted_list


def print_results(path, word_count, my_list):
    print("============== BOOKBOT ===============")
    print(f"Analyzing book found at {path}...")
    print("------------- Word Count -------------")
    print(f"Found {word_count} total words")
    print("----------- Character Count ----------")
    print_list(my_list)

def print_list(sorted_list):
    for item in sorted_list:
        c = item["char"]
        v = item["num"]
        if c.isalpha():
            print(f"{c}: {v}")

def main():
    if len(sys.argv) !=  2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # book_path = "books/frankenstein.txt"
    book_path = sys.argv[1] 
    text = get_book_text(book_path)
    num_words = get_num_words(text)

    my_dict = get_chars_dict(text)

    sorted_list = get_sorted_list(my_dict)
    print_results(book_path, num_words, sorted_list)

def get_book_text(path):
    file_contents = None
    with open(path) as f:
        file_contents = f.read()
    return file_contents

if __name__ == "__main__":
    main()
