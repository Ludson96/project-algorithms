def is_palindrome_recursive(
    word: str, low_index: int, high_index: int
) -> bool:
    if not word:
        return False

    if high_index <= low_index:
        return True
    elif word[low_index] != word[high_index]:
        return False
    else:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
