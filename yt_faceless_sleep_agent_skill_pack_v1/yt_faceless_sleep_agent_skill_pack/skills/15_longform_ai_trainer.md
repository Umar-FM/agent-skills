# Skill 15: Longform AI Trainer

```yaml
id: longform_ai_trainer
category: copy_systems
inspired_by:
  - Saim profile corpus voice-training post
  - Saim long-form faceless AI snippets
```

## Purpose

Create a voice card and writing constraints before generating long-form scripts. This reduces generic AI tone and makes scripts consistent.

## Saim-heavy nuggets embedded

- Train AI on target audience, tone, forbidden words, and sentence structure before writing.
- Long-form should have intro tension, chapter escalation, and mini payoffs.
- Use max sentence-length rules when needed.
- Voice consistency is a system, not a preference.

## Inputs

```yaml
channel_name: string
audience: string
content_type: sleep | documentary | explainer | essay
reference_voice_samples:
  - sample_text
brand_attributes:
  - attribute
forbidden_words:
  - word
sentence_rules:
  max_words_standard: integer
  max_words_sleep: integer
```

## Workflow

1. Create an audience card: who they are, why they click, what they dislike, what they already know.
2. Create a tone card: energy, warmth, authority, humor, pacing, sentence length.
3. Create a forbidden list: clichés, hype words, phrases that sound like AI, banned claims.
4. Create approved phrase patterns: openings, transitions, payoffs, CTAs.
5. Create long-form structure rules: intro tension, chapter escalation, mini payoff, transition, final reframe.
6. Run a sample rewrite test before full script generation.
7. Save the voice card and attach it to every script brief.

## Output schema

```yaml
voice_card:
  audience:
    identity:
    click_reason:
    dislikes:
    knowledge_level:
  tone:
    energy:
    warmth:
    authority:
    pacing:
    humor:
    sentence_length:
  forbidden_words:
    - word_or_phrase:
  approved_patterns:
    openings:
      - pattern:
    transitions:
      - pattern:
    payoffs:
      - pattern:
    ctas:
      - pattern:
  longform_rules:
    intro:
    chapters:
    mini_payoffs:
    transitions:
    conclusion:
  sample_rewrite:
    before:
    after:
```

## Agent prompts

### Voice-card builder

```text
Build a long-form YouTube voice card for this channel. Define the audience, click reason, dislikes, tone, pacing, sentence length, forbidden words, approved phrase patterns, and long-form structure rules. Then rewrite the sample paragraph in the approved voice.
```

### AI-tone scrubber

```text
Review this script for generic AI voice. Flag clichés, vague claims, unnatural transitions, repeated sentence patterns, and over-polished phrases. Rewrite flagged lines using the channel voice card.
```

## Quality gates

- Voice card must exist before script generation.
- Forbidden words and clichés must be concrete.
- One sample rewrite must prove the style.
- Sleep and standard modes need different sentence rhythm rules.

## Examples

### Sleep voice card excerpt

Energy: low. Authority: calm and specific. Pacing: slow, with soft transitions. Forbidden: shocking, unbelievable, insane, smash, terrifying truth. Approved transition: “And from here, the story becomes quieter.”

## Failure modes

- Asking AI to “write in a human tone” with no examples.
- Changing voice every video.
- Using forbidden words in titles/hooks anyway.
- Overfitting to one creator’s voice.
