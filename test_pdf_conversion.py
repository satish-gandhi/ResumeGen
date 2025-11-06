#!/usr/bin/env python3
"""
Test PDF conversion functionality.
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from resume_optimizer.generators.pdf_converter import PDFConverter

print("=" * 70)
print("Testing PDF Conversion")
print("=" * 70)

# Initialize converter
converter = PDFConverter()

# Check if LibreOffice is available
print(f"\nLibreOffice path: {converter.libreoffice_path}")
print(f"PDF conversion available: {converter.is_available()}")

if not converter.is_available():
    print("\n❌ LibreOffice not found!")
    print("\nTo install LibreOffice:")
    print("  Mac: brew install --cask libreoffice")
    print("  Linux: sudo apt-get install libreoffice")
    print("  Windows: Download from https://www.libreoffice.org/")
    sys.exit(1)

# Test conversion with test resume
test_docx = "input/resume.docx"

import os
if not os.path.exists(test_docx):
    print(f"\n⚠️  Test file not found: {test_docx}")
    print("Please ensure you have a resume.docx in the input/ directory")
    sys.exit(1)

print(f"\n✓ LibreOffice found!")
print(f"\nTesting conversion of: {test_docx}")

try:
    pdf_path = converter.convert_to_pdf(test_docx, output_dir="output")
    print(f"\n✓ SUCCESS! PDF created at: {pdf_path}")

    # Check file size
    import os
    size_kb = os.path.getsize(pdf_path) / 1024
    print(f"  PDF size: {size_kb:.1f} KB")

    print("\n" + "=" * 70)
    print("PDF conversion is working correctly!")
    print("=" * 70)

except Exception as e:
    print(f"\n❌ FAILED: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
