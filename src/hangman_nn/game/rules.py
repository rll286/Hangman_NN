MAX_MISSES: int = 6


def normalize_letter(letter: str) -> str:
    """
    Normalize a letter to lowercase and reject any non-alphabetic characters.

    args:
        letter (str): The letter to normalize.

    returns:
        str: the normalized letter if alphabetic, otherwise raise a ValueError.

    raises:
        ValueError: If the letter is not a single alphabetic character.
    """
    if len(letter) != 1 or not letter.isalpha():
        raise ValueError("Input must be a single alphabetic character.")
    return letter.lower()


def normalize_word(word: str) -> str:
    """
    Normalize the word to lowercase and reject any non-alphabetic characters,
    empty strings, spaces, or punctuation.

    args:
        word (str): The word to normalize.

    returns:
        str: the normalized word if valid, otherwise raise a ValueError.

    raises:
        ValueError: If the word is empty, contains spaces, punctuation, or
        non-alphabetic characters.
    """
    if not word or not word.isalpha():
        raise ValueError(
            "Input must be a non-empty string containing only alphabetic characters."
        )
    return word.lower()


def validate_word_length(word_length: int, *, maximum: int | None = None) -> None:
    """
    Require positive word length and reject lengths greater than the maximum if
    specified.

    args:
        word_length (int): The length of the word to validate.
        maximum (int | None): The maximum allowed length of the word. If None, no
        maximum is enforced.

    raises:
        ValueError: If the word length is not positive or exceeds the maximum length.
    """
    if word_length <= 0:
        raise ValueError("Word length must be positive.")
    if maximum is not None and word_length > maximum:
        raise ValueError(f"Word length must not exceed {maximum} characters.")
