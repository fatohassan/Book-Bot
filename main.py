def main():
    path = "books/frankenstein.txt"
    text_list = read_the_text(path)
    num_of_words = words_count(text_list)
    num_of_each_char = char_count(text_list)
    print(num_of_words)
    print(num_of_each_char)

def read_the_text(from_path):
    with open(from_path) as f:
        return f.read() 

def words_count(text_list):
    the_count = text_list.split()
    return len(the_count)

def char_count(text_list):
    chars = {}
    char_lower_case = text_list.lower()
    for letter in char_lower_case:
        if letter in chars:
            chars[letter] += 1
        else:
            chars[letter] = 1
    return chars


main()
