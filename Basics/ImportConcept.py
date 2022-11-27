# Import the Path class from the pathlib module
from pathlib import Path

# Use a variable to store the Path object returned
currentpath = Path()
print(currentpath.exists())
# Print all the files in the current path or directory
for file in currentpath.glob('*'):
    print(file)
