# Skill 13: Docuseries Builder

```yaml
id: docuseries_builder
category: longform_strategy
inspired_by:
  - Saim profile corpus docuseries pattern
```

## Purpose

Build multi-episode or long-form docuseries arcs that feel progressively deeper rather than episodic and flat.

## Saim-heavy nuggets embedded

- Docuseries means unraveling something bigger.
- Pattern: small event → larger force → hidden mechanism → final revelation.
- Each section should reveal a deeper layer.

## Inputs

```yaml
series_topic: string
number_of_episodes: integer
content_engine: invisible_force | domino_effect | false_win | polarization | anti_tutorial
audience: string
mode: standard | sleep
research_pack: optional
```

## Workflow

1. Define the central mystery or mechanism of the series.
2. Find the small opening event that can pull viewers in.
3. Identify the larger force behind the event.
4. Identify the hidden mechanism that most viewers miss.
5. Define the final revelation or reframe.
6. Create episode arcs where each episode answers one question and opens a bigger one.
7. For sleep mode, keep the reveals gentle and atmospheric.

## Output schema

```yaml
docuseries_blueprint:
  series_promise:
  central_question:
  opening_small_event:
  larger_force:
  hidden_mechanism:
  final_revelation:
  episode_map:
    - episode:
      title:
      question_answered:
      bigger_question_opened:
      story_format:
      cliffhanger_or_soft_transition:
      sleep_adjustment:
  continuity_devices:
    - device:
```

## Agent prompts

### Docuseries blueprint prompt

```text
Build a docuseries blueprint using this pattern: small event → larger force → hidden mechanism → final revelation. Each episode must answer a specific question and open a deeper one. For sleep mode, make the tension subtle and use soft transitions instead of cliffhangers.
```

## Quality gates

- Central question must be clear in one sentence.
- Each episode must add a new layer, not repeat the same premise.
- Final revelation must be supported by research.
- Sleep docuseries must avoid urgent cliffhanger language.

## Examples

### Sleep docuseries example

Series: “Roads That Disappeared.” Episode 1 starts with one buried road. Episode 2 reveals trade routes. Episode 3 reveals climate and water. Episode 4 reveals political neglect. Final reframe: roads vanish when the systems around them vanish.

## Failure modes

- Making a playlist rather than a docuseries arc.
- Opening too broad instead of with a small event.
- Using an unsupported final twist.
- Ending every episode with the same vague tease.
