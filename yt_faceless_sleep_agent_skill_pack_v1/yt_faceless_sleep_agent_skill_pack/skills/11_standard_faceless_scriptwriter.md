# Skill 11: Standard Faceless Scriptwriter

```yaml
id: standard_faceless_scriptwriter
category: copy_scriptwriting
inspired_by:
  - Saim AI conveyor-belt thread
  - Saim storytelling formats
  - Saim long-form AI snippets
```

## Purpose

Write retention-oriented faceless scripts for standard documentaries, explainers, business breakdowns, essays, and story videos.

## Saim-heavy nuggets embedded

- Build around hook, story, pivot, twist, and outro.
- Use open loops and mini payoffs in long-form.
- Format comes before topic.
- Train tone and forbidden words before drafting.

## Inputs

```yaml
video_brief:
  title:
  thumbnail_summary:
  topic:
  content_engine:
  story_format:
  target_length_minutes:
  audience:
  voice_card:
  research_pack:
  cta_goal:
```

## Workflow

1. Read title and thumbnail; define the exact promise.
2. Read research pack; list factual constraints and do-not-claim items.
3. Write 5 hook options; choose one based on clarity and curiosity.
4. Create a beat outline with open loops and mini payoffs every 60–90 seconds.
5. Write the script in sections: intro tension, setup, escalation, pivot, reveal, payoff, CTA.
6. Add visual directions for each section.
7. Run a bloat pass to remove repetition and generic filler.
8. Run a fact-check pass against the research pack.
9. Run a policy/originality pre-check before handing to production.

## Output schema

```yaml
script_package:
  title:
  thumbnail_summary:
  selected_hook:
  hook_pattern:
  promise:
  beat_outline:
    - timestamp:
      section:
      open_loop:
      payoff:
      visual_direction:
  full_script:
    - timestamp:
      narration:
      visual_direction:
      retention_function:
  cta:
  fact_check_flags:
    - issue:
      fix:
  bloat_removed:
    - line_or_section:
      reason:
```

## Agent prompts

### Faceless script prompt

```text
Write a faceless YouTube script from this brief. The first line must confirm the title/thumbnail promise. The intro must create tension, then the body should move through setup, escalation, pivot, reveal, and payoff. Add mini-payoffs every 60–90 seconds. Include visual directions. Do not invent facts beyond the research pack.
```

### Retention pass prompt

```text
Review this script for retention. Mark every open loop, payoff, slow section, repeated idea, and weak transition. Add a retention beat every 60–90 seconds without adding fake drama.
```

## Quality gates

- First 30 seconds must score at least 8/10 for clarity and curiosity.
- Every major claim must trace to research or be removed.
- No section should exist without a retention function.
- CTA must not interrupt the payoff.

## Examples

### Standard structure

Title: “Why This Tiny Channel Beat Everyone.” Beat map: hook explains it was not niche luck; setup shows competitor landscape; escalation reveals format loop; pivot shows why others copied wrong thing; payoff gives operating system.

## Failure modes

- Overwriting with generic motivational filler.
- Using cliffhangers that never resolve.
- Starting with broad context before the hook.
- Adding unsupported twists.
