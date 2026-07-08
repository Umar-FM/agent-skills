# Skill 12: Sleep Scriptwriter

```yaml
id: sleep_scriptwriter
category: copy_scriptwriting_sleep
inspired_by:
  - Saim sleep-story note
  - Saim hook notes
  - Wanner sleep-channel safety thread
```

## Purpose

Write long-form sleep scripts that combine low-arousal narration with enough curiosity to earn the click and sustain background listening.

## Saim-heavy nuggets embedded

- Sleep channels serve a behavior loop: people want to relax or fall asleep while a story continues.
- Sleep content needs emotional packaging, not just a topic.
- Use soft hooks: curiosity without adrenaline.
- Repeat the calming promise, not the same substance.

## Inputs

```yaml
video_brief:
  title:
  topic:
  sleep_state: rainy | library | fireside | cosmic | cabin | desert_night | custom
  length_minutes: 60 | 90 | 120 | 180 | 240
  chapter_length_minutes: 8_to_12
  audience:
  voice_card:
  research_pack:
  ambience:
  avoid:
    - graphic_violence
    - loud_cta
    - panic_words
    - sudden_music
```

## Workflow

1. Define the soft promise: what the listener will learn or imagine while relaxing.
2. Write a calm opening that confirms the title and gives permission to drift off.
3. Build chapters of 8–12 minutes, each with one gentle question and one soft payoff.
4. Use sensory details: weather, light, texture, distance, footsteps, maps, rooms, sky, water.
5. Keep sentence rhythm medium-long and smooth; avoid punchy hype cadence.
6. Use transitions that make it okay to miss details.
7. For mysteries, avoid graphic or panic language; frame curiosity as quiet exploration.
8. Add a soft CTA only after the listener is settled or at the end.
9. Include visual/audio notes: no sudden brightness, no loud stings, no jarring cuts.

## Output schema

```yaml
sleep_script_package:
  title:
  soft_promise:
  sleep_state:
  opening_hook:
  listener_permission_line:
  chapter_map:
    - chapter_number:
      timestamp_start:
      chapter_title:
      gentle_question:
      sensory_anchor:
      facts_or_story_points:
      soft_payoff:
      transition_line:
  narration:
    - timestamp:
      text:
      voice_direction:
      visual_direction:
      ambience_note:
  soft_cta:
  policy_notes:
  source_notes:
```

## Agent prompts

### Sleep script prompt

```text
Write a long-form sleep script for this topic: {topic}. The tone should be calm, specific, and low-arousal. Open with a soft promise and permission to drift off. Use chapters every 8–12 minutes, each with one gentle question and one soft payoff. Use sensory detail but do not invent factual claims. Avoid loud CTAs, shock language, graphic violence, and sudden tonal shifts.
```

### Sleep rewrite pass

```text
Rewrite this section for sleep. Lower the emotional temperature, smooth the sentence rhythm, remove hype, remove sudden transitions, and keep curiosity gentle. Preserve factual meaning.
```

## Quality gates

- Opening must include soft promise and permission to relax.
- No chapter should spike arousal with sudden danger, gore, yelling, or aggressive CTA.
- Each chapter must have distinct substance, not filler repetition.
- Visual and audio notes must protect sleep continuity.
- Educational descriptions/source notes should be included for factual videos.

## Examples

### Sleep hook example

“Tonight, we are going to wander through the quiet edges of the ancient world, where old roads fade into sand and the names of cities become softer with time. You do not need to remember every date. Let the story move slowly in the background.”

### Chapter loop example

Gentle question: Why did this road vanish while others survived? Soft payoff: because roads needed water, trade, repairs, and political attention; when those faded, stone became memory.

## Failure modes

- Writing a normal documentary and merely adding rain sounds.
- Using crime/horror hooks that are too sharp for sleep.
- Repeating the same ambience, chapter structure, and visuals with no substantive variation.
- Inventing “ancient secrets” without source support.
