# Skill 16: Visual Production Segmenter

```yaml
id: visual_production_segmenter
category: production
inspired_by:
  - Wiz/Julian ecosystem AI segmentation concept
  - Saim production stack references
```

## Purpose

Turn approved scripts into visual production plans for editors or AI-asset agents.

## Saim-heavy nuggets embedded

- Segment scripts into visual beats instead of generating one vague asset list.
- Maintain character/location/style consistency while preserving variation.
- Use human QA for AI visuals.
- Production simplicity is acceptable if the viewer promise is strong and originality is clear.

## Inputs

```yaml
script_package: object
visual_style: string
mode: standard | sleep
asset_sources_allowed:
  - ai_generated
  - licensed_stock
  - public_domain
  - original_graphics
visuals_per_minute: integer
budget: number
```

## Workflow

1. Split the script into visual beats of 5–20 seconds for standard videos or 15–60 seconds for sleep videos.
2. Assign visual type: AI image, slow pan, stock footage, map, archival image, text card, diagram, black screen, ambient loop.
3. Create prompts or asset briefs for each beat.
4. Maintain style guide: aspect ratio, color temperature, camera movement, texture, character consistency, era accuracy.
5. Add variation notes so the video does not look like one repeated template.
6. Add risk notes: copyright, factual mismatch, uncanny faces, violent imagery, medical/financial claims.
7. Produce an editor timeline.

## Output schema

```yaml
visual_plan:
  style_guide:
    aspect_ratio:
    color_temperature:
    motion:
    texture:
    sleep_brightness_rules:
  recurring_elements:
    - element:
  segments:
    - segment_id:
      timestamp_start:
      timestamp_end:
      narration_excerpt:
      visual_type:
      asset_source:
      prompt_or_asset_brief:
      motion_instruction:
      variation_note:
      risk_note:
  qa_checklist:
    - check:
```

## Agent prompts

### Visual segmentation prompt

```text
Segment this script into production beats. For each beat, assign visual type, asset source, prompt or asset brief, motion instruction, variation note, and risk note. In sleep mode, avoid sudden brightness changes, fast cuts, and startling images.
```

## Quality gates

- Every segment must map to narration.
- Asset rights must be known or flagged.
- Sleep visuals must preserve low arousal.
- Repeated visuals must be intentional and varied enough to avoid template risk.

## Examples

### Sleep visual segment

Narration: “The road moved past olive groves and low stone walls.” Visual: slow AI-generated moonlit Roman road, no people, soft rain, 35-second pan, muted brightness, no sudden movement.

## Failure modes

- Using random stock footage that contradicts the script.
- Reusing identical AI prompts across many videos.
- Over-cutting sleep videos.
- Generating historical visuals that look modern without noting it.
