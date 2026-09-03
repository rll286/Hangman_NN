from hangman_nn.game.rules import (
    normalize_letter,
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

