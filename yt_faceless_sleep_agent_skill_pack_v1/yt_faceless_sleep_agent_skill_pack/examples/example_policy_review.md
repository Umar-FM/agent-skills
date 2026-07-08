# Example Policy Review

```yaml
policy_review:
  video_title: Fall Asleep to the Quiet Mysteries of Ancient Roads
  reviewer: policy_originality_guard
  review_date: 2026-07-07
  overall_risk: low_medium
  decision: revise
  script_originality:
    score_1_10: 8
    notes: Original narration and distinct chapter plan. Some generic AI phrasing appears in transitions.
    required_fixes:
      - Replace repeated phrase “throughout history” with specific transitions.
      - Add source note for Roman road maintenance claims.
  repetitive_template_risk:
    score_1_10: 4
    similar_to_previous_uploads:
      - similarity: same rain-library intro as last 3 uploads
        fix: vary opening scene to moonlit road and map table
  reused_content_risk:
    score_1_10: 3
    third_party_assets:
      - asset: archival map image
        license: public_domain_claimed
        transformation_or_commentary: used with narration explaining map context
        risk: verify source page/license before upload
  ai_genericity_risk:
    score_1_10: 5
    generic_sections:
      - section: chapter transitions
        fix: rewrite with specific sensory/subject-linked transitions
  metadata_accuracy:
    score_1_10: 8
    title_claims_supported: true
    thumbnail_claims_supported: true
  asset_rights:
    music: none
    ambience: licensed rain loop
    visuals: mixed AI-generated and public-domain pending license verification
    voice: licensed AI voice plan
  final_required_fixes:
    - Verify public-domain map licenses.
    - Add educational source/context notes to description.
    - Rewrite repeated transitions.
    - Vary intro visual from previous uploads.
  final_notes: Approve after revisions.
```
