# Multi-Source Candidate Transformer

## Overview

The **Multi-Source Candidate Transformer** is a modular data processing pipeline that consolidates candidate information from multiple sources into a single, standardized candidate profile.

The system accepts data from:

* ATS (Applicant Tracking System)
* Resume (PDF)
* Recruiter Notes (Text)

It normalizes, merges, validates, scores, and projects the information into a unified JSON output.

---

# Features

* Parse candidate information from multiple sources
* Extract structured data from PDF resumes
* Normalize data into a common schema
* Merge candidate information using configurable source priorities
* Calculate confidence score for extracted information
* Validate mandatory fields
* Generate standardized JSON output
* Track source provenance for parsed fields
* Extract:

  * Name
  * Email
  * Phone Number
  * Headline
  * Skills
  * Education
  * Experience
  * Projects
  * Certifications
  * Achievements
  * LinkedIn
  * GitHub

---

# Project Architecture

```
                ATS JSON
                    │
                    ▼
              ATS Parser
                    │

 Resume PDF ──► Resume Parser
                    │

 Recruiter Notes ─► Notes Parser
                    │
                    ▼
              Normalization
                    │
                    ▼
                Candidate Merge
                    │
                    ▼
           Confidence Calculator
                    │
                    ▼
                Validation
                    │
                    ▼
                Projection
                    │
                    ▼
         Final Candidate JSON
```

---

# Folder Structure

```
Multi-Source-Candidate-Transformer/
│
├── config/
│   ├── projection.json
│   └── source_priority.json
│
├── input/
│   ├── ats.json
│   ├── recruiter_notes.txt
│   └── resume.pdf
│
├── output/
│   └── final_candidate.json
│
├── parsers/
│   ├── ats_parser.py
│   ├── resume_parser.py
│   ├── notes_parser.py
│   └── base_parser.py
│
├── pipeline/
│   ├── normalizer.py
│   ├── merger.py
│   ├── confidence.py
│   └── projection.py
│
├── validators/
│   └── validator.py
│
├── utils/
│   ├── constants.py
│   └── helpers.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Pipeline Workflow

### Step 1 – Parse Inputs

The pipeline reads data from:

* ATS JSON
* Resume PDF
* Recruiter Notes

Each source is parsed independently.

---

### Step 2 – Normalize

The extracted information is converted into a common schema.

Examples include:

* Standardized phone numbers
* Lowercase emails
* Duplicate removal
* Consistent field names

---

### Step 3 – Merge

Candidate information from all sources is merged using configurable source priorities.

Example priority:

```
ATS > Resume > Recruiter Notes
```

---

### Step 4 – Confidence Calculation

A confidence score is calculated based on field completeness and availability.

Example:

```
Overall Confidence = 1.0
```

---

### Step 5 – Validation

Mandatory fields are validated before generating the final output.

Validation checks include:

* Candidate ID
* Name
* Email
* Phone Number
* Skills

---

### Step 6 – Projection

The merged candidate is transformed into the required output schema.

---

# Technologies Used

* Python 3
* pdfplumber
* Regular Expressions (Regex)
* JSON
* Object-Oriented Programming (OOP)

---

# Input Files

### ATS

```
input/ats.json
```

### Resume

```
input/resume.pdf
```

### Recruiter Notes

```
input/recruiter_notes.txt
```

---

# Output

```
output/final_candidate.json
```

Example:

```json
{
  "candidate_id": "C001",
  "full_name": "RAM PRABHA M",
  "emails": [
    "prabhaidol@gmail.com"
  ],
  "phones": [
    "8838758349"
  ],
  "headline": "AI/ML & Full Stack Developer",
  "experience": [
    {
      "company": "Software Solution",
      "role": "Full Stack Developer Intern",
      "years": 1
    }
  ],
  "skills": [
    "Python",
    "Java",
    "SQL",
    "Machine Learning"
  ],
  "overall_confidence": 1.0
}
```

---

# How to Run

Clone the repository:

```bash
git clone <repository-url>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

The generated output will be available in:

```
output/final_candidate.json
```

---

# Design Principles

* Modular Architecture
* Separation of Concerns
* Configurable Source Priorities
* Extensible Parser Design
* Reusable Pipeline Components
* Clean Code Practices

---

# Future Improvements

* OCR support for scanned resumes
* AI-based resume parsing using NLP
* REST API integration
* Database storage
* Duplicate candidate detection
* Web dashboard for visualization
* Support for DOCX and image resumes

---

# Author

**Ram Prabha M**


GitHub: https://github.com/RamPrabha-hash

LinkedIn: https://linkedin.com/in/ram-prabha-m
