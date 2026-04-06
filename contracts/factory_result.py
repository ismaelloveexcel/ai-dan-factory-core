from dataclasses import dataclass
from typing import Optional


@dataclass
class FactoryResult:
    """Output contract for a completed factory run."""

    version: str
    project_id: str
    run_id: str
    status: str
    stage: str
    repo_url: str
    deployment_url: str
    health_status: str
    quality_score: float
    monitor_signal: str
    recommended_action: str
    last_checked_at: str
    error_message: Optional[str] = None
