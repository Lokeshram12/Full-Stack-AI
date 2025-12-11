import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
api_key = os.getenv("GOOGLE_API_KEY", "")

if not api_key:
    print("Error: GOOGLE_API_KEY not found in .env file")
    exit(1)

# Configure with your API key
genai.configure(api_key=api_key)

# Use the correct method to generate content
# gemini-2.5-flash is the latest stable model
try:
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content("Explain how AI works in a few words")
    print(response.text)
except Exception as e:
    print(f"Error: {e}")
    print("\n⚠️  Quota Exceeded on Free Tier")
    print("Solutions:")
    print("1. Enable billing: https://console.cloud.google.com/project/_/billing")
    print("2. Wait 5-10 minutes for activation")
    print("3. Check rate limits: https://ai.google.dev/docs/rate-limits")