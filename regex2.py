
import re

def check_email(email):
    regex_email = r'^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$'
    match_email = re.match(regex_email, email)
    return match_email is not None

def check_eduid(eduid):
    regex_eduid = r'^[a-zA-Z][a-zA-Z]+\d*@sum\.ba$'
    match_eduid = re.match(regex_eduid, eduid)
    return match_eduid is not None

email = input("Unesite e-mail: ")
eduid = input("Unesite eduId: ")

valid_email = check_email(email)
valid_eduid = check_eduid(eduid)

if valid_email:
    print("Uneseni e-mail je validan.")
else:
    print("Uneseni e-mail nije validan.")

if valid_eduid:
    print("Uneseni eduId je validan.")
else:
    print("Uneseni eduId nije validan.")
