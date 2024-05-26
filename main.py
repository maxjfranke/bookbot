def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print_report(text,  book_path)

def dict_to_sorted_list(dict):
    dict_list = []
    for key, value in dict.items():
        dict_list.append({'letter': key, 'count': value})

    return sorted(dict_list, reverse=True, key=lambda x: x['count'])

def print_report(string, path):
    words = get_word_count(string)
    letters = get_letter_dict(string)
    sorted_letters = dict_to_sorted_list(letters)

    print(f"--- Printing report for {path} ---\n {words} words found in the document\n")
    
    for letter in sorted_letters:
        if letter['letter'].isalpha():
            print(f"The '{letter['letter']}' character was found {letter['count']} times")

    print("--- End report ---")


def get_letter_dict(string):
    letters = {}
    lower_string = string.lower()
    for char in lower_string:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1

    return letters

def get_word_count(string):
    words = string.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
        
main()