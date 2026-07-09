from dataclasses import dataclass, field
from typing import Dict, List
from services.metadata_service import (
    MetadataService,
)

@dataclass
class PersonalInfo:
    name: str = ""
    email: str = ""
    phone: str = ""
    location: str = ""
    linkedin: str = ""
    github: str = ""


@dataclass
class Education:
    degree: str = ""
    institution: str = ""
    start_year: str = ""
    end_year: str = ""
    cgpa: str = ""


@dataclass
class Experience:
    company: str = ""
    role: str = ""
    duration: str = ""
    description: str = ""


@dataclass
class Project:
    title: str = ""
    description: str = ""
    technologies: List[str] = field(default_factory=list)


@dataclass
class ResumeData:
    """
    Structured representation of a parsed resume.
    """

    personal_info: PersonalInfo = field(default_factory=PersonalInfo)

    education: List[Education] = field(default_factory=list)

    experience: List[Experience] = field(default_factory=list)

    projects: List[Project] = field(default_factory=list)

    skills: List[str] = field(default_factory=list)

    certifications: List[str] = field(default_factory=list)

    achievements: List[str] = field(default_factory=list)

    languages: List[str] = field(default_factory=list)

    # ⭐ New
    # Stores the raw text of each detected resume section.
    sections: Dict[str, str] = field(default_factory=dict)
    metadata: dict = field(
    default_factory=dict
)
