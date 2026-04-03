# character counter

from pathlib import Path

file_path = Path(__file__).parent/"sample_file.txt"
char_length = 0
with open(file_path, "r") as file:
    char = file.read()
    
print(len(char))

