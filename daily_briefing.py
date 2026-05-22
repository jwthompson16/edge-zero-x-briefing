from datetime import datetime
import os
from anthropic import Anthropic

print("=== Edge Zero Daily X Briefing ===")
print("Date:", datetime.now().strftime("%B %d, %Y"))
print("")

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

if not ANTHROPIC_API_KEY:
    print("❌ Error: ANTHROPIC_API_KEY not found!")
else:
    print("✅ Anthropic API Key found!")
    
    try:
        client = Anthropic(api_key=ANTHROPIC_API_KEY)
        
        prompt = """
        Create a professional daily briefing for Edge Zero (low-voltage transformer monitoring for utilities).
        Current date: """ + datetime.now().strftime("%B %d, %Y") + """

        Format exactly like this:

        **Daily X Feed Briefing** (""" + datetime.now().strftime("%B %d, %Y") + """)

        ### 1. Smart Grid
        [Summary]

        ### 2. Regulatory Rulings on Electric Utilities in the U.S.
        [Summary]

        ### 3. Competitors to Edge Zero
        [Summary]

        ### 4. Electric Utility Issues Edge Zero Could Address
        [Summary]

        ### Summary & Opportunities
        Key takeaways for Edge Zero.
        """

        message = client.messages.create(
            model="claude-3-5-sonnet-20240620",   # or claude-3-opus-20240229 if you have access
            max_tokens=800,
            temperature=0.7,
            messages=[{"role": "user", "content": prompt}]
        )
        
        print(message.content[0].text)
        
    except Exception as e:
        print("❌ Claude Error:", str(e))

print("\nTest complete.")
