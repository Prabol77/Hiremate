from dataclasses import dataclass, field
from typing import List


@dataclass
class JobInfo:
    """
    Basic information about the job posting.
    """

    title: str = ""
    company: str = ""
    location: str = ""
    employment_type: str = ""


@dataclass
class JobRequirement:
    """
    Education and experience requirements.
    """

    education: List[str] = field(default_factory=list)
    experience: str = ""


@dataclass
class JobData:
    """
    Structured representation of a Job Description.
    """

    job_info: JobInfo = field(default_factory=JobInfo)

    requirements: JobRequirement = field(default_factory=JobRequirement)

    skills: List[str] = field(default_factory=list)

    responsibilities: List[str] = field(default_factory=list)

    preferred_skills: List[str] = field(default_factory=list)

    keywords: List[str] = field(default_factory=list)
