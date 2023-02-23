file = open('test.txt')
print(file.read())
# When we try to print the file again it does not print anything, it is empty
print(file.read())
# same over here, because once we open a file and read it once, the cursor is set to the end of the file
print(file.read())
# so when we try to read it again, it cant read anything as there is nothing left to read
print(file.read())
# To solve this we use the seek method
# we pass 0 in the seek method, indicating it to return to the index position or the starting position.
file.seek(0)
print(file.read())
file.seek(0)
print(file.readline())  # used to read a single line
file.seek(0)
print(file.readlines())  # used to read all the lines as a single line
file.seek(0)
write_file = open('test.txt', 'w')  # opens the file in a write mode
write_file.write('This is an addition through the code')
print(file.read())
file.close()  # it is always a good pratice to close the files we have opened.
write_file.close()
