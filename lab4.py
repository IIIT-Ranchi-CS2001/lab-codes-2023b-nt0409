# Input sentence
sentence = "Madam Arora teaches malayalam"

# Convert the sentence to lowercase to ensure case insensitivity
sentence = sentence.lower()

# Split the sentence into words
words = []
word = ""
for char in sentence:
    if char == " ":
        if word:
            words.append(word)
            word = ""
    else:
        word += char
if word:
    words.append(word)

# Function to check if a word is a palindrome
def is_palindrome(word):
    length = len(word)
    for i in range(length // 2):
        if word[i] != word[length - i - 1]:
            return False
    return True

# Count palindrome words
palindrome_count = 0
for word in words:
    if is_palindrome(word):
        palindrome_count += 1

print("Number of palindrome words:", palindrome_count)
