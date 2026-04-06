from dataclasses import dataclass


@dataclass
class BuildBrief:
    """Describes the input contract for a factory run."""

    project_name: str
    description: str
    target_repo: str
