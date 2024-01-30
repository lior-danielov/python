import re  # regular expressions

# email = 'jose@tecladocode.com'          # @ = at sign
# expression = '[a-z]+'
# expression = '[a-z\.]+'

# matches = re.findall(expression, email)
# print(matches)

# name = matches[0]
# domain = f'{matches[1]}.{matches[2]}'
# print(domain)
# domain = matches[1]
# print(domain)

# email = 'tal@sharabi.com'
# parts = email.split('@')
# name = parts[0]
# domain = parts[1]
# print(parts)
# print(name)
# print(domain)


# validating a given email address, using EDD (error driven dev.)
def validate_email(email):
    # split the email to 2 parts
    parts = email.split("@")

    if len(parts) != 2:
        return False

    # validate username
    username = parts[0]
    if not username or not re.match(r"[a-zA-Z0-9_\.]+", username):
        return False

    # validate domain
    domain = parts[1]
    if not domain or "." not in domain:
        return False

    # split the domain to 2 parts
    subdomains = domain.split(".")
    if len(subdomains) < 2:
        return False

    return True


# examples

# good (valid) emails
valid_emails = ["Eyal@Eyal.com", "869tal@sh.sh.com"]

# bad (invalid) emails
invalid_emails = ["user", "user@", "shmuel.perl@rich.com", "user@invalid", "tal.ex", "@.com"]

for email in valid_emails:
    if validate_email(email):
        print(f"{email} is valid")
    else:
        print(f"{email} is invalid")

for email in invalid_emails:
    if validate_email(email):
        print(f"{email} is valid (SHOULD BE INVALID)")
    else:
        print(f"{email} is invalid as expected")





