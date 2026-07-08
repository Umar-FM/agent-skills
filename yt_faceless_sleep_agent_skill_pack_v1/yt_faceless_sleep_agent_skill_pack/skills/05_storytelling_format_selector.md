# Skill 05: Storytelling Format Selector

```yaml
id: storytelling_format_selector
category: strategy
inspired_by:
  - Saim profile corpus storytelling-format bank
```

## Purpose

Choose a proven story shape before writing. This prevents blank-page scripts and turns topics into repeatable video structures.

## Saim-heavy nuggets embedded

- Story formats are inventory.
- Use origin, rise/fall, before/after, timeline, cause/effect, chain reaction, turning point, lesson learned, parallel, behind-the-scenes.
- Use hidden/truth formats: hidden truth, wrong narrative, overlooked variable, real reason, silent factor, unseen system, illusion, misdirection, buried detail, ignored evidence.

## Inputs

```yaml
topic: string
content_engine: string
viewer_state: string
video_length: string
content_type: sleep | standard | explainer | docuseries | short
known_facts:
  - fact:
```

## Workflow

1. Identify whether the topic is event-driven, character-driven, system-driven, mystery-driven, or lesson-driven.
2. Choose 3 candidate story formats.
3. For each candidate, outline the first 5 beats.
4. Score each format on curiosity, clarity, retention, originality, and sleep fit if relevant.
5. Select the best format and one backup.
6. Generate section headings and open loops.
7. Pass the selected format to the scriptwriter.

## Output schema

```yaml
candidate_formats:
  - format_name:
    fit_score_1_10:
    curiosity_score_1_10:
    retention_score_1_10:
    originality_score_1_10:
    sleep_fit_1_10:
    beat_outline:
      - beat:
selected_format:
  name:
  reason:
  section_map:
    - section_title:
      open_loop:
      payoff:
backup_format:
  name:
  when_to_use:
```

## Agent prompts

### Format selection prompt

```text
Choose the best story format for this topic: {topic}. Candidate formats include origin, rise/fall, timeline, chain reaction, turning point, hidden truth, wrong narrative, overlooked variable, real reason, unseen system, buried detail, and ignored evidence. Score each candidate and select the format that creates the strongest retention without misleading the viewer.
```

## Quality gates

- Format must be explicit before the script begins.
- Selected format must match the title promise.
- For sleep videos, the format must sustain curiosity without loud tension.
- For educational videos, the format must preserve factual clarity.

## Examples

### Topic transformation

Topic: old maps. Weak approach: list facts about maps. Strong format: “buried detail.” Sections reveal strange map details that show what people feared, misunderstood, or desired. Sleep version uses slow scene-setting and gentle reveals.

## Failure modes

- Choosing “timeline” for every topic.
- Using hidden-truth framing where no hidden truth exists.
- Creating a twist that overstates the evidence.
- Changing story format halfway through the script.
