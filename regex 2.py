import re
def is_valid_email(email):
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return re.search(regex, email) is not None
email1 = "user@mywebsite-name.com"
email2 = "user@example.website"

print(f"{email1} is valid:{is_valid_email(email1)}")
print(f"{email2} is valid:{is_valid_email(email2)}")