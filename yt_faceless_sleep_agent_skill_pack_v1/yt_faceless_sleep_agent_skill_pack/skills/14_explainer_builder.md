# Skill 14: Explainer Builder

```yaml
id: explainer_builder
category: copy_scriptwriting
inspired_by:
  - Saim profile corpus explainer patterns
```

## Purpose

Turn confusing, scary, or contested topics into clear mechanism-driven explainers.

## Saim-heavy nuggets embedded

- Explainers convert complexity to clarity, fear to understanding, conflict to mechanism, failure to root cause, tension to timeline, and shock to explanation.
- Start with the viewer’s emotional confusion, then walk them to mechanism.
- Use examples, misconceptions, timelines, and root causes.

## Inputs

```yaml
topic: string
viewer_confusion: string
viewer_level: beginner | intermediate | expert
mode: standard | sleep
length_minutes: integer
research_pack: object
```

## Workflow

1. Define the viewer’s starting confusion or fear.
2. Define the mechanism the viewer should understand by the end.
3. Choose an explainer conversion: complexity→clarity, fear→understanding, conflict→mechanism, failure→root cause, tension→timeline, shock→explanation.
4. Write a simple thesis.
5. Create a section map: problem, misconception, mechanism, example, implication, recap.
6. Add analogies for beginner audiences.
7. For sleep mode, make the explanation slower and sensory, with less urgency.

## Output schema

```yaml
explainer_blueprint:
  viewer_start_state:
  viewer_end_state:
  conversion_type:
  thesis:
  misconceptions:
    - misconception:
      correction:
  mechanism_steps:
    - step:
      simple_explanation:
      example:
  section_map:
    - section:
      purpose:
      visual_direction:
  hook:
  conclusion:
  sleep_adjustments:
```

## Agent prompts

### Explainer prompt

```text
Build an explainer for this topic. Start with the viewer’s confusion, choose one conversion pattern, and move them to a clear mechanism. Include misconceptions, examples, analogies, visuals, and a concise conclusion. Do not overstate evidence.
```

## Quality gates

- The viewer’s before/after state must be explicit.
- Every analogy must clarify, not distort.
- No jargon without explanation.
- Sleep explainers must slow down but still teach.

## Examples

### Explainer example

Topic: Why cities get buried. Conversion: complexity→clarity. Mechanism steps: dust, flooding, abandonment, rebuilding, archaeology, modern excavation. Sleep version: walk slowly through layers of a city at night.

## Failure modes

- Explaining everything chronologically when a mechanism would be clearer.
- Using jargon as a substitute for insight.
- Creating false certainty in disputed topics.
- Making sleep explainers too dense.
