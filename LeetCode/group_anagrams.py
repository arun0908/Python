# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
# the original letters exactly once.
# Ex: Input: strs = ["eat","tea","tan","ate","nat","bat"] Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# 1. We can solve this by first storing the number of occurrences of each letter in a word in a list
# 2. We initialize a list which has 26 indexes similar to a-z to store the above-mentioned occurrences for each word
# 3. We then use this list as a key in a dictionary, where the words with similar key are appended as values in a dict
# 4. To solve the problem when there is no key in the dictionary, we use a default dictionary instead of a normal dict
# 5. We create this default dictionary as a list, so that we can append list of words with same key and then return only
#    the values of the dict

from collections import defaultdict


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    result = defaultdict(list)
    for word in strs:
        count = [0] * 26
        for c in word:
            count[ord(c) - ord("a")] += 1
        result[tuple(count)].append(word)

    return result.values()


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))