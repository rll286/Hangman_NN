from dataclasses import dataclass

from hangman_nn.game.rules import (
    MAX_MISSES,
    validate_word_length,
)


@dataclass(frozen=True, slots=True)
class GameState:
    """
    An individual game state which will be discarded on the next state.

    pattern: None meaning no letter revieled,
        otherwise the letter is in its correct position
    guessed_letters: All letters guessed
    wrong_letters: A subset of guessed letters that are not in the word
    misses: The number of wrong guesses for the game
    """

    pattern: tuple[str | None, ...]
    guessed_letters: frozenset[str]
    wrong_letters: frozenset[str]
    misses: int


def create_initial_state(word_length: int) -> GameState:
    """
    Create the initial game state for a word of the given length.

    The initial state has an empty pattern, no guessed letters, no wrong letters,
        and zero misses.

    Args:
        word_length (int): The length of the word to guess.

    Returns:
        GameState: The initial game state for the word of the given length.
    """
    validate_word_length(word_length)
    return GameState(
        pattern=tuple([None] * word_length),
        guessed_letters=frozenset(),
        wrong_letters=frozenset(),
        misses=0,
    )


def validate_state(state: GameState) -> None:
    """
    Make sure the pattern has positive length,
    the revieled characters are lowercase alphabetic,
    and all revieled characters are within guessed letters.

    Check that wrong letters is a subset of guessed letters.

    Make sure the numbers of misses is non-negative,
    is equal to the number of wrong letters,
    and does not exceed the maximum allowed misses.

    Args:
        state (GameState): The game state to validate.

    Raises:
        ValueError: If any of the validation checks fail.
    """

    if len(state.pattern) <= 0:
        raise ValueError("Pattern must have positive length")
    for char in state.pattern:
        if char is not None and (not char.isalpha() or not char.islower()):
            raise ValueError("Revealed characters must be lowercase alphabetic")
        if char is not None and char not in state.guessed_letters:
            raise ValueError("Revealed characters must be within guessed letters")

    for char in state.guessed_letters:
        if char not in state.pattern and char not in state.wrong_letters:
            raise ValueError(
                "Guessed letters must be either in the pattern or in the wrong letters"
            )

    if not state.wrong_letters.issubset(state.guessed_letters):
        raise ValueError("Wrong letters must be a subset of guessed letters")

    if state.misses < 0:
        raise ValueError("Number of misses cannot be negative")
    if state.misses != len(state.wrong_letters):
        raise ValueError(
            "Number of misses must be equal to the number of wrong letters"
        )
    if state.misses > MAX_MISSES:
        raise ValueError("Number of misses cannot exceed the maximum allowed misses")


def is_finished(state: GameState) -> bool:
    """
    Check if the game state represents a finished game.

    A game is finished if either all leters in the pattern have been revealed
    or the number of misses has reached the maximum allowed misses.

    Args:
        state (GameState): The game state to check.

    Returns:
        bool: True if the game is finished, False otherwise.
    """
    return is_won(state) or is_lost(state)


def is_won(state: GameState) -> bool:
    """
    Check if the game state represents a won game.

    A game is won if all letters in the pattern have been revealed.

    Args:
        state (GameState): The game state to check.

    Returns:
        bool: True if the game is won, False otherwise.
    """
    return all(char is not None for char in state.pattern)


def is_lost(state: GameState) -> bool:
    """
    Check if the game state represents a lost game.

    A game is lost if the number of misses has reached the maximum allowed misses.

    Args:
        state (GameState): The game state to check.

    Returns:
        bool: True if the game is lost, False otherwise.
    """
    return state.misses >= MAX_MISSES
