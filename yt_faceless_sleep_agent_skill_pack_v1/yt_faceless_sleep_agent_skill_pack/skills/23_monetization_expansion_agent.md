# Skill 23: Monetization Expansion Agent

```yaml
id: monetization_expansion_agent
category: business
inspired_by:
  - WizofYT public snippets on monetizing faceless audiences beyond simple PDFs
  - Wanner automation-level framing
```

## Purpose

Plan monetization beyond basic AdSense while respecting audience fit and channel trust.

## Saim-heavy nuggets embedded

- Faceless audiences can be monetized beyond one product type.
- Channel type determines monetization path: sleep differs from educational, branded, or automation channels.
- Do not damage retention/trust with mismatched offers.

## Inputs

```yaml
channel:
  niche:
  audience:
  monthly_views:
  monetization_status:
  top_videos:
  audience_comments:
  email_or_community_assets:
  brand_safety_level:
risk_tolerance: low | medium | high
```

## Workflow

1. Classify the channel audience: passive sleep, active learner, buyer intent, hobbyist, status/luxury, professional, fan community.
2. Identify monetization paths: AdSense, sponsorships, affiliate, newsletter, community, membership, digital product, licensing, lead generation, merch, app/tool.
3. Score each path on audience fit, trust risk, operational complexity, and revenue potential.
4. For sleep channels, prioritize low-friction monetization: AdSense, ambient/sleep playlists, sponsorships aligned with relaxation, optional memberships.
5. For educational faceless channels, consider newsletters, guides, tools, affiliates, and communities.
6. Design CTA placement that does not hurt viewer state.
7. Create a 90-day monetization test plan.

## Output schema

```yaml
monetization_plan:
  audience_type:
  current_revenue_streams:
  candidate_streams:
    - stream:
      audience_fit_1_10:
      trust_risk_1_10:
      complexity_1_10:
      potential_1_10:
      cta_placement:
      test_plan:
  recommended_sequence:
    - phase:
      stream:
      reason:
  avoid:
    - stream:
      reason:
```

## Agent prompts

### Monetization planner prompt

```text
Create a monetization expansion plan for this faceless channel. Classify the audience, score possible revenue streams, and recommend a sequence that protects trust and retention. For sleep channels, avoid intrusive CTAs and mismatched aggressive offers.
```

## Quality gates

- Offer must match audience state.
- Sleep channels should not interrupt relaxation with hard sells.
- Monetization claims must be conservative and tested.
- Sponsorships must fit brand safety and audience trust.

## Examples

### Sleep monetization fit

Good fit: calm sponsor reads, sleep/relaxation apps if compliant, ambient playlist membership, long compilations, AdSense. Weak fit: aggressive trading affiliate, loud mid-roll script, unrelated hustle product.

## Failure modes

- Assuming all faceless channels can sell the same product.
- Adding CTAs that harm retention.
- Promoting risky financial/health claims without compliance.
- Ignoring brand-safety concerns.
