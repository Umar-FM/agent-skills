# Skill 03: Comment Pain Miner

```yaml
id: comment_pain_miner
category: market_intelligence
inspired_by:
  - Saim niche research thread comment-gap method
```

## Purpose

Mine YouTube, Reddit, TikTok, and X comments for unmet demand. This converts audience annoyance, confusion, and requests into topics, hooks, and script sections.

## Saim-heavy nuggets embedded

- Start where the audience is annoyed.
- Repeated complaints reveal product-market fit gaps.
- Comments can supply topic angles, missing context, and better hooks.
- Trend plus bad content equals opportunity.

## Inputs

```yaml
sources:
  - platform: youtube | reddit | tiktok | x | other
    url_or_query:
competitor_or_topic: string
min_comments_to_scan: integer
content_type: sleep | faceless_documentary | explainer | other
```

## Workflow

1. Collect comments from outlier videos and adjacent forums.
2. Classify each comment as request, confusion, complaint, praise, skepticism, timestamp drop, or repeat-viewing signal.
3. Cluster repeated phrases and unmet needs.
4. Translate each cluster into a topic angle, title angle, script section, or production fix.
5. Identify language the audience uses naturally and save it in a voice-of-customer bank.
6. Score each gap by frequency, emotional intensity, and ease of solving.
7. Recommend tests that answer the gap more clearly than competitors.

## Output schema

```yaml
comment_clusters:
  - cluster_name:
    frequency:
    representative_paraphrases:
    audience_emotion:
    unmet_need:
    content_opportunity:
    title_angle:
    script_section:
    production_fix:
    priority_1_10:
voice_of_customer_bank:
  - phrase:
    use_case:
recommended_tests:
  - title:
    hook:
    gap_solved:
    differentiation:
```

## Agent prompts

### Comment gap prompt

```text
Analyze these comments as market research. Do not summarize sentiment generally. Extract repeated unmet demand: what viewers wish the creator explained, skipped, slowed down, made longer, made calmer, sourced better, or covered next. Cluster the comments and turn each cluster into a video idea, hook, or script section.
```

## Quality gates

- At least 5 clusters for a deep scan.
- Each cluster must map to a concrete action.
- Use audience language, but do not plagiarize individual comments.
- Mark low-frequency/high-intensity comments separately from high-frequency needs.

## Examples

### Sleep-channel comment gap

Comments say: “voice is too sharp,” “wish this was 3 hours,” “music woke me up,” and “please do Byzantine history.” The miner outputs: soften sibilance, produce longer versions, remove sudden music swells, and add a Byzantine sleep-history video with a calm title.

## Failure modes

- Treating comments as compliments only.
- Overreacting to one loud commenter.
- Ignoring timestamps where viewers report drop-offs or annoyance.
- Using comment language in a way that exposes private or personal details.
