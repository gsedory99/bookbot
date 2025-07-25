from stats import get_num_words
from stats import character_counter
from stats import sort_counts
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        book_contents = f.read()
        return book_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_Filepath = sys.argv[1]
    book_text = get_book_text(book_Filepath)
    word_number = get_num_words(book_text)
    
    
    word_dict = character_counter(book_text)
    
    sorted_char_list = sort_counts(word_dict)
  
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_Filepath}...")
    print("----------- Word Count ----------")
    print(f" Found {word_number} total words")
    print(f"--------- Character Count -------")
    for item in sorted_char_list:
        print(f"{item['char']}: {item['num']}")
   # print(character_counter(book_text))


    

if __name__ == "__main__":
    main()

