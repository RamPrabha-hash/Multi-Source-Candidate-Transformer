class Projection:

    def __init__(self, config_path):
        self.config_path = config_path

    def project(self, candidate):

        final = {}

        # -------------------------
        # CORE FIELDS (NO DROPPING)
        # -------------------------
        final["candidate_id"] = candidate.get("candidate_id")
        final["full_name"] = candidate.get("full_name")

        final["emails"] = candidate.get("emails", [])
        final["phones"] = candidate.get("phones", [])

        final["location"] = candidate.get("location")

        # FIX: headline should NEVER be lost
        final["headline"] = candidate.get("headline")

        # FIX: keep experience ONLY (remove years_experience dependency)
        final["experience"] = candidate.get("experience", [])

        final["skills"] = candidate.get("skills", [])

        final["education"] = candidate.get("education", [])

        final["overall_confidence"] = candidate.get("overall_confidence", 0.0)

        return final