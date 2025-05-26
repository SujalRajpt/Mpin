from main import evaluate_mpin

# Test dates
dob = "2003-03-31"
spouse_dob = "2004-03-15"
anniversary = "2025-03-14"


# 1. Common MPIN (from list)
def test_common_mpin():
    result = evaluate_mpin("1234")
    assert "COMMONLY_USED" in result["reasons"]


# 2. Low entropy MPIN
def test_low_entropy_mpin():
    result = evaluate_mpin("1112")
    assert "COMMONLY_USED" in result["reasons"]


# 3. Exact DOB variant match
def test_dob_exact_match():
    result = evaluate_mpin("0331", dob=dob)
    assert "DEMOGRAPHIC_DOB_SELF" in result["reasons"]


# 4. Exact spouse DOB match
def test_spouse_dob_exact_match():
    result = evaluate_mpin("200403", spouse_dob=spouse_dob)
    assert "DEMOGRAPHIC_DOB_SPOUSE" in result["reasons"]


# 5. Exact anniversary match
def test_anniversary_exact_match():
    result = evaluate_mpin("0314", anniversary=anniversary)
    assert "DEMOGRAPHIC_ANNIVERSARY" in result["reasons"]


# 6. Hamming distance = 1 with DOB variant
def test_dob_hamming_distance_match():
    result = evaluate_mpin("030303", dob=dob)
    assert "DEMOGRAPHIC_DOB_SELF" in result["reasons"]


# 7. MPIN with all digits same (low entropy)
def test_all_same_digits():
    result = evaluate_mpin("2222")
    assert "COMMONLY_USED" in result["reasons"]


# 8. Strong, unique MPIN
def test_strong_mpin():
    result = evaluate_mpin("7395")
    assert not result["reasons"]  # No reasons implies strong


# 9. MPIN matches year+month from DOB
def test_year_month_match():
    result = evaluate_mpin("200303", dob=dob)
    assert "DEMOGRAPHIC_DOB_SELF" in result["reasons"]


# 10. MPIN off by 1 from spouse DOB variant
def test_spouse_dob_hamming_match():
    result = evaluate_mpin("200406", spouse_dob=spouse_dob)
    assert "DEMOGRAPHIC_DOB_SPOUSE" in result["reasons"]


# 11. 6-digit common MPIN
def test_common_6_digit():
    result = evaluate_mpin("123456")
    assert "COMMONLY_USED" in result["reasons"]


# 12. MPIN with increasing sequence
def test_increasing_sequence():
    result = evaluate_mpin("4567")
    assert "COMMONLY_USED" in result["reasons"]


# 13. MPIN with reverse sequence
def test_reverse_sequence():
    result = evaluate_mpin("4321")
    assert "COMMONLY_USED" in result["reasons"]


# 14. MPIN similar to anniversary
def test_anniversary_hamming_match():
    result = evaluate_mpin("2025", anniversary=anniversary)
    assert "DEMOGRAPHIC_ANNIVERSARY" in result["reasons"]


# 15. MPIN with birth year full
def test_full_year_match():
    result = evaluate_mpin("2003", dob=dob)
    assert "DEMOGRAPHIC_DOB_SELF" in result["reasons"]


# 16. MPIN with just day and year
def test_day_year_combo():
    result = evaluate_mpin("152004", spouse_dob=spouse_dob)
    assert "DEMOGRAPHIC_DOB_SPOUSE" in result["reasons"]


# 17. MPIN is just today's day + time (no match expected)
def test_only_day_match():
    result = evaluate_mpin("252234", spouse_dob=spouse_dob)
    assert not result["reasons"]


# 18. MPIN is far from DOB (no match expected)
def test_far_hamming_distance():
    result = evaluate_mpin("201805", dob=dob)
    assert not result["reasons"]


# 19. MPIN with mix of repeated digits but high entropy
def test_repeated_but_strong():
    result = evaluate_mpin("1223")
    assert not result["reasons"]


# 20. Very strong and random 6-digit PIN
def test_strong_6_digit():
    result = evaluate_mpin("738291")
    assert not result["reasons"]


if __name__ == "__main__":
    test_common_mpin()
    test_low_entropy_mpin()
    test_dob_exact_match()
    test_spouse_dob_exact_match()
    test_anniversary_exact_match()
    test_dob_hamming_distance_match()
    test_all_same_digits()
    test_strong_mpin()
    test_year_month_match()
    test_spouse_dob_hamming_match()
    test_common_6_digit()
    test_increasing_sequence()
    test_reverse_sequence()
    test_anniversary_hamming_match()
    test_full_year_match()
    test_day_year_combo()
    test_only_day_match()
    test_far_hamming_distance()
    test_repeated_but_strong()
    test_strong_6_digit()

    print("All tests passed")
