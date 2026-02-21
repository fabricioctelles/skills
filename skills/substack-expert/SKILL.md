---
name: substack-expert
description: Substack platform expert. Guides post formatting, SEO optimization (titles, slugs, meta descriptions), native engagement strategies (Notes, Chat), and conversion to paid subscriptions.
metadata:
  author: ft.ia.br
  version: "1.0"
  date: 2026-02-20
  repository: https://github.com/fabricioctelles/skills
  license: Apache 2.0
---

# Substack Expert

**Overview**
This skill guides AI agents in creating, formatting, and optimizing Substack publications. The focus is on maximizing newsletter reach using embedded SEO techniques, visual formatting tactics to work around the minimalist editor's restrictions, and strategies for converting free readers to paid subscribers.

## Step-by-Step Instructions

### 1. Visual Formatting and Editor Usage
* **Text Centering:** Since Substack doesn't offer a native button to center regular text, use the quote tool to create visual breaks. Select the text, click "insert quote" and then choose "pull quote". The text will be formatted centrally to highlight phrases or statistics.
* **Hierarchy:** Structure content using `Heading 1`, `Heading 2`, and `Heading 3` to improve readability and facilitate search engine crawling.
* **Interactive Engagement:** Take advantage of native custom buttons (e.g., *Subscribe*, *Share*, *Leave a comment*) and include user-exclusive polls, which work as an excellent passive email collector.

### 2. Search Engine Optimization (SEO) and Metadata
While posts are sent via email, they are indexable digital assets on Google. Follow these rules:
* **Headlines:** Keep between 40 and 60 characters (increases CTR by up to 33.3%). Avoid vague titles. Use clear modifiers, keywords, and signal authority (e.g., "Tested", "Expert Guide"). 
* **URL Slug:** Substack generates automatic slugs often filled with useless numbers and characters. Manually modify it to contain only 3 to 5 main keywords and eliminate dates to keep the post "evergreen" (e.g., `/substack-seo-strategy`).
* **Meta Description:** Create an attractive description between 155-160 characters, using the keyword and a call to action (CTA) for the reader.
* **Image Alt Text:** Image descriptions should focus primarily on accessibility and include the article's keywords organically.

### 3. Growth Strategies and Organic Discovery
* **Substack Notes:** *Notes* is the platform's number one discovery engine. Publish small snippets, make connections, and leave authentic comments on other publications. Readers subscribe when they see a name frequently with authority.
* **Rotating Recommendations:** Don't treat other newsletter recommendations passively. Monthly, check the Analytics section to see which creators sent the most traffic and create direct collaborations, rotating recommended partners every 30-60 days.

### 4. Monetization (Free -> Paid Conversion)
* **"Tease & Convert" Strategy:** Don't use the paywall by simply cutting the text in half. Offer the valuable article for free, but lock a utility bonus behind the paywall for paying subscribers (e.g., spreadsheets, templates, AI prompts, audio recordings). This proves value before asking for money.
* **VIP Reader Outreach:** Go to the Dashboard, filter user engagement for those with "4 and 5 stars" of activity, and send direct emails to these "superfans" with a special offer or invitation to the paid plan.

## Input and Output Examples

**Input Scenario:**
"Create SEO definitions for an article about how digital nomads can choose the best smartwatches."

**Optimized Output:**
* **Title (SEO/Subject Line):** *The 5 Best Smartwatches for Digital Nomads in 2025* (Utility trigger, audience specification, and timeliness).
* **Meta Description:** Discover the essential smartwatch features for trails and global travel. Read the complete guide for Digital Nomads and choose your gear.
* **Custom URL Slug:** `/smartwatches-digital-nomads` (No wasted numbers, 3 to 5 words).

## Edge Cases and Observations
* **Email Subjects and Spam Filter:** When configuring Subject Lines, ensure they don't exceed 50 characters to avoid being cut off on mobile. Avoid ALL CAPS and excessive exclamation points or triggers like "Buy Now", which reduce delivery rates.
* **Homepage Design:** For advanced organization, suggest grouping posts into **Tags** (like newspaper sections) and add these categories directly to the navigation bar through the *Website Themes* panel, using advanced layouts (Magazine or Highlight).
* **Welcome Emails (Automation):** Never leave the default welcome email. Urge the agent to customize it to introduce the author, set publishing expectations, and compile links to the best articles.

Aqui está a seção em inglês, focada exclusivamente nas melhores práticas de formatação e baseada nas limitações e recursos nativos do editor do Substack, pronta para ser adicionada ao seu arquivo `SKILL.md`:


### Post Formatting Tips and Best Practices

* **Centering Text Hack:** Substack's minimalist editor lacks a standard center-align button for regular body text. To center text, select it, click "insert quote," and choose "pull quote". This creates a visual break and is perfect for highlighting key phrases or statistics.
* **Structuring and Readability:** Keep your paragraphs short and easy to read. Use headings (Heading 1 through Heading 6) to create a clear hierarchy and guide the reader through your content. 
* **Styling Tools:** Utilize bold, italics, strikethrough, and hyperlinks to guide the reader's eye and improve text scannability. Use bullet points, numbered lists, and dividers to break up long sections.
* **Using Quotes:** Differentiate text using quote styles. Use "block quotes" to clearly indicate long excerpts from external sources, and "pull quotes" for emphasis.
* **Visuals and Media:** Break up heavy text by inserting images, GIFs, or charts. When adding images, you can choose between single images or galleries, and adjust the image width to "wide" or "full". Always include captions and **alt text**, which helps visually impaired readers and boosts your SEO.
* **Interactive Buttons:** Make use of Substack's built-in engagement tools. Insert buttons like "Subscribe", "Share your post", "Leave a comment", or create Custom buttons with specific URLs to drive actions from your readers.
```
