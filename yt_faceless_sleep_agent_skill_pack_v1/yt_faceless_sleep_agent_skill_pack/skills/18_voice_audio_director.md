# Skill 18: Voice and Audio Director

```yaml
id: voice_audio_director
category: production_audio
inspired_by:
  - Saim production-stack mentions
  - Saim sleep-story model
```

## Purpose

Specify narration, pacing, cleanup, ambience, and mix rules for faceless videos, especially sleep channels.

## Saim-heavy nuggets embedded

- Voice tone, cadence, and pauses matter as much as the script.
- Sleep-story models often use AI voice, rain, and long-form ambience, but must avoid generic repetition.
- Free/low-cost tools can work early if the audio is clean.

## Inputs

```yaml
script_package: object
mode: standard | sleep
voice_type: human | ai | hybrid
ambience: none | rain | fireplace | room_tone | cosmic | forest | custom
platform_loudness_target: string
voice_card: object
```

## Workflow

1. Define narrator persona: age impression, warmth, authority, distance from mic, energy.
2. Define cadence: words per minute, pause length, emphasis, breathiness, sibilance tolerance.
3. Define ambience: loop length, volume under voice, no sudden changes, licensing status.
4. Define cleanup: noise reduction, de-essing, compression, EQ, mouth noise removal.
5. For sleep, lower energy, soften consonants, avoid dramatic rises, keep ambience stable.
6. For standard, allow more dynamic emphasis but avoid harsh loudness shifts.
7. Create a QA checklist for final audio.

## Output schema

```yaml
audio_spec:
  narrator_persona:
    tone:
    energy:
    warmth:
    authority:
  cadence:
    words_per_minute:
    pause_rules:
    emphasis_rules:
  ambience:
    type:
    source_license:
    volume_relative_to_voice:
    loop_rules:
  processing:
    noise_reduction:
    de_essing:
    compression:
    eq:
    normalization:
  sleep_safety:
    no_sudden_sfx:
    no_loud_cta:
    no_music_swells:
  qa_checklist:
    - check:
```

## Agent prompts

### Audio direction prompt

```text
Create an audio spec for this video. Define narrator persona, cadence, ambience, mix rules, cleanup, and QA. In sleep mode, prioritize low arousal, stable volume, soft consonants, slow pauses, and no sudden effects.
```

## Quality gates

- Audio must be intelligible on phones and gentle on headphones.
- Sleep audio must have no sudden stings or volume jumps.
- Ambience must be licensed or original.
- Voice must match channel voice card.

## Examples

### Sleep audio spec excerpt

WPM: 105–125. Pauses: 0.7–1.5 seconds at section turns. Ambience: rain at -24 to -30 LUFS relative feel, no thunder cracks. CTA: whispered/soft, after early settling period or at end.

## Failure modes

- Using a dramatic trailer voice for sleep content.
- Letting AI voice mispronounce names without QA.
- Using unlicensed ambience loops.
- Adding sudden music cues to create “retention.”
