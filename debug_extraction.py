#!/usr/bin/env python3
"""
Debug the extraction process step by step.
"""

from docx import Document
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))
from resume_optimizer.parsers.resume_parser import ResumeParser

print("=" * 70)
print("Debugging Bullet Point Extraction")
print("=" * 70)

doc = Document("input/resume.docx")
parser = ResumeParser("input/resume.docx")

in_relevant_section = False
current_section = None
bullet_count = 0

print("\nStep-by-step paragraph processing:\n")

for idx, paragraph in enumerate(doc.paragraphs):
    text = paragraph.text.strip()
    if not text:
        continue

    # Check if entering work/projects section
    is_work_section = parser.is_work_or_project_section(text)
    if is_work_section:
        in_relevant_section = True
        current_section = text
        print(f"Para {idx}: ENTERING SECTION: {text}")
        print(f"  → in_relevant_section = True\n")
        continue

    # Check if leaving relevant sections
    if in_relevant_section and text.lower().startswith(('education', 'skills', 'certifications', 'awards')):
        print(f"Para {idx}: LEAVING SECTION: {text}")
        print(f"  → in_relevant_section = False\n")
        in_relevant_section = False
        continue

    # Check if it's a bullet point
    is_bullet = parser.is_bullet_point(paragraph)

    if in_relevant_section:
        print(f"Para {idx}: {text[:60]}...")
        print(f"  Style: {paragraph.style.name}")
        print(f"  Is bullet: {is_bullet}")
        print(f"  In section: {current_section}")

        if is_bullet:
            bullet_count += 1
            print(f"  ✓ EXTRACTED as bullet #{bullet_count}")
        else:
            print(f"  ✗ NOT extracted")
        print()

print("=" * 70)
print(f"Total bullets extracted: {bullet_count}")
print("=" * 70)

# Now run the actual parser
print("\nRunning actual parser...")
actual_bullets = parser.extract_bullet_points()
print(f"Actual parser result: {len(actual_bullets)} bullets")
