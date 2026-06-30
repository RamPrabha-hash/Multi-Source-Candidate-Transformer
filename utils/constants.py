SOURCE_ATS = "ATS"
SOURCE_RESUME = "Resume"
SOURCE_NOTES = "Recruiter Notes"


SOURCE_CONFIDENCE = {
    SOURCE_ATS: 0.95,
    SOURCE_RESUME: 0.90,
    SOURCE_NOTES: 0.70
}


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


SKILL_ALIASES = {

    "py": "Python",
    "python programming": "Python",
    "python3": "Python",

    "ml": "Machine Learning",
    "machine learning": "Machine Learning",

    "sql server": "SQL",
    "mysql": "SQL"
}