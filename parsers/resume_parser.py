import re
import pdfplumber

from parsers.base_parser import BaseParser
from utils.helpers import create_candidate, clean_text
from utils.constants import SOURCE_RESUME


class ResumeParser(BaseParser):

    def __init__(self, file_path: str):
        self.file_path = file_path

    def extract_text(self) -> str:

        text = ""

        with pdfplumber.open(self.file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        return clean_text(text)

    def parse(self):

        text = self.extract_text()
        candidate = create_candidate()

        lines = [line.strip() for line in text.split("\n") if line.strip()]

        if lines:
            candidate["full_name"] = lines[0].title()

        emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)

        if emails:
            candidate["emails"] = list(set(emails))

        phones = re.findall(r'(\+?\d[\d\s-]{8,15}\d)', text)

        for phone in phones:
            phone = re.sub(r"\D", "", phone)

            if len(phone) >= 10:
                candidate["phones"].append(phone)

        candidate["phones"] = list(set(candidate["phones"]))

        if len(lines) > 1:
            candidate["headline"] = lines[1]

        skill_list = [

            "Python",
            "Java",
            "SQL",
            "Machine Learning",
            "Deep Learning",
            "NLP",
            "Git",
            "GitHub",
            "Streamlit",
            "Flask",
            "React",
            "React.js",
            "Node.js",
            "Bootstrap",
            "Tailwind CSS",
            "HTML",
            "CSS",
            "JavaScript",
            "Pandas",
            "Scikit-learn",
            "REST APIs",
            "Data Structures",
            "C",
            "C++",
            "VS Code",
            "Figma",
            "NPM"

        ]

        candidate["skills"] = []

        lower_text = text.lower()

        for skill in skill_list:

            if skill.lower() in lower_text:
                candidate["skills"].append(skill)

        candidate["skills"] = sorted(list(set(candidate["skills"])))

        education = []

        degree_patterns = [

            ("B.E", "Computer Science and Engineering"),
            ("B.Tech", ""),
            ("M.E", ""),
            ("M.Tech", "")

        ]

        for degree, field in degree_patterns:

            if degree.lower() in lower_text:

                education.append({

                    "degree": degree,
                    "field": field

                })

                break

        candidate["education"] = education

        candidate["experience"] = []

        experience_patterns = [

            (
                r'Data Science Intern\s*-\s*(.*?)\s*\(',
                "Data Science Intern"
            ),

            (
                r'Full Stack Developer Intern\s*-\s*(.*?)\s*\(',
                "Full Stack Developer Intern"
            ),

            (
                r'AI Engineer Intern\s*-\s*(.*?)\s*\(',
                "AI Engineer Intern"
            )

        ]

        for pattern, role in experience_patterns:

            match = re.search(pattern, text, re.IGNORECASE)

            if match:

                company = match.group(1).strip()

                candidate["experience"].append({

                    "company": company,
                    "role": role,
                    "years": 1

                })


        candidate["projects"] = []

        project_names = [

            "TrueMark",
            "Field to Feed",
            "AI Meeting Summarizer",
            "UCASE App",
            "Yoga Bot"

        ]

        for project in project_names:

            if project.lower() in lower_text:
                candidate["projects"].append(project)

        candidate["certifications"] = []

        certifications = [

            "Infosys Springboard Python Certification",
            "NEXT WAVE AI Workshop"

        ]

        for cert in certifications:

            if cert.lower() in lower_text:
                candidate["certifications"].append(cert)

        candidate["achievements"] = []

        achievements = [

            "Winner, Rathinam Tech Festa 2025",
            "Runner-up, Ideathon"

        ]

        for achievement in achievements:

            if achievement.lower() in lower_text:
                candidate["achievements"].append(achievement)

        candidate["links"] = {}

        linkedin = re.search(

            r'linkedin\.com/\S+',

            text,

            re.IGNORECASE

        )

        github = re.search(

            r'github\.com/\S+',

            text,

            re.IGNORECASE

        )

        if linkedin:
            candidate["links"]["linkedin"] = linkedin.group()

        if github:
            candidate["links"]["github"] = github.group()

        for key, value in candidate.items():

            if value not in [None, "", [], {}]:
                candidate["provenance"][key] = SOURCE_RESUME

        return candidate