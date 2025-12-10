import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

# Test the same word in different contexts
test_sentences = [
    "My name is Lokesh",
    "The name of the company",
    "What is your name?",
    "I know his name already",
    "name name name"  # Word repeated
]

print("=== Token Value Consistency Test ===\n")

# First, get tokens for individual words
individual_words = {
    "name": " name",
    "word": " word",
    "is": " is",
    "My": "My"
}

print("--- Individual Word Token Values ---")
for word_desc, word in individual_words.items():
    token = enc.encode(word)[0]
    print(f"'{word}' -> Token: {token}")

print("\n--- Same Words in Different Sentences ---")
for sentence in test_sentences:
    tokens = enc.encode(sentence)
    print(f"\nSentence: '{sentence}'")
    print(f"All Tokens: {tokens}")
    
    # Show individual tokens
    for i, token in enumerate(tokens):
        decoded = enc.decode([token])
        print(f"  Position {i}: Token {token:6d} -> {repr(decoded)}")
