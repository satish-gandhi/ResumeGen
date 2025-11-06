"""
Resume Generator Module
Writes modified bullet points back to resume while preserving exact formatting.
"""

from docx import Document
from typing import List, Dict
import os
from copy import deepcopy


class ResumeGenerator:
    """Generates modified resume with updated bullet points while preserving formatting."""

    def __init__(self, original_document: Document):
        """
        Initialize the generator with the original document.

        Args:
            original_document: The original python-docx Document object
        """
        self.document = original_document

    def update_bullet_points(self, bullet_points: List[Dict]) -> None:
        """
        Update bullet points in the document with rewritten text.

        Args:
            bullet_points: List of bullet point dicts containing:
                - paragraph_index: Index of paragraph in document
                - rewritten_text: New text to use
                - original_paragraph: Original paragraph object
        """
        for bullet in bullet_points:
            if 'rewritten_text' not in bullet:
                continue

            para_idx = bullet['paragraph_index']
            paragraph = self.document.paragraphs[para_idx]

            # Get the bullet indicator from original text
            original_text = paragraph.text.strip()
            bullet_char = '•'  # Default

            # Detect original bullet character
            for char in ['•', '●', '○', '■', '▪', '-', '*']:
                if original_text.startswith(char):
                    bullet_char = char
                    break

            # Preserve paragraph formatting
            # Clear existing runs but keep paragraph formatting
            for run in paragraph.runs:
                run.text = ''

            # Add new text with bullet indicator
            new_text = f"{bullet_char} {bullet['rewritten_text']}"

            # Create new run with original formatting
            if paragraph.runs:
                # Use formatting from first run
                new_run = paragraph.runs[0]
                new_run.text = new_text
            else:
                # Create new run if none exist
                paragraph.add_run(new_text)

    def save(self, output_path: str) -> None:
        """
        Save the modified document to a file.

        Args:
            output_path: Path where to save the modified resume
        """
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        self.document.save(output_path)
        print(f"Modified resume saved to: {output_path}")

    def get_document(self) -> Document:
        """
        Get the document object.

        Returns:
            Document: The python-docx Document object
        """
        return self.document

    @staticmethod
    def create_from_template(template_path: str, output_path: str, bullet_points: List[Dict]) -> 'ResumeGenerator':
        """
        Create a generator from a template file and immediately update it.

        Args:
            template_path: Path to template resume
            output_path: Path to save modified resume
            bullet_points: List of bullet points with rewritten_text

        Returns:
            ResumeGenerator: Generator instance with updated document
        """
        # Load the template
        doc = Document(template_path)

        # Create generator
        generator = ResumeGenerator(doc)

        # Update bullet points
        generator.update_bullet_points(bullet_points)

        # Save
        generator.save(output_path)

        return generator
