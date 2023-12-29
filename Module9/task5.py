with open("text.txt", "r") as f:
    text = f.read()

text = ''.join(filter(str.isalpha, text)).lower()
letters_count = {}
for letter in text:
    if letter in letters_count:
        letters_count[letter] += 1
    else:
        letters_count[letter] = 1

total_letters = sum(letters_count.values())
letters_freq = [(letter, count/total_letters) for letter, count in letters_count.items()]
letters_freq.sort(key=lambda x: (-x[1], x[0]))

with open("analysis.txt", "w") as f:
    for letter, freq in letters_freq:
        f.write(f"{letter} {freq:.3f}\n")