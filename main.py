from stats import get_num_words
from stats import count_chars

def get_book_text(filepath):
   
    with open(filepath) as f:
        return f.read()
        
def main():
    book_text = get_book_text("/home/lilpeach/workspace/github.com/bookbot/books/frankenstein.txt")

    words_list = book_text.split()
    word_count = get_num_words(words_list)
    
    char_counts = count_chars(book_text)

    #return

    # Print word count first
    print(f"{word_count} words found in the document")
    
    # Fix 2: Print the char_counts dictionary, not the function
    print(char_counts)

    #print(f"{count_chars}")
    #print(f"{word_count} words found in the document")
    
    
    #print(f"{num_words} words found in the document")
    

    #num_words = len(words_list)


   # print(f"{num_words} words found in the document")




#{num_words} words found in the document
#def main():
#    book_text = get_book_text("/home/lilpeach/workspace/github.com/bookbot/books/frankenstein.txt")
#    print(book_text)

main()
