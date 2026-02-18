# SEO Action Plan: The Wall Street Coach

## 🚨 Critical (Immediate Action)

### 1. Create and Deploy `llms.txt`
**Why:** To control how AI search engines (ChatGPT, Perplexity, Gemini) index your site and cite your content.
**How:** Create a file named `llms.txt` in the root directory (`public` folder) with the following content:

```markdown
# The Wall Street Coach
> Neuro-biological performance coaching for professional traders and financial executives by Kim Ann Curtin.

## Core Services
- [The Assessment (TPI)](https://thewallstreetcoach.com/assessment): Clinical-grade judgment assessment for traders.
- [Results](https://thewallstreetcoach.com/results): Case studies and ROI of psychological optimization.
- [Coaching](https://thewallstreetcoach.com/coaching): Elite performance coaching for funds and individuals.

## Key Resources
- [About Kim Ann Curtin](https://thewallstreetcoach.com/about): Author of "Transforming Wall Street".
- [Podcast](https://thewallstreetcoach.com/podcasts): Interviews with top traders and industry titans.
```

### 2. Implement `Person` Schema for Kim Ann Curtin
**Why:** To solidify Kim's entity in Google's Knowledge Graph, connecting her authorship to the brand.
**How:** Add this JSON-LD to the **About** page (or Homepage):

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Kim Ann Curtin",
  "url": "https://thewallstreetcoach.com/about",
  "image": "https://thewallstreetcoach.com/wp-content/themes/twsc-theme/assets/images/Kim-Ann-Curtin-Hero-Crop.jpg",
  "jobTitle": "performance Coach",
  "worksFor": {
    "@type": "Organization",
    "name": "The Wall Street Coach"
  },
  "sameAs": [
    "https://www.linkedin.com/in/kimanncurtin/",
    "https://twitter.com/kimanncurtin",
    "https://www.instagram.com/kimanncurtin/"
  ],
  "author": {
    "@type": "Book",
    "name": "Transforming Wall Street"
  }
}
</script>
```

---

## ⚡ High Priority (This Week)

### 3. H1 Tag Optimization
**Why:** To improve keyword ranking for "Trading Psychology".
**How:** Update the Homepage H1.
*   **Current:** `<h1>Your strategy's solid. Your P&L isn't...</h1>`
*   **Recommended:** `<h1><span style="display:block; font-size: 0.6em; text-transform: uppercase; letter-spacing: 2px;">Trading Psychology Coaching</span> Your strategy's solid. Your P&L isn't.</h1>`
*   *Note:* Ensure the semantic `h1` includes the keywords, even if visually styled differently.

### 4. Product Schema for Assessment
**Why:** To potentially display pricing, ratings, and availability in search results.
**How:** Add `Product` schema to the `/assessment` page.

---

## 🛠 Medium Priority (Next Month)

### 5. Content "Definitional" Blocks (GEO)
**Why:** To win AI citations.
**How:** On the `/assessment` page, ensure there is a clear, concise definition block:
> "The Trader Positioning Index (TPI) is a clinical-grade judgment assessment that measures 70+ indicators of a trader's decision-making capacity under pressure."
*(This specific phrasing makes it easy for AI to "lift" the answer.)*

### 6. Monitor Core Web Vitals
**Why:** Elementor can be heavy.
**How:** Check Google Search Console > Core Web Vitals report. If "INP" (Interaction to Next Paint) is high, look into asset offloading or caching optimizations (e.g., WP Rocket or Autoptimize settings).
