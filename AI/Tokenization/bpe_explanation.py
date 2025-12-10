"""
Explanation of BPE (Byte Pair Encoding) - The Math Behind Tiktoken

BPE Algorithm Steps:
====================

1. INITIALIZATION: Start with individual bytes/characters
   Example: "hello" -> ['h', 'e', 'l', 'l', 'o']

2. FREQUENCY COUNT: Count all adjacent pairs
   Example pairs in corpus:
   - ('h', 'e'): 156 times
   - ('e', 'l'): 203 times
   - ('l', 'l'): 87 times
   - ('l', 'o'): 142 times

3. MERGE MOST FREQUENT: Find the most frequent pair and merge it
   Example: ('e', 'l') appears 203 times (most frequent)
   Replace all occurrences: "hello" -> "helo"
   New vocabulary: {'h', 'e', 'l', 'o', 'el'}

4. REPEAT: Repeat steps 2-3 until vocabulary size or iteration limit reached
   This creates longer and longer tokens

5. FINAL VOCABULARY: A mapping of token IDs to their string representations
"""

import tiktoken

# Get the GPT-4o tokenizer
enc = tiktoken.encoding_for_model("gpt-4o")

print("=" * 70)
print("TIKTOKEN - BYTE PAIR ENCODING (BPE) DEMONSTRATION")
print("=" * 70)

# Example 1: Simple word tokenization
text1 = "hello"
tokens1 = enc.encode(text1)
print(f"\nExample 1: '{text1}'")
print(f"Tokens: {tokens1}")
for token in tokens1:
    print(f"  Token {token}: {repr(enc.decode([token]))}")

# Example 2: Show vocabulary statistics
print(f"\n{'=' * 70}")
print("TOKENIZER VOCABULARY INFORMATION")
print(f"{'=' * 70}")
vocab_size = enc.n_vocab
print(f"Total vocabulary size: {vocab_size} tokens")
print(f"This means GPT-4o can represent text using {vocab_size} different tokens")

# Example 3: Compression ratio
print(f"\n{'=' * 70}")
print("COMPRESSION RATIO (How Efficient is BPE?)")
print(f"{'=' * 70}")

test_texts = [
    "hello world",
    "The quick brown fox jumps over the lazy dog",
    "Machine learning is fascinating"
]

for text in test_texts:
    # Count characters
    char_count = len(text)
    
    # Count tokens
    tokens = enc.encode(text)
    token_count = len(tokens)
    
    # Compression ratio
    compression = char_count / token_count
    
    print(f"\nText: '{text}'")
    print(f"  Characters: {char_count}")
    print(f"  Tokens: {token_count}")
    print(f"  Compression Ratio: {compression:.2f} chars/token")

# Example 4: Why common words get merged earlier
print(f"\n{'=' * 70}")
print("WHY COMMON WORDS GET SINGLE TOKENS")
print(f"{'=' * 70}")
print("""
In BPE training:
- Common character pairs like 't', 'h' appear millions of times → merged early
- This creates single tokens for "the", "and", "ing", etc.
- Rare words get broken into subword tokens

Example frequency in typical English corpus:
- "the" appears ~7% of all text → single token (very efficient)
- "Lokesh" appears rarely → split into subwords " Lok" + "esh"
""")

# Demonstrate this
common_words = ["the", "and", "is", "you", "that"]
print("\nCommon words (usually single tokens):")
for word in common_words:
    tokens = enc.encode(word)
    token_ids = tokens
    print(f"  '{word}' -> {len(tokens)} token(s): {token_ids}")

print("\nRare/Proper nouns (usually multiple tokens):")
rare_words = ["Lokesh", "Xyzzy", "Qwerty"]
for word in rare_words:
    tokens = enc.encode(word)
    print(f"  '{word}' -> {len(tokens)} tokens: {tokens}")
    for token in tokens:
        print(f"      Token {token}: {repr(enc.decode([token]))}")

# Example 5: The Math Formula
print(f"\n{'=' * 70}")
print("BPE MATHEMATICAL FORMULA")
print(f"{'=' * 70}")
print("""
During training, BPE repeatedly finds:

    pair = argmax(frequency(pair_i) for all adjacent pairs)
    
    vocabulary = vocabulary ∪ {merge(pair)}
    
    corpus = replace_all(pair, merge(pair), corpus)

Repeat until:
    - Vocabulary size reaches target (e.g., 100k tokens)
    - Iteration limit reached
    - Frequency threshold not met

Result: A tokenizer that efficiently compresses text using statistically
optimal subword units learned from the training corpus.
""")

# Example 6: Token efficiency
print(f"\n{'=' * 70}")
print("WHY THIS MATTERS FOR LANGUAGE MODELS")
print(f"{'=' * 70}")
print("""
GPT-4o processes tokens, not characters:
- Input: "Hello world" → [Hello] [world] = 2 tokens
- Processing: 2 tokens through the model (more efficient)
- Alternative (char-level): 11 tokens for 11 characters

Tokens are the "vocabulary" that neural networks actually understand.
Smaller token count = faster processing, lower cost, better efficiency.
""")
