# Problem 2: Variable-Length Coding
# Given sentence
sentence = "fanchao is a super cool person"

# Remove spaces
text = sentence.replace(" ", "")

# Count how often each letter appears
print("Letter Frequencies:")
for letter in sorted(set(text)):
    print(letter, ":", text.count(letter))

# Assign a binary code to each letter
codes = {
    "o": "101",
    "a": "010",
    "c": "011",
    "e": "0000",
    "f": "0001",
    "h": "0010",
    "i": "0011",
    "l": "1000",
    "n": "1001",
    "p": "1100",
    "r": "1101",
    "s": "1110",
    "u": "1111"
}

# Convert the sentence into binary
encoded = ""

for letter in text:
    encoded += codes[letter]

print("\nEncoded Message:")
print(encoded)

# Check the prefix rule
prefix_free = True

for code1 in codes.values():
    for code2 in codes.values():
        if code1 != code2 and code2.startswith(code1):
            prefix_free = False

print("\nPrefix Rule:")
print("Passed" if prefix_free else "Failed")

# Calculate variable-length coding bits
variable_bits = len(encoded)

# Calculate fixed-length coding bits (4 bits per letter)
fixed_bits = len(text) * 4

# Compare the results
print("\nComparison:")
print("Variable-length bits:", variable_bits)
print("Fixed-length bits:", fixed_bits)
print("Bits saved:", fixed_bits - variable_bits)
