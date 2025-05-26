## How It Works

### 1. Common MPINs

I collected commonly used mpins such as `123456`, `000000`, or `111111`. These are checked first because they are easy to guess and should not be used.


### 2. Shannon Entropy

**Shannon entropy** is used to measure how random the MPIN is.

* If the MPIN has repeated or predictable characters (like `111111` or `121212`), it gets a low score.
* A score below **1.3** is considered weak.
* This value of 1.3 can be changed later if you want to make the check stricter or more lenient.



### 3. Increasing or Decreasing Patterns

The program checks if your MPIN follows a simple number pattern like:

* `123456` (ascending)
* `654321` (descending)

These kinds of MPINs are easy to guess and are marked as weak.


### 4. Hamming Distance

Even if your MPIN is not exactly the same as a personal date (like your birthday), we check if it's just 1 or 2 digits away from it.

For example, if your spouse's birthday is `2003-01-21`, and your MPIN is `200322`, it is marked as weak because it's very similar to `200321`.

This helps catch MPINs that are only slightly different from dates people often use. The sestivity for this can be adjusted in code. Right now we are going with hamming distance < 1 indicate a weak mpin.



### 5. Date Variants

For each personal date you give (your birth date, your spouse's birth date, or anniversary), the program creates different versions of it such as:

* `YYYYMMDD`
* `DDMMYYYY`
* `YYMMDD`
* `MMDDYY`

It then checks if your MPIN matches any of these or is very close to any of them.
I have compiled a list of common pins from https://github.com/Slon104/Common-PIN-Analysis-from-haveibeenpwned.com.git. 


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
* Uses Python inbuilt libraries like `datetime` and `math`



## License

This project is licensed under the MIT License. 

