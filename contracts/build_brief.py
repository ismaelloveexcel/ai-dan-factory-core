from dataclasses import dataclass, field


@dataclass
class BuildBrief:
    """Input contract for a factory run."""

    version: str
    project_id: str
    project_name: str
    problem: str
    solution: str
    target_user: str
    monetization: str
    target_repo: str
    constraints: dict = field(default_factory=dict)
