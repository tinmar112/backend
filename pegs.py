def pegs(ref: list[str], test: list[str]) -> str:
    """Implements the matching algorithm which returns pegs for the Mastermind game."""
    assert len(ref) == len(test)

    n = len(ref)
    pegs: str = ' '
    already_counted_ref: list[int] = []
    already_counted_test: list[int] = []

    # First, we have to treat red pegs, which have priority over white pegs.
    for i in range(n):
        if ref[i] == test[i]:
            pegs = pegs + ' red'
            already_counted_ref.append(i)
            already_counted_test.append(i)

    # Now treating white pegs.
    for i in range(n):
        for j in range(n):
            if ref[i] == test[j] and (i not in already_counted_ref) and (j not in already_counted_test):
                pegs = pegs + ' white'
                already_counted_ref.append(i)
                already_counted_test.append(j)

    return pegs