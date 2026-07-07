# 09 — Agent Prompt Templates and Workflows

This module provides reusable prompts for agents using this skill. These prompts help standardize research, diagnosis, drafting, editing, testing, and campaign creation.

Use these prompts as internal workflows or user-facing request templates.

## 1. Universal copy generation prompt

```markdown
You are using the Ultimate Copywriter & Marketer skill.

Task: Write [asset type] for [product/offer].

Inputs:
- Audience:
- Awareness stage:
- Market sophistication:
- Product/category:
- Offer:
- Desired outcome:
- Unique mechanism:
- Proof:
- Objections:
- Competitors/alternatives:
- Tone/voice:
- Channel:
- CTA:
- Constraints/compliance:

Process:
1. State assumptions if inputs are missing.
2. Diagnose audience, awareness, offer strength, proof gaps, and objections.
3. Build the persuasion spine.
4. Draft the copy.
5. Provide 2-5 variants where useful.
6. Explain why the strongest version works.
7. Suggest tests or proof improvements.
```

## 2. Copy brief prompt

```markdown
Build a complete copy brief for this offer.

Product/offer:
[details]

Known audience:
[details]

Known proof:
[details]

Known constraints:
[details]

Return:
- Business objective
- Asset/channel recommendation
- Primary audience
- Buyer/user/approver distinction
- Awareness stage
- Market sophistication
- Core pain
- Desired future
- Trigger events
- Alternatives
- Positioning statement
- Unique mechanism
- Offer components
- Proof inventory
- Proof gaps
- Objection map
- CTA recommendation
- Tone guidance
- Research questions still unanswered
```

## 3. Message map prompt

```markdown
Create a message map from the following research notes.

Research notes:
[paste notes, VOC, call excerpts, reviews, support tickets, sales objections]

Return:
1. Repeated customer phrases worth using.
2. Top pains, ranked by intensity.
3. Desired outcomes.
4. Trigger events.
5. Failed alternatives.
6. Buying criteria.
7. Objections.
8. Emotional stakes.
9. Functional stakes.
10. Proof needed.
11. Headline seeds.
12. FAQ seeds.
13. Messaging pillars.
14. Core message hypothesis.
15. Recommended asset strategy.
```

## 4. Voice-of-customer mining prompt

```markdown
Analyze the following customer language and extract copy-ready insights.

VOC source:
[paste reviews/interviews/tickets/calls]

Tag each useful quote as one or more:
- pain_current_state
- desired_outcome
- trigger_event
- failed_alternative
- objection_price
- objection_time
- objection_trust
- objection_complexity
- objection_fit
- buying_criterion
- proof_needed
- emotional_language
- functional_language
- category_language
- competitor_comparison
- headline_seed
- FAQ_seed

Return a table:
| Theme | Raw quote | Tag | Copy implication | Sample copy |
```

## 5. Positioning prompt

```markdown
Develop positioning for this product.

Product:
[details]

Customers:
[details]

Alternatives:
[details]

Unique capabilities:
[details]

Proof:
[details]

Return:
- Competitive alternatives
- Unique capabilities
- Value enabled by each capability
- Best-fit customers
- Category options with pros/cons
- Recommended positioning statement
- One-line description
- Messaging pillars
- Differentiation copy
- Homepage hero examples
- Sales narrative
```

## 6. Offer improvement prompt

```markdown
Improve this offer before writing copy.

Current offer:
[details]

Audience:
[details]

Price/terms:
[details]

Proof:
[details]

Objections:
[details]

Return:
1. Offer diagnosis.
2. Stronger core promise.
3. Named mechanism options.
4. Deliverables clarification.
5. Timeline recommendation.
6. Bonuses/accelerators that remove friction.
7. Risk reversal options.
8. Ethical urgency/scarcity options.
9. Revised offer stack.
10. CTA recommendation.
11. Sales page hero and offer section draft.
```

## 7. Headline generation prompt

```markdown
Generate headline options for [asset/channel].

Audience:
...
Awareness stage:
...
Offer:
...
Core promise:
...
Mechanism:
...
Proof:
...
Tone:
...

Generate 30 headlines in these categories:
- Direct outcome
- Problem diagnosis
- Mechanism-led
- Proof-led
- Contrarian
- Question
- Invitation
- Warning/risk
- Before/after
- Category reframe

For each, include when to use it.
End by selecting the top 5 and explaining why.
```

## 8. Landing page prompt

```markdown
Write a conversion-focused landing page for this campaign.

Traffic source:
...
Audience:
...
Awareness stage:
...
Ad/email hook:
...
Offer:
...
Proof:
...
Objections:
...
CTA:
...
Voice:
...

Return:
- Strategic diagnosis
- Page outline
- Hero section with 5 headline variants
- Problem section
- Mechanism section
- Benefits/use cases
- Proof section
- Offer section
- FAQ
- CTA sections
- Microcopy
- Test recommendations
```

## 9. Homepage prompt

```markdown
Write or rewrite a homepage for [brand/product].

Inputs:
- Primary audience:
- Secondary audiences:
- Category:
- Positioning:
- Core promise:
- Mechanism:
- Top use cases:
- Proof:
- Objections:
- Desired CTAs:
- Brand voice:

Return:
1. Homepage strategy.
2. Above-the-fold copy with variants.
3. Section-by-section wireframe.
4. Proof placement plan.
5. CTA hierarchy.
6. Persona/segment routing copy if needed.
7. FAQ.
8. Boilerplate.
9. SEO title/meta description.
```

## 10. Sales page prompt

```markdown
Write a long-form sales page for [offer].

Audience:
...
Awareness:
...
Sophistication:
...
Offer stack:
...
Price/terms:
...
Guarantee:
...
Proof:
...
Deadline/urgency:
...
Objections:
...
Voice:
...

Return:
- Lead strategy
- Full page draft with section headers
- Offer stack copy
- Bonus copy if relevant
- Guarantee section
- FAQ
- CTA blocks
- Final close
- Claims requiring proof
- Test ideas
```

## 11. Email sequence prompt

```markdown
Write an email sequence for [campaign goal].

Audience:
...
Relationship to list:
...
Offer:
...
Deadline:
...
Proof:
...
Objections:
...
Voice:
...
Number of emails:
...

Return for each email:
- Goal
- Subject line options
- Preview text
- Body copy
- CTA
- Segmentation notes

Include sequence logic and recommended send timing.
```

## 12. Cold email prompt

```markdown
Write cold email variants for [offer] targeting [specific prospect segment].

Prospect context:
...
Trigger/relevance:
...
Pain hypothesis:
...
Offer/mechanism:
...
Proof:
...
CTA:
...
Tone:
...

Return:
- 5 subject lines
- 5 email variants: trigger-based, pain-based, proof-based, referral-style, soft-breakup
- Personalization fields to research
- Follow-up sequence
- Compliance notes
```

## 13. Ad copy prompt

```markdown
Create paid ad variants for [platform].

Audience:
...
Traffic temperature:
...
Offer:
...
Landing page promise:
...
Proof:
...
Restrictions:
...
Voice:
...

Generate variants by angle:
- Pain
- Outcome
- Mechanism
- Proof
- Contrarian
- Social proof
- Offer
- Retargeting

For each include:
- Primary text
- Headline
- Description
- CTA
- Creative concept
- Landing page match note
```

## 14. VSL/script prompt

```markdown
Write a VSL script for [offer].

Audience:
...
Awareness:
...
Sophistication:
...
Core problem:
...
Old way:
...
New mechanism:
...
Proof:
...
Offer:
...
Guarantee:
...
CTA:
...
Length target:
...

Return:
- Hook options
- Full script with timestamps/sections
- Slide/visual suggestions
- Pattern interrupts
- Proof moments
- Objection handling
- CTA close
```

## 15. Product page prompt

```markdown
Write an ecommerce product page.

Product:
...
Audience/use occasion:
...
Primary benefit:
...
Features/materials/specs:
...
Reviews/proof:
...
Shipping/returns:
...
Variants/sizing:
...
Brand voice:
...

Return:
- Product title/subtitle
- Hero copy
- Benefit bullets
- Feature sections
- Sensory/practical details
- Review highlights
- FAQ
- CTA and microcopy
- Email/ad snippets
```

## 16. Brand voice prompt

```markdown
Create a brand voice guide.

Brand:
...
Audience:
...
Category:
...
Positioning:
...
Values/beliefs:
...
Existing voice examples:
...
Competitors to avoid sounding like:
...

Return:
- Voice summary
- Voice dimensions
- Do/don't table
- Preferred words
- Banned words
- Tone by context
- Sample rewrites
- CTA style
- Boilerplates
- Social/email/page examples
```

## 17. Content strategy prompt

```markdown
Build a content strategy for [brand].

Business objective:
...
Audience:
...
Offer/product:
...
Sales cycle:
...
Current channels:
...
Proof/expertise:
...
Competitors:
...

Return:
- Content mission
- Audience and buying stages
- Content pillars
- Belief shifts
- SEO topic clusters
- Social formats
- Newsletter concept
- Lead magnets
- Sales enablement assets
- 30-day editorial calendar
- Repurposing plan
- Measurement plan
```

## 18. Copy critique prompt

```markdown
Critique and improve this copy.

Copy:
[paste copy]

Context:
- Audience:
- Asset/channel:
- Goal:
- Offer:
- Proof:
- Voice:

Return:
1. Overall diagnosis.
2. Scorecard from 1-5 for relevance, clarity, promise, mechanism, proof, differentiation, offer, objections, CTA, voice, readability, ethics.
3. Top 5 issues.
4. Revised copy.
5. Line-by-line improvements.
6. Proof gaps.
7. Test recommendations.
```

## 19. Proof-gap prompt

```markdown
Audit the proof in this copy.

Copy:
[paste copy]

Known proof assets:
[paste proof]

Return:
- Claim-proof map
- Unsupported claims
- Weak proof
- Proof placement recommendations
- Better testimonial questions
- Case study opportunities
- Demonstration ideas
- Safer wording for unsupported claims
```

## 20. Objection-map prompt

```markdown
Build an objection map for this offer.

Offer:
...
Audience:
...
Price/commitment:
...
Alternatives:
...
Sales objections heard:
...

Return:
| Objection | Root fear | Buyer stage | Copy response | Proof needed | Offer fix |

Also write:
- FAQ section
- Objection-handling email
- Sales-call talk track
```

## 21. Funnel prompt

```markdown
Design a full funnel for [offer].

Audience:
...
Traffic sources:
...
Awareness stages:
...
Offer ladder:
...
Proof:
...
Budget/team constraints:
...

Return:
- Funnel strategy
- Entry points by awareness stage
- Lead magnets
- Landing pages
- Email sequences
- Retargeting ads
- Sales enablement assets
- Measurement plan
- 90-day test roadmap
```

## 22. A/B test prompt

```markdown
Create a testing plan for this asset.

Asset:
...
Current performance:
...
Traffic source:
...
Audience:
...
Known issues:
...

Return:
- Diagnosis
- Highest-impact test opportunities
- 5 hypotheses
- Variants to test
- Primary and secondary metrics
- Sample size/time cautions
- Test log template
- Next tests based on possible outcomes
```

## 23. Compliance-safe rewrite prompt

```markdown
Rewrite this copy to be more compliant and ethically persuasive.

Copy:
[paste copy]

Category:
[health/finance/legal/security/environment/income/etc.]

Known substantiation:
...
Required disclaimers:
...

Return:
- Risky claims identified
- Safer rewrites
- Required proof/disclaimer suggestions
- Revised copy
- Notes on claims that should be reviewed by legal/compliance
```

## 24. Sales deck prompt

```markdown
Create a B2B sales deck narrative and slide copy.

Audience/company type:
...
Problem:
...
Market change:
...
Solution:
...
Proof:
...
Implementation:
...
Business case:
...
Next step:
...

Return:
- Narrative arc
- Slide-by-slide titles
- Slide copy
- Speaker notes
- Proof/data placement
- Objection slides
- Champion forwarding note
```

## 25. Case study prompt

```markdown
Write a case study from these notes.

Customer:
...
Situation before:
...
Problem/stakes:
...
Alternatives tried:
...
Implementation:
...
Results:
...
Quote:
...
Product/service used:
...

Return:
- Title options
- Executive summary
- Full case study
- Pull quotes
- Metric callouts
- Social post version
- Sales email version
- Landing page proof block
```

## 26. Comparison page prompt

```markdown
Write a fair comparison page.

Our product:
...
Alternative/competitor/category:
...
Audience:
...
Use cases where we are better:
...
Use cases where alternative may be better:
...
Proof:
...
Tone:
...

Return:
- Fair framing
- Comparison table
- Use-case guidance
- Migration/switching copy
- FAQ
- CTA
- Compliance note to verify competitor claims
```

## 27. Category creation prompt

```markdown
Develop category/design narrative for an emerging product.

Product:
...
Old category:
...
Why old category fails:
...
Market change:
...
New problem:
...
New way:
...
Unique capabilities:
...
Proof:
...

Return:
- Category name options
- Strategic narrative
- Old way vs new way table
- Homepage hero
- Sales deck opening
- Thought leadership angles
- Analyst/investor explanation
- Risks of this category framing
```

## 28. Rewrite in multiple tones prompt

```markdown
Rewrite this copy in multiple tones while preserving the strategy.

Copy:
[paste]

Strategy that must remain:
- Audience:
- Promise:
- Mechanism:
- Proof:
- CTA:

Tone variants:
- Clear/direct
- Premium/restraint
- Warm/human
- Challenger/contrarian
- Technical/expert
- Playful/light

Return each version and explain when to use it.
```

## 29. Campaign concept prompt

```markdown
Create campaign concepts for [offer/product].

Audience:
...
Core buyer truth:
...
Problem:
...
Promise:
...
Mechanism:
...
Proof:
...
Brand voice:
...
Channels:
...

Return 5 campaign platforms. For each:
- Big idea
- Core line
- Why it works
- Homepage/landing hero
- 3 ad examples
- Email subject/body opening
- Social post idea
- Visual concept
- CTA
```

## 30. Final packaging prompt

```markdown
Package the final copy deliverable for a user.

Include:
- Assumptions
- Strategy summary
- Final copy
- Variants
- Implementation notes
- Proof gaps
- Testing recommendations
- Compliance cautions

Make it clear, organized, and immediately usable.
```

## Agent workflow macros

### Macro: Diagnose before drafting

```markdown
Before drafting, diagnose:
Audience:
Awareness:
Sophistication:
Problem:
Desired outcome:
Mechanism:
Proof:
Offer:
Objections:
CTA:
Missing info:
```

### Macro: Turn feature into benefit

```markdown
For each feature, produce:
Feature:
Functional benefit:
Business/emotional benefit:
Proof/mechanism:
Copy line:
```

### Macro: Generate angles

```markdown
Generate 20 angles across:
Pain, cost, speed, ease, risk, status, control, identity, contrarian, mechanism, proof, comparison, timing, enemy.
For each, include a headline and first paragraph.
```

### Macro: Improve specificity

```markdown
Rewrite this copy by replacing vague claims with:
- Exact audience
- Exact workflow
- Exact outcome
- Exact mechanism
- Exact proof
- Exact timeframe
- Exact CTA
```

### Macro: Add proof

```markdown
For each claim in this copy:
1. Identify the claim.
2. Identify the skepticism it creates.
3. Add the strongest available proof.
4. If proof is missing, rewrite the claim more safely.
```

### Macro: Build email sequence from page

```markdown
Turn this landing/sales page into an email sequence:
- Email 1: announcement
- Email 2: problem/stakes
- Email 3: mechanism
- Email 4: proof/story
- Email 5: objection
- Email 6: offer stack
- Email 7: urgency/final CTA
```

## Final prompting rule

The best prompt does not ask the agent to “make it persuasive.” It gives the agent enough context to diagnose the buyer, strengthen the offer, choose the right argument, and write copy that can be believed.
