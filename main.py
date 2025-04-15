from stats import counting_nwords_in_book, counting_char, sorting_dic, print_sorted_dic
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

def get_book_text(file_path:str):
    
    # opening the with function
    with open(file_path) as f:
        file_content = f.read()
    return file_content 

def main():
    print("============ BOOKBOT ============\n"
          "Analyzing book found at books/frankenstein.txt...\n"
          "----------- Word Count ----------\n"
          f"{counting_nwords_in_book(get_book_text(path))}\n"
          "--------- Character Count -------")
    print_sorted_dic(sorting_dic(counting_char(get_book_text(path))))
    print("============= END ===============")


main()
