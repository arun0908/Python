# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

def lengthOfLastWord(s: str) -> int:
    word = s.split()
    return len(word[-1])


print(lengthOfLastWord('a'))  # 1
print(lengthOfLastWord("Hello World"))  # 5
print(lengthOfLastWord("   fly me   to   the moon  "))  # 4
