# Skill 08: AI Pattern Recognition Prompt Chain

```yaml
id: ai_pattern_recognition_prompt_chain
category: research_packaging
inspired_by:
  - Saim strategic YouTube mining workflow
  - Saim AI conveyor-belt thread
```

## Purpose

Use models as structured analysts for titles, thumbnails, hooks, comments, and scripts. This skill turns messy competitor examples into pattern libraries.

## Saim-heavy nuggets embedded

- Ask AI to analyze title triggers, word patterns, emotional appeals, and structure hints.
- Use separate passes for research, writing, and fact-check/editing.
- Train models on tone before asking them to write.
- Use AI to compress patterns, not to clone outputs.

## Inputs

```yaml
examples:
  titles:
    - string
  thumbnail_summaries:
    - string
  hooks:
    - string
  comments:
    - string
analysis_goal: title | thumbnail | hook | full_format | comment_gap | script_tone
channel_voice_card: optional
```

## Workflow

1. Clean the input examples and remove irrelevant metadata.
2. Run a title-pattern analysis pass.
3. Run a thumbnail-tension analysis pass.
4. Run a first-30-second hook analysis pass.
5. Run a comment-gap analysis pass if comments are available.
6. Ask the model to infer the underlying viewer behavior and emotional packaging.
7. Ask for original variants that use the pattern without reusing wording.
8. Run a final “clone risk” pass to flag outputs too close to examples.

## Output schema

```yaml
pattern_report:
  viewer_behavior:
  emotional_packaging:
  title_patterns:
    - pattern:
      examples_paraphrased:
      original_variants:
  thumbnail_tension_patterns:
    - pattern:
      original_variants:
  hook_patterns:
    - pattern:
      original_variants:
  comment_gap_patterns:
    - gap:
      content_response:
  clone_risk_flags:
    - issue:
      fix:
```

## Agent prompts

### Title pattern analyzer

```text
Analyze these YouTube titles. Do not create titles yet. Extract recurring structures, trigger words, curiosity gaps, specificity level, emotional promise, and implied story format. Then describe how to create original titles using the same logic without copying wording.
```

### Thumbnail tension analyzer

```text
Analyze these thumbnail descriptions. Identify the visual subject, contrast, implied conflict, emotional promise, text style, and curiosity gap. Create original thumbnail concepts that use the same tension logic but different visual composition and assets.
```

### Clone-risk checker

```text
Compare these generated titles/hooks/concepts against the examples. Flag anything that is too close in wording, structure, visual idea, or claim. Rewrite flagged items to preserve the viewer behavior while changing the creative substance.
```

## Quality gates

- Pattern report must include original variants.
- Clone-risk pass is mandatory before using generated outputs.
- Do not ask AI to summarize competitor scripts into reusable scripts.
- For factual niches, separate pattern analysis from fact generation.

## Examples

### Pattern chain use case

Input: 30 successful sleep-history titles. Output: patterns like “Fall asleep to [specific place] + [quiet mystery]” or “[duration] of calm stories from [era/place].” The agent then creates original titles about different places, different mysteries, and different research angles.

## Failure modes

- Letting AI average examples into bland generic titles.
- Generating near-duplicates of competitor titles.
- Mixing analysis and writing in one prompt with no QA.
- Forgetting to check factual claims after packaging generation.
