# Agent Team Orchestration

## Operating thesis

A successful faceless/sleep YouTube operation is not one mega-prompt. It is a conveyor belt of specialized roles. The system should take a market signal, convert it into an original format, write and produce the video, guard against policy risk, and learn from analytics.

## Agent team

```yaml
agent_team:
  market_intelligence_lead:
    skills:
      - yt_outlier_scout
      - competitor_format_miner
      - comment_pain_miner
    cadence: weekly
    output: outlier_board, comment_gap_report

  format_strategist:
    skills:
      - format_engine_selector
      - storytelling_format_selector
      - packaging_scientist
    cadence: per_approved_outlier
    output: format_blueprint

  copy_chief:
    skills:
      - hook_writer
      - standard_faceless_scriptwriter
      - sleep_scriptwriter
      - docuseries_builder
      - explainer_builder
    cadence: per_video
    output: approved_script

  research_editor:
    skills:
      - research_conveyor_belt
      - topic_research_prompt_builder
      - longform_ai_trainer
    cadence: per_video
    output: source_pack, voice_card, script_brief

  production_director:
    skills:
      - visual_production_segmenter
      - visual_contrast_editor
      - voice_audio_director
    cadence: per_video
    output: edit_brief, asset_prompts, audio_spec

  risk_and_policy_editor:
    skills:
      - policy_originality_guard
    cadence: pre_production_and_pre_upload
    output: approve_revise_reject

  publishing_manager:
    skills:
      - upload_metadata_agent
    cadence: per_upload
    output: title, thumbnail_text, description, chapters, pinned_comment

  growth_analyst:
    skills:
      - analytics_diagnosis_agent
      - monetization_expansion_agent
    cadence: 48h_7d_28d_monthly
    output: next_tests, format_updates, monetization_plan

  production_pm:
    skills:
      - production_pm_va_operator
    cadence: continuous
    output: SOPs, hiring_briefs, QA_checklists
```

## Approval flow

```yaml
approval_flow:
  1_market_signal:
    owner: market_intelligence_lead
    must_pass:
      - fresh_outlier_found
      - repeatable_format_detected
      - production_feasible
      - no_direct_copying

  2_format_blueprint:
    owner: format_strategist
    must_pass:
      - viewer_behavior_defined
      - emotional_packaging_defined
      - engine_selected
      - original_angle_defined

  3_script_brief:
    owner: research_editor
    must_pass:
      - factual_material_collected
      - uncertainty_marked
      - tension_bank_present
      - voice_card_present

  4_script:
    owner: copy_chief
    must_pass:
      - first_30_seconds_score_8_plus
      - retention_beats_present
      - title_promise_matched
      - no_generic_ai_tone

  5_policy_review:
    owner: risk_and_policy_editor
    must_pass:
      - materially_original_script
      - varied_substance
      - asset_rights_clear
      - educational_or_narrative_value_clear

  6_production:
    owner: production_director
    must_pass:
      - visual_variation
      - audio_quality
      - sleep_or_standard_pacing_correct
      - no_mismatched_assets

  7_upload:
    owner: publishing_manager
    must_pass:
      - title_thumbnail_hook_alignment
      - accurate_description
      - chapters
      - educational_context_or_sources_when_relevant

  8_iteration:
    owner: growth_analyst
    must_pass:
      - metrics_captured
      - diagnosis_recorded
      - next_test_defined
```

## Cadence

- Daily: one outlier scan, one comment-mining pass, one script or production deliverable.
- Weekly: review 25–50 outliers, approve 3–5 video briefs.
- Monthly: review channel positioning, monetization, and policy risk.
- Quarterly: decide whether to scale, pivot, or kill the channel.
