import re
def validate_email(email):
    pattern = r'^[A-Za-z0-9]+([._-]?[A-Za-z0-9]+)*@[A-Za-z0-9]+([.-]?[A-Za-z0-9]+)*\.[A-Za-z]{2,}$'
    if not email:
        return "Invalid Email: Missing email"
    if email.count("@") == 0:
        return "Invalid Email: Missing @ symbol"
    if email.count("@") > 1:
        return "Invalid Email: Multiple @ symbols"
    if re.fullmatch(pattern, email):
        return "Valid Email"
    return "Invalid Email: Incorrect format or invalid characters"
def validate_registration(reg_id):
    pattern = r'^CSE[0-9]{7}$'
    if not reg_id:
       return "Invalid ID: Missing registration ID"
    if re.fullmatch(pattern, reg_id):
        return "Valid Registration ID"
    return "Invalid ID: Incorrect format"
# Main program
email = input("Enter student email: ")
reg_id = input("Enter registration ID: ")
print("\n--- Validation Results ---")
print(validate_email(email))
print(validate_registration(reg_id))

