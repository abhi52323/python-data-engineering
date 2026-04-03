from pathlib import Path

file_path = Path(__file__).parent/"sample file.txt"

with open(file_path,"r") as file:
    words = sum(map(lambda line: len(line.split()), file))
    print("Total words:", words)