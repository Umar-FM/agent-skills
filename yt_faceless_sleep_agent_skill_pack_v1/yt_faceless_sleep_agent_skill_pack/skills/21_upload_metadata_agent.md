# Skill 21: Upload Metadata Agent

```yaml
id: upload_metadata_agent
category: publishing
inspired_by:
  - Saim packaging workflow
  - Wanner educational-description safety suggestion
  - YouTube monetization policy
```

## Purpose

Create accurate, aligned upload metadata that improves click-through while supporting viewer trust and policy safety.

## Saim-heavy nuggets embedded

- Title, thumbnail, and hook must align.
- For sleep/factual channels, educational descriptions and resources can strengthen authenticity.
- Packaging should not promise what the script does not deliver.

## Inputs

```yaml
video_package:
  title_candidates:
  selected_title:
  thumbnail_concept:
  script_summary:
  chapter_map:
  sources:
  cta_goal:
  channel_voice_card:
mode: standard | sleep
```

## Workflow

1. Validate title accuracy against script.
2. Create description opening that repeats the viewer promise naturally.
3. For factual content, include source/context notes without overloading the viewer.
4. Create chapters based on actual script sections.
5. Create pinned comment that invites useful feedback or next-topic requests.
6. Create tags/keywords only as secondary support.
7. Create a soft CTA for sleep mode or a direct CTA for standard mode.
8. Run metadata through policy/originality guard.

## Output schema

```yaml
metadata_package:
  title:
  thumbnail_text:
  description:
    opening:
    context:
    sources_or_resources:
    cta:
  chapters:
    - timestamp:
      title:
  pinned_comment:
  tags:
    - tag:
  hashtags:
    - hashtag:
  end_screen_plan:
  metadata_accuracy_notes:
```

## Agent prompts

### Metadata prompt

```text
Create upload metadata for this video. Ensure the title, thumbnail, description, chapters, and pinned comment all match the script. For sleep mode, keep the CTA soft and preserve the calming promise. For factual content, include educational context or source notes.
```

## Quality gates

- No metadata claim may exceed the script evidence.
- Chapters must match actual timestamps/sections.
- Sleep descriptions should be calming and clear, not hype-heavy.
- Pinned comment should mine future audience demand.

## Examples

### Sleep description opening

“A calm long-form journey through old roads, quiet cities, and forgotten details from the ancient world. Let the story play softly in the background while you rest, read, or fall asleep.”

## Failure modes

- Keyword-stuffing descriptions.
- Using sensational thumbnail text for a calm video.
- Adding fake sources or vague “research says” claims.
- Using a loud CTA in sleep metadata.
