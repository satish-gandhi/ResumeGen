#!/usr/bin/env python3
"""
Demo the new structured output format.
"""

from bullets_config import get_structured_bullets

print("=" * 80)
print("DEMO: New Structured Output Format")
print("=" * 80)
print()

structured_data = get_structured_bullets()

# Show work experience format
work_exp_num = 1
for work in structured_data['work_experience']:
    print(f"WORK EXPERIENCE #{work_exp_num}: {work['company']}")
    print(f"{work['title']} | {work['dates']}")
    print("-" * 80)

    for bullet in work['bullets']:
        print(f"• {bullet}")
        print(f"  [{len(bullet)} chars]")
        print()

    work_exp_num += 1
    print()

# Show projects format
project_num = 1
for project in structured_data['projects']:
    print(f"PROJECT #{project_num}: {project['name']}")
    print("-" * 80)

    for bullet in project['bullets']:
        print(f"• {bullet}")
        print(f"  [{len(bullet)} chars]")
        print()

    project_num += 1
    print()

print("=" * 80)
print("✓ This is how your output file will be organized!")
print("  After running main.py, each bullet will be optimized for the job description.")
print("=" * 80)
