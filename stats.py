
def get_num_words(words_list):
    num_words = len(words_list)
    return num_words

def count_chars(text):
    # Create an empty dictionary to store our counts
    char_counts = {}
    
    # Convert the text to lowercase
    lowered_text = text.lower()
    
    # Loop through each character in the lowered text
    for char in lowered_text:
        
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
        
    return char_counts

def chars_dict_to_sorted_list(char_counts):
    chars_list = []

    for char, count in char_counts.items():
        char_dict = {"char": char, "count": count}

        chars_list.append(char_dict)

    def sort_on(dict):
        return dict["count"]
    
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list