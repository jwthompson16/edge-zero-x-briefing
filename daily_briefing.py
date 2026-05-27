from datetime import datetime
import os
from openai import OpenAI

print("=== Edge Zero Daily X Briefing ===")
print("Date:", datetime.now().strftime("%B %d, %Y"))
print("")

briefing = "Error generating briefing. Please check the logs."

try:
    # Using GitHub's Free Models
    client = OpenAI(
        base_url="https://models.inference.ai.azure.com",
        api_key=os.getenv("GITHUB_TOKEN")
    )

    prompt = f"""
    You are an analyst for Edge Zero (low-voltage transformer monitoring solutions).

    Create a professional daily briefing.

    Current date: {datetime.now().strftime('%B %d, %Y')}

    Format exactly like this:

    **Daily X Feed Briefing** ({datetime.now().strftime('%B %d, %Y')})

    ### 1. Smart Grid
    [Summary]

    ### 2. Regulatory Rulings on Electric Utilities in the U.S.
    [Summary]

    ### 3. Competitors to Edge Zero
    [Summary]

    ### 4. Electric Utility Issues Edge Zero Could Address
    [Summary]

    ### Summary & Opportunities for Edge Zero
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=800,
        temperature=0.7
    )
    
    briefing = response.choices[0].message.content
    print(briefing)

except Exception as e:
    print("Error:", str(e))
    briefing = f"Briefing generation failed today.\nError: {str(e)}"

# Always create the file for email
with open("briefing.md", "w", encoding="utf-8") as f:
    f.write(briefing)

print("\nBriefing process completed.")
