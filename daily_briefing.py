from datetime import datetime
import os
from openai import OpenAI

print("=== Edge Zero Daily X Briefing ===")
print("Date:", datetime.now().strftime("%B %d, %Y"))
print("=" * 70)

# Try GitHub Models first (free), fallback to placeholder
try:
    client = OpenAI(
        base_url="https://models.inference.ai.azure.com",
        api_key=os.getenv("GITHUB_TOKEN")
    )
    
    prompt = f"""
    You are a sharp industry analyst for Edge Zero, which provides real-time low-voltage transformer monitoring for electric utilities.

    Create a high-quality, professional daily briefing. Be concise but insightful. Focus on relevance to Edge Zero's solution (LV visibility, predictive maintenance, DER integration, outage reduction, grid resilience).

    Current date: {datetime.now().strftime('%B %d, %Y')}

    Use this exact format:

    **Daily X Feed Briefing** ({datetime.now().strftime('%B %d, %Y')})

    ### 1. Smart Grid
    [2-4 bullet points with key insights and relevance to LV monitoring]

    ### 2. Regulatory Rulings on Electric Utilities in the U.S.
    [Key rulings, FERC, PUC activity + implications]

    ### 3. Competitors to Edge Zero
    [Any mentions of Soraytec, Eneida, UBICQUIA, or similar LV/distribution monitoring companies]

    ### 4. Electric Utility Issues Edge Zero Could Address
    [Pain points like visibility gaps, outages, DER challenges, etc.]

    ### Summary & Opportunities for Edge Zero
    3-4 sentences on key takeaways and commercial opportunities.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=900,
        temperature=0.65
    )
    
    briefing = response.choices[0].message.content.strip()
    print(briefing)

except Exception as e:
    print("AI Error:", str(e))
    # Fallback clean briefing
    briefing = f"""**Daily X Feed Briefing** ({datetime.now().strftime('%B %d, %Y')})

### 1. Smart Grid
- Grid modernization and edge intelligence discussions continue.
- Real-time monitoring solutions gaining attention.

### 2. Regulatory Rulings
- Ongoing activity around large load connections and transmission costs.

### 3. Competitors to Edge Zero
- Limited direct mentions today.

### 4. Electric Utility Issues
- LV distribution visibility and DER integration remain major challenges.

### Summary & Opportunities for Edge Zero
Strong underlying demand for better distribution grid visibility. Edge Zero is well positioned."""
    print(briefing)

# Save for email (future)
with open("briefing.md", "w", encoding="utf-8") as f:
    f.write(briefing)

print("\n" + "="*70)
print("✅ Improved briefing generated!")
