# Pattern Mining Playbook

Use this when extracting repeatable YouTube structures from outliers, competitors, comments, titles, thumbnails, hooks, or scripts. Copy the operating logic, never the creative work.

## Source posture

Creator advice and public competitor examples are inputs for hypotheses, not authority. Convert them into testable claims about viewer behavior, packaging, retention, production cost, and policy risk.

## Core rules

1. Search for rewarded viewer behavior before naming a niche. A niche is useful only when it describes a repeated viewer state and promise.
2. Treat outliers as market data, not inspiration. Normalize against channel size, upload age, format, and recent baseline where possible.
3. Extract format logic: title structure, thumbnail tension, hook confirmation, emotional trigger, pacing, proof type, CTA placement, and production leverage.
4. Mine comments for unmet demand, not only sentiment. Repeated complaints, skipped details, confusion, and topic requests become backlog candidates.
5. Run a clone-risk check before using generated concepts, titles, hooks, visuals, or script angles.

## Outlier scan fields

```yaml
outlier:
  video_title:
  channel_name:
  subscribers:
  views:
  upload_date:
  video_age_days:
  views_to_subscriber_ratio:
  length:
  production_style:
  title_formula:
  thumbnail_formula:
  first_30_seconds_summary:
  emotional_trigger:
  behavior_loop:
  repeated_format_evidence:
  comment_gap:
  demand_score_1_10:
  repeatability_score_1_10:
  production_cost_score_1_10:
  originality_room_1_10:
  policy_risk_1_10:
```

## Content engines

- **Invisible force:** reveal the hidden system behind an outcome.
- **Domino effect:** show how one small event cascaded into larger consequences.
- **Anti-tutorial:** teach through failures, mistakes, or what not to do.
- **False win:** show why a supposed success created a trap.
- **Polarization:** frame a contested choice, rivalry, or belief.

Choose one dominant engine for a channel or format. A clear engine makes the channel repeatable without making each upload identical.

## Story formats

Use story formats as inventory before drafting:

- origin, rise/fall, before/after, timeline, cause/effect, chain reaction, turning point;
- lesson learned, parallel stories, behind-the-scenes, hidden truth, wrong narrative;
- overlooked variable, real reason, silent factor, unseen system, illusion, misdirection, buried detail, ignored evidence.

## AI-assisted pattern chain

Use model passes to analyze patterns, not to clone competitor output:

1. Clean examples and remove irrelevant metadata.
2. Analyze title structures, trigger words, specificity, emotional promise, and implied story format.
3. Analyze thumbnail descriptions for subject, contrast, implied conflict, text style, and curiosity gap.
4. Analyze first-30-second hooks for click confirmation and next-minute curiosity.
5. Cluster comments into unmet demand, objections, confusion, pacing issues, voice/audio complaints, and repeat-viewing signals.
6. Infer viewer behavior and emotional packaging.
7. Generate original variants using different wording, assets, subjects, and proof.
8. Run clone-risk review against the source examples.

For additional reusable prompts, see [Prompt bank](PROMPT_BANK.md).

## Prompt patterns

```text
Analyze these YouTube titles. Do not create titles yet. Extract recurring structures, trigger words, curiosity gaps, specificity level, emotional promise, and implied story format. Then describe how to create original titles using the same logic without copying wording.
```

```text
Analyze these thumbnail descriptions. Identify visual subject, contrast, emotion, implied conflict, text style, and curiosity gap. Then create original thumbnail concepts using the same tension logic but different imagery and composition.
```

```text
Analyze these comments as market research. Cluster repeated unmet demand, complaints, confusion, skipped details, desired topics, pacing issues, voice/audio complaints, and repeat-viewing signals. Turn each cluster into topic ideas, hook angles, script sections, or production fixes.
```

```text
Compare these generated ideas against the competitor examples. Flag anything too similar in wording, title structure, thumbnail concept, script angle, voice, or visual composition. Rewrite flagged items to preserve viewer behavior while changing creative substance.
```

## Quality gate

PASS only when:

- each transferable pattern names the viewer behavior it serves;
- recommendations use current or date-stamped evidence;
- original variants materially differ in subject, wording, visual composition, and proof;
- policy, rights, and repetitive-template risk are scored before production;
- weak or snippet-only evidence is labeled as directional.
