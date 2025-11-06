# Example Files

This directory contains example files to help you get started with Resume Optimizer.

## Files

- `sample_job_description.txt` - Example job description for a Senior Software Engineer role
- `sample_resume.docx` - Example resume template (create your own based on this format)

## How to Use Examples

### Quick Test

1. Copy the sample job description to the input folder:
```bash
cp examples/sample_job_description.txt input/job_description.txt
```

2. Create your own `input/resume.docx` based on the format guidelines in the main README

3. Run the optimizer:
```bash
python main.py
```

## Creating Your Resume Template

Your resume should follow this structure for best results:

### Recommended Format

```
[Your Name]
[Contact Information]

PROFESSIONAL SUMMARY
[Brief summary of your experience]

WORK EXPERIENCE

Company Name | Job Title | Date Range
• [Bullet point describing achievement or responsibility]
• [Another bullet point with quantifiable results]
• [More bullet points...]

Another Company | Job Title | Date Range
• [Bullet points...]

PROJECTS

Project Name | Technologies Used
• [Bullet describing the project and your contribution]
• [Impact and results achieved]

SKILLS
[List of skills by category]

EDUCATION
[Degree, Institution, Year]
```

### Important Notes

1. **Use bullet points** for work experience and projects (•, -, *, etc.)
2. **Section headers** should include keywords like:
   - Work Experience / Professional Experience / Experience
   - Projects / Technical Projects / Key Projects
3. **Consistent formatting** throughout the document
4. **One page** is recommended for best results

## Tips for Job Descriptions

For best optimization results, your job description should include:

- Required technical skills and technologies
- Desired experience levels
- Key responsibilities
- Preferred qualifications
- Team/company context

The more detailed your job description, the better the AI can tailor your bullet points!
