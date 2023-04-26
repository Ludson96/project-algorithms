def is_palindrome_iterative(word):
    if not word:
        return False
    n = len(word) - 1

    for letter in word:
        if n <= 0:
            return True
        if letter != word[n]:
            return False
        n -= 1
    return True
