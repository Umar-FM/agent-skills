# Skill 10: Topic Research Prompt Builder

```yaml
id: topic_research_prompt_builder
category: research
inspired_by:
  - Saim prompt libraries for wellness, crypto, sports, philosophy, finance, aviation/luxury
```

## Purpose

Generate niche-specific research prompts that force depth, structure, and source awareness before scripting.

## Saim-heavy nuggets embedded

- Saim’s prompt banks ask for foundations, terminology, history, current state, misconceptions, examples, research consensus, timelines, and applications.
- Different niches need different research shapes.
- Beginner clarity matters; explain terminology and resistance points.

## Inputs

```yaml
niche: history | wellness | finance | crypto | sports | philosophy | aviation | luxury | true_crime | science | custom
topic: string
audience_level: beginner | intermediate | expert
content_type: sleep | standard | explainer | docuseries
source_standard: light | normal | strict
```

## Workflow

1. Identify the niche and required research dimensions.
2. Create a prompt that collects core facts, timeline, terminology, misconceptions, examples, disputes, and visual references.
3. Add niche-specific cautions: health claims, financial advice, crypto risk, true-crime ethics, historical uncertainty.
4. Add a beginner-translation section if the audience is non-expert.
5. Add sleep-mode sensory/context section when relevant.
6. Add output schema so the researcher returns structured material.

## Output schema

```yaml
research_prompt:
  niche:
  topic:
  prompt_text:
  required_sections:
    - section:
  cautions:
    - caution:
  output_schema:
    field:
      description:
```

## Agent prompts

### Build a niche research prompt

```text
Create a research prompt for this niche and topic: {niche}, {topic}. The prompt must force the researcher to collect core facts, timeline, terminology, misconceptions, examples, disputed claims, audience questions, and visual references. Include niche-specific cautions and a structured output schema.
```

## Quality gates

- Prompt must include uncertainty handling.
- Prompt must include source expectations.
- Prompt must include misconceptions or audience resistance.
- Prompt must adapt for sleep vs standard tone.

## Examples

### Finance prompt shape

Ask for theory, empirical data, regulation, market mechanics, risk, implementation examples, misconceptions, and “not financial advice” boundaries.

### Philosophy prompt shape

Ask for historical context, key arguments, thinkers, terminology, logic, primary texts, schools of thought, and modern relevance.

### Sports prompt shape

Ask for athlete/coach dossier, timeline, game breakdown, technique deconstruction, sports economics, stats, and visual moments.

## Failure modes

- Using a generic research prompt for every niche.
- Missing legal/medical/financial caution areas.
- Asking for “interesting facts” without structure.
- Forgetting audience level.
