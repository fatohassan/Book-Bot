def main():
    path = "books/frankenstein.txt"
    text_list = read_the_text(path)
    num_of_words = words_count(text_list)
    num_of_each_char = char_count(text_list)
    char_listed = final_dict_list(num_of_each_char)
    print(num_of_words)
    print(char_listed)
    print(f"--- Begin report of {path} ---")
    print(f"{num_of_words} words found in the document /n")

    for item in char_listed:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def sort_on(d):
    return d["num"]

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

def final_dict_list(num_of_each_char):
    char_list = []
    for each in num_of_each_char:
        char_list.append({"char": each, "num": num_of_each_char[each]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list

main()

