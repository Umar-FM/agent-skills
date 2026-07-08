# Skill 09: Research Conveyor Belt

```yaml
id: research_conveyor_belt
category: research
inspired_by:
  - Saim AI conveyor-belt thread
```

## Purpose

Create a staged research-to-script pipeline. This skill separates idea collection, factual research, story shaping, fact-checking, and bloat removal.

## Saim-heavy nuggets embedded

- Use one pass to pull ideas and facts, another to shape human story, another to fact-check and trim.
- Ask for deeper controversy, drama, hidden stories, and tensions after the basic summary.
- Train the tone before drafting.
- Flag AI-sounding or fake-sounding lines before production.

## Inputs

```yaml
topic: string
content_type: sleep | standard | explainer | docuseries
length_target_minutes: integer
audience: string
voice_card:
  tone:
  pacing:
  forbidden_words:
source_requirements:
  min_sources: integer
  primary_sources_preferred: boolean
```

## Workflow

1. Generate a 5-point basic summary of the topic.
2. Collect timelines, characters, places, terms, and disputed claims.
3. Identify hidden tensions: controversy, contradiction, human stakes, mystery, mechanism, or neglected detail.
4. Create a fact table with confidence levels.
5. Create a “do not claim” list for uncertain or unsupported claims.
6. Create a story spine: hook, setup, escalation, reveal, payoff, transition.
7. Create visual research notes for editor/visual agent.
8. Pass research to the scriptwriter, then review the script for factual and AI-tone issues.

## Output schema

```yaml
research_pack:
  topic:
  five_point_summary:
    - point:
  timeline:
    - date:
      event:
      confidence:
  key_people_places_terms:
    - item:
      relevance:
  tension_bank:
    - tension:
      type:
      viewer_reason_to_care:
  verified_facts:
    - fact:
      source:
      confidence:
  uncertain_or_disputed:
    - claim:
      caution:
  do_not_claim:
    - claim:
      reason:
  story_spine:
    hook:
    setup:
    escalation:
    reveal:
    payoff:
  visual_research_notes:
    - scene:
      possible_visuals:
```

## Agent prompts

### Research pass prompt

```text
Research this topic for a YouTube video: {topic}. First give a 5-point summary. Then identify deeper tensions: controversy, contradictions, hidden stories, human stakes, mechanisms, and overlooked details. Separate verified facts from uncertain claims. Include a “do not claim” section.
```

### Story spine prompt

```text
Using the research pack, build a story spine for a {content_type} video. The story should have a hook, setup, escalation, reveal, payoff, and transitions. For sleep mode, make the tension gentle and avoid sudden emotional spikes.
```

### Fact-check and bloat-trim prompt

```text
Review this script against the research pack. Flag unsupported claims, fake-sounding lines, vague claims, repeated phrases, and sections that do not advance the viewer’s understanding or sleep experience. Rewrite only the problematic lines.
```

## Quality gates

- Every factual script must include a do-not-claim list.
- Every tension must be supportable or clearly framed as uncertainty.
- Research and scriptwriting should be separate passes.
- Sleep research must include sensory details but not invent facts as if true.

## Examples

### Sleep history research use

Topic: ancient libraries. The conveyor belt outputs verified facts about known libraries, disputed claims about destruction, sensory scene notes, and a gentle story spine around how knowledge traveled, survived, and disappeared.

## Failure modes

- Using one web article as the whole research base.
- Letting AI invent historical details for atmosphere.
- Failing to distinguish myth, legend, and verified history.
- Skipping fact-check because the video is “just for sleep.”
