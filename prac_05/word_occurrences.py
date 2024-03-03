"""
Word Occurrences
Estimate: 20 minutes
Actual:   25 minutes
"""

# Ask user for input
user_input = input("Text: ")

# Split the input string into words
words = user_input.split()

# Count occurrences of each word using a dictionary
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

# Find the length of the longest word
max_word_length = max(len(word) for word in word_counts)

# Print counts sorted alphabetically and aligned nicely
for word, count in sorted(word_counts.items()):
    print(f"{word:>{max_word_length}} : {count}")
