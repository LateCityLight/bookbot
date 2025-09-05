from stats import num_words, characters, char_sort
import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]


def main():
    content = get_book_text(book_path)
    word_count = num_words(content)
    character_count = characters(content)
    sorted_char_list = char_sort(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    # Loop through the sorted list of characters
    for item in sorted_char_list:
        char = item["char"]
        # Use the .isalpha() method to check if the character is in the alphabet
        if char.isalpha():
            count = item["num"]
            print(f"{char}: {count}")

    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
        
    return content

main()