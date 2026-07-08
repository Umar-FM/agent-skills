# YouTube Agent Skills: Faceless Business Operating System

A modular skills package for running a profitable, faceless YouTube business with specialized agents. The system is optimized for the two creator-controlled performance bottlenecks that most directly shape distribution:

- **Packaging performance:** earning the right click from the right viewer.
- **Viewing performance:** holding attention, delivering the promise, and creating satisfaction.

The suite does **not** optimize CTR or AVD in isolation. Its working north star is **qualified watch time per impression**: a strong package that attracts the intended viewer, followed by a video that keeps and satisfies that viewer. Revenue, originality, policy compliance, and production efficiency are enforced as parallel constraints.

## What is included

- 25 agent skills, each in its own folder.
- A general-manager/orchestrator skill that routes work and enforces stage gates.
- Canonical handoff contracts so agents produce compatible outputs.
- Shared doctrine, metrics, diagnostic trees, policy guardrails, format playbooks, sleep-channel guidance, and pattern-mining guidance.
- Reusable Markdown, CSV, and JSON templates.
- Machine-readable schemas and a skill routing index.
- Standard-library Python tools for validation and metric calculations.
- A worked example for a faceless entertainment-education video.

## Installation

Copy the required folders from `skills/` into the skill directory used by your agent environment. Keep the `shared/` folder beside them so relative references resolve.

Start with these core roles:

1. `youtube-business-orchestrator`
2. `channel-strategy-architect`
3. `idea-format-developer`
4. `packaging-director`
5. `story-retention-scriptwriter`
6. `retention-video-editor`
7. `analytics-experimentation-scientist`
8. `rights-policy-brand-safety`
9. `ai-pattern-mining-analyst` when deriving patterns from examples
10. `sleep-channel-architect` and `sleep-scriptwriter` for sleep or background-listening channels

Add the remaining specialists as production volume and monetization complexity increase.

## Operating sequence

`CHANNEL_THESIS -> IDEA_POOL -> CONCEPT_GREENLIT -> PACKAGING_LOCKED -> RESEARCH_LOCKED -> SCRIPT_LOCKED -> ASSETS_READY -> ROUGH_CUT -> FINAL_CUT -> PUBLISH_READY -> LIVE -> POSTMORTEM -> ITERATION`

No agent may skip a gate merely to maintain a publishing schedule. A late strong video is usually more valuable than an on-time weak video; an efficient system reduces lateness by rejecting weak concepts early.

## Core doctrine

1. **Idea strength sets the ceiling.** Editing cannot rescue a concept nobody wants.
2. **Packaging is a promise.** The first 30 seconds must confirm and begin fulfilling it.
3. **Optimize click-and-watch together.** High CTR with weak viewing is usually a mismatch; high viewing with weak CTR is usually undiscovered value.
4. **Respect the viewer's time.** Remove setup that does not increase comprehension, stakes, emotion, or payoff.
5. **Faceless cannot mean personality-less.** Voice, point of view, visual grammar, humor, taste, and standards must be recognizable.
6. **Efficient cannot mean mass-produced.** Every video must contain materially different substance and original synthesis.
7. **Use evidence hierarchies.** Separate verified fact, reasonable inference, opinion, and creative dramatization.
8. **Measure by surface and audience.** Home, Suggested, Search, Subscriptions, Shorts, and external traffic behave differently.
9. **Monetize the audience's intent, not their trust.** Revenue offers should be congruent with why viewers came.
10. **Every upload is an experiment.** State the hypothesis before publishing and diagnose one primary bottleneck afterward.

## Recommended project folder

For each video, create:

```text
projects/<video-id>/
  00-context/
  01-concept/
  02-packaging/
  03-research/
  04-script/
  05-production/
  06-edit/
  07-publish/
  08-analytics/
  09-revenue/
```

Use the templates in `shared/templates/`, the artifact definitions in `shared/HANDOFF_CONTRACTS.md`, and the sleep/pattern playbooks when those modes apply.

## Current-policy warning

Platform features, monetization thresholds, advertising rules, AI disclosure requirements, and product availability change. The source library was checked on **2026-06-23**, but the policy agent must verify current official YouTube documentation before any consequential publishing or monetization decision.
