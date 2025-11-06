"""
Resume Parser Module
Extracts bullet points from resume Word documents while preserving structure.
"""

from docx import Document
from typing import List, Dict, Tuple
import re


class ResumeParser:
    """Parser for extracting and identifying bullet points from resume documents."""

    def __init__(self, resume_path: str):
        """
        Initialize the parser with a resume document.

        Args:
            resume_path: Path to the resume Word document (.docx)
        """
        self.resume_path = resume_path
        self.document = Document(resume_path)
        self.bullet_points = []

    def is_bullet_point(self, paragraph) -> bool:
        """
        Check if a paragraph is a bullet point.

        Args:
            paragraph: A docx paragraph object

        Returns:
            bool: True if paragraph is a bullet point
        """
        text = paragraph.text.strip()

        # Check for bullet point indicators
        bullet_indicators = ['•', '●', '○', '■', '▪', '-', '*']

        # Check if text starts with bullet or if paragraph has bullet style
        if any(text.startswith(indicator) for indicator in bullet_indicators):
            return True

        # Check paragraph style for list/bullet formatting
        if paragraph.style.name and 'list' in paragraph.style.name.lower():
            return True

        return False

    def is_work_or_project_section(self, text: str) -> bool:
        """
        Check if text indicates start of work experience or projects section.

        Args:
            text: Text to check

        Returns:
            bool: True if text indicates relevant section
        """
        text_lower = text.lower()
        keywords = [
            'work experience', 'professional experience', 'experience',
            'employment', 'career', 'projects', 'technical projects',
            'key projects', 'selected projects'
        ]
        return any(keyword in text_lower for keyword in keywords)

    def extract_bullet_points(self) -> List[Dict]:
        """
        Extract all bullet points from work experience and projects sections.

        Returns:
            List of dicts containing bullet point info with keys:
                - paragraph_index: Index of paragraph in document
                - text: Original text of bullet point
                - section: Section name (if identified)
                - character_count: Length of text
        """
        self.bullet_points = []
        current_section = None
        in_relevant_section = False

        for idx, paragraph in enumerate(self.document.paragraphs):
            text = paragraph.text.strip()

            # Check if we're entering a work/projects section
            if self.is_work_or_project_section(text):
                in_relevant_section = True
                current_section = text
                continue

            # Check if we've left the relevant sections (e.g., entered Education)
            if in_relevant_section and text.lower().startswith(('education', 'skills', 'certifications', 'awards')):
                in_relevant_section = False
                continue

            # Extract bullet points only from relevant sections
            if in_relevant_section and self.is_bullet_point(paragraph):
                # Remove bullet indicator from text
                clean_text = text
                for indicator in ['•', '●', '○', '■', '▪', '-', '*']:
                    if clean_text.startswith(indicator):
                        clean_text = clean_text[1:].strip()
                        break

                bullet_info = {
                    'paragraph_index': idx,
                    'text': clean_text,
                    'section': current_section,
                    'character_count': len(clean_text),
                    'original_paragraph': paragraph
                }
                self.bullet_points.append(bullet_info)

        return self.bullet_points

    def get_document(self) -> Document:
        """
        Get the loaded document object.

        Returns:
            Document: The python-docx Document object
        """
        return self.document

    def get_bullet_points_summary(self) -> str:
        """
        Get a summary of extracted bullet points.

        Returns:
            str: Formatted summary of bullet points
        """
        summary = f"Extracted {len(self.bullet_points)} bullet points:\n\n"

        for i, bp in enumerate(self.bullet_points, 1):
            summary += f"{i}. [{bp['character_count']} chars] {bp['text'][:100]}...\n"

        return summary
