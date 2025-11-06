#!/usr/bin/env python3
"""
Resume Optimizer - Main Script
Optimizes resume bullet points to align with job descriptions using AI.
Uses static bullet points from bullets_config.py
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from resume_optimizer.parsers.resume_parser import ResumeParser
from resume_optimizer.rewriters.ai_rewriter import AIBulletRewriter
from resume_optimizer.generators.resume_generator import ResumeGenerator
from resume_optimizer.generators.pdf_converter import PDFConverter
from bullets_config import get_all_bullets, get_bullet_count


def read_job_description(job_desc_path: str) -> str:
    """
    Read job description from file.

    Args:
        job_desc_path: Path to job description file (.txt or .docx)

    Returns:
        str: Job description text
    """
    if job_desc_path.endswith('.txt'):
        with open(job_desc_path, 'r', encoding='utf-8') as f:
            return f.read()
    elif job_desc_path.endswith('.docx'):
        from docx import Document
        doc = Document(job_desc_path)
        return '\n'.join([para.text for para in doc.paragraphs])
    else:
        raise ValueError("Job description must be .txt or .docx file")


def main():
    """Main execution function."""
    # Load environment variables
    load_dotenv()

    print("=" * 60)
    print("Resume Optimizer - AI-Powered Bullet Point Customizer")
    print("=" * 60)

    # Configuration
    RESUME_PATH = os.getenv("RESUME_PATH", "input/resume.docx")
    JOB_DESC_PATH = os.getenv("JOB_DESC_PATH", "input/job_description.txt")
    OUTPUT_PATH = os.getenv("OUTPUT_PATH", "output/optimized_resume.docx")
    MIN_CHARS = int(os.getenv("MIN_BULLET_CHARS", "180"))
    MAX_CHARS = int(os.getenv("MAX_BULLET_CHARS", "220"))
    CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-sonnet-4-5-20250929")

    # Validate input files exist
    if not os.path.exists(RESUME_PATH):
        print(f"Error: Resume file not found at: {RESUME_PATH}")
        print("Please place your resume at 'input/resume.docx' or set RESUME_PATH in .env")
        sys.exit(1)

    if not os.path.exists(JOB_DESC_PATH):
        print(f"Error: Job description file not found at: {JOB_DESC_PATH}")
        print("Please place job description at 'input/job_description.txt' or set JOB_DESC_PATH in .env")
        sys.exit(1)

    print(f"\n📄 Resume: {RESUME_PATH}")
    print(f"📋 Job Description: {JOB_DESC_PATH}")
    print(f"📝 Output: {OUTPUT_PATH}")
    print(f"📏 Character Range: {MIN_CHARS}-{MAX_CHARS} per bullet\n")

    # Step 1: Load Static Bullet Points
    print("Step 1/4: Loading static bullet points from config...")
    static_bullets = get_all_bullets()
    print(f"✓ Loaded {len(static_bullets)} bullet points from bullets_config.py\n")

    if len(static_bullets) == 0:
        print("Error: No bullet points found in bullets_config.py")
        print("Please define your bullet points in bullets_config.py")
        sys.exit(1)

    # Parse resume to get paragraph positions (for updating the .docx later)
    parser = ResumeParser(RESUME_PATH)
    parsed_bullets = parser.extract_bullet_points()

    # Create bullet_info dicts from static bullets
    bullet_points = []
    for i, bullet_text in enumerate(static_bullets):
        bullet_info = {
            'text': bullet_text,
            'character_count': len(bullet_text),
            'index': i
        }
        # If we have parsed positions, use them
        if i < len(parsed_bullets):
            bullet_info['paragraph_index'] = parsed_bullets[i]['paragraph_index']
            bullet_info['original_paragraph'] = parsed_bullets[i]['original_paragraph']
        bullet_points.append(bullet_info)

    # Step 2: Read Job Description
    print("Step 2/4: Reading job description...")
    job_description = read_job_description(JOB_DESC_PATH)
    print(f"✓ Loaded job description ({len(job_description)} characters)\n")

    # Step 3: Rewrite Bullet Points
    print("Step 3/4: Rewriting bullet points with AI...")
    print("(This may take a few minutes...)\n")

    try:
        rewriter = AIBulletRewriter(model=CLAUDE_MODEL)
        rewritten_bullets = rewriter.batch_rewrite_with_context(
            bullet_points,
            job_description,
            min_chars=MIN_CHARS,
            max_chars=MAX_CHARS
        )
        print(f"\n✓ Successfully rewrote {len(rewritten_bullets)} bullet points\n")

        # Show summary
        print("Summary of changes:")
        print("-" * 60)
        for i, bullet in enumerate(rewritten_bullets, 1):
            original_len = bullet['character_count']
            new_len = bullet['rewritten_char_count']
            print(f"{i}. {original_len} → {new_len} chars")
            print(f"   Before: {bullet['text'][:80]}...")
            print(f"   After:  {bullet['rewritten_text'][:80]}...")
            print()

    except Exception as e:
        print(f"Error during rewriting: {e}")
        print("\nPlease ensure:")
        print("1. ANTHROPIC_API_KEY is set in .env file")
        print("2. You have internet connection")
        print("3. Your API key is valid and has credits")
        sys.exit(1)

    # Step 4: Save Rewritten Bullets
    print("\nStep 4/4: Saving optimized bullets...")

    # Save to text file for easy copy-paste
    output_txt = OUTPUT_PATH.replace('.docx', '_bullets.txt')
    with open(output_txt, 'w', encoding='utf-8') as f:
        f.write("=" * 70 + "\n")
        f.write("OPTIMIZED RESUME BULLET POINTS\n")
        f.write("=" * 70 + "\n\n")

        for i, bullet in enumerate(rewritten_bullets, 1):
            f.write(f"{i}. [{bullet['rewritten_char_count']} chars]\n")
            f.write(f"   {bullet['rewritten_text']}\n\n")

    print(f"✓ Saved optimized bullets to: {output_txt}")

    # Try to update the resume.docx if structure matches
    docx_created = False
    if len(parsed_bullets) == len(rewritten_bullets):
        try:
            generator = ResumeGenerator(parser.get_document())
            generator.update_bullet_points(rewritten_bullets)
            generator.save(OUTPUT_PATH)
            print(f"✓ Updated resume saved to: {OUTPUT_PATH}")
            docx_created = True
        except Exception as e:
            print(f"⚠️  Could not auto-update resume.docx: {e}")
            print(f"   Please manually copy bullets from: {output_txt}")
    else:
        print(f"⚠️  Resume structure mismatch (config has {len(rewritten_bullets)} bullets, resume has {len(parsed_bullets)})")
        print(f"   Please manually copy bullets from: {output_txt}")

    # Convert to PDF
    output_pdf = OUTPUT_PATH.replace('.docx', '.pdf')
    pdf_created = False

    if docx_created:
        try:
            print(f"\nGenerating PDF from optimized resume...")
            pdf_converter = PDFConverter()

            if not pdf_converter.is_available():
                print(f"⚠️  LibreOffice not found - PDF generation skipped")
                print(f"   Install LibreOffice to enable PDF conversion:")
                print(f"   Mac: brew install --cask libreoffice")
                print(f"   Linux: sudo apt-get install libreoffice")
            else:
                pdf_path = pdf_converter.convert_to_pdf(OUTPUT_PATH)
                print(f"✓ PDF resume saved to: {pdf_path}")
                pdf_created = True
        except Exception as e:
            print(f"⚠️  Could not generate PDF: {e}")
            print(f"   You can manually convert {OUTPUT_PATH} to PDF")

    print("\n" + "=" * 60)
    print("✓ Success! Your optimized bullets are ready.")
    print(f"📁 Bullets file: {output_txt}")
    if os.path.exists(OUTPUT_PATH):
        print(f"📁 Resume file: {OUTPUT_PATH}")
    if pdf_created and os.path.exists(output_pdf):
        print(f"📁 PDF resume: {output_pdf}")
    print("=" * 60)


if __name__ == "__main__":
    main()
