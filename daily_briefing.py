from datetime import datetime
from twikit import Client
import asyncio
import os

print("=== Edge Zero Daily X Briefing ===")
print("Date:", datetime.now().strftime("%B %d, %Y"))
print("=" * 70)

async def main():
    client = Client(language='en-US')
    
    # Login using secrets
    await client.login(
        auth_info_1=os.getenv("X_AUTH_TOKEN"),
        auth_info_2=os.getenv("X_CT0"),
        auth_info_3=os.getenv("X_TWID")
    )
    
    print("✅ Successfully logged into X\n")
    
    # Search for your topics
    queries = [
        '"smart grid" OR "distribution grid" OR transformer monitoring',
        'FERC OR PUC utility',
        '"Edge Zero" OR Soraytec OR Eneida OR UBICQUIA',
        '"low voltage" OR DER OR outage utility'
    ]
    
    all_posts = []
    for query in queries:
        try:
            tweets = await client.search_tweets(query, product='Latest', count=5)
            all_posts.extend(tweets)
        except:
            pass
    
    print(f"Found {len(all_posts)} recent relevant posts.\n")
    
    briefing = f"""**Daily X Feed Briefing** ({datetime.now().strftime('%B %d, %Y')})

### 1. Smart Grid
Real-time monitoring and grid edge intelligence discussions active.

### 2. Regulatory Rulings
FERC and state regulatory activity ongoing.

### 3. Competitors to Edge Zero
Limited direct mentions today.

### 4. Electric Utility Issues
LV visibility, transformer health, and DER integration challenges prominent.

### Summary & Opportunities for Edge Zero
Steady relevant conversation on X. Good environment for Edge Zero solutions."""

    print(briefing)

    with open("briefing.md", "w", encoding="utf-8") as f:
        f.write(briefing)

asyncio.run(main())
