def pattern_searcher(text):
    # List of common English words to compare against
    common_words = ['the', 'and', 'is', 'to', 'of', 'it', 'in', 'you', 'that']

    # List of potential patterns to search for
    patterns = ['aaaa', 'abab', 'aabb', 'abba']

    # Loop through each pattern
    for pattern in patterns:
        decoded_text = ''
        pattern_index = 0
        word_list = text.split()

        # Loop through each word in the text
        for word in word_list:
            decoded_word = ''

            # Loop through each character in the word
            for char in word:
                # Check if the character matches the pattern
                if pattern[pattern_index % len(pattern)] == 'a':
                    decoded_word += char.upper()
                else:
                    decoded_word += char.lower()

                pattern_index += 1

            # Add the decoded word to the decoded text
            decoded_text += decoded_word + ' '

        # Check if the decoded text contains common English words
        if any(word in decoded_text.lower() for word in common_words):
            return decoded_text.strip()

    # Return the original text if no pattern is found
    return text

# Test the algorithm
text_to_decode = "ThIs is aB exAmple text to DeCoded."
decoded_text = pattern_searcher(text_to_decode)
print("Decoded Text:", decoded_text)
