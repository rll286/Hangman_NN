from hangman_nn.game.state import (
    GameState,
    create_initial_state,
    is_finished,
    is_lost,
    is_won,
    validate_state,
)


def test_create_initial_state():
    word_length = 5
    state = create_initial_state(word_length)
    assert state.pattern == tuple([None] * word_length)
    assert state.guessed_letters == frozenset()
    assert state.wrong_letters == frozenset()
    assert state.misses == 0


def test_validate_state():
    state = create_initial_state(5)
    validate_state(state)

    state = GameState(
        pattern=tuple(["a", None, None, None, None]),
        guessed_letters=frozenset(),
        wrong_letters=frozenset(),
        misses=0,
    )
    try:
        validate_state(state)
    except ValueError:
        pass
    else:
        raise AssertionError(
            "Validation did not fail for guessed letters not in the guessed set"
        )

    state = GameState(
        pattern=tuple([None] * 5),
        guessed_letters=frozenset("a"),
        wrong_letters=frozenset(),
        misses=0,
    )
    try:
        validate_state(state)
    except ValueError:
        pass
    else:
        raise AssertionError(
            "Validation did not fail for guessed letters not in the pattern or wrong "
            "letters set"
        )

    state = GameState(
        pattern=("A", "1", None, None, None),
        guessed_letters=frozenset(["a", "1"]),
        wrong_letters=frozenset(),
        misses=0,
    )
    try:
        validate_state(state)
    except ValueError:
        pass
    else:
        raise AssertionError(
            "Validation did not fail for uppercase letters and non-alphabetic "
            "characters"
        )

    state = GameState(
        pattern=tuple([None] * 5),
        guessed_letters=frozenset(["a"]),
        wrong_letters=frozenset("a"),
        misses=0,
    )
    try:
        validate_state(state)
    except ValueError:
        pass
    else:
        raise AssertionError(
            "Validation did not fail for misses not matching missed letter set"
        )

    state = GameState(
        pattern=tuple([None] * 5),
        guessed_letters=frozenset("a"),
        wrong_letters=frozenset("a"),
        misses=-1,
    )
    try:
        validate_state(state)
    except ValueError:
        pass
    else:
        raise AssertionError("Validation did not fail for negative misses")

    state = GameState(
        pattern=tuple([None] * 5),
        guessed_letters=frozenset("a"),
        wrong_letters=frozenset("a"),
        misses=7,
    )
    try:
        validate_state(state)
    except ValueError:
        pass
    else:
        raise AssertionError("Validation did not fail for excessive misses")

    state = GameState(
        pattern=(), guessed_letters=frozenset(), wrong_letters=frozenset(), misses=0
    )
    try:
        validate_state(state)
    except ValueError:
        pass
    else:
        raise AssertionError("Validation did not fail for empty pattern")


def test_is_won():
    state = GameState(
        pattern=("a", "b", "c", "d", "e"),
        guessed_letters=frozenset(["a", "b", "c", "d", "e"]),
        wrong_letters=frozenset(),
        misses=0,
    )
    assert is_won(state)

    state = GameState(
        pattern=("a", "b", "c", "d", None),
        guessed_letters=frozenset(["a", "b", "c", "d"]),
        wrong_letters=frozenset(),
        misses=0,
    )
    assert not is_won(state)


def test_is_lost():
    state = GameState(
        pattern=("a", "b", "c", "d", None),
        guessed_letters=frozenset(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]),
        wrong_letters=frozenset(["e", "f", "g", "h", "i", "j"]),
        misses=6,
    )
    assert is_lost(state)

    state = GameState(
        pattern=("a", "b", "c", "d", None),
        guessed_letters=frozenset(["a", "b", "c", "d", "e", "f", "g"]),
        wrong_letters=frozenset(["e", "f", "g"]),
        misses=3,
    )
    assert not is_lost(state)


def test_is_finished():
    state = GameState(
        pattern=("a", "b", "c", "d", "e"),
        guessed_letters=frozenset(["a", "b", "c", "d", "e"]),
        wrong_letters=frozenset(),
        misses=0,
    )
    assert is_finished(state)

    state = GameState(
        pattern=("a", "b", "c", "d", None),
        guessed_letters=frozenset(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]),
        wrong_letters=frozenset(["e", "f", "g", "h", "i", "j"]),
        misses=6,
    )
    assert is_finished(state)

    state = GameState(
        pattern=("a", "b", "c", "d", None),
        guessed_letters=frozenset(["a", "b", "c", "d"]),
        wrong_letters=frozenset(),
        misses=0,
    )
    assert not is_finished(state)
