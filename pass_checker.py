import re
import string

def check_password_strength(password):
    """
    Evaluate strength of a password based on multiple criteria:
    - length (minimum 8 characters)
    - upercase and lowercase letters
    - numbers
    - special characters
    - avoids common passwords

    Returns:
        str: Strength feedback (weak,moderate, strong) with suggestions
    """

    # List of comnnon weak passwords
    common_passwords = ["password", "123456", "123456789", "qwerty", "abc123"]

    #checkfor common passwords
    if password.lower() in common_passwords:
        return "Weak - Your password is too common. Choose something unique."
    
    #Define regex patterns
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(rf"[{re.escape(string.punctuation)}]", password) is None

    #calculate strength score
    errors = [length_error,lowercase_error, uppercase_error, digit_error, special_char_error]
    score = errors.count(False)

    #provide detailed feedback
    if score <=2:
        return "Weak - Use a mix of uppercase, lowercase, numbers, and special characters."
    elif score == 3 or score == 4:
        return "Moderate - Add more complexity like special characters or numbers"
    else:
        return "Strong - Great job! your password is secure."
    
# code execution
if __name__ =='__main__':
    print("Password Strength Checker\n -----------------------------")
    password = input("Input your password: ")
    strength = check_password_strength(password)
    print(f"\nPassword Strength: {strength}")