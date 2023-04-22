# Given a string s, return the number of segments in the string.
# A segment is defined to be a contiguous sequence of non-space characters.

def countSegments(s: str) -> int:
    if s == '':
        return 0
    else:
        # my_list = s.split()
        # my_list = s.split(' ') can be used, but it only splits based on
        # single whitespace and incase there are more than one
        # whitespaces, it fails. Even re.split(r"\s+",s) regex split fails.
        return len(s.split())


print(countSegments("Hello, my name is John"))  # 5
print(countSegments("Hello"))  # 1
