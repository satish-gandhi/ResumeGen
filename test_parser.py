#!/usr/bin/env python3
"""
Test the resume parser with the created resume.
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from resume_optimizer.parsers.resume_parser import ResumeParser

# Parse the resume
print("=" * 70)
print("Testing Resume Parser")
print("=" * 70)

parser = ResumeParser("input/resume.docx")
bullet_points = parser.extract_bullet_points()

print(f"\n✓ Extracted {len(bullet_points)} bullet points\n")

# Show details
print("Bullet Point Analysis:")
print("-" * 70)

for i, bp in enumerate(bullet_points, 1):
    char_count = bp['character_count']
    status = "✓" if 180 <= char_count <= 220 else "⚠️"

    print(f"\n{i}. {status} {char_count} characters")
    print(f"   Section: {bp['section']}")
    print(f"   Text: {bp['text'][:100]}...")

    if char_count < 180:
        print(f"   → Too short by {180 - char_count} characters")
    elif char_count > 220:
        print(f"   → Too long by {char_count - 220} characters")

# Statistics
char_counts = [bp['character_count'] for bp in bullet_points]
within_range = sum(1 for c in char_counts if 180 <= c <= 220)
below_range = sum(1 for c in char_counts if c < 180)
above_range = sum(1 for c in char_counts if c > 220)

print("\n" + "=" * 70)
print("Statistics:")
print("-" * 70)
print(f"Total bullets: {len(bullet_points)}")
print(f"Within range (180-220): {within_range} ({within_range/len(bullet_points)*100:.1f}%)")
print(f"Below 180 chars: {below_range}")
print(f"Above 220 chars: {above_range}")
print(f"Average length: {sum(char_counts)/len(char_counts):.1f} characters")
print(f"Min length: {min(char_counts)} characters")
print(f"Max length: {max(char_counts)} characters")
print("=" * 70)
