from datetime import datetime
import os
from openai import OpenAI

print("=== Edge Zero Daily X Briefing ===")
print("Date:", datetime.now().strftime("%B %d, %Y"))
print("")

# Use GitHub's free Models
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.getenv("GITHUB_TOKEN")   # GitHub automatically provides this
)

prompt = f"""
You are an analyst for Edge Zero. Create a daily briefing from recent X activity.

Current date: {datetime.now().strftime('%B %d, %Y')}

Format exactly like this:

**Daily X Feed Briefing** ({datetime.now().strftime('%B %d, %Y')})

### 1. Smart Grid
[Key insights]

### 2. Regulatory Rulings
[Key insights]

### 3. Competitors to Edge Zero
[Key insights]

### 4. Utility Issues Edge Zero Can Solve
[Key insights]

### Summary & Opportunities
"""

try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",           # or "llama-3.1-70b" etc.
        messages=[{"role": "user", "content": prompt}],
        max_tokens=800,
        temperature=0.7
    )
    print(response.choices[0].message.content)
except Exception as e:
    print("Error:", str(e))
