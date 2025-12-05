# password_utils.py
import string

def check_password_strength(password: str) -> dict:
    """
    Check the strength of a password based on:
    - Length
    - Uppercase letters
    - Lowercase letters
    - Digits
    - Special characters

    Returns a dictionary with:
    - score (0–7)
    - label ("Very Weak", "Weak", "Medium", "Strong", "Very Strong")
    - details (what criteria passed/failed)
    - suggestions (how to improve)
    """

    # --- 1. Basic setup ---
    length = len(password)
    score = 0
    suggestions = []
    details = {}

    # --- 2. Length scoring ---
    if length < 8:
        length_points = 0
        suggestions.append("Use at least 8 characters.")
    elif 8 <= length <= 11:
        length_points = 1
    elif 12 <= length <= 15:
        length_points = 2
    else:  # length >= 16
        length_points = 3

    score += length_points
    details["length"] = {
        "value": length,
        "points": length_points,
        "passed": length >= 8
    }

    # --- 3. Character type checks ---
    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    special_characters = string.punctuation
    has_special = any(ch in special_characters for ch in password)

    # Uppercase
    if has_upper:
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter (A–Z).")

    # Lowercase
    if has_lower:
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter (a–z).")

    # Digit
    if has_digit:
        score += 1
    else:
        suggestions.append("Add at least one number (0–9).")

    # Special character
    if has_special:
        score += 1
    else:
        suggestions.append("Add at least one special character (e.g. @, #, $, %).")

    details["has_upper"] = has_upper
    details["has_lower"] = has_lower
    details["has_digit"] = has_digit
    details["has_special"] = has_special

    # --- 4. Determine strength label based on score ---
    if score <= 2:
        label = "Very Weak"
    elif 3 <= score <= 4:
        label = "Weak"
    elif score == 5:
        label = "Medium"
    elif score == 6:
        label = "Strong"
    else:  # score == 7
        label = "Very Strong"

    # --- 5. Extra suggestion for stronger passwords ---
    if length < 12:
        suggestions.append("Increase length to at least 12 characters for better security.")

    # --- 6. Build and return result ---
    result = {
        "password": password,
        "score": score,
        "label": label,
        "details": details,
        "suggestions": suggestions
    }

    return result
