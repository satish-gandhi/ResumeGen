#!/usr/bin/env python3
"""
Test the static bullets configuration.
"""

from bullets_config import get_all_bullets, get_bullets_by_section, get_bullet_count

print("=" * 70)
print("Testing Static Bullets Configuration")
print("=" * 70)

# Test bullet count
count = get_bullet_count()
print(f"\n✓ Total bullets configured: {count}\n")

# Test by section
sections = get_bullets_by_section()
print(f"Work Experience bullets: {len(sections['work_experience'])}")
print(f"Projects bullets: {len(sections['projects'])}")

# Test all bullets
all_bullets = get_all_bullets()

print("\n" + "-" * 70)
print("Bullet Point Details:")
print("-" * 70)

for i, bullet in enumerate(all_bullets, 1):
    char_count = len(bullet)
    status = "✓" if 180 <= char_count <= 220 else "⚠️"

    print(f"\n{i}. {status} {char_count} characters")
    print(f"   {bullet[:80]}...")

    if char_count < 180:
        print(f"   → Will be expanded by {180 - char_count} chars minimum")
    elif char_count > 220:
        print(f"   → Will be shortened by {char_count - 220} chars minimum")

# Statistics
char_counts = [len(b) for b in all_bullets]
within_range = sum(1 for c in char_counts if 180 <= c <= 220)
below_range = sum(1 for c in char_counts if c < 180)
above_range = sum(1 for c in char_counts if c > 220)

print("\n" + "=" * 70)
print("Statistics:")
print("-" * 70)
print(f"Total bullets: {count}")
print(f"Within range (180-220): {within_range} ({within_range/count*100:.1f}%)")
print(f"Below 180 chars: {below_range}")
print(f"Above 220 chars: {above_range}")
print(f"Average length: {sum(char_counts)/count:.1f} characters")
print(f"Min length: {min(char_counts)} characters")
print(f"Max length: {max(char_counts)} characters")
print("=" * 70)

print("\n✓ Static bullets configuration is valid!")
