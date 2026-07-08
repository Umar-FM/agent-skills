# Skill 02: Competitor Format Miner

```yaml
id: competitor_format_miner
category: market_intelligence
inspired_by:
  - Saim profile corpus competitor-watching note
  - Saim strategic YouTube mining workflow
```

## Purpose

Turn competitor channels into format intelligence. This skill watches a small set of competitors deeply enough to extract repeatable structures, not surface-level topic ideas.

## Saim-heavy nuggets embedded

- Watch five competitor channels for a focused block and extract ideas from their outliers.
- Open 10–15 top performers and study first 30 seconds.
- Find title, thumbnail, hook, structure, length, pacing, and voice-tone patterns.
- Look for three to four videos that use the same structure and still perform.

## Inputs

```yaml
competitor_channels:
  - url_or_name:
scan_depth: shallow | standard | deep
videos_per_channel: integer
niche_goal: string
content_type: sleep | documentary | explainer | shorts
operator_constraints:
  budget:
  tools:
  team_size:
```

## Workflow

1. For each competitor, identify the top 10 videos by views and top 10 recent videos by relative performance.
2. Group videos by visible format: list, mystery, sleep doc, timeline, rise/fall, hidden truth, reaction, essay, compilation, story reading.
3. Find recurring structures that appear in 3+ successful videos.
4. Record the first 30 seconds of each winning format.
5. Record upload cadence and production complexity.
6. Record comment complaints and repeated audience requests.
7. Create a format map with “copyable logic” and “do-not-copy assets.”
8. Generate original format variants that fit the operator’s budget.

## Output schema

```yaml
competitors:
  - channel:
    positioning:
    recurring_formats:
      - format_name:
        example_videos:
        average_length:
        title_pattern:
        thumbnail_pattern:
        hook_pattern:
        pacing_pattern:
        visual_pattern:
        voice_pattern:
        production_complexity:
        audience_requests:
        weaknesses:
        copyable_logic:
        do_not_copy:
original_format_variants:
  - name:
    viewer_promise:
    title_examples:
    hook_examples:
    production_requirements:
    policy_notes:
```

## Agent prompts

### Competitor format mining prompt

```text
Analyze these competitor channels: {competitor_channels}. Your job is not to copy their topics. Extract the repeatable formats that are working. For each format, describe the viewer promise, emotional trigger, title logic, thumbnail logic, first 30-second hook pattern, pacing, visual system, and production complexity. Then create original variants that preserve the viewer behavior but change the creative substance.
```

## Quality gates

- Each format must be supported by at least 2–3 examples or marked as speculative.
- The output must separate structure from assets.
- Each variant must be feasible under the stated budget.
- Each variant must include a differentiation angle.

## Examples

### Format extraction example

Competitor format: “calm lost city documentaries.” Copyable logic: a place-based mystery, slow opening scene, educational chapters, ambient rain, curiosity title. Do not copy: exact city list, thumbnail composition, voice, script, map sequence, or chapter wording.

## Failure modes

- Only listing video topics.
- Overvaluing subscriber count instead of relative performance.
- Ignoring weak comments that reveal better angles.
- Producing clones that increase reused/inauthentic-content risk.
