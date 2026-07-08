# Skill 01: YT Outlier Scout

```yaml
id: yt_outlier_scout
category: market_intelligence
inspired_by:
  - Saim niche research thread
  - Saim strategic YouTube mining workflow
```

## Purpose

Find fresh YouTube videos that reveal demand before the market is obvious. The scout identifies low-subscriber/high-view anomalies, records their packaging and format, and ranks them by repeatability, cost, and policy risk.

## Saim-heavy nuggets embedded

- Use outliers as data, not inspiration.
- Look for recent high-view videos on low-subscriber or young channels.
- Study hook, intro, CTA, story, title, thumbnail, pacing, and format.
- Prefer behavior loops over broad niches.

## Inputs

```yaml
niche_seed: string
language: string
target_country: string
content_type: sleep | faceless_documentary | explainer | shorts | other
freshness_window: 7_days | 30_days | 90_days
minimum_views: integer
maximum_subscribers: integer | unknown_allowed
production_budget_per_video: number
risk_tolerance: low | medium | high
```

## Workflow

1. Search YouTube with 10–20 seed phrases related to the viewer behavior, not only the topic.
2. Use recent filters first. Prioritize videos published in the last 7–30 days when possible.
3. Collect videos where views are unusually high relative to subscriber count or channel age.
4. Open each video and record the first 30 seconds: opening line, visual, music, voice, pace, and promise.
5. Extract title formula, thumbnail formula, emotional trigger, video length, and production style.
6. Check whether the format repeats across 3+ videos, either on the same channel or across similar channels.
7. Mine the top comments for unmet demand, confusion, objections, and topic requests.
8. Score opportunity on demand, repeatability, production cost, originality room, and policy risk.
9. Recommend 5–15 original test angles that use the same behavior loop without copying creative assets.

## Output schema

```yaml
outliers:
  - video_title:
    channel_name:
    channel_subscribers:
    views:
    upload_date:
    video_age_days:
    views_to_subscriber_ratio:
    video_length:
    production_style:
    title_formula:
    thumbnail_formula:
    first_30_seconds_summary:
    emotional_trigger:
    behavior_loop:
    repeated_format_evidence:
    comment_gap:
    demand_score_1_10:
    repeatability_score_1_10:
    production_cost_score_1_10:
    originality_room_1_10:
    policy_risk_1_10:
recommended_tests:
  - original_title:
    format_to_test:
    why_it_maps_to_outlier:
    what_must_be_original:
    estimated_cost:
    risk_notes:
```

## Agent prompts

### Outlier scan prompt

```text
You are a YouTube market scout. Find fresh outliers in this niche: {niche_seed}. Prioritize videos from small or medium channels with unusually high views, recent upload dates, and simple repeatable production. For each outlier, extract the behavior loop, emotional trigger, title formula, thumbnail formula, first 30 seconds, and why the algorithm may be rewarding it. Do not recommend copying the video. Recommend original tests that use the same viewer behavior.
```

## Quality gates

- At least 25 outliers for a serious weekly scan.
- At least 5 outliers must be recent, not years-old evergreen giants.
- Every recommended test must name the original value-add.
- Policy risk must be scored before any production recommendation.
- No direct title/script/thumbnail copying.

## Examples

### Sleep outlier interpretation

A 2-hour “rainy medieval castle history” video from a 40K-subscriber channel gets 420K views in 12 days. The scout should not say “copy medieval castles.” It should extract: long sleep session behavior, calm mystery packaging, rain ambience, chaptered history, low-arousal narration, and likely older/US evergreen audience.

## Failure modes

- Chasing old videos with millions of views but no recent evidence.
- Confusing niche demand with one-off viral luck.
- Copying a competitor’s exact topic/title/thumbnail instead of extracting the format.
- Ignoring policy risk because the production is cheap.
