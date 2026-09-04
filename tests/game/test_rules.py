from hangman_nn.game.rules import (
    normalize_letter,
    normalize_word,
    validate_word_length,
)


def test_normalize_letter():
    assert normalize_letter("A") == "a"
    assert normalize_letter("b") == "b"
    try:
        normalize_letter("1")
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for non-alphabetic character")


def test_normalize_word():
    assert normalize_word("Hello") == "hello"
    assert normalize_word("world") == "world"
    try:
        normalize_word("Hello123")
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for non-alphabetic characters")
    try:
        normalize_word("")
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for empty string")


def test_validate_word_length():
    validate_word_length(3)
    try:
        validate_word_length(0)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for non-positive word length")
    try:
        validate_word_length(5, maximum=3)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for word exceeding maximum length")
