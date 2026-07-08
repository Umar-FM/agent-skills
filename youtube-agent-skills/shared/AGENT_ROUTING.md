# Agent Routing and Invocation Guide

## Router rule

The orchestrator should classify every request by the **artifact that must change**, not by the user's wording.

| Request symptom | Route first to | Possible secondary route |
|---|---|---|
| “What channel should we make?” | `channel-strategy-architect` | audience, trend, finance, monetization |
| “Find video ideas” | `idea-format-developer` | audience and trend intelligence |
| “Analyze these competitor examples/patterns” | `ai-pattern-mining-analyst` | trend, packaging, title, thumbnail |
| “Build a sleep channel” | `sleep-channel-architect` | strategy, policy, monetization |
| “This topic should work, but how do we frame it?” | `packaging-director` | idea developer |
| “Make a thumbnail” | `thumbnail-art-director` | packaging director |
| “Write titles” | `title-copywriter` | packaging director |
| “Research this topic” | `research-fact-checker` | rights/policy for high-risk claims |
| “Write the script” | `story-retention-scriptwriter`; use `sleep-scriptwriter` for sleep/background-listening scripts | research and packaging must already be locked |
| “Plan visuals” | `faceless-visual-producer` | research and editor |
| “Narrate/mix it” | `voice-sound-producer` | script and editor |
| “Edit for retention” | `retention-video-editor` | script and packaging |
| “Upload/SEO/distribute” | `publishing-seo-distribution` | compliance and community |
| “Turn it into Shorts” | `shorts-repurposing-strategist` | editor and publishing |
| “Why did this video fail?” | `analytics-experimentation-scientist` | route diagnosis to the relevant owner |
| “How do we make money?” | `monetization-revenue-architect` | sponsor sales and finance |
| “Get sponsors” | `sponsorship-affiliate-sales` | monetization, research, compliance |
| “Build community” | `community-audience-development` | strategy and analytics |
| “Is this allowed/safe?” | `rights-policy-brand-safety` | qualified specialist if escalated |
| “Manage the team/calendar” | `production-operations-manager` | orchestrator |
| “Is this profitable?” | `finance-unit-economics` | analytics and monetization |

## Sequential versus parallel work

### Sequential dependencies

- Channel thesis before pillar-level ideation.
- Concept greenlight before packaging lock.
- Packaging lock before script lock.
- Research lock before final factual script.
- Script lock before full asset production.
- Story rough cut before expensive polish.
- Final cut before upload packet lock.
- Publication before performance postmortem.

### Safe parallel work

- Audience research and trend intelligence.
- AI pattern mining after examples are collected and before package/script generation.
- Sleep-channel visual, voice, and metadata standards after the sleep blueprint is approved.
- Thumbnail asset exploration and title generation after the packaging hypotheses exist.
- Visual research and voice preparation after script structure stabilizes.
- Monetization planning and finance modeling after audience intent is clear.
- Community launch planning and Shorts selection while the final cut is reviewed.

## Invocation contract

When invoking a specialist, provide:

```yaml
project_id: <stable id>
current_state: <canonical state>
requested_artifact: <artifact>
locked_inputs:
  - <paths or contents>
open_questions:
  - <question>
constraints:
  budget:
  runtime:
  deadline:
  policy:
success_criteria:
  - <criterion>
```

The specialist should respond with:

```yaml
decision: PASS|RETURN|REJECT|ESCALATE
artifact_path: <path>
primary_rationale: <one paragraph>
assumptions: []
risks: []
next_owner: <skill>
```

## Conflict resolution

- Audience promise conflict: `channel-strategy-architect` recommends; orchestrator decides.
- Packaging versus script conflict: the package cannot lie and the script cannot ignore it; reopen the concept if neither can adapt honestly.
- Retention versus factual nuance: preserve truth; improve structure and visualization rather than removing essential qualification.
- Sponsor versus editorial conflict: editorial and compliance win.
- Quality versus schedule conflict: reduce scope before lowering the quality floor.
- Views versus profit conflict: finance and strategy present the tradeoff; orchestrator chooses based on stage and runway.
