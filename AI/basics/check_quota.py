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

print("=" * 70)
print("GEMINI API - MODEL & QUOTA CHECK")
print("=" * 70)

# List available models
print("\n📋 Available Models:")
print("-" * 70)
try:
    models = genai.list_models()
    for model in models:
        print(f"  • {model.name}")
        if hasattr(model, 'supported_generation_methods'):
            print(f"    Methods: {model.supported_generation_methods}")
except Exception as e:
    print(f"Error listing models: {e}")

print("\n" + "=" * 70)
print("TROUBLESHOOTING QUOTA ISSUES")
print("=" * 70)
print("""
If you're seeing quota exceeded errors on a NEW API key:

1. ✅ ENABLE BILLING (Required!)
   - Go to: https://console.cloud.google.com/project/_/billing
   - Add a payment method
   - Wait 5-10 minutes for activation

2. ✅ UPGRADE TO PAID PLAN
   - Free tier has very limited quota
   - Paid plan gives you much higher limits
   - First $5 free credit included

3. ✅ VERIFY API IS ENABLED
   - Go to: https://console.cloud.google.com/apis/library
   - Search for "Generative AI API"
   - Click "Enable"

4. ✅ CHECK RATE LIMITS
   - https://ai.google.dev/docs/rate-limits

Current Status:
  API Key: {'✓ Configured' if api_key else '✗ Missing'}
  Project: Check Google Cloud Console for details
""")
