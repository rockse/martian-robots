def evaluate_guess(pattern, guess):
    if not isinstance(pattern, list) and not isinstance(guess, list):
        raise Exception('Please enter input in proper format, use lists')

    right_matches = 0
    wrong_matches = 0

    temp_pattern = []
    temp_guess = []

    for a, b in zip(pattern, guess):
        if a == b:
            right_matches += 1
        else:
            temp_pattern.append(a)
            temp_guess.append(b)

    for a in temp_guess:
        if a in temp_pattern:
            wrong_matches += 1
            temp_pattern.remove(a)

    return (right_matches, wrong_matches)


if __name__ == '__main__':
    print(evaluate_guess([1,4,2,6], [1,4,6,3]))


# Tests
assert evaluate_guess([1,4,2,6], [1,4,6,3]) == (2,1)
assert evaluate_guess([1,4,2,5,5,6], [1,5,5,3,1,6]) == (2,2)
