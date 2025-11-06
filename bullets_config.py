"""
Static Bullet Points Configuration

Define your resume bullet points here. These will be rewritten based on each job description.
The structure must match your resume.docx template exactly.
"""

# Work Experience Bullets
WORK_EXPERIENCE_BULLETS = [
    # Ghost Founder LLC - Software Engineer (Aug 2023 – Present)
    "Integrated AWS IoT and MQTT pipelines with secure token-based access, improving device data integrity and ensuring frictionless telemetry delivery across all deployed units",
    "Refactored frontend state management using Context API and React hooks, improving render efficiency by ~25% and enabling responsive control across 20+ deployed devices",
    "Designed reusable UI components for device health, usage analytics, and alert notifications, enhancing internal tool UX consistency and reducing front-end code duplication by 40%",
    "Partnered with hardware and backend teams to standardize API schemas and data contracts, improving integration reliability and simplifying multi-service debugging",
    "Containerized Python microservices using Docker, improving portability and CI/CD consistency, and aligning deployments across edge devices and cloud instances",
    "Secured $5 million in pre-seed funding by demonstrating system reliability, scalability, and operational efficiency",
    "Applied software QA methodologies by writing test plans and defining requirements, improving test coverage by 30% and catching 95% of defects pre-release",

    # American Airlines - Student Researcher (Jan 2023 – May 2023)
    "Deployed Python ETL pipelines on AWS to process 10M+ operational logs with secure handling of sensitive data, enabling compliant and efficient model-training workflows",
    "Applied machine learning models (Scikit-learn, Pandas, NumPy) to identify key drivers of customer satisfaction, uncover operational anomalies, and improve data interpretation for leadership reviews",
    "Developed customer churn prediction models using Random Forest and K-Nearest Neighbors, achieving 92% accuracy through hyperparameter tuning and optimization",
]

# Projects Bullets
PROJECTS_BULLETS = [
    # Cal | Personalized AI Fitness Coach for iOS
    "Deployed an iOS fitness app in Swift, integrating Apple HealthKit and REST APIs, and released a TestFlight beta that drove strong adoption and active usage among pilot users",
    "Integrated secure REST APIs and user auth flows with AWS Lambda and Core ML, ensuring privacy of health data while enabling real-time, adaptive workout recommendations",
    "Automated model retraining and logging with AWS S3 and CloudWatch, enhancing observability of ML performance and ensuring continuous, reliable recommendations",

    # Bloom | Depression Prediction using AI
    "Created an AI-powered depression prediction tool using Convolutional Neural Networks (CNNs) and multiple regression models, achieving 92% accuracy with only a 6% false-negative rate to minimize missed at-risk cases",
    "Deployed Python/React portal on AWS with Postgres backing for secure data handling and API auth, improving reliability and user privacy for clinical AI predictions",

    # Moodify | Playlist generation using API based on moods
    "Constructed a Node.js backend with mood classification models (~85% accuracy), automating mood tagging and enabling scalable real-time playlist generation",
    "Integrated AWS API Gateway and Lambda for secure mood-based playlist requests, improving latency by 35% and standardizing API observability across frontend and backend",
]

# Combine all bullets in the order they appear in the resume
ALL_BULLETS = WORK_EXPERIENCE_BULLETS + PROJECTS_BULLETS


def get_all_bullets():
    """
    Get all bullet points to be optimized.

    Returns:
        List of bullet point strings
    """
    return ALL_BULLETS


def get_bullets_by_section():
    """
    Get bullet points organized by section.

    Returns:
        Dict with 'work_experience' and 'projects' keys
    """
    return {
        'work_experience': WORK_EXPERIENCE_BULLETS,
        'projects': PROJECTS_BULLETS
    }


def get_bullet_count():
    """
    Get total count of bullets.

    Returns:
        int: Total number of bullets
    """
    return len(ALL_BULLETS)
