from pathlib import Path

# read the local file
file_path = Path(__file__).parent/"sample_file.txt"
with open(file_path, "r") as file:
    sample_file = file.read()
    #print(sample_file)

words = sample_file.split()

counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1


sorted_words = sorted(counts.items(), key=lambda word: word[1], reverse=True)

for word, freq in sorted_words:
    print(word, ":", freq)
