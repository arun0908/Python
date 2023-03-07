# file = open('test.txt')
# print(file.read())
# # When we try to print the file again it does not print anything, it is empty
# print(file.read())
# # same over here, because once we open a file and read it once, the cursor is set to the end of the file
# print(file.read())
# # so when we try to read it again, it cant read anything as there is nothing left to read
# print(file.read())
# # To solve this we use the seek method
# # we pass 0 in the seek method, indicating it to return to the index position or the starting position.
# file.seek(0)
# print(file.read())
# file.seek(0)
# print(file.readline())  # used to read a single line
# file.seek(0)
# print(file.readlines())  # used to read all the lines as a single line
# file.seek(0)
# write_file = open('test.txt', 'w')  # opens the file in a write mode
# write_file.write('This is an addition through the code')
# print(file.read())
# file.close()  # it is always a good pratice to close the files we have opened.
# write_file.close()

with open('test.txt', mode = 'r') as my_file: # instead of manually opening and closing a file, use of with block helps to close file after execution
    print(my_file.read())
    print(my_file.read()) # cannot be printed because the cursor needs to be set to 0
    my_file.seek(0)
    print(my_file.read())
    print()
try:
    print(my_file.read()) # prints an error as the file has been closed after the use of open block
except ValueError as err:
    print(err)
print()
with open('test.txt', mode = 'r+') as my_file:
    print(my_file.read())
    my_file.write('Trying to replace the existing text')
    print()
    print(my_file.read())
