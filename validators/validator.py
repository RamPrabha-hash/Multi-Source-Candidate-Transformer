class Validator:

    def validate(self, candidate: dict) -> tuple:
   
        errors = []

        if not candidate.get("full_name"):
            errors.append("Full name is missing.")

        if not candidate.get("emails"):
            errors.append("Email is missing.")

        if not candidate.get("skills"):
            errors.append("Skills are missing.")

 
        experience = candidate.get("years_experience")

        if experience is not None:

            if not isinstance(experience, (int, float)):
                errors.append("Years of experience must be a number.")

        return len(errors) == 0, errors