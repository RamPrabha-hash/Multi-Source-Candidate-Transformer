"""
Main Pipeline

Runs the complete Multi-Source Candidate Transformer.
"""

from parsers.ats_parser import ATSParser
from parsers.resume_parser import ResumeParser
from parsers.notes_parser import NotesParser

from pipeline.normalizer import Normalizer
from pipeline.merger import Merger
from pipeline.confidence import Confidence
from pipeline.projection import Projection

from validators.validator import Validator

from utils.helpers import save_json
from pprint import pprint


def main():

    print("=" * 60)
    print(" Multi-Source Candidate Transformer ")
    print("=" * 60)

    # -----------------------------------
    # Parse Input Sources
    # -----------------------------------

    ats_parser = ATSParser("input/ats.json")
    resume_parser = ResumeParser("input/resume.pdf")
    notes_parser = NotesParser("input/recruiter_notes.txt")

    ats_candidate = ats_parser.parse()
    resume_candidate = resume_parser.parse()
    notes_candidate = notes_parser.parse()

    print("✓ Parsed ATS")
    print("✓ Parsed Resume")
    print("✓ Parsed Recruiter Notes")

    # -----------------------------------
    # Normalize
    # -----------------------------------

    normalizer = Normalizer()

    ats_candidate = normalizer.normalize(ats_candidate)
    resume_candidate = normalizer.normalize(resume_candidate)
    notes_candidate = normalizer.normalize(notes_candidate)

    print("✓ Normalization Complete")

    # -----------------------------------
    # Merge
    # -----------------------------------

    merger = Merger("config/source_priority.json")

    merged_candidate = merger.merge(
        ats_candidate,
        resume_candidate,
        notes_candidate
    )

    print("✓ Merge Complete")

    print("\n================ MERGED CANDIDATE ================\n")
    pprint(merged_candidate)
    print("\n==================================================\n")

    # -----------------------------------
    # Confidence
    # -----------------------------------

    confidence = Confidence()

    merged_candidate = confidence.calculate(
        merged_candidate
    )

    print("✓ Confidence Calculated")

    print("\n============== AFTER CONFIDENCE ==================\n")
    pprint(merged_candidate)
    print("\n==================================================\n")

    # -----------------------------------
    # Validation
    # -----------------------------------

    validator = Validator()

    valid, errors = validator.validate(
        merged_candidate
    )

    if not valid:

        print("\nValidation Errors:")

        for error in errors:
            print("-", error)

    else:
        print("✓ Validation Successful")

    # -----------------------------------
    # Projection
    # -----------------------------------

    projection = Projection(
        "config/projection.json"
    )

    final_output = projection.project(
        merged_candidate
    )

    print("✓ Projection Complete")

    print("\n================ FINAL OUTPUT ====================\n")
    pprint(final_output)
    print("\n==================================================\n")

    # -----------------------------------
    # Save Output
    # -----------------------------------

    save_json(
        final_output,
        "output/final_candidate.json"
    )

    print("\nOutput saved to:")
    print("output/final_candidate.json")

    print("\nProject Completed Successfully!")


if __name__ == "__main__":
    main()