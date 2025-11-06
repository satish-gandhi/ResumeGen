"""
PDF Converter Module
Converts Word documents to PDF while preserving formatting.
"""

import os
import subprocess
import shutil
from pathlib import Path


class PDFConverter:
    """Converts .docx files to PDF using LibreOffice."""

    def __init__(self):
        """Initialize the PDF converter and check for LibreOffice."""
        self.libreoffice_path = self._find_libreoffice()

    def _find_libreoffice(self):
        """
        Find LibreOffice executable on the system.

        Returns:
            str: Path to LibreOffice executable or None if not found
        """
        # Common LibreOffice locations
        possible_paths = [
            'libreoffice',  # Linux/Mac (in PATH)
            'soffice',      # Alternative name
            '/usr/bin/libreoffice',  # Linux
            '/usr/bin/soffice',      # Linux alternative
            '/Applications/LibreOffice.app/Contents/MacOS/soffice',  # Mac
            'C:\\Program Files\\LibreOffice\\program\\soffice.exe',  # Windows
            'C:\\Program Files (x86)\\LibreOffice\\program\\soffice.exe',  # Windows 32-bit
        ]

        for path in possible_paths:
            if shutil.which(path) or os.path.exists(path):
                return path

        return None

    def is_available(self):
        """
        Check if PDF conversion is available.

        Returns:
            bool: True if LibreOffice is available
        """
        return self.libreoffice_path is not None

    def convert_to_pdf(self, docx_path: str, output_dir: str = None) -> str:
        """
        Convert a .docx file to PDF.

        Args:
            docx_path: Path to the .docx file
            output_dir: Directory to save the PDF (default: same as docx)

        Returns:
            str: Path to the generated PDF file

        Raises:
            FileNotFoundError: If LibreOffice is not installed
            RuntimeError: If conversion fails
        """
        if not self.is_available():
            raise FileNotFoundError(
                "LibreOffice is not installed. Please install LibreOffice to enable PDF conversion:\n"
                "  Mac: brew install --cask libreoffice\n"
                "  Linux: sudo apt-get install libreoffice\n"
                "  Windows: Download from https://www.libreoffice.org/"
            )

        if not os.path.exists(docx_path):
            raise FileNotFoundError(f"Input file not found: {docx_path}")

        # Determine output directory
        if output_dir is None:
            output_dir = os.path.dirname(docx_path)

        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Get absolute paths
        abs_docx_path = os.path.abspath(docx_path)
        abs_output_dir = os.path.abspath(output_dir)

        # Build LibreOffice command
        # --headless: run without GUI
        # --convert-to pdf: convert to PDF format
        # --outdir: specify output directory
        cmd = [
            self.libreoffice_path,
            '--headless',
            '--convert-to',
            'pdf',
            '--outdir',
            abs_output_dir,
            abs_docx_path
        ]

        try:
            # Run LibreOffice conversion
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode != 0:
                raise RuntimeError(
                    f"PDF conversion failed:\n"
                    f"Command: {' '.join(cmd)}\n"
                    f"Error: {result.stderr}"
                )

            # Determine output PDF path
            docx_filename = os.path.basename(abs_docx_path)
            pdf_filename = docx_filename.rsplit('.', 1)[0] + '.pdf'
            pdf_path = os.path.join(abs_output_dir, pdf_filename)

            if not os.path.exists(pdf_path):
                raise RuntimeError(
                    f"PDF file was not created at expected location: {pdf_path}"
                )

            return pdf_path

        except subprocess.TimeoutExpired:
            raise RuntimeError("PDF conversion timed out after 30 seconds")
        except Exception as e:
            raise RuntimeError(f"PDF conversion failed: {e}")

    def convert_multiple(self, docx_paths: list, output_dir: str = None) -> list:
        """
        Convert multiple .docx files to PDF.

        Args:
            docx_paths: List of paths to .docx files
            output_dir: Directory to save PDFs (default: same as each docx)

        Returns:
            list: List of paths to generated PDF files
        """
        pdf_paths = []
        for docx_path in docx_paths:
            try:
                pdf_path = self.convert_to_pdf(docx_path, output_dir)
                pdf_paths.append(pdf_path)
            except Exception as e:
                print(f"Warning: Failed to convert {docx_path}: {e}")

        return pdf_paths
