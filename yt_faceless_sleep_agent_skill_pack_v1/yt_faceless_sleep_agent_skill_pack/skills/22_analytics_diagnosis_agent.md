# Skill 22: Analytics Diagnosis Agent

```yaml
id: analytics_diagnosis_agent
category: growth_analytics
inspired_by:
  - Saim underperformance snippet
  - Saim outlier/packaging methodology
```

## Purpose

Diagnose video performance and convert metrics into the next test. This skill separates packaging problems from topic, hook, retention, and production problems.

## Saim-heavy nuggets embedded

- When a video underperforms, the symptom points to the layer that needs fixing.
- Outliers should update the format map.
- Comments and retention graphs reveal what to test next.
- Do not change everything at once.

## Inputs

```yaml
video_metrics:
  impressions:
  ctr:
  average_view_duration:
  average_percentage_viewed:
  retention_graph_notes:
  first_30_sec_retention:
  first_5_min_retention:
  traffic_sources:
  subscribers_gained:
  comments:
  rpm_if_available:
video_package:
  title:
  thumbnail:
  hook:
  length:
  topic:
  script_structure:
```

## Workflow

1. Classify the primary problem: impressions, CTR, first-30 retention, mid-video retention, topic satisfaction, production, or monetization.
2. If impressions are low, review topic demand and channel authority.
3. If CTR is low, review title/thumbnail promise and specificity.
4. If first-30 retention is low, review hook alignment and opening pace.
5. If mid-video retention drops, review section pacing, payoff timing, visuals, and audio.
6. If comments complain, cluster them with comment_pain_miner.
7. Recommend one packaging test and one content-structure test at a time.
8. Update the format rules based on evidence.

## Output schema

```yaml
diagnosis:
  primary_issue: impressions | ctr | first_30_sec | mid_retention | topic | production | monetization | unclear
  evidence:
    - metric:
      interpretation:
  likely_causes:
    - cause:
      confidence:
  recommended_tests:
    title_tests:
      - title:
    thumbnail_tests:
      - concept:
    hook_tests:
      - hook_change:
    structure_tests:
      - change:
    topic_tests:
      - topic:
  updated_format_rules:
    - rule:
  do_not_change_yet:
    - element:
```

## Agent prompts

### Analytics diagnosis prompt

```text
Diagnose this video. Separate click problem, hook problem, retention problem, topic problem, and production problem. Use metrics and comments as evidence. Recommend a small number of tests, not a full rebuild. Update the channel’s format rules only where the evidence is strong.
```

## Quality gates

- Diagnosis must cite metric evidence.
- Recommend no more than 3 primary tests at once.
- Do not declare a topic dead from one weak upload.
- For sleep videos, interpret long-tail performance over longer windows too.

## Examples

### Diagnosis examples

High impressions + low CTR = packaging problem. Good CTR + bad first 30 seconds = hook/promise mismatch. Good first 5 minutes + sharp drop at chapter 2 = pacing or chapter transition issue. Good retention + low impressions = topic/search/browse distribution issue.

## Failure modes

- Changing niche, title, thumbnail, hook, voice, and length all at once.
- Ignoring traffic source differences.
- Judging sleep videos too early when they may accrue long-tail sessions.
- Overfitting to a tiny sample.
