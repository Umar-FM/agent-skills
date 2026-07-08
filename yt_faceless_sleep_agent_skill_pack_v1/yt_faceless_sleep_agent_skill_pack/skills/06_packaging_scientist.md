# Skill 06: Packaging Scientist

```yaml
id: packaging_scientist
category: copy_packaging
inspired_by:
  - Saim strategic YouTube mining workflow
  - Saim niche research thread
```

## Purpose

Diagnose and create titles, thumbnails, and opening alignment. Packaging earns the click; the first 30 seconds must prove the click was correct.

## Saim-heavy nuggets embedded

- Study title formulas, thumbnail patterns, emotional appeals, hook words, and structure hints.
- First line should connect to title/thumbnail promise.
- Thumbnail tension and title curiosity must point to the same question.
- Packaging beats production early when the format is simple.

## Inputs

```yaml
video_topic: string
viewer_behavior: string
content_engine: string
story_format: string
competitor_outliers:
  - title:
    thumbnail_summary:
    hook_summary:
constraints:
  no_clickbait: true
  sleep_safe: boolean
  max_title_chars: integer
```

## Workflow

1. Define the exact viewer question the package must create.
2. Write 20 titles using different structures: mystery, contradiction, time/place, number, hidden system, soft sleep promise, before/after, consequence.
3. Write 10 thumbnail concepts with one visual subject and one tension idea.
4. Write 10 thumbnail text options under 4 words when text is needed.
5. Pair titles and thumbnails; remove pairs that ask different questions.
6. Write the first 30 seconds for the top 3 packages.
7. Score title-thumbnail-hook alignment.
8. Recommend 3 A/B test candidates.

## Output schema

```yaml
packaging_brief:
  viewer_question:
  title_options:
    - title:
      formula:
      curiosity_gap:
      accuracy_check:
      sleep_safe:
      score_1_10:
  thumbnail_concepts:
    - concept:
      subject:
      tension:
      text:
      visual_contrast:
      score_1_10:
  best_pairs:
    - title:
      thumbnail_concept:
      first_30_seconds:
      alignment_score_1_10:
      risk_notes:
recommended_test:
  primary:
  backup_1:
  backup_2:
```

## Agent prompts

### Packaging generation prompt

```text
Create packaging for this video: {video_topic}. The viewer behavior is {viewer_behavior}. The content engine is {content_engine}. Generate title options, thumbnail concepts, thumbnail text, and first-30-second hooks. Every package must ask one clear question and the opening must immediately prove the title/thumbnail was accurate. Avoid hype the script cannot pay off.
```

## Quality gates

- Title, thumbnail, and hook must ask the same core question.
- No title should require a claim the research cannot support.
- Sleep titles should combine calm benefit with specific curiosity.
- Thumbnail should be legible at small size.
- Top package must include a first-30-second script.

## Examples

### Sleep packaging example

Topic: ancient libraries. Weak: “Ancient Libraries Documentary.” Stronger: “Fall Asleep to the Quiet Mysteries of Ancient Libraries.” Thumbnail: candlelit shelves, old map, tiny text “LOST ROOMS.” First line confirms libraries and opens a calm mystery.

## Failure modes

- Creating a great title but unrelated thumbnail.
- Using “shocking” language in a sleep video.
- Letting AI generate generic titles like “You Won’t Believe…” without a specific mechanism.
- Ignoring first-30-second alignment.
