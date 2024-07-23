import string
def check_password_strength(password):
  """Checks the strength of a password based on various criteria.
  Args:
    password: The password to be evaluated.
  Returns:
    A string indicating the password strength (weak, medium, strong, very strong).
  """
  length = len(password)
  has_upper = any(char.isupper() for char in password)
  has_lower = any(char.islower() for char in password)
  has_digit = any(char.isdigit() for char in password)
  has_special = any(char in string.punctuation for char in password)
  strength = 0
  if length >= 8:
    strength += 1
  if has_upper:
    strength += 1
  if has_lower:
    strength += 1
  if has_digit:
    strength += 1
  if has_special:
    strength += 1
  if strength == 0:
    return "Very weak"
  elif strength == 1 or strength == 2:
    return "Weak"
  elif strength == 3 or strength == 4:
    return "Medium"
  else:
    return "Strong"
if __name__ == "__main__":
  password = input("Enter your password: ")
  strength = check_password_strength(password)
  print("Password strength:", strength)
