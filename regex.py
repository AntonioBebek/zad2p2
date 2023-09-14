import re

regex = r"^A.*\d.*\s.*B$"

test_string = "Ana 3 B"

match = re.match(regex, test_string)

if match:
    print("Podudaranje pronađeno!")
else:
    print("Podudaranje nije pronađeno.")
