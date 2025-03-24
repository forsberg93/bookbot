import sys
from stats import get_num_words, count_chars, chars_dict_to_sorted_list

def get_book_text(filepath):
   
    with open(filepath) as f:
        return f.read()
        
def main():

        # Check for command line arguments
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    book_text = get_book_text(path)
    #filepath = ("/home/lilpeach/workspace/github.com/bookbot/books/frankenstein.txt")
    #book_text = get_book_text(filepath)
    #book_text = get_book_text("/home/lilpeach/workspace/github.com/bookbot/books/frankenstein.txt")

    word_count = get_num_words(book_text.split())
    char_counts = count_chars(book_text)
    sorted_chars = chars_dict_to_sorted_list(char_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():  # Only print alphabetical characters
            print(f"{char}: {count}")
    
    print("============= END ===============")
    
if __name__ == "__main__":
    main()
