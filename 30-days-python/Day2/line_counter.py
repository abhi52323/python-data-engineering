from pathlib import Path

file_path = Path(__file__).parent/"sample file.txt"

with open(file_path,"r") as file:
    lines = len(list(map(lambda line: line, file)))
    print(lines)