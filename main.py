#!/usr/bin/env python3
"""
Resume Optimizer - Main Script
Optimizes resume bullet points to align with job descriptions using AI.
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

    # Step 1: Parse Resume
    print("Step 1/4: Parsing resume...")
    parser = ResumeParser(RESUME_PATH)
    bullet_points = parser.extract_bullet_points()
    print(f"✓ Extracted {len(bullet_points)} bullet points from work experience and projects\n")

    if len(bullet_points) == 0:
        print("Warning: No bullet points found. Please ensure your resume has bullet points in work experience or projects sections.")
        sys.exit(1)

    # Step 2: Read Job Description
    print("Step 2/4: Reading job description...")
    job_description = read_job_description(JOB_DESC_PATH)
    print(f"✓ Loaded job description ({len(job_description)} characters)\n")

    # Step 3: Rewrite Bullet Points
    print("Step 3/4: Rewriting bullet points with AI...")
    print("(This may take a few minutes...)\n")

    try:
        rewriter = AIBulletRewriter()
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

    # Step 4: Generate Modified Resume
    print("\nStep 4/4: Generating optimized resume...")
    generator = ResumeGenerator(parser.get_document())
    generator.update_bullet_points(rewritten_bullets)
    generator.save(OUTPUT_PATH)

    print("\n" + "=" * 60)
    print("✓ Success! Your optimized resume is ready.")
    print(f"📁 Saved to: {OUTPUT_PATH}")
    print("=" * 60)


if __name__ == "__main__":
    main()
