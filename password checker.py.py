
import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[@$!%*?&#]', password) is not None

    strength_score = sum([
        length_criteria,
        lowercase_criteria,
        uppercase_criteria,
        number_criteria,
        special_char_criteria
    ])

    # Feedback based on the strength score
    if strength_score == 5:
        strength_feedback = "Very Strong"
    elif strength_score == 4:
        strength_feedback = "Strong"
    elif strength_score == 3:
        strength_feedback = "Moderate"
    elif strength_score == 2:
        strength_feedback = "Weak"
    else:
        strength_feedback = "Very Weak"

    # Detailed feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_char_criteria:
        feedback.append("Password should include at least one special character (e.g., @$!%*?&).")

    return {
        "strength": strength_feedback,
        "feedback": feedback
    }

# Example usage
password = input("Enter a password to assess: ")
assessment = assess_password_strength(password)
print(f"Password Strength: {assessment['strength']}")
if assessment['feedback']:
    print("Feedback:")
    for item in assessment['feedback']:
        print(f" - {item}")