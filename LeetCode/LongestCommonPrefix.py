# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

def solution(strs: list[str]) -> str:
    strs.sort(key=len)
    prefix = strs[0]
    for i in range(len(prefix), 0, -1):
        if all([prefix[:i] == strs[j][:i] for j in range(1, len(strs))]):
            return prefix[:i]
    return ""


