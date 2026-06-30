"""
Normalizer

Cleans and standardizes candidate data.
"""

from utils.constants import SKILL_ALIASES


class Normalizer:
    """
    Normalize candidate data.
    """

    def normalize(self, candidate: dict) -> dict:

        # -----------------------------
        # Name
        # -----------------------------
        if candidate["full_name"]:
            candidate["full_name"] = candidate["full_name"].strip().title()

        # -----------------------------
        # Emails
        # -----------------------------
        candidate["emails"] = [
            email.strip().lower()
            for email in candidate["emails"]
        ]

        # Remove duplicate emails
        candidate["emails"] = list(set(candidate["emails"]))

        # -----------------------------
        # Skills
        # -----------------------------
        normalized_skills = []

        for skill in candidate["skills"]:

            skill = skill.strip()

            key = skill.lower()

            if key in SKILL_ALIASES:
                skill = SKILL_ALIASES[key]

            if skill not in normalized_skills:
                normalized_skills.append(skill)

        candidate["skills"] = normalized_skills

        return candidate