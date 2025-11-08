def num_words(book_string):
    words = book_string.split()
    num_of_words = len(words)
    return num_of_words

def get_num_chars(book_string):
    chars_count= {}
    for char in book_string:
        low_char = char.lower()
        if low_char not in chars_count:
            chars_count[low_char] = 1
        elif low_char in chars_count:
            chars_count[low_char] += 1
    return chars_count

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list