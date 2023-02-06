# Imagine a converstion between two users in a chat app. Given a two dimensional string array messages, reprsenting messages from each user,
# your task is to render the conversation in a message window. Specifically messages[i] represents the ith message in the conversation
# in the following format: [<user>, <text>]. Note that messages[i][0] is either "1" or "2" to describe which user sent the message.
# To render the messenger window, each message must start on a new line. You are given two integers width and userWidth, where width represents
# the width of the entire messenger window and userWidth represents the maximum number of charecters that can be rendered on each line of he conversation.
# Messages which exceed userWidth should be rendered on multiple lines. Words in the message are not allowed to be split in the middle, and it is
# guaranteed that no word in the message has length exceeding userWidth.In the messenger window, messages from user "1" should be aligned o the
# left and messages from user "2" should be aligned to the right. To visulaize te messenger window, enclose the conversation into a frame with
# vertical bars and astericks. The leftmost and rightmost sides of the frame should have vertical bars (the | charecter) and the topmost and bottommost
# lines of the frame should have astericks (the * charecter with the length of width) and 2 + symbols on the edges (aligned with the vertical bars |)

# Example: messages = [["1", "Hello how r u"], ["2", "good ty"], ["2", "u"], ["1", "mee too bro"]]
# width = 15 and userWidth = 5. The output should be
# solution(messages, width, userWidth) = ["+***************+","|Hello    |, "|how r  |", "|u  |","|  good|", "|  ty|", "|  u|", "|mee  |","|too  |","|bro  |","+***************+"]
# Note the charecter "u" from the firt message has been moved to a new line as there was'nt enough space on the previous line because of userWidth = 5.
# Note that line "how r" contains 4 charecters and the next line does not start with a space beacuse space should be eliminated with a new line starts

def solution(messages, width, userWidth):
    left_margin = 3
    right_margin = width - userWidth - left_margin

    result = []
    result.append("*" * width)

    for message in messages:
        user, text = message
        lines = []
        line = ""
        words = text.split(" ")
        for word in words:
            if len(line) + len(word) + 1 <= userWidth:
                line += word + " "
            else:
                lines.append(line)
                line = word + " "
        lines.append(line)

        for i in range(len(lines)):
            if user == "1":
                result.append("|" + " " * left_margin + lines[i] + " " * (
                    userWidth - len(lines[i])) + " " * right_margin + "|")
            else:
                result.append("|" + " " * right_margin + lines[i] + " " * (
                    userWidth - len(lines[i])) + " " * left_margin + "|")

    result.append("*" * width)
    return result


print(solution([["1", "Hello how r u"], ["2", "good ty"],
      ["2", "u"], ["1", "mee too bro"]], 15, 5))
