from mpin_strength_checker import (
    calculate_shannon_entropy,
    generate_date_variants,
    hamming_distance,
    check_increasing_and_decreasing_sequence,
    COMMON_MPINS,
)


def evaluate_mpin(mpin, dob=None, spouse_dob=None, anniversary=None):
    reasons = []

    if (
        mpin in COMMON_MPINS
        or calculate_shannon_entropy(mpin)
        < 1.3  # this can be adjusted based on requirements
        or check_increasing_and_decreasing_sequence(mpin)
    ):
        reasons.append("COMMONLY_USED")

    def check_against_demographic(date_str, label):
        variants = generate_date_variants(date_str)
        if mpin in variants:
            reasons.append(label)
        elif any(hamming_distance(mpin, v) <= 1 for v in variants):
            reasons.append(label)

    if dob:
        check_against_demographic(dob, "DEMOGRAPHIC_DOB_SELF")
    if spouse_dob:
        check_against_demographic(spouse_dob, "DEMOGRAPHIC_DOB_SPOUSE")
    if anniversary:
        check_against_demographic(anniversary, "DEMOGRAPHIC_ANNIVERSARY")

    return {
        "reasons": reasons,
    }


if __name__ == "__main__":
    # test with user input
    print("Welcome to the MPIN Strength Checker!")
    print("Please enter your details to evaluate your MPIN strength.")
    dob = input("Enter your date of birth (yyyy-mm-dd): ")
    spouse_dob = input("Enter your spouse's date of birth (yyyy-mm-dd): ")
    anniversary = input("Enter your anniversary date (yyyy-mm-dd): ")
    mpin = input("Enter your MPIN: ")
    result = evaluate_mpin(
        mpin, dob=dob, spouse_dob=spouse_dob, anniversary=anniversary
    )
    print(f"MPIN Strength : {result}")

    # test input with hardcoded cases

    # print(
    #     evaluate_mpin(
    #         "987654",
    #         dob="2003-03-31",
    #         spouse_dob="2004-04-03",
    #         anniversary="2010-01-01",
    #     )
    # )
