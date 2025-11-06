"""
Static Bullet Points Configuration

Define your resume bullet points here. These will be rewritten based on each job description.
Organized by company/project for better output formatting.
"""

# Work Experience - organized by company
WORK_EXPERIENCE = [
    {
        'company': 'Ghost Founder LLC',
        'title': 'Software Engineer',
        'dates': 'Aug 2023 – Present',
        'bullets': [
            "Integrated AWS IoT and MQTT pipelines with secure token-based access, improving device data integrity and ensuring frictionless telemetry delivery across all deployed units",
            "Refactored frontend state management using Context API and React hooks, improving render efficiency by ~25% and enabling responsive control across 20+ deployed devices",
            "Designed reusable UI components for device health, usage analytics, and alert notifications, enhancing internal tool UX consistency and reducing front-end code duplication by 40%",
            "Partnered with hardware and backend teams to standardize API schemas and data contracts, improving integration reliability and simplifying multi-service debugging",
            "Containerized Python microservices using Docker, improving portability and CI/CD consistency, and aligning deployments across edge devices and cloud instances",
            "Secured $5 million in pre-seed funding by demonstrating system reliability, scalability, and operational efficiency",
            "Applied software QA methodologies by writing test plans and defining requirements, improving test coverage by 30% and catching 95% of defects pre-release",
        ]
    },
    {
        'company': 'American Airlines',
        'title': 'Student Researcher',
        'dates': 'Jan 2023 – May 2023',
        'bullets': [
            "Deployed Python ETL pipelines on AWS to process 10M+ operational logs with secure handling of sensitive data, enabling compliant and efficient model-training workflows",
            "Applied machine learning models (Scikit-learn, Pandas, NumPy) to identify key drivers of customer satisfaction, uncover operational anomalies, and improve data interpretation for leadership reviews",
            "Developed customer churn prediction models using Random Forest and K-Nearest Neighbors, achieving 92% accuracy through hyperparameter tuning and optimization",
        ]
    },
]

# Projects - organized by project
PROJECTS = [
    {
        'name': 'Cal | Personalized AI Fitness Coach for iOS',
        'bullets': [
            "Deployed an iOS fitness app in Swift, integrating Apple HealthKit and REST APIs, and released a TestFlight beta that drove strong adoption and active usage among pilot users",
            "Integrated secure REST APIs and user auth flows with AWS Lambda and Core ML, ensuring privacy of health data while enabling real-time, adaptive workout recommendations",
            "Automated model retraining and logging with AWS S3 and CloudWatch, enhancing observability of ML performance and ensuring continuous, reliable recommendations",
        ]
    },
    {
        'name': 'Bloom | Depression Prediction using AI',
        'bullets': [
            "Created an AI-powered depression prediction tool using Convolutional Neural Networks (CNNs) and multiple regression models, achieving 92% accuracy with only a 6% false-negative rate to minimize missed at-risk cases",
            "Deployed Python/React portal on AWS with Postgres backing for secure data handling and API auth, improving reliability and user privacy for clinical AI predictions",
        ]
    },
    {
        'name': 'Moodify | Playlist generation using API based on moods',
        'bullets': [
            "Constructed a Node.js backend with mood classification models (~85% accuracy), automating mood tagging and enabling scalable real-time playlist generation",
            "Integrated AWS API Gateway and Lambda for secure mood-based playlist requests, improving latency by 35% and standardizing API observability across frontend and backend",
        ]
    },
]


def get_all_bullets():
    """
    Get all bullet points as a flat list (for backward compatibility).

    Returns:
        List of bullet point strings
    """
    bullets = []
    for work in WORK_EXPERIENCE:
        bullets.extend(work['bullets'])
    for project in PROJECTS:
        bullets.extend(project['bullets'])
    return bullets


def get_structured_bullets():
    """
    Get bullet points organized by company/project.

    Returns:
        Dict with 'work_experience' and 'projects' keys containing structured data
    """
    return {
        'work_experience': WORK_EXPERIENCE,
        'projects': PROJECTS
    }


def get_bullet_count():
    """
    Get total count of bullets.

    Returns:
        int: Total number of bullets
    """
    return len(get_all_bullets())


# For backward compatibility
def get_bullets_by_section():
    """
    Get bullet points organized by section (legacy format).

    Returns:
        Dict with 'work_experience' and 'projects' keys
    """
    work_bullets = []
    for work in WORK_EXPERIENCE:
        work_bullets.extend(work['bullets'])

    project_bullets = []
    for project in PROJECTS:
        project_bullets.extend(project['bullets'])

    return {
        'work_experience': work_bullets,
        'projects': project_bullets
    }

