def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    num_words = get_num_words(text)
    char_counts = count_characters(text)
    
    print_report(book_path, num_words, char_counts)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_characters(text):
    char_count = {}
    text = text.lower()
    for char in text:
        if char.isalpha():  # Only count alphabet characters
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count


def sort_on(dict):
    return dict["num"]


def print_report(book_path, num_words, char_counts):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    sorted_char_counts = [{"char": char, "num": count} for char, count in char_counts.items()]
    sorted_char_counts.sort(reverse=True, key=sort_on)
    
    for item in sorted_char_counts:
        char = item["char"]
        count = item["num"]
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")


main()
