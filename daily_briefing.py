from datetime import datetime
import os
from openai import OpenAI

print("=== Edge Zero Daily X Briefing ===")
print("Date:", datetime.now().strftime("%B %d, %Y"))
print("")

# GitHub Models (Free)
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.getenv("GITHUB_TOKEN")
)

prompt = f"""
You are an analyst for Edge Zero. Create a daily briefing.

Current date: {datetime.now().strftime('%B %d, %Y')}

Format exactly like this:

**Daily X Feed Briefing** ({datetime.now().strftime('%B %d, %Y')})

### 1. Smart Grid
No major posts today.

### 2. Regulatory Rulings
No major posts today.

### 3. Competitors to Edge Zero
No major posts today.

### 4. Electric Utility Issues Edge Zero Could Address
No major posts today.

### Summary & Opportunities for Edge Zero
System is working. Real content will appear once X search is added.
"""

try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=600,
        temperature=0.7
    )
    briefing = response.choices[0].message.content
    print(briefing)
except Exception as e:
    print("Error:", str(e))
    briefing = "Briefing generated with placeholder content."

# Always create the file
with open("briefing.md", "w", encoding="utf-8") as f:
    f.write(briefing)

print("\nBriefing process completed.")
