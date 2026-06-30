import json
import os


class Merger:

    def __init__(self, priority_file):

        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        priority_path = os.path.join(base_path, priority_file)

        with open(priority_path, "r", encoding="utf-8") as file:
            self.priority = json.load(file)

    def merge(self, ats, resume, notes):

        candidate = {}

        candidate["candidate_id"] = ats.get("candidate_id")
        candidate["full_name"] = ats.get("name") or resume.get("full_name")

        candidate["location"] = ats.get("location") or None

        candidate["headline"] = ats.get("title") or None

        candidate["experience"] = []

        # 1. PRIORITY: Resume Experience
        if resume.get("experience"):
            candidate["experience"] = resume["experience"]

        # 2. FALLBACK: ATS Experience
        elif ats.get("experience") and ats.get("title"):

            candidate["experience"].append({
                "company": ats.get("company", "Unknown"),
                "role": ats.get("title"),
                "years": ats.get("experience")
            })

        candidate["emails"] = []

        if ats.get("email"):
            candidate["emails"].append(ats["email"])
        elif resume.get("emails"):
            candidate["emails"] = resume["emails"]

        candidate["phones"] = []

        if ats.get("phone"):
            candidate["phones"].append(ats["phone"])
        elif resume.get("phones"):
            candidate["phones"] = resume["phones"]

        candidate["skills"] = resume.get("skills", [])

        candidate["education"] = resume.get("education", [])

        candidate["links"] = resume.get("links", {})

        candidate["notes"] = notes

        return candidate