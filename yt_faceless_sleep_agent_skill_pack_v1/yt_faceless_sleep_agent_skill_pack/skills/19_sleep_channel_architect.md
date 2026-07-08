# Skill 19: Sleep Channel Architect

```yaml
id: sleep_channel_architect
category: channel_strategy_sleep
inspired_by:
  - Saim sleep-story note
  - Saim emotional packaging idea
  - Wanner sleep-channel safety thread
  - YouTube monetization policy
```

## Purpose

Design sleep channels that can scale while preserving originality, variety, and monetization safety.

## Saim-heavy nuggets embedded

- Sleep is a viewer state, not just a niche.
- People sleep to whisper/long-form stories; serve that behavior loop.
- Use emotional packaging: calm mystery, cozy history, cosmic wonder, rainy folklore.
- Wanner-style safety suggestions: brand intro, pattern interruptions, varied subjects, educational descriptions/resources.
- YouTube policy: avoid repetitive/mass-produced/template content with little variation.

## Inputs

```yaml
channel_goal: string
sleep_subniche: history | mythology | horror | space | nature | fiction | meditation | custom
target_audience: string
risk_tolerance: low | medium | high
production_budget_per_video: number
voice_type: human | ai | hybrid
visual_budget: low | medium | high
upload_cadence: string
```

## Workflow

1. Define the sleep-state promise: what the viewer feels and why they return.
2. Choose the content engine and story formats that fit sleep.
3. Define recurring brand devices: intro line, ambience, narrator persona, chapter style, visual motif.
4. Design variation rules: different eras, places, subjects, chapter structures, visual motifs, source types.
5. Create a 30-video map with distinct subjects and research angles.
6. Define policy-safety rules: original scripts, educational context, varied substance, asset rights, no mass template repetition.
7. Define production specs: length, voice, ambience, visuals, chapters, CTA placement.
8. Define monetization path and risk review cadence.

## Output schema

```yaml
channel_blueprint:
  name:
  promise:
  viewer_state:
  emotional_packaging:
  dominant_engine:
  supporting_story_formats:
  narrator_persona:
  ambience_system:
  visual_system:
  recurring_brand_devices:
    - device:
  variation_rules:
    - rule:
  video_length_range:
  chapter_length_range:
  upload_cadence:
  monetization_paths:
  policy_safety_rules:
    - rule:
30_video_map:
  - title:
    category:
    unique_research_angle:
    soft_hook:
    visual_variation:
    source_or_originality_note:
    policy_risk:
```

## Agent prompts

### Sleep channel blueprint prompt

```text
Design a sleep-channel blueprint for this subniche: {sleep_subniche}. Define the viewer state, emotional packaging, channel promise, dominant engine, narrator persona, ambience, visual system, recurring brand devices, variation rules, and a 30-video topic map. Make it scalable without looking mass-produced or repetitive.
```

## Quality gates

- Blueprint must define both repetition and variation.
- Every topic in the 30-video map must have a unique research or story angle.
- Policy-safety rules must be explicit.
- Sleep promise must be clear in one sentence.

## Examples

### Recommended first channel

Working name: Sleepy Lost Histories. Promise: calm long-form stories about lost places, forgotten inventions, quiet mysteries, old maps, and vanished roads. Dominant engine: invisible force. Sleep state: rainy library. Variation rules: rotate eras, places, object types, and chapter structures.

## Failure modes

- Building a black-screen generic AI-story factory.
- Using the same title formula, same visuals, and same story shape for every upload.
- Ignoring educational/source context in factual sleep videos.
- Choosing horror hooks that make the channel less sleep-friendly.
