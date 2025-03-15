def get_book_text(filepath):
   
    with open(filepath) as f:
        return f.read()
        
def main():
    book_text = get_book_text("/home/lilpeach/workspace/github.com/bookbot/books/frankenstein.txt")
    print(book_text)

main()
