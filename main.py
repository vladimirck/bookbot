import sys
from stats import word_counter, character_counter, convert_to_sorted_list

def get_book_text(filepath: str)-> str:
    file_contents = ""
    with open(filepath) as file:
        file_contents = file.read()

    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    file_path = sys.argv[1]
    book_string = get_book_text(file_path)
    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at {file_path}...\n")
    print("----------- Word Count ----------\n")
    print(f"Found {word_counter(book_string)} total words\n")
    print("--------- Character Count -------")
    char_stats = character_counter(book_string)
    for val in convert_to_sorted_list(char_stats):
        if val["char"].isalpha():
            print(f"{val["char"]}: {val["count"]}")
    print("============= END ===============")

main()
