# MPIN Strength Checker

This project helps you check how strong or weak a 6-digit MPIN (Mobile PIN) is. It looks for common patterns, checks if the MPIN is based on personal information like your date of birth, and tests how random or predictable the MPIN is.


## How It Works

### 1. Common MPINs

We have collected a list of MPINs that are most commonly used by people, such as `123456`, `000000`, or `111111`. These are checked first because they are easy to guess and should not be used.



### 2. Shannon Entropy

We use something called **Shannon entropy** to measure how random the MPIN is.

* If the MPIN has repeated or predictable characters (like `111111` or `121212`), it gets a low score.
* A score below **1.3** is considered weak.
* This value of 1.3 can be changed later if you want to make the check stricter or more lenient.



### 3. Increasing or Decreasing Patterns

The program checks if your MPIN follows a simple number pattern like:

* `123456` (numbers go up)
* `654321` (numbers go down)

These kinds of MPINs are easy to guess and are marked as weak.



### 4. Hamming Distance

Even if your MPIN is not exactly the same as a personal date (like your birthday), we check if it's just 1 or 2 digits away from it.

For example, if your spouse's birthday is `2003-01-21`, and your MPIN is `200322`, it is marked as weak because it's very similar to `200321`.

This helps catch MPINs that are only slightly different from dates people often use.



### 5. Date Variants

For each personal date you give (your birth date, your spouse's birth date, or anniversary), the program creates different versions of it such as:

* `YYYYMMDD`
* `DDMMYYYY`
* `YYMMDD`
* `MMDDYY`

It then checks if your MPIN matches any of these or is very close to any of them.


## Example

```bash
Enter your date of birth (yyyy-mm-dd): 1990-01-01
Enter your spouse's date of birth (yyyy-mm-dd): 1995-05-15
Enter your anniversary date (yyyy-mm-dd): 2020-10-10
Enter your MPIN: 199505
MPIN Strength: WEAK
Reasons: ['DEMOGRAPHIC_DOB_SPOUSE']
```

## Built With

* Python 3
* Uses basic Python inbuilt libraries like `datetime` and `math`
* Easy to understand and plug into other apps


## License

This project is licensed under the MIT License. You are free to use, share, or improve it.

