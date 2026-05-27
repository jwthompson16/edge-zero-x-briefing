from datetime import datetime
import os
from openai import OpenAI

print("=== Edge Zero Daily X Briefing ===")
print("Date:", datetime.now().strftime("%B %d, %Y"))
print("")

# Using GitHub's Free AI Models (no extra cost)
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.getenv("GITHUB_TOKEN")   # Automatically available in GitHub Actions
)

prompt = f"""
You are an analyst for Edge Zero, a company specializing in low-voltage transformer monitoring for electric utilities.

Create a professional daily briefing based on recent activity on X.

Current date: {datetime.now().strftime('%B %d, %Y')}

Format exactly like this:

**Daily X Feed Briefing** ({datetime.now().strftime('%B %d, %Y')})

### 1. Smart Grid
[Key relevant posts and why they matter]

### 2. Regulatory Rulings on Electric Utilities in the U.S.
[Key relevant posts and implications]

### 3. Competitors to Edge Zero
[Any mentions of competitors or similar solutions]

### 4. Electric Utility Issues Edge Zero Could Address
[Relevant challenges/opportunities]

### Summary & Opportunities for Edge Zero
Key takeaways and potential opportunities.
"""

try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",        # Free tier model
        messages=[{"role": "user", "content": prompt}],
        max_tokens=900,
        temperature=0.7
    )
    briefing = response.choices[0].message.content
    print(briefing)
    
    # Save for email
    with open("briefing.md", "w", encoding="utf-8") as f:
        f.write(briefing)

except Exception as e:
    print("Error generating briefing:", str(e))
    with open("briefing.md", "w", encoding="utf-8") as f:
        f.write("Error generating briefing today.")
