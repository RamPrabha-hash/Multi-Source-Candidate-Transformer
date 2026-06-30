"""
Validator

Validates the final candidate profile.
"""


class Validator:
    """
    Validate candidate data.
    """

    def validate(self, candidate: dict) -> tuple:
        """
        Returns:
            (is_valid, errors)
        """

        errors = []

        # -----------------------------
        # Full Name
        # -----------------------------
        if not candidate.get("full_name"):
            errors.append("Full name is missing.")

        # -----------------------------
        # Email
        # -----------------------------
        if not candidate.get("emails"):
            errors.append("Email is missing.")

        # -----------------------------
        # Skills
        # -----------------------------
        if not candidate.get("skills"):
            errors.append("Skills are missing.")

        # -----------------------------
        # Experience
        # -----------------------------
        experience = candidate.get("years_experience")

        if experience is not None:

            if not isinstance(experience, (int, float)):
                errors.append("Years of experience must be a number.")

        # -----------------------------
        # Validation Result
        # -----------------------------
        return len(errors) == 0, errors