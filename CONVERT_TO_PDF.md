# Converting Your Optimized Resume to PDF

The Resume Optimizer automatically attempts to generate a PDF version of your optimized resume. However, PDF generation requires LibreOffice to be installed and properly configured.

## Automatic PDF Generation

When you run `python main.py`, the tool will:
1. Create `output/optimized_resume.docx`
2. Automatically convert it to `output/optimized_resume.pdf` (if LibreOffice is available)

### Prerequisites for Automatic PDF Generation

**Mac:**
```bash
brew install --cask libreoffice
```

**Linux:**
```bash
sudo apt-get update
sudo apt-get install libreoffice
```

**Windows:**
- Download and install from https://www.libreoffice.org/

## Manual PDF Conversion (Recommended)

If automatic PDF generation doesn't work or you want more control over the output, use one of these manual methods:

### Method 1: Microsoft Word (Best Quality)
1. Open `output/optimized_resume.docx` in Microsoft Word
2. File → Save As
3. Choose "PDF" as the format
4. Click Save

**Advantages:**
- Preserves all formatting perfectly
- Font rendering matches original
- Professional quality output

### Method 2: Google Docs
1. Go to Google Drive (https://drive.google.com)
2. Upload `output/optimized_resume.docx`
3. Right-click the file → Open with → Google Docs
4. File → Download → PDF Document (.pdf)

**Advantages:**
- Free
- No software installation needed
- Good formatting preservation

### Method 3: LibreOffice (Free, Local)
1. Install LibreOffice (see above)
2. Open `output/optimized_resume.docx` in LibreOffice Writer
3. File → Export as PDF
4. Configure PDF options (quality, compression, etc.)
5. Click Export

**Advantages:**
- Free and open source
- Runs locally
- Good PDF export options

### Method 4: Online Converters (Quick)

Use reputable online converters (be cautious with sensitive information):
- https://www.ilovepdf.com/word_to_pdf
- https://www.adobe.com/acrobat/online/word-to-pdf.html (Adobe official)
- https://cloudconvert.com/docx-to-pdf

**Advantages:**
- No installation needed
- Very fast
- Works on any device

**Disadvantages:**
- Uploads your resume to external servers
- May not preserve complex formatting

## Troubleshooting Automatic PDF Generation

### "LibreOffice not found"
- Install LibreOffice using the commands above
- Restart your terminal after installation
- Verify installation: `which libreoffice` or `which soffice`

### "PDF generation failed"
- The .docx file may have complex formatting that LibreOffice can't handle
- Try Method 1 (Microsoft Word) or Method 2 (Google Docs) for best results

### "source file could not be loaded"
- The document may be corrupted
- Try opening and re-saving the .docx file manually first
- Use an alternative conversion method

## Recommended Workflow

For best results, we recommend:

1. Run the optimizer: `python main.py`
2. Review `output/optimized_resume_bullets.txt`
3. If automatic PDF generation fails, manually convert using Microsoft Word or Google Docs
4. Always review the final PDF to ensure formatting is correct

## Quality Checklist

Before sending your PDF resume:
- [ ] All bullet points are visible and properly formatted
- [ ] No text is cut off or overflowing
- [ ] Font sizes and styles match the original
- [ ] Page breaks are in the correct places (should be 1 page)
- [ ] Contact information is accurate and clickable (if applicable)
- [ ] File size is reasonable (< 1 MB)

## Tips for Perfect PDF Output

1. **Use standard fonts** in your resume.docx (Arial, Calibri, Times New Roman)
2. **Keep it simple** - complex formatting may not convert well
3. **Test the PDF** by opening it in multiple PDF readers
4. **Check on mobile** - ensure it's readable on phones/tablets
5. **Verify links** - make sure email and LinkedIn links work (if included)

## Still Having Issues?

If PDF generation continues to fail:
1. The optimized bullets are always saved to `output/optimized_resume_bullets.txt`
2. You can copy these bullets and paste them into your original resume
3. Then convert your resume to PDF using your preferred method

This workflow ensures you always have access to the optimized content, regardless of PDF generation issues.
