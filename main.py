def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    report = get_report(chars_dict)
    print(f"--- Begin report for {book_path} ---")
    print(f"{num_words} are found in this book")
    for match in report:
        print(f"The '{match[0]}' character was found {match[1]} times")
    print(f"--- End Report")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for letter in text:
        lowered = letter.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_character_sums(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_report(chars_dict):
    report_list = []
    for key, value in chars_dict.items():
        if key.isalpha():
            report_list.append((key, value))
    return sorted(report_list, key = sort_on, reverse=True)

def sort_on(character):
    return character[1]

main()