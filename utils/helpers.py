"""
Helper functions used across the project.
"""

import json
from copy import deepcopy

from utils.constants import CANONICAL_SCHEMA


def load_json(file_path: str) -> dict:
    """
    Load a JSON file.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json(data: dict, file_path: str):
    """
    Save dictionary as JSON.
    """

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def clean_text(text: str) -> str:
    """
    Remove extra spaces/tabs within each line, while
    preserving line breaks (needed for parsers that rely
    on document structure, e.g. name on its own line).
    """

    if not text:
        return ""

    lines = [" ".join(line.split()) for line in text.splitlines()]
    return "\n".join(line for line in lines if line)


def split_location(location: str) -> dict:
    """
    Convert:
    'Chennai, India'

    into

    {
        "city": "Chennai",
        "country": "India"
    }
    """

    result = {
        "city": None,
        "country": None
    }

    if not location:
        return result

    parts = [part.strip() for part in location.split(",")]

    if len(parts) >= 2:
        result["city"] = parts[0]
        result["country"] = parts[1]

    return result


def create_candidate() -> dict:
    """
    Return a fresh candidate schema.
    """

    return deepcopy(CANONICAL_SCHEMA)