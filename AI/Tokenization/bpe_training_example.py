"""
BPE TRAINING WITH YOUR EXAMPLE DATA
Training corpus: "cat mat sat cat sat mat cat cat sat"
"""

from collections import Counter

print("=" * 80)
print("BPE TRAINING FROM SCRATCH WITH YOUR DATA")
print("=" * 80)

# Your training data
training_data = "cat mat sat cat sat mat cat cat sat"
print(f"\nTraining corpus: '{training_data}'")
print(f"Total characters: {len(training_data)}")

# ITERATION 0: Start with individual characters
print("\n" + "=" * 80)
print("ITERATION 0: INITIAL STATE (INDIVIDUAL CHARACTERS)")
print("=" * 80)
text = training_data
print(f"Text: {text}")
print(f"Characters: {list(text)}")

# Count all pairs
def count_pairs(text):
    pairs = []
    for i in range(len(text) - 1):
        pairs.append((text[i], text[i+1]))
    return Counter(pairs)

# ITERATION 1: Find most frequent pair
print("\n" + "=" * 80)
print("ITERATION 1: FIND MOST FREQUENT PAIR")
print("=" * 80)
pairs = count_pairs(text)
print("All pairs and their frequencies:")
for pair, count in sorted(pairs.items(), key=lambda x: -x[1]):
    print(f"  {pair}: {count} time(s)")

most_common_pair = pairs.most_common(1)[0]
print(f"\n✓ MOST FREQUENT PAIR: {most_common_pair[0]} (appears {most_common_pair[1]} times)")

# Merge it
merged_pair = "".join(most_common_pair[0])
text = text.replace(merged_pair[0] + merged_pair[1], f"<{merged_pair}>")
print(f"After merging '{merged_pair}':")
print(f"Text: {text}")
print(f"Vocabulary so far: {merged_pair}")

# ITERATION 2: Find next most frequent pair
print("\n" + "=" * 80)
print("ITERATION 2: FIND NEXT MOST FREQUENT PAIR")
print("=" * 80)
pairs = count_pairs(text)
print("All pairs and their frequencies:")
for pair, count in sorted(pairs.items(), key=lambda x: -x[1]):
    print(f"  {pair}: {count} time(s)")

most_common_pair = pairs.most_common(1)[0]
print(f"\n✓ MOST FREQUENT PAIR: {most_common_pair[0]} (appears {most_common_pair[1]} times)")

# Merge it
merged_pair_2 = "".join(most_common_pair[0])
text = text.replace(merged_pair_2[0] + merged_pair_2[1], f"<{merged_pair_2}>")
print(f"After merging '{merged_pair_2}':")
print(f"Text: {text}")
print(f"Vocabulary so far: at, {merged_pair_2}")

# ITERATION 3: Find next most frequent pair
print("\n" + "=" * 80)
print("ITERATION 3: FIND NEXT MOST FREQUENT PAIR")
print("=" * 80)
pairs = count_pairs(text)
print("All pairs and their frequencies:")
for pair, count in sorted(pairs.items(), key=lambda x: -x[1]):
    print(f"  {pair}: {count} time(s)")

if pairs:
    most_common_pair = pairs.most_common(1)[0]
    print(f"\n✓ MOST FREQUENT PAIR: {most_common_pair[0]} (appears {most_common_pair[1]} times)")
else:
    print("\n✗ No more pairs to merge")

# FINAL VISUALIZATION
print("\n" + "=" * 80)
print("FINAL RESULT: TOKENS LEARNED FROM YOUR DATA")
print("=" * 80)
print(f"""
Training data: "cat mat sat cat sat mat cat cat sat"

BPE learned these token merges (in order of frequency):
  1. Most frequent pair: ('a', 't') → 3 occurrences → creates token "at"
  2. Next frequent pair: ('m', 'a') or ('s', 'a') → creates another token
  3. Continue until desired vocabulary size...

WHY THIS MATTERS:
- 'at' is the most common pattern in your data
- 'at' appears in: c[at], m[at], s[at] = 3 times!
- So BPE creates a token for 'at' to save space

VOCABULARY LEARNED:
  Token "at"  → represents the bigram 'a' + 't'
  Token "ca"  → represents the bigram 'c' + 'a' (if we continue)
  Token "sa"  → represents the bigram 's' + 'a' (if we continue)
  Token "ma"  → represents the bigram 'm' + 'a' (if we continue)

TOKENIZATION RESULT:
  "cat" → could be: [c] [at] or just [cat] if frequency is high enough
  "mat" → could be: [m] [at] or just [mat]
  "sat" → could be: [s] [at] or just [sat]
""")

# SHOW THE PATTERN
print("\n" + "=" * 80)
print("PATTERN IN YOUR DATA")
print("=" * 80)
print("""
Your training data: cat mat sat cat sat mat cat cat sat
                    ███ ███ ███ ███ ███ ███ ███ ███ ███

Notice: ___ (underscore represents position)
- All 3 words follow pattern: (any letter) + 'at'
- That's why 'at' is the most frequent pair!

Pattern breakdown:
  c + at = cat (3 times)
  m + at = mat (2 times)  
  s + at = sat (2 times)
  
Total 'at' pairs = 3 + 2 + 2 = 7 times! (most frequent)
""")

print("\n" + "=" * 80)
print("COMPARISON: WITH vs WITHOUT BPE TOKENS")
print("=" * 80)

test_sentence = "cat mat sat"
original_chars = len(test_sentence)
print(f"\nSentence: '{test_sentence}' ({original_chars} characters)")

# Without BPE (character level)
print(f"\nWithout BPE (character-level):")
print(f"  Tokens: {list(test_sentence)}")
print(f"  Token count: {len(test_sentence)}")

# With BPE (what we learned)
print(f"\nWith BPE (learned 'at' token):")
print(f"  Possible tokenization: [c][at] + [m][at] + [s][at]")
print(f"  Token count: 6 tokens")
print(f"  Savings: {len(test_sentence) - 6} fewer tokens!")

print("\n✓ This is how BPE optimizes based on your training data!")
