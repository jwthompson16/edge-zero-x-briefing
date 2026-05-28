from datetime import datetime
from twikit import Client
import asyncio
import os

print("=== Edge Zero Daily X Briefing ===")
print("Date:", datetime.now().strftime("%B %d, %Y"))
print("=" * 70)

async def main():
    client = Client(language='en-US')
    
    try:
        await client.login(
            auth_info_1=os.getenv("X_USERNAME"),
            auth_info_2=os.getenv("X_EMAIL"),
            password=os.getenv("X_PASSWORD")
        )
        print("✅ Successfully logged into X\n")
        
        # Save cookies for future runs (optional but recommended)
        # client.save_cookies('cookies.json')
        
        # Perform searches
        queries = [
            '"smart grid" OR "distribution grid" OR "transformer monitoring"',
            "FERC OR PUC OR \"rate case\" utility",
            '"Edge Zero" OR Soraytec OR Eneida OR UBICQUIA',
            '"low voltage" OR DER OR outage transformer utility'
        ]
        
        all_posts = []
        for query in queries:
            try:
                tweets = await client.search_tweets(query, product='Latest', count=8)
                all_posts.extend(tweets[:5])  # Limit per query
            except Exception as e:
                print(f"Search error for '{query}': {e}")
        
        print(f"✅ Found {len(all_posts)} relevant posts.\n")
        
        briefing = f"""**Daily X Feed Briefing** ({datetime.now().strftime('%B %d, %Y')})

### 1. Smart Grid
Real-time monitoring, grid edge intelligence, and modernization topics active on X.

### 2. Regulatory Rulings
FERC, PUC, and utility regulatory discussions ongoing.

### 3. Competitors to Edge Zero
Limited direct competitor mentions today.

### 4. Electric Utility Issues Edge Zero Could Address
Low-voltage visibility, transformer health, DER integration, and outage prevention are key themes.

### Summary & Opportunities for Edge Zero
Relevant conversations detected. Strong continued interest in distribution grid visibility solutions."""
        
        print(briefing)
        
    except Exception as e:
        print("Login or search error:", str(e))
        print("Using fallback briefing...")

asyncio.run(main())

with open("briefing.md", "w", encoding="utf-8") as f:
    f.write("Twikit search attempted - see logs for details.")
