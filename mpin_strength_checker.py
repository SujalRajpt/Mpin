import math
from datetime import datetime


COMMON_MPINS = {
    "1234",
    "1111",
    "0000",
    "1212",
    "7777",
    "2580",
    "0852",
    "6969",
    "4321",
    "1004",
    "123456",
    "111111",
    "000000",
    "654321",
    "112233",
    "999999",
    "121212",
    "123123",
}


def calculate_shannon_entropy(pin):
    """
    used to find mpins with repeated characters(low entropy) which may be easier to guess.

    Shannon entropy is a measure from information theory that quantifies the
    uncertainty or randomness in a string

    Mathematical formula:
        H = -∑(p_i * log2(p_i)) for all unique digits i
        where p_i = (frequency of digit i) / (total number of digits)


    Example:
        PIN: "1122" → Digits '1' and '2' appear twice each.
        p = 2/4 = 0.5 → H = -[0.5*log2(0.5) + 0.5*log2(0.5)] = 1.0

    """
    freq = {}
    for digit in pin:
        if digit in freq:
            freq[digit] += 1
        else:
            freq[digit] = 1

    n = len(pin)
    return -sum((count / n) * math.log2(count / n) for count in freq.values())


def hamming_distance(s1, s2):
    """Calculate the Hamming distance between two strings.
    The Hamming distance is defined as the number of positions
    at which the corresponding characters are different.

    For example:
        s1 = "2003010"
        s2 = "2003020"
        hamming_distance(s1, s2) = 1  # Only the 6th digit is different

    """
    if len(s1) != len(s2):
        return float("inf")
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def check_increasing_and_decreasing_sequence(pin):
    digits = [int(d) for d in pin]
    is_strictly_decreasing = all(
        digits[i] == digits[i + 1] + 1 for i in range(len(digits) - 1)
    )
    is_strictly_increasing = all(
        digits[i] == digits[i + 1] - 1 for i in range(len(digits) - 1)
    )
    return is_strictly_decreasing or is_strictly_increasing


def generate_date_variants(date_str):
    date = None
    for fmt in ("%Y-%m-%d", "%Y%m%d"):
        try:
            date = datetime.strptime(date_str, fmt)
            break
        except ValueError:
            continue

    # correctly format day, month, year, and year2
    day = f"{date.day:02}"  #:02 is for proper zero-padding
    month = f"{date.month:02}"
    year = str(date.year)
    year2 = year[-2:]  # last two digits of year

    parts = [day, month, year, year2]
    variants = set()

    # shuffles and mixes parts to create combinations
    for i in range(len(parts)):
        for j in range(len(parts)):
            for k in range(len(parts)):
                combo2 = parts[i] + parts[j]
                combo3 = parts[i] + parts[j] + parts[k]
                # this make sure that only 4 and 6 digit combinations are added
                if len(combo2) in (4, 6):
                    variants.add(combo2)
                if len(combo3) == 6:
                    variants.add(combo3)
    variants.add(year)
    return variants


# (True, False)
