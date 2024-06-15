def string_reverse(string):
    if len(string) == 1:
        return string
    else:
        return string_reverse(string[1:]) + string[:1]


print(string_reverse("hello"))
