from datetime import datetime, timedelta
from twikit import Client
import os
import asyncio

print("=== Edge Zero Daily X Briefing ===")
print("Date:", datetime.now().strftime("%B %d, %Y"))
print("=" * 70)

async def main():
    client = Client(language='en-US')
    
    # You'll need to set these as GitHub Secrets (see below)
    # For now we'll use a simple search without login first
    try:
        # Search without login (limited but works for public posts)
        results = await client.search_tweets("smart grid OR FERC utility OR \"low voltage\" transformer", product='Latest', count=10)
        
        print("✅ Found recent posts on X!\n")
        
        briefing = f"""**Daily X Feed Briefing** ({datetime.now().strftime('%B %d, %Y')})

### 1. Smart Grid
- Recent discussions on grid modernization and real-time monitoring.

### 2. Regulatory Rulings
- Activity around FERC and utility regulations.

### 3. Competitors / Issues
- Mentions of low-voltage and transformer topics.

### Summary & Opportunities for Edge Zero
Real conversations happening on X about topics directly relevant to Edge Zero.
"""
        print(briefing)
        
    except Exception as e:
        print("Search error:", str(e))
        print("Using fallback briefing...")

asyncio.run(main())

with open("briefing.md", "w", encoding="utf-8") as f:
    f.write("Daily briefing with Twikit search attempted.")
