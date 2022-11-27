# Data for the new york city weather for the first few days in the month of january. Data manipulation using dictionary.
weather = {
    "Jan 1": 27,
    "Jan 2": 31,
    "Jan 3": 23,
    "Jan 4": 34,
    "Jan 5": 37,
    "Jan 6": 38,
    "Jan 7": 29,
    "Jan 8": 30,
    "Jan 9": 35,
    "Jan 10": 30
}
arr = [27, 31, 23, 34, 37, 38, 29, 30, 35, 30]
print("Average weather in the first week of january: ", sum(arr[0:7])/len(arr[0:7]))
print("Maximum weather in first 10 days of January: ",max(arr))
print("Temperature on Jan 9th: ", weather["Jan 9"])
print("Temperature on Jan 4th: ", weather["Jan 4"])

# poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in python and print
# every word and its count as show below. Think about the best data structure that you can use to solve this problem
str_dict = {}
with open('poem.txt', "r") as f:
    for line in f:
        tokens = line.split(' ')
        for token in tokens:
            token = token.replace('\n', '')
            if token in str_dict:
                str_dict[token] += 1
            else:
                str_dict[token] = 1
print(str_dict)




