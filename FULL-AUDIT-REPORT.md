# SEO Audit Report: The Wall Street Coach
**Date:** February 18, 2026
**Domain:** https://thewallstreetcoach.com
**Business Type:** Expert Consulting / Digital Service

## Executive Summary
The Wall Street Coach has a strong brand foundation with excellent authority signals (E-E-A-T) and a modern technical stack (WordPress + Elementor + Yoast SEO). The primary opportunities lie in **structured data expansion** (specifically for the personal brand "Kim Ann Curtin"), **AI Search Optimization (GEO)**, and **keyword-focused heading structures**.

**Overall SEO Health Score:** **82/100**

### Top 3 Critical Issues
1.  **Missing Person Schema**: Despite the brand revolving around Kim Ann Curtin, the `Person` schema is not prominently defined on the homepage, limiting Knowledge Graph connection.
2.  **No `llms.txt`**: The site lacks an `llms.txt` file, missing a key opportunity to control how AI search engines (ChatGPT, Perplexity, Gemini) consume your high-value content.
3.  **H1 Optimization**: The homepage H1 is a compelling marketing hook ("Your strategy's solid...") but lacks core keywords like "Trading Psychology Coach" or "Performance Coaching", weakening topical relevance for search engines.

### Top 3 Quick Wins
1.  **Implement `Person` Schema**: Add detailed `Person` schema for Kim Ann Curtin to the homepage or About page.
2.  **Create `llms.txt`**: Add a simple text file to guide AI crawlers to your best content (Assessment, Results, Coaching).
3.  **Optimize Homepage H1**: Adjust H1 to include primary keywords while keeping the hook (e.g., "Trading Psychology Coaching: Fix Your P&L in Minutes, Not Years").

---

## 1. Technical SEO (22/25)
**Status:** ✅ Strong

*   **Crawlability**: `robots.txt` is valid and maps to `sitemap_index.xml`. No blocking of AI crawlers detected.
*   **Sitemap**: `sitemap_index.xml` is present, up-to-date (last modified 2026-02-17), and correctly categorized (post, page, category).
*   **Security**: HTTPS is enforced.
*   **Mobile**: Responsive design is implemented via Elementor; touch targets appear sufficient.
*   **Performance**: Lazy loading (`loading="lazy"`, `data-src`) is implemented for images, including logos and hero images, using EWWW Image Optimizer and Autoptimize.

**Recommendations:**
*   Monitor Core Web Vitals (LCP/INP) via Google Search Console, as Elementor can sometimes introduce heavy DOM elements.

## 2. Content Quality & E-E-A-T (23/25)
**Status:** ✅ Excellent

*   **Experience**: deeply personal narratives ("I spent over a decade in the trenches...") demonstrate clear first-hand experience.
*   **Expertise**: "18+ years coaching", "Wall Street 50", and specific methodology (TPI) clearly establish expertise.
*   **Authoritativeness**: High-profile testimonials (e.g., Thuan Q. Pham, former CTO of Uber) and media logos (Blackstone, Morgan Stanley) provide massive social proof.
*   **Trustworthiness**: Clear contact info, Privacy Policy, and Terms of Use are present.

**Recommendations:**
*   Ensure every blog post and the "About" page clearly links back to Kim's specific credentials/bio page to reinforce the Knowledge Graph entity.

## 3. On-Page SEO (18/20)
**Status:** ⚠️ Good, with specific tweaks needed

*   **Title Tags**: "High Quality Coaching for Traders by Kim Ann Curtin | The Wallstreet Coach" - Good, includes keywords.
*   **Meta Descriptions**: Well-written, compelling, and click-worthy.
*   **Headings**:
    *   *Issue*: The Homepage H1 is long and purely persuasive: "Your strategy's solid. Your P&L isn't. What if the fix took minutes, not years?"
    *   *Fix*: Search engines value direct keyword labeling. Consider a structure like: `<span class="sub">Trading Psychology Coaching</span> Your strategy's solid...`
*   **URL Structure**: Clean and descriptive (`/assessment`, `/results`).

## 4. Schema & Structured Data (5/10)
**Status:** ⚠️ Needs Improvement

*   **Detected**: `Organization`, `WebSite`, `WebPage`, `BreadcrumbList` (via Yoast).
*   **Missing**:
    *   **Person**: Critical for Kim Ann Curtin. This connects "The Wall Street Coach" entity to "Kim Ann Curtin" the person in Google's Knowledge Graph.
    *   **Service/Product**: The "Trader Positioning Index" and "Elite Performance Coaching" should be wrapped in `Product` (with `AggregateRating` if possible) or `Service` schema.
    *   **FAQ**: The FAQ section on the homepage is visible text but doesn't appear to be marked up with `FAQPage` schema (though note: Google restricted FAQ snippets in late 2023, it's still valid for structure).

**Recommendations:**
*   Add **Person Schema** to the homepage or About page.
*   Add **Product Schema** to the `/assessment` page.

## 5. Images (5/5)
**Status:** ✅ Excellent

*   **Optimization**: Lazy loading is active.
*   **Alt Text**: Present on key images (e.g., "Kim Ann Curtin", "The Wall Street Coach", client logos).
*   **Formats**: usage of modern formats/CDNs seems likely via the optimization plugins.

## 6. AI Search Readiness / GEO (9/15)
**Status:** ⚠️ Emerging Opportunity

*   **Crawler Access**: Good. AI bots are not blocked.
*   **llms.txt**: ❌ Missing. Creating this file at the root allows you to explicitly tell AI answering engines what your site is about and which pages are most important.
*   **Citability**: The content is punchy and persuasive, which is great for humans. For AI, including clear, definitional blocks (e.g., "The Trader Positioning Index is a clinical-grade judgment assessment...") helps win "featured snippet" style answers in AI chats.

**Recommendations:**
*   Create an `llms.txt` file immediately.
*   Add a "Definition" block for TPI on the Assessment page to secure direct answers in Perplexity/Gemini.

---

## Conclusion
The site is in very good shape. It avoids common technical pitfalls and excels in brand authority. The next level of growth comes from **technical E-E-A-T (Schema)** and **Generative Engine Optimization (llms.txt)** to ensure Kim is cited as *the* authority when traders ask AI for help.
