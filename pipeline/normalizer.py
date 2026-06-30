from utils.constants import SKILL_ALIASES


class Normalizer:

    def normalize(self, candidate: dict) -> dict:


        if candidate["full_name"]:
            candidate["full_name"] = candidate["full_name"].strip().title()

        candidate["emails"] = [
            email.strip().lower()
            for email in candidate["emails"]
        ]

        # Remove duplicate emails
        candidate["emails"] = list(set(candidate["emails"]))

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