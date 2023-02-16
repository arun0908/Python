# Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed,
# and the character will be typed 1 or more times. You examine the typed characters of the keyboard.
# Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.


def isLongPressedName(name: str, typed: str) -> bool:
    name_dict = {}
    typed_dict = {}
    for i in name:
        name_dict[i] = 1 + name_dict.get(i, 0)
    for i in typed:
        typed_dict[i] = 1 + typed_dict.get(i, 0)
    for i in name_dict:
        if i not in typed_dict or (typed_dict[i] < name_dict[i]):
            return False
    return True


print(isLongPressedName("alex", "aaleex"))
print(isLongPressedName("saeed", "ssaaedd"))
