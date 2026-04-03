from pathlib import Path

file_path = Path(__file__).parent/"sample_file.txt"

word_freq = {}

with open(file_path, "r") as file:
    for line in file:
        for char in line:
            if char in word_freq:
                word_freq[char] += 1
            else:
                word_freq[char] = 1

# sort by most frequent first

sorted_freq = sorted(word_freq.items(), key = lambda x: x[1], reverse= True)

print(f"{'Character':<15} {'Count'}")
print("-" * 25)
for char, count in sorted_freq:
    label = repr(char)   # shows \n, \t etc. clearly
    print(f"{label:<15} {count}")