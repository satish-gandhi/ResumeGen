# Resume Optimizer

AI-powered resume customizer that tailors your resume bullet points to match specific job descriptions while maintaining your original resume format and keeping everything within one page.

## Features

- **Smart Bullet Point Rewriting**: Uses Claude AI to rewrite work experience and project bullet points to align with target job descriptions
- **Format Preservation**: Maintains exact formatting, styling, and layout of your original resume
- **Character Control**: Ensures each bullet point stays between 180-220 characters to prevent page overflow
- **Selective Updates**: Only modifies bullet points in work experience and projects sections, leaving other sections untouched
- **Batch Processing**: Processes all bullet points efficiently while showing progress
- **PDF Output**: Automatically generates PDF version (requires LibreOffice) or provides manual conversion options

## How It Works

1. **Configure**: Define your resume bullet points once in `bullets_config.py`
2. **Analyze**: Reads the target job description
3. **Optimize**: Uses AI to rewrite each bullet point to highlight relevant skills and achievements
4. **Output**: Generates three files:
   - `optimized_resume_bullets.txt` - Optimized bullets (copy-paste ready)
   - `optimized_resume.docx` - Updated Word document (if structure matches)
   - `optimized_resume.pdf` - PDF version (if LibreOffice is available)

## Installation

### Prerequisites

- Python 3.8 or higher
- An Anthropic API key ([Get one here](https://console.anthropic.com/))

### Setup

1. Clone this repository:
```bash
git clone <repository-url>
cd ResumeGen
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
```bash
cp .env.example .env
```

4. Edit `.env` and add your Anthropic API key:
```
ANTHROPIC_API_KEY=your_actual_api_key_here
```

## Usage

### Basic Usage

1. **Configure your bullet points** (one-time setup):
   - Edit `bullets_config.py`
   - Add your resume bullet points to `WORK_EXPERIENCE_BULLETS` and `PROJECTS_BULLETS`
   - Save the file

2. **Add job description**:
   - Place the job description in `input/job_description.txt` (or `.docx`)

3. **Run the optimizer**:
   ```bash
   python main.py
   ```

4. **Get your optimized resume**:
   - `output/optimized_resume_bullets.txt` - Copy-paste ready bullets
   - `output/optimized_resume.docx` - Updated Word document (if successful)
   - `output/optimized_resume.pdf` - PDF version (if LibreOffice available)
   - See [CONVERT_TO_PDF.md](CONVERT_TO_PDF.md) for manual PDF conversion options

### Custom Paths

You can specify custom paths in your `.env` file:

```env
RESUME_PATH=path/to/your/resume.docx
JOB_DESC_PATH=path/to/job_description.txt
OUTPUT_PATH=path/to/output_resume.docx
```

### Character Limits

Adjust bullet point length constraints in `.env`:

```env
MIN_BULLET_CHARS=180
MAX_BULLET_CHARS=220
```

These limits ensure your resume stays within one page while maintaining impactful content.

### Configuring Your Bullet Points

The `bullets_config.py` file contains your static bullet points. Edit this file to match your resume:

```python
# Work Experience Bullets
WORK_EXPERIENCE_BULLETS = [
    "Your first work experience bullet point here",
    "Your second work experience bullet point here",
    # ... add all your work experience bullets
]

# Projects Bullets
PROJECTS_BULLETS = [
    "Your first project bullet point here",
    "Your second project bullet point here",
    # ... add all your project bullets
]
```

**Tips:**
- Add bullets in the exact order they appear in your resume
- Each bullet should be a complete string (no bullet characters like • or -)
- You can organize with comments to mark different companies/projects
- Run `python test_static_bullets.py` to verify your configuration

## Project Structure

```
ResumeGen/
├── main.py                          # Main execution script
├── bullets_config.py                # Your static bullet points (EDIT THIS!)
├── test_static_bullets.py           # Test your bullet configuration
├── requirements.txt                 # Python dependencies
├── .env.example                     # Environment variables template
├── README.md                        # This file
├── input/                           # Input files directory
│   ├── resume.docx                  # Your resume template (optional)
│   └── job_description.txt          # Target job description
├── output/                          # Generated output
│   ├── optimized_resume_bullets.txt # Optimized bullets (copy-paste ready)
│   └── optimized_resume.docx        # Auto-updated resume (if possible)
├── examples/                        # Example files
│   └── sample_job_description.txt
└── src/
    └── resume_optimizer/
        ├── parsers/                 # Resume parsing modules
        │   └── resume_parser.py
        ├── rewriters/               # AI rewriting modules
        │   └── ai_rewriter.py
        └── generators/              # Resume generation modules
            └── resume_generator.py
```

## Quick Start

1. **Edit `bullets_config.py`** with your resume bullet points
2. **Test your config**: `python test_static_bullets.py`
3. **Add your API key** to `.env` file
4. **Add job description** to `input/job_description.txt`
5. **Run optimizer**: `python main.py`
6. **Copy optimized bullets** from `output/optimized_resume_bullets.txt`

## Configuration Options

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `ANTHROPIC_API_KEY` | Your Anthropic API key (required) | None |
| `RESUME_PATH` | Path to your resume | `input/resume.docx` |
| `JOB_DESC_PATH` | Path to job description | `input/job_description.txt` |
| `OUTPUT_PATH` | Output path for optimized resume | `output/optimized_resume.docx` |
| `MIN_BULLET_CHARS` | Minimum characters per bullet | 180 |
| `MAX_BULLET_CHARS` | Maximum characters per bullet | 220 |

## Examples

### Before Optimization
```
• Developed web application using Python and JavaScript for client projects
```

### After Optimization (for a Backend Engineer role)
```
• Architected and deployed scalable Python-based microservices handling 100K+ daily requests, implementing RESTful APIs and optimizing database queries to reduce response time by 40% for enterprise clients
```

## Troubleshooting

### "No bullet points found in bullets_config.py"
- Make sure you've edited `bullets_config.py` with your actual resume bullets
- Check that `WORK_EXPERIENCE_BULLETS` and `PROJECTS_BULLETS` lists are not empty
- Run `python test_static_bullets.py` to verify your configuration

### "API key error"
- Verify your `ANTHROPIC_API_KEY` is set correctly in `.env`
- Ensure you have credits in your Anthropic account

### "Character count warnings"
- The tool automatically adjusts bullets to fit 180-220 character range
- If you see warnings, the AI will retry to meet the constraints

### "Format looks different"
- The tool preserves most formatting, but complex styling may need manual adjustment
- Check that your original resume uses standard Word formatting

### PDF Generation Issues
- **LibreOffice not found**: Install LibreOffice for automatic PDF generation
  - Mac: `brew install --cask libreoffice`
  - Linux: `sudo apt-get install libreoffice`
- **PDF generation failed**: Use manual conversion methods (see [CONVERT_TO_PDF.md](CONVERT_TO_PDF.md))
  - Recommended: Open .docx in Microsoft Word → Save as PDF
  - Alternative: Use Google Docs or online converters
- The optimized bullets are always saved to `.txt` file regardless of PDF generation

## Advanced Usage

### Using as a Library

You can import and use the modules programmatically:

```python
from resume_optimizer.parsers.resume_parser import ResumeParser
from resume_optimizer.rewriters.ai_rewriter import AIBulletRewriter
from resume_optimizer.generators.resume_generator import ResumeGenerator

# Parse resume
parser = ResumeParser("path/to/resume.docx")
bullets = parser.extract_bullet_points()

# Rewrite bullets
rewriter = AIBulletRewriter(api_key="your-key")
job_desc = "Your job description here..."
rewritten = rewriter.batch_rewrite_with_context(bullets, job_desc)

# Generate new resume
generator = ResumeGenerator(parser.get_document())
generator.update_bullet_points(rewritten)
generator.save("output.docx")
```

## Cost Considerations

- The tool uses Claude 3.5 Sonnet by default
- Cost depends on number of bullet points (typically $0.10-0.50 per resume)
- Each bullet point requires 1-2 API calls
- See [Anthropic pricing](https://www.anthropic.com/api) for details

## Privacy & Security

- Your resume and job descriptions are processed locally
- Only bullet point text is sent to Anthropic's API for rewriting
- No data is stored by the API after processing
- Sensitive files are excluded from git via `.gitignore`

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

MIT License - see LICENSE file for details

## Support

For issues or questions:
1. Check existing GitHub issues
2. Review troubleshooting section above
3. Create a new issue with details about your problem

## Acknowledgments

- Built with [python-docx](https://python-docx.readthedocs.io/) for Word document handling
- Powered by [Anthropic Claude](https://www.anthropic.com/) for intelligent text rewriting
