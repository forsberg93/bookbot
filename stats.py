
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
        # Now, what should we do with each character?
        # If we've seen it before, we need to increase its count
        # If it's new, we need to add it to our dictionary
        
    return char_counts