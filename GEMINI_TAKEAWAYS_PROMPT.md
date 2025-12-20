# GEMINI PROMPT FOR GENERATING EPISODE TAKEAWAYS
## The Wall Street Coach Podcast

---

## PROMPT (Copy this into Google Sheets/Gemini):

```
You are an expert content strategist for a trading psychology coaching business. Your task is to extract the most valuable, actionable takeaways from a podcast episode transcript.

**About the Podcast:**
The Wall Street Coach Podcast is hosted by Kim Ann Curtin, a trading psychology coach with 18+ years of experience working with hedge fund managers, prop traders, and retail investors. The show focuses on the mental and emotional aspects of trading—discipline, fear, greed, mindset, and peak performance.

**Your Task:**
Read the transcript below and create a "Key Takeaways" section that:

1. **Opens with a hook** (1-2 sentences) - What makes this episode valuable? Why should someone listen?

2. **Lists 3-5 Key Insights** - The most powerful, actionable ideas from the episode. Each should be:
   - A concrete insight or principle (not vague platitudes)
   - Something a trader can apply immediately
   - Written in a way that makes the reader want to hear more

3. **Closes with who this episode is for** (1 sentence) - What type of trader will benefit most?

**Format your response EXACTLY like this:**

[HOOK]
[2-3 sentences that capture the essence and make someone want to listen]

**Key Insights:**
• [Insight 1 - specific, actionable, compelling]
• [Insight 2 - specific, actionable, compelling]
• [Insight 3 - specific, actionable, compelling]
• [Insight 4 - if applicable]
• [Insight 5 - if applicable]

**Best for:** [1 sentence describing ideal listener]

**Guidelines:**
- Use Kim's actual language and concepts from the transcript when possible
- If there's a guest, highlight their unique expertise
- Focus on INSIGHTS, not episode structure ("In this episode, Kim discusses...")
- Make it valuable standalone content—not just a teaser
- Keep total length between 150-250 words
- Write in a professional but warm tone

**Episode Title:** {TITLE}

**Transcript:**
{TRANSCRIPT}
```

---

## EXAMPLE OUTPUT (What good takeaways look like):

**Episode: Secrets of Market Wizards Revealed with George Coyle**

George Coyle—co-author of the upcoming Market Wizards book with Jack Schwager—reveals the surprising truth about what separates legendary traders from everyone else: it's not their strategies, it's their unwavering self-belief in the face of repeated failure.

**Key Insights:**
• **The only 3 principles that matter:** After studying 100 years of great traders, George found just three consistent elements: respect price action, ride your winners, and cut your losses. Everything else is personal preference.
• **Unshakeable faith is the edge:** Every Market Wizard failed repeatedly before succeeding—but they never quit. They had "unshakeable faith" in themselves when all evidence suggested they should give up.
• **Complexity is almost always bad:** The best traders simplify relentlessly. If your system can't be explained simply, it's probably not robust.
• **Defense wins championships:** Survival is the real key. Once you can survive long enough, you'll eventually hit the right conditions to win big.

**Best for:** Traders looking to understand the psychological DNA of legendary performers—and adopt it themselves.

---

## TIPS FOR GOOGLE SHEETS:

1. Create a new column called "Takeaways"
2. Use the formula: `=GEMINI(A1, B1)` where A1 is the prompt and B1 is the transcript
3. Or use: `=AI.GENERATE("Your prompt here" & C2)` with C2 being the transcript column
4. Process in batches to avoid rate limits

---

## ALTERNATIVE SHORTER PROMPT (if you need less tokens):

```
Extract 3-5 KEY TAKEAWAYS from this trading psychology podcast transcript. Focus on specific, actionable insights that traders can apply immediately. Format as bullet points. Include a 1-sentence hook at the start and who the episode is best for at the end.

Episode: {TITLE}
Transcript: {TRANSCRIPT}
```

