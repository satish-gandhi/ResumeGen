"""
AI-Powered Bullet Point Rewriter Module
Uses Claude AI to rewrite resume bullet points to align with job descriptions.
"""

from anthropic import Anthropic
from typing import List, Dict
import os


class AIBulletRewriter:
    """Rewrites resume bullet points using Claude AI to match job descriptions."""

    def __init__(self, api_key: str = None, model: str = "claude-3-5-sonnet-20240620"):
        """
        Initialize the AI rewriter.

        Args:
            api_key: Anthropic API key (if None, reads from ANTHROPIC_API_KEY env var)
            model: Claude model to use (default: claude-3-5-sonnet-20240620)
        """
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("API key must be provided or set in ANTHROPIC_API_KEY environment variable")

        self.client = Anthropic(api_key=self.api_key)
        self.model = model

    def rewrite_bullet_points(
        self,
        bullet_points: List[str],
        job_description: str,
        min_chars: int = 180,
        max_chars: int = 220
    ) -> List[str]:
        """
        Rewrite all bullet points to align with job description.

        Args:
            bullet_points: List of original bullet points
            job_description: Target job description
            min_chars: Minimum character count per bullet
            max_chars: Maximum character count per bullet

        Returns:
            List of rewritten bullet points
        """
        rewritten = []

        for i, bullet in enumerate(bullet_points):
            print(f"Rewriting bullet point {i + 1}/{len(bullet_points)}...")
            rewritten_bullet = self.rewrite_single_bullet(
                bullet, job_description, min_chars, max_chars
            )
            rewritten.append(rewritten_bullet)

        return rewritten

    def rewrite_single_bullet(
        self,
        bullet_text: str,
        job_description: str,
        min_chars: int = 180,
        max_chars: int = 220
    ) -> str:
        """
        Rewrite a single bullet point to align with job description.

        Args:
            bullet_text: Original bullet point text
            job_description: Target job description
            min_chars: Minimum character count
            max_chars: Maximum character count

        Returns:
            Rewritten bullet point text
        """
        prompt = f"""You are an expert resume writer. Your task is to rewrite the following resume bullet point to better align with the provided job description while maintaining truthfulness and impact.

Original Bullet Point:
{bullet_text}

Job Description:
{job_description}

Requirements:
1. The rewritten bullet point MUST be between {min_chars} and {max_chars} characters (including spaces)
2. Highlight skills, technologies, and achievements that align with the job description
3. Use strong action verbs and quantifiable metrics where possible
4. Maintain the truthfulness of the original accomplishment - do not fabricate details
5. Make it compelling and relevant to the target role
6. Return ONLY the rewritten bullet point text, nothing else

Rewritten Bullet Point:"""

        message = self.client.messages.create(
            model=self.model,
            max_tokens=300,
            messages=[{"role": "user", "content": prompt}]
        )

        rewritten = message.content[0].text.strip()

        # Validate character count
        if len(rewritten) < min_chars or len(rewritten) > max_chars:
            # Retry with explicit character count emphasis
            rewritten = self._retry_with_char_limit(
                bullet_text, job_description, min_chars, max_chars, len(rewritten)
            )

        return rewritten

    def _retry_with_char_limit(
        self,
        bullet_text: str,
        job_description: str,
        min_chars: int,
        max_chars: int,
        current_length: int
    ) -> str:
        """
        Retry rewriting with explicit character count correction.

        Args:
            bullet_text: Original bullet point
            job_description: Job description
            min_chars: Minimum characters
            max_chars: Maximum characters
            current_length: Length of previous attempt

        Returns:
            Corrected bullet point
        """
        if current_length < min_chars:
            instruction = f"expand it to be at least {min_chars} characters"
        else:
            instruction = f"shorten it to be at most {max_chars} characters"

        prompt = f"""You are an expert resume writer. Rewrite the following bullet point to align with the job description.

Original Bullet Point:
{bullet_text}

Job Description:
{job_description}

CRITICAL REQUIREMENT: The output MUST be between {min_chars} and {max_chars} characters exactly (including spaces).
Your previous attempt was {current_length} characters, so you need to {instruction}.

Guidelines:
- Use strong action verbs and quantifiable results
- Highlight relevant skills and technologies from the job description
- Maintain truthfulness - do not fabricate information
- Return ONLY the bullet point text, nothing else

Rewritten Bullet Point:"""

        message = self.client.messages.create(
            model=self.model,
            max_tokens=300,
            messages=[{"role": "user", "content": prompt}]
        )

        return message.content[0].text.strip()

    def batch_rewrite_with_context(
        self,
        bullet_points: List[Dict],
        job_description: str,
        min_chars: int = 180,
        max_chars: int = 220
    ) -> List[Dict]:
        """
        Rewrite bullet points while preserving their metadata.

        Args:
            bullet_points: List of bullet point dicts with 'text' and other metadata
            job_description: Target job description
            min_chars: Minimum character count
            max_chars: Maximum character count

        Returns:
            List of bullet point dicts with 'rewritten_text' added
        """
        for bullet in bullet_points:
            rewritten_text = self.rewrite_single_bullet(
                bullet['text'],
                job_description,
                min_chars,
                max_chars
            )
            bullet['rewritten_text'] = rewritten_text
            bullet['rewritten_char_count'] = len(rewritten_text)

        return bullet_points
