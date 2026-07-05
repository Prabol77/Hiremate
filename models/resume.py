from dataclasses import dataclass, field
from typing import List


@dataclass
class PersonalInfo:
    name: str = ""
    email: str = ""
    phone: str = ""
    location: str = ""


@dataclass
class Education:
    degree: str = ""
    institution: str = ""
    cgpa: str = ""


@dataclass
class ResumeData:
    personal_info: PersonalInfo = field(default_factory=PersonalInfo)

    education: List[Education] = field(default_factory=list)

    skills: List[str] = field(default_factory=list)

    projects: List[str] = field(default_factory=list)

    experience: List[str] = field(default_factory=list)

    certifications: List[str] = field(default_factory=list)