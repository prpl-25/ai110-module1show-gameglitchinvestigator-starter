from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


# --- check_guess ---

def test_check_guess_correct():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_check_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message

def test_check_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_check_guess_too_high_message():
    _, message = check_guess(60, 50)
    assert "LOWER" in message

def test_check_guess_too_low_message():
    _, message = check_guess(40, 50)
    assert "HIGHER" in message

def test_check_guess_boundary_low():
    outcome, _ = check_guess(1, 1)
    assert outcome == "Win"

def test_check_guess_boundary_high():
    outcome, _ = check_guess(100, 100)
    assert outcome == "Win"

def test_check_guess_off_by_one_high():
    outcome, _ = check_guess(51, 50)
    assert outcome == "Too High"

def test_check_guess_off_by_one_low():
    outcome, _ = check_guess(49, 50)
    assert outcome == "Too Low"


# --- get_range_for_difficulty ---

def test_range_easy():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_range_normal():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 50

def test_range_hard():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 100

def test_range_normal_easier_than_hard():
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert normal_high < hard_high

def test_range_easy_easier_than_normal():
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    assert easy_high < normal_high

def test_range_unknown_difficulty():
    low, high = get_range_for_difficulty("Unknown")
    assert low == 1
    assert high == 100


# --- parse_guess ---

def test_parse_guess_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_valid_float_truncates():
    ok, value, err = parse_guess("3.7")
    assert ok is True
    assert value == 3

def test_parse_guess_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err

def test_parse_guess_none():
    ok, value, err = parse_guess(None)
    assert ok is False
    assert value is None
    assert err

def test_parse_guess_non_numeric():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err

def test_parse_guess_negative_number():
    ok, value, err = parse_guess("-5")
    assert ok is True
    assert value == -5

def test_parse_guess_zero():
    ok, value, err = parse_guess("0")
    assert ok is True
    assert value == 0


# --- update_score ---

def test_update_score_win_early():
    # attempt 1: 100 - 10*(1+1) = 80 points
    new_score = update_score(0, "Win", 1)
    assert new_score == 80

def test_update_score_win_minimum_points():
    # Late attempt where formula would give < 10, should give minimum 10
    new_score = update_score(0, "Win", 20)
    assert new_score == 10

def test_update_score_win_adds_to_existing():
    new_score = update_score(50, "Win", 1)
    assert new_score == 130

def test_update_score_too_low_deducts():
    new_score = update_score(50, "Too Low", 1)
    assert new_score == 45

def test_update_score_too_high_odd_attempt_deducts():
    new_score = update_score(50, "Too High", 1)
    assert new_score == 45

def test_update_score_too_high_even_attempt_adds():
    new_score = update_score(50, "Too High", 2)
    assert new_score == 55

def test_update_score_unknown_outcome_unchanged():
    new_score = update_score(50, "Unknown", 1)
    assert new_score == 50
