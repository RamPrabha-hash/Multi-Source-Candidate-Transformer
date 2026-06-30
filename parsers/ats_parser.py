"""
ATS Parser

Converts ATS JSON into canonical intermediate schema.
"""

from parsers.base_parser import BaseParser
from utils.constants import SOURCE_ATS
from utils.helpers import load_json, create_candidate, split_location


class ATSParser(BaseParser):

    def __init__(self, file_path: str):
        self.file_path = file_path

    def parse(self) -> dict:

        ats_data = load_json(self.file_path)

        candidate = create_candidate()

        # -----------------------------
        # BASIC INFO
        # -----------------------------
        candidate["candidate_id"] = ats_data.get("candidate_id")
        candidate["name"] = ats_data.get("name")

        # -----------------------------
        # CONTACT
        # -----------------------------
        if ats_data.get("email"):
            candidate["emails"].append(ats_data["email"])

        if ats_data.get("phone"):
            candidate["phones"].append(ats_data["phone"])

        # -----------------------------
        # LOCATION (NO GUESSING)
        # -----------------------------
        candidate["location"] = split_location(ats_data.get("location"))

        # -----------------------------
        # PROFESSIONAL INFO
        # -----------------------------
        candidate["title"] = ats_data.get("title")

        # IMPORTANT: keep only raw number here
        candidate["experience"] = ats_data.get("experience")

        candidate["skills"] = ats_data.get("skills", [])

        candidate["company"] = ats_data.get("current_company")

        # -----------------------------
        # PROVENANCE
        # -----------------------------
        for key, value in candidate.items():
            if value not in [None, [], {}, ""]:
                candidate["provenance"][key] = SOURCE_ATS

        return candidate