def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_char(text):
    char_dictionary = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0, 
                       'i' : 0, 'j' : 0, 'k' : 0, 'l' : 0, 'm' : 0, 'n' : 0, 'o' : 0, 'p' : 0,
                       'q' : 0, 'r' : 0, 's' : 0, 't' : 0, 'u' : 0, 'v' : 0, 'w' : 0, 'x' : 0,
                       'y' : 0, 'z' : 0, 'æ' : 0, 'â' : 0, 'ê' : 0, 'ë' : 0, 'ô' : 0}
    for char in text:
        temp = char.lower()
        if temp in char_dictionary:
            temp_num = char_dictionary[temp] + 1
            char_dictionary[temp] = temp_num

    return char_dictionary
