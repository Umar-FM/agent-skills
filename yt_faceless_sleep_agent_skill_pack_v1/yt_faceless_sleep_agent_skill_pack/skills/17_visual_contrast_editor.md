# Skill 17: Visual Contrast Editor

```yaml
id: visual_contrast_editor
category: production
inspired_by:
  - Saim profile corpus visual contrast note
```

## Purpose

Plan visual variation to reduce fatigue in standard videos and preserve gentle novelty in sleep videos.

## Saim-heavy nuggets embedded

- Saim points to visual contrast changes every 5–10 seconds as a way to reset visual fatigue.
- For sleep, adapt the principle: subtle novelty instead of energetic contrast.
- Visual rhythm should match viewer state.

## Inputs

```yaml
visual_plan: object
mode: standard | sleep
video_length_minutes: integer
current_cut_density: string
viewer_state: string
```

## Workflow

1. Classify the video mode: standard retention or sleep continuity.
2. For standard mode, mark visual reset opportunities every 5–10 seconds: brightness, scale, shot type, graphic, zoom, text, archival cut.
3. For sleep mode, mark soft variation every 20–60 seconds: slow pan, scene dissolve, slight location shift, ambience continuity, chapter card.
4. Identify visual monotony risk and over-stimulation risk.
5. Create an edit rhythm map.
6. Add QA notes for brightness, motion speed, text density, and audio sync.

## Output schema

```yaml
edit_rhythm_map:
  mode:
  reset_interval_guideline:
  monotony_risks:
    - risk:
      fix:
  overstimulation_risks:
    - risk:
      fix:
  timeline_notes:
    - timestamp:
      current_visual:
      recommended_reset:
      reason:
  sleep_specific_rules:
    max_brightness_jump:
    max_motion_speed:
    transition_style:
```

## Agent prompts

### Visual rhythm prompt

```text
Review this visual plan for fatigue and pacing. In standard mode, recommend visual resets every 5–10 seconds where useful. In sleep mode, recommend gentle visual novelty every 20–60 seconds without sudden brightness, fast cuts, or startling images.
```

## Quality gates

- Standard videos must avoid static slides for too long unless intentional.
- Sleep videos must avoid harsh contrast jumps.
- Visual rhythm must support the script’s retention function.
- Every reset must have a purpose.

## Examples

### Adapted sleep contrast

Instead of bright/dim cuts every 5 seconds, a sleep video uses slow dissolves between candlelit library shelves, rain on a window, and a dim map table. Novelty stays gentle.

## Failure modes

- Applying high-energy editing rules to sleep content.
- Adding visual changes that distract from narration.
- Keeping one static AI image for hours with no variation.
- Ignoring brightness spikes.
