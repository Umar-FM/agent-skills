# Skill 24: Production PM / VA Operator

```yaml
id: production_pm_va_operator
category: operations
inspired_by:
  - Saim broke-guide/systemization notes
  - Saim YouTube automation as systems
```

## Purpose

Turn the skills into repeatable SOPs for a solo operator, VA team, or agent team. Learn the roles manually once, then automate or delegate.

## Saim-heavy nuggets embedded

- Do every role yourself once before automating or hiring.
- YouTube automation is a system: idea, script, edit, upload, analytics, revenue.
- Trade time for leverage early; buy back time after the process is understood.
- Foundation matters more than trying to master everything in 30 days.

## Inputs

```yaml
operation_stage: solo | first_va | small_team | agent_team | scaling
weekly_video_target: integer
budget_per_video: number
team_members:
  - role:
current_sops:
  - sop:
quality_issues:
  - issue:
```

## Workflow

1. Map the full production chain: outlier research, brief, research, packaging, script, policy, visuals, audio, edit, upload, analytics.
2. Identify which steps the operator has personally completed at least once.
3. Create SOPs for each step with inputs, outputs, quality gates, and owner.
4. Define handoff formats between agents/people.
5. Define QA checklists and escalation rules.
6. Decide what to delegate next based on bottleneck, not preference.
7. Create hiring/test tasks for VAs, researchers, editors, and scriptwriters.
8. Measure production cost, cycle time, revision count, and performance outcome.

## Output schema

```yaml
ops_plan:
  stage:
  production_chain:
    - step:
      owner:
      input:
      output:
      quality_gate:
      sop_link:
  manual_experience_check:
    - step:
      operator_has_done_once: true | false
      action:
  bottlenecks:
    - bottleneck:
      evidence:
      fix:
  delegation_plan:
    - role:
      task:
      test_assignment:
      qa_criteria:
  weekly_cadence:
    monday:
    tuesday:
    wednesday:
    thursday:
    friday:
  metrics:
    - metric:
```

## Agent prompts

### Production system prompt

```text
Build an SOP and delegation plan for this YouTube operation. Map every step from outlier research to analytics. Identify which steps the operator must do manually once before delegating. Recommend what to automate or hire next based on bottlenecks and quality risk.
```

## Quality gates

- Every handoff must have a clear input and output.
- No role should receive a vague task like “make it better.”
- QA owner must be separate from creator where possible.
- Policy review cannot be skipped to hit upload cadence.

## Examples

### First VA task

Ask VA to fill 20 rows of the outlier board with title, channel, views, subs, upload age, length, thumbnail summary, first 30-second summary, and comment gaps. Grade accuracy before giving creative decisions.

## Failure modes

- Hiring before understanding the task.
- Delegating strategy to low-context assistants.
- No QA checklist.
- Optimizing production volume before finding a format that works.
