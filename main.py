from stats import get_num_words
from stats import character_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    try:
        title = sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # Call get_book_text with relative path to frankenstein.txt
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {title}...")
    text = get_book_text(title)
    print("----------- Word Count ----------")
    words = get_num_words(text)
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    count = character_count(text)
    for char, num in sorted(count.items(), key=lambda x: x[1], reverse=True):
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")
main()