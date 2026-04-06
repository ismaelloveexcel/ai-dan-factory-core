from dataclasses import dataclass


@dataclass
class FactoryResult:
    """Describes the output contract for a completed factory run."""

    status: str
    stage: str
    message: str
