from datetime import datetime
import os
from openai import OpenAI

print("=== Edge Zero Daily X Briefing ===")
print("Date:", datetime.now().strftime("%B %d, %Y"))
print("")

LLM_API_KEY = os.getenv("LLM_API_KEY")

if not LLM_API_KEY:
    print("❌ Error: LLM_API_KEY secret not found!")
    print("Please check your GitHub Secrets.")
else:
    print("✅ API Key found!")
    
    try:
        client = OpenAI(api_key=LLM_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Create a short test briefing for Edge Zero."}],
            max_tokens=100
        )
        print(response.choices[0].message.content)
    except Exception as e:
        print("❌ OpenAI Error:", str(e))

print("\nTest complete.")
