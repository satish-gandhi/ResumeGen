# Resume Optimizer

AI-powered resume customizer that tailors your resume bullet points to match specific job descriptions while maintaining your original resume format and keeping everything within one page.

## Features

- **Smart Bullet Point Rewriting**: Uses Claude AI to rewrite work experience and project bullet points to align with target job descriptions
- **Format Preservation**: Maintains exact formatting, styling, and layout of your original resume
- **Character Control**: Ensures each bullet point stays between 180-220 characters to prevent page overflow
- **Selective Updates**: Only modifies bullet points in work experience and projects sections, leaving other sections untouched
- **Batch Processing**: Processes all bullet points efficiently while showing progress

## How It Works

1. **Parse**: Extracts bullet points from your resume's work experience and projects sections
2. **Analyze**: Reads the target job description
3. **Optimize**: Uses AI to rewrite each bullet point to highlight relevant skills and achievements
4. **Generate**: Creates a new resume with optimized bullets while preserving original formatting

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

1. Place your resume in the `input/` directory as `resume.docx`
2. Place the job description in `input/job_description.txt` (or `.docx`)
3. Run the optimizer:

```bash
python main.py
```

4. Your optimized resume will be saved to `output/optimized_resume.docx`

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

## Project Structure

```
ResumeGen/
├── main.py                          # Main execution script
├── requirements.txt                 # Python dependencies
├── .env.example                     # Environment variables template
├── README.md                        # This file
├── input/                           # Input files directory
│   ├── resume.docx                  # Your original resume
│   └── job_description.txt          # Target job description
├── output/                          # Generated resumes
│   └── optimized_resume.docx        # AI-optimized resume
├── examples/                        # Example files
│   ├── sample_resume.docx
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

## How to Prepare Your Resume

For best results:

1. **Use a Word document** (`.docx` format)
2. **Include clear section headers** like "Work Experience", "Projects", "Professional Experience"
3. **Use bullet points** for achievements (•, -, *, etc.)
4. **Keep formatting consistent** throughout your resume
5. **One page format** - the tool helps maintain this by controlling bullet length

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

### "No bullet points found"
- Ensure your resume has bullet points in "Work Experience" or "Projects" sections
- Check that section headers contain keywords like "experience", "projects", "employment"

### "API key error"
- Verify your `ANTHROPIC_API_KEY` is set correctly in `.env`
- Ensure you have credits in your Anthropic account

### "Character count warnings"
- The tool automatically adjusts bullets to fit 180-220 character range
- If you see warnings, the AI will retry to meet the constraints

### "Format looks different"
- The tool preserves most formatting, but complex styling may need manual adjustment
- Check that your original resume uses standard Word formatting

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
