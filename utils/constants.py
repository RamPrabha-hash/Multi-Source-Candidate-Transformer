"""
Project-wide constants and canonical schema.

Every parser converts its source into this schema.
Every transformer expects this schema.
"""

# -----------------------------
# Supported Input Sources
# -----------------------------

SOURCE_ATS = "ATS"
SOURCE_RESUME = "Resume"
SOURCE_NOTES = "Recruiter Notes"


# -----------------------------
# Source Confidence Scores
# -----------------------------
# Higher = More trustworthy

SOURCE_CONFIDENCE = {
    SOURCE_ATS: 0.95,
    SOURCE_RESUME: 0.90,
    SOURCE_NOTES: 0.70
}


# -----------------------------
# Canonical Candidate Schema
# -----------------------------

CANONICAL_SCHEMA = {
    "candidate_id": None,
    "full_name": None,
    "emails": [],
    "phones": [],
    "location": {
        "city": None,
        "country": None
    },
    "links": {
        "linkedin": None,
        "github": None,
        "portfolio": None,
        "other": []
    },
    "headline": None,
    "years_experience": None,
    "skills": [],
    "experience": [],
    "education": [],
    "provenance": {},
    "overall_confidence": 0.0
}


# -----------------------------
# Skill Normalization Map
# -----------------------------

SKILL_ALIASES = {

    "py": "Python",
    "python programming": "Python",
    "python3": "Python",

    "ml": "Machine Learning",
    "machine learning": "Machine Learning",

    "sql server": "SQL",
    "mysql": "SQL"
}