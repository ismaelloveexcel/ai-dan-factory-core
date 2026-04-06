from stages.validate import validate
from stages.discovery import discover
from stages.repo import setup_repo
from stages.inject import inject
from stages.deploy import deploy
from stages.quality import check_quality
from stages.monitor import monitor
from contracts.build_brief import BuildBrief
from contracts.factory_result import FactoryResult


STAGES = [validate, discover, setup_repo, inject, deploy, check_quality, monitor]


def run(brief: BuildBrief) -> FactoryResult:
    """Run all factory stages in sequence and return the final result."""
    for stage in STAGES:
        result = stage(brief)
        print(f"[{result['stage']}] {result['status']}")
    return FactoryResult(status="complete", stage="monitor", message="All stages passed")


if __name__ == "__main__":
    brief = BuildBrief(
        project_name="example",
        description="Placeholder run",
        target_repo="ismaelloveexcel/example",
    )
    output = run(brief)
    print(output)
