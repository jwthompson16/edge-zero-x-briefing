from datetime import datetime
import os
import json
import requests
from openai import OpenAI

# Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TO_EMAIL = os.getenv("TO_EMAIL")

TOPICS = {
    "smart_grid": '"smart grid" OR "distribution grid" OR "grid edge" OR transformer monitoring',
    "regulatory": "FERC OR PUC OR \"utility commission\" OR \"rate case\" OR merger utility",
    "competitors": '"Edge Zero" OR Soraytec OR Eneida OR UBICQUIA OR "low voltage monitoring"',
    "issues": '"low voltage" OR transformer OR outage OR DER OR "distribution grid" utility'
}

def get_sample_posts():
    """For now, we'll simulate posts. Later we can add real search."""
    # This is a placeholder - real search is more complex in GitHub Actions
    return {
        "smart_grid": [{"text": "Sample post about smart grid advancements..."}],
        "regulatory": [{"text": "Sample FERC ruling today..."}],
        "competitors": [{"text": "Competitor news..."}],
        "issues": [{"text": "Utility issue that Edge Zero can solve..."}]
    }

def generate_briefing(posts):
    client = OpenAI(api_key=OPENAI_API_KEY)
    
    prompt = f"""
    Create a professional daily briefing for Edge Zero (LV transformer monitoring company).

    Current date: {datetime.now().strftime('%B %d, %Y')}

    Posts found: {json.dumps(posts, indent=2)}

    Format exactly like this:

    **Daily X Feed Briefing for Edge Zero** ({datetime.now().strftime('%B %d, %Y')})

    ### 1. Smart Grid
    [Summary + relevance]

    ### 2. Regulatory Rulings on Electric Utilities
    [Summary]

    ### 3. Competitors to Edge Zero
    [Summary]

    ### 4. Electric Utility Issues Edge Zero Could Address
    [Summary]

    ### Summary & Opportunities
    Key takeaways and why this matters for Edge Zero.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    
    return response.choices[0].message.content

def main():
    print("=== Starting Daily Briefing ===")
    
    posts = get_sample_posts()
    briefing = generate_briefing(posts)
    
    print(briefing)
    
    # Save to file so workflow can use it
    with open("briefing.md", "w", encoding="utf-8") as f:
        f.write(briefing)

if __name__ == "__main__":
    main()
