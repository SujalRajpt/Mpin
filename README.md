# 🔐 MPIN Strength Checker

This tool helps evaluate the strength of a **Mobile PIN (MPIN)** to protect users from easily guessable and weak codes. It uses a combination of heuristics and entropy analysis to flag weak MPINs based on common patterns and personal data.

---

## 📱 What is an MPIN?

An **MPIN (Mobile Personal Identification Number)** is typically a 4- to 6-digit numeric code used to authenticate users on mobile apps, especially in banking and financial services. Since it's short and user-defined, it’s often vulnerable to poor choices like `123456`, birth dates, or repetitive patterns.

This tool aims to **prevent weak or predictable MPINs** and encourages the use of safer combinations.

---

## ⚙️ How It Works

Your MPIN is analyzed using the following checks:

---

### 1. 🔢 Common MPINs List

We start by comparing your MPIN with a known list of the most commonly used (and leaked) PINs like:

* `123456`
* `000000`
* `1986`

These PINs are widely used and easily guessable. Even something like `1986` might seem personal or obscure but is among the most leaked combinations.

> 📚 Source: [Common PIN Analysis from haveibeenpwned.com](https://github.com/Slon104/Common-PIN-Analysis-from-haveibeenpwned.com.git)

---

### 2. 📉 Shannon Entropy

**Shannon entropy** is used to measure the randomness of the MPIN.

* Repetitive or patterned MPINs (like `111111`, `121212`) have **low entropy**.
* A score below **1.3** is marked as **weak**.
* You can tweak this threshold in the code to be stricter or more lenient.

> 💡 Entropy gives an idea of how hard it would be to guess the MPIN randomly.

---

### 3. 🔼 Ascending/Descending Patterns

We detect common numeric sequences that are predictable, such as:

* `123456` (ascending)
* `654321` (descending)

These are marked **weak** because they follow simple, linear patterns that attackers commonly try first.

---

### 4. 🧠 Hamming Distance from Personal Dates

Checks how *similar* the MPIN is to sensitive dates like your:

* Date of Birth
* Spouse's DOB
* Anniversary

Example:
If your spouse’s birthday is `2003-01-21` and your MPIN is `200322`, it’s flagged **weak** — only one digit changed from `200321`.

> 🧮 We use **Hamming distance** to measure similarity. MPINs with a distance less than **1** from a date variant are considered unsafe. This threshold is configurable.

---

### 5. 🗓️ Date Variant Matching

For each personal date (DOB, spouse’s DOB, anniversary), we generate several formats like:

* `YYYYMMDD` → `19900101`
* `DDMMYYYY` → `01011990`
* `YYMMDD` → `900101`
* `MMDDYY` → `010190`

The tool then checks if your MPIN **matches or closely resembles** any of these variants.

---

## 🧪 Example

```bash
Enter your date of birth (yyyy-mm-dd): 1990-01-01
Enter your spouse's date of birth (yyyy-mm-dd): 1995-05-15
Enter your anniversary date (yyyy-mm-dd): 2020-10-10
Enter your MPIN: 199505

MPIN Strength: WEAK
Reasons: ['DEMOGRAPHIC_DOB_SPOUSE']
```

---

## 🛠️ Built With

* Python 3
* Uses standard Python libraries:

  * `datetime`
  * `math`
  * `collections`
  * `itertools`

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](./LICENSE) file for details.

---

## 🚀 Future Improvements (Optional Section)

Here are a few ideas for expanding this tool:

* Support for 4-digit MPINs
* Integration with password managers or apps
* Web or mobile interface for non-technical users
* Machine learning model for PIN pattern learning
* Add support for non-numeric PINs (alphanumeric)

