from datetime import datetime
import os
from openai import OpenAI

print("=== Edge Zero Daily X Briefing ===")
print("Date:", datetime.now().strftime("%B %d, %Y"))
print("")

try:
    client = OpenAI(
        base_url="https://models.inference.ai.azure.com",
        api_key=os.getenv("GITHUB_TOKEN")
    )

    prompt = f"""
    Create a short daily briefing for Edge Zero about smart grid, utilities, and related topics.
    Current date: {datetime.now().strftime('%B %d, %Y')}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=600
    )
    print(response.choices[0].message.content)

except Exception as e:
    print("Error using GitHub Models:", str(e))
    print("\nGitHub Actions is working, but AI call had an issue.")
