# Skill 07: Hook Writer

```yaml
id: hook_writer
category: copy_scriptwriting
inspired_by:
  - Saim hook construction notes
  - Saim strategic YouTube mining workflow
```

## Purpose

Write opening hooks that connect to the click and create a reason to keep watching. Supports standard faceless and sleep modes.

## Saim-heavy nuggets embedded

- Hook should confirm expectation and create curiosity.
- Watch the first 30 seconds of outliers to learn hook patterns.
- Every hook is a pattern, not a script; steal logic, not wording.
- For long-form, hook should set tension and lead into chapter escalation.

## Inputs

```yaml
title: string
thumbnail_summary: string
video_topic: string
content_engine: string
story_format: string
mode: standard | sleep | documentary | shorts
viewer_state: string
tone_card:
  tone:
  forbidden_words:
  sentence_length:
```

## Workflow

1. Identify the promise made by title and thumbnail.
2. Write the confirmation line: prove the viewer clicked the right video.
3. Write the curiosity line: create a question, contradiction, or unresolved image.
4. Write the stakes line: why this matters or why it is worth staying.
5. For standard mode, add tension and pace.
6. For sleep mode, soften stakes into gentle curiosity and permission to relax.
7. Produce 10 hook options and classify each by pattern.
8. Select the best 3 and score them on clarity, curiosity, accuracy, and tone fit.

## Output schema

```yaml
hook_options:
  - hook:
    pattern: contradiction | unfinished_story | hidden_mechanism | soft_mystery | threat | number_mystery | before_after | sensory_scene
    confirms_title: true
    curiosity_gap:
    stakes:
    tone_fit_1_10:
    accuracy_risk_1_10:
selected_hooks:
  primary:
  backup:
  sleep_variant_if_needed:
```

## Agent prompts

### Standard hook prompt

```text
Write 10 hooks for this video. Each hook must be 40–70 words, line 1 must connect directly to the title/thumbnail, and line 2 must open a curiosity gap. Classify each hook by pattern. Avoid fake urgency and claims not supported by the brief.
```

### Sleep hook prompt

```text
Write 10 calm sleep-video hooks. Each should softly confirm the title promise, create gentle curiosity, and give the listener permission to relax. Avoid loud stakes, aggressive CTAs, gore, panic words, and rapid-fire questions.
```

## Quality gates

- Line 1 must match title/thumbnail.
- Hook must make a specific promise, not generic intrigue.
- No unsupported “truth nobody knows” claims.
- Sleep hooks must not wake the listener with hype language.
- Standard hooks must avoid over-explaining before tension is created.

## Examples

### Standard hook pattern

Title: “The Tiny Channel That Beat Everyone With One Format.” Hook: “This channel did not win because the niche was empty. It won because one repeatable format matched a behavior YouTube was already rewarding. Once you see the pattern, you will start noticing it everywhere.”

### Sleep hook pattern

Title: “Fall Asleep to the Quiet Mysteries of Ancient Roads.” Hook: “Tonight, we are going to follow old roads after the day has gone quiet. Some crossed empires, some disappeared under fields, and some still explain how distant cities learned to speak to one another.”

## Failure modes

- Opening with “welcome back” before giving a reason to stay.
- Repeating the title word-for-word without deepening it.
- Adding stakes that the rest of the video never pays off.
- Using too many questions in a sleep hook.
