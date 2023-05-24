# Define the letter values
letter_values = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
    'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23,
    'X': 24, 'Y': 25, 'Z': 26
}


# Calculate the number corresponding to the character
def calculate_word_sum(word):
    word = word.upper()
    total_sum = 0

    for char in word:
        if char in letter_values:
            char_value = letter_values[char]
            total_sum += char_value

    return total_sum

# Input the word and print the percent 
while True:
    input_word = input("Enter a word (e.g., ATTITUDE) to see the percent: ")
    word_sum = calculate_word_sum(input_word)
    print("The percent of this word is: ", word_sum, "%")
