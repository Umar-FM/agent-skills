# Skill 04: Format Engine Selector

```yaml
id: format_engine_selector
category: strategy
inspired_by:
  - Saim profile corpus content-engine list
```

## Purpose

Choose the dominant emotional/narrative engine for a channel or video. A clear engine makes a faceless channel repeatable without making it feel generic.

## Saim-heavy nuggets embedded

- Pick one engine per channel: invisible force, domino effect, anti-tutorial, false win, or polarization.
- A format is stronger than a niche because it predicts audience feeling.
- Use emotional packaging to define what the viewer comes back for.

## Inputs

```yaml
channel_or_video_goal: string
topic_area: string
audience_state: curious | anxious | sleepy | ambitious | angry | nostalgic | confused | other
risk_tolerance: low | medium | high
content_length: shorts | 8_12_min | 15_40_min | 60_180_min
```

## Workflow

1. Define the viewer’s current emotional state and desired emotional payoff.
2. Choose one dominant engine from the engine menu.
3. Map the engine to title logic, hook logic, script structure, and visual tone.
4. Choose 1–2 supporting story formats but do not mix too many engines.
5. Write a one-sentence channel/video promise.
6. Generate 10 topic variants that use the same engine with different substance.
7. Reject engine-topic combinations that create policy, factual, or tone mismatch.

## Output schema

```yaml
selected_engine:
  name:
  why_it_fits:
  viewer_emotion_start:
  viewer_emotion_end:
  title_logic:
  hook_logic:
  script_shape:
  visual_tone:
  sleep_safe_adjustments:
  policy_risks:
  examples:
    - topic:
      title:
      hook:
rejected_engines:
  - name:
    reason:
```

## Agent prompts

### Engine selection prompt

```text
Given this topic and audience state, select the best faceless content engine: invisible force, domino effect, anti-tutorial, false win, or polarization. Explain the viewer emotion, title logic, hook logic, script structure, and why this engine is safer or stronger than alternatives. Then create 10 original topic ideas using that engine.
```

## Quality gates

- One dominant engine only unless there is a strong reason.
- The engine must affect title, hook, and structure, not just the description.
- Sleep videos must avoid high-arousal polarization unless softened heavily.
- Each topic variant must be materially different.

## Examples

### Sleep history engine choice

Topic: lost Roman roads. Best engine: invisible force. Promise: reveal how roads quietly shaped empire, trade, military power, and daily life. Sleep adjustment: make the hidden system calm and atmospheric rather than urgent or conspiratorial.

## Failure modes

- Mixing too many engines in one script.
- Using polarization for sleep content and accidentally raising arousal.
- Picking an engine that creates clickbait the script cannot pay off.
- Treating engine choice as cosmetic.
