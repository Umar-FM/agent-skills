#!/usr/bin/env python3
"""Validate the YouTube skill suite structure using only the standard library."""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
errors: list[str] = []

skills = sorted((ROOT / 'skills').glob('*/SKILL.md'))
if not skills:
    errors.append('No skills found')

names: set[str] = set()
for path in skills:
    text = path.read_text(encoding='utf-8')
    match = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not match:
        errors.append(f'{path}: missing YAML-style front matter')
        continue
    fm = match.group(1)
    name_m = re.search(r'^name:\s*(.+)$', fm, re.M)
    desc_m = re.search(r'^description:\s*(.+)$', fm, re.M)
    if not name_m or not desc_m:
        errors.append(f'{path}: front matter needs name and description')
        continue
    name = name_m.group(1).strip()
    if name in names:
        errors.append(f'Duplicate skill name: {name}')
    names.add(name)
    if path.parent.name != name:
        errors.append(f'{path}: folder must match skill name {name}')
    for required in ['# Purpose', '# Workflow', '# Required outputs', '# Quality gate', '# Handoff']:
        if required not in text:
            errors.append(f'{path}: missing section {required}')

for schema in (ROOT / 'shared' / 'schemas').glob('*.json'):
    try:
        json.loads(schema.read_text(encoding='utf-8'))
    except Exception as exc:
        errors.append(f'{schema}: invalid JSON: {exc}')

index_path = ROOT / 'skill-index.json'
try:
    index = json.loads(index_path.read_text(encoding='utf-8'))
    index_names = {x['name'] for x in index['skills']}
    if index_names != names:
        errors.append(f'skill-index mismatch: missing={names-index_names}, extra={index_names-names}')
except Exception as exc:
    errors.append(f'skill-index invalid: {exc}')

manifest = ROOT / 'manifest.txt'
listed = set(manifest.read_text(encoding='utf-8').splitlines()) if manifest.exists() else set()
actual = {str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file() and p.name != 'manifest.txt'}
if listed != actual:
    errors.append(f'manifest mismatch: missing={sorted(actual-listed)[:5]}, extra={sorted(listed-actual)[:5]}')

if errors:
    print('\n'.join(f'ERROR: {e}' for e in errors))
    sys.exit(1)
print(f'OK: {len(skills)} skills, {len(actual)} files validated')
