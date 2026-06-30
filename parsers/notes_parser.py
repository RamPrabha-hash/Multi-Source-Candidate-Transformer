"""
Notes Parser

Reads recruiter notes and converts them into the
project's canonical candidate schema.
"""

from parsers.base_parser import BaseParser
from utils.constants import SOURCE_NOTES
from utils.helpers import create_candidate, clean_text


class NotesParser(BaseParser):
    """
    Parser for recruiter notes.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

    def parse(self) -> dict:
        """
        Parse recruiter notes into the canonical schema.
        """

        candidate = create_candidate()

        with open(self.file_path, "r", encoding="utf-8") as file:
            text = clean_text(file.read())

        # Store recruiter notes as headline
        candidate["headline"] = text

        # Provenance
        for key, value in candidate.items():
            if value not in [None, [], {}, ""]:
                candidate["provenance"][key] = SOURCE_NOTES

        return candidate