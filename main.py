path_to_file = "books/frankenstein.txt"

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = count_words(text)
    chars = count_chars(text)
    stortdict = dict(sorted(chars.items(), key=lambda x: x[1], reverse=True))
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document \n")
    for char, count in stortdict.items():
        print(f"The word '{char}' was found {count} times")
    print(f"--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    lowercase = text.lower()
    unique_chars = set(lowercase)
    
    countchar = {}
    for l in unique_chars:
        if l.isalpha() is True:
            count = lowercase.count(l)
            countchar[l] = count
    
    return countchar

main()