class Confidence:

    def calculate(self, candidate):

        score = 0
        total = 6

        if candidate.get("emails") and len(candidate["emails"]) > 0:
            score += 1

        if candidate.get("phones") and len(candidate["phones"]) > 0:
            score += 1

        if candidate.get("skills") and len(candidate["skills"]) > 0:
            score += 1

        if candidate.get("education") and len(candidate["education"]) > 0:
            score += 1

        if candidate.get("experience") is not None:
            score += 1

        if candidate.get("links") and len(candidate["links"]) > 0:
            score += 1

        candidate["overall_confidence"] = round(score / total, 2)

        return candidate