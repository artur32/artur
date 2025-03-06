def print_string(word):
    return word


def is_palindrome(word):
    word = word.lower()
    return word[::-1]

def count_vowels(word):
    vowels = "aбвгдеёжзАБВГДЕЁЖЗ"
    return sum(1 for letter in word if letter in vowels)

def removeduplicates(word):
    unique_chars = ""
    for char in word:
        if char not in unique_chars:
            unique_chars += char