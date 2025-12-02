from stats import get_character_counts,get_two_keyed_dict_list, sort_on,print_report
import sys

def get_book_text(filePath):
    return open(filePath, 'r').read()

def check_for_file():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")

def main():
    book_path = check_for_file()
    if book_path is None:
        sys.exit(1)
    book_text = get_book_text(book_path)
    character_counts_dict = get_character_counts(book_text)
    formatted_dict_list = get_two_keyed_dict_list(character_counts_dict)
    formatted_dict_list.sort(reverse=True, key=sort_on)
    print_report(formatted_dict_list)

main()