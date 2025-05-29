def pegs(ref: list[str], test: list[str]) -> str:
    """Implements the matching algorithm which returns pegs for the Mastermind game."""
    assert len(ref) == len(test)

    n = len(ref)
    result = ['empty'] * n
    already_counted_ref = []
    already_counted_test = []

    # First, assign 'red' pegs (correct color and position)
    for i in range(n):
        if ref[i] == test[i]:
            result[i] = 'red'
            already_counted_ref.append(i)
            already_counted_test.append(i)

    # Then assign 'white' pegs (correct color, wrong position)
    for j in range(n):
        if result[j] == 'empty':  # skip already matched positions
            for i in range(n):
                if (
                    ref[i] == test[j]
                    and i not in already_counted_ref
                    and j not in already_counted_test
                ):
                    result[j] = 'white'
                    already_counted_ref.append(i)
                    already_counted_test.append(j)
                    break  # only one match per test[j]

    return ' '.join(result)