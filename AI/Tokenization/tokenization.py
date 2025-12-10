import tiktoken


enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey, My name is Lokesh"

tokens = enc.encode(text)

print("Tokens: ", tokens)
print("\n--- Token to Text Mapping ---")
for token in tokens:
    decoded = enc.decode([token])
    print(f"Token: {token:6d} -> Text: {repr(decoded)}")

dec = enc.decode(tokens)

print("Decoded Text: ", dec)