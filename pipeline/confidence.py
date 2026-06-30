"""
Confidence Scoring Module

Computes completeness-based confidence score
for the final candidate profile.
"""


class Confidence:

    def calculate(self, candidate):

        score = 0
        total = 6

        # -------------------------
        # EMAIL
        # -------------------------
        if candidate.get("emails") and len(candidate["emails"]) > 0:
            score += 1

        # -------------------------
        # PHONE
        # -------------------------
        if candidate.get("phones") and len(candidate["phones"]) > 0:
            score += 1

        # -------------------------
        # SKILLS
        # -------------------------
        if candidate.get("skills") and len(candidate["skills"]) > 0:
            score += 1

        # -------------------------
        # EDUCATION
        # -------------------------
        if candidate.get("education") and len(candidate["education"]) > 0:
            score += 1

        # -------------------------
        # EXPERIENCE
        # -------------------------
        if candidate.get("experience") is not None:
            score += 1

        # -------------------------
        # LINKS
        # -------------------------
        if candidate.get("links") and len(candidate["links"]) > 0:
            score += 1

        candidate["overall_confidence"] = round(score / total, 2)

        return candidate