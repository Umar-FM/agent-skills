# Skill 20: Policy Originality Guard

```yaml
id: policy_originality_guard
category: risk_policy
inspired_by:
  - YouTube monetization policy
  - Saim safe format-extraction interpretation
  - Wanner sleep-channel safety thread
```

## Purpose

Review videos, channels, scripts, visuals, and metadata for originality, repetition, reused-content, asset, and AI-template risk before production and upload.

## Saim-heavy nuggets embedded

- Extract format logic, not assets or wording.
- Sleep/faceless automation must avoid mass-produced, repetitive, templated content.
- Similar formats can be acceptable only when the substance of each video is materially different.
- Generic AI templates without original insight are high risk.

## Inputs

```yaml
video_package:
  title:
  script:
  visual_plan:
  audio_plan:
  description:
  sources:
  previous_10_uploads:
  asset_licenses:
channel_context:
  niche:
  format:
  upload_cadence:
  monetization_status:
```

## Workflow

1. Check script originality: original narration, commentary, story value, educational value, and source use.
2. Compare against previous 10 uploads for repeated template, repeated substance, repeated visuals, and repeated title formula.
3. Check reused-content risk: third-party clips, readings, compilations, public-domain material, transformations, commentary.
4. Check AI-template risk: generic script, repeated prompts, little variation, no original insight.
5. Check asset rights: music, ambience, stock footage, AI-image terms, archival images, voices.
6. Check metadata accuracy: title, thumbnail, description, chapters, claims.
7. Score risks and issue approve, revise, or reject.
8. List required fixes before publication.

## Output schema

```yaml
policy_review:
  overall_risk: low | medium | high
  decision: approve | revise | reject
  script_originality:
    score_1_10:
    issues:
      - issue:
        fix:
  repetitive_template_risk:
    score_1_10:
    comparison_to_previous_uploads:
      - similarity:
        fix:
  reused_content_risk:
    score_1_10:
    assets_or_segments:
      - asset:
        risk:
        license_or_transformation:
        fix:
  ai_genericity_risk:
    score_1_10:
    issues:
      - issue:
        fix:
  metadata_accuracy:
    score_1_10:
    issues:
      - issue:
        fix:
  required_fixes:
    - priority:
      fix:
  final_notes:
```

## Agent prompts

### Policy review prompt

```text
Review this video package for YouTube originality, repetitive-template, reused-content, AI-genericity, metadata, and asset-rights risk. Compare it to the previous 10 uploads. Decide approve, revise, or reject. If revise or reject, list required fixes. Be stricter with generic AI narration, repeated visuals, repeated templates, readings of material not created by us, and low educational/narrative value.
```

## Quality gates

- Reject if the video is generic AI narration over repetitive visuals with minimal original substance.
- Revise if title promises a claim the script cannot support.
- Revise if factual sleep video has no educational context or source notes.
- Reject if asset rights are unknown for core visuals/audio.
- Approve only when the video is materially original and varied.

## Examples

### High-risk example

100 uploads with the same black screen, same rain loop, same AI voice, same generic story prompt, and titles like “Sleep Story #47.” Decision: reject or heavily revise.

### Lower-risk example

A calm history video with original research, distinct chapters, varied visuals, source notes in the description, licensed ambience, and a unique topic compared with prior uploads. Decision: likely approve after checks.

## Failure modes

- Treating monetization risk as only copyright risk.
- Ignoring similarity across the channel.
- Approving AI scripts because they “sound fine” despite generic substance.
- Assuming public-domain material can be monetized without transformation or context.
