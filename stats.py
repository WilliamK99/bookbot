def get_num_words(text):
    return len(text.split())

def character_count(text):
    text = text.lower()
    char_dict = {}
    #Count each character
    for char in text:
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict