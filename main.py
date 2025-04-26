def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = word_count(text)
    count = 0
    for word in words:
        count = count + 1
    print (f"{count} words found in the documentt")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    count = text.split()
    return count

main()