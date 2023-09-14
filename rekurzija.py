def print_string_reverse(string):
    if len(string) == 0:
        return
    else:
        print_string_reverse(string[1:])
        print(string[0], end='')

print_string_reverse("Antonio Bebek")
