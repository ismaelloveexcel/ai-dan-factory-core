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


def run_factory(brief: BuildBrief) -> FactoryResult:
    """Run all factory stages in sequence and return the final result."""
    last_stage = ""
    for stage_fn in STAGES:
        result = stage_fn(brief)
        last_stage = result["stage"]
        print(f"[{result['stage']}] {result['status']} — {result['summary']}")
        if result["status"] != "ok":
            return FactoryResult(
                version=brief.version,
                project_id=brief.project_id,
                run_id="run-001",
                status="failed",
                stage=last_stage,
                repo_url="",
                deployment_url="",
                health_status="unknown",
                quality_score=0.0,
                monitor_signal="none",
                recommended_action="review_error",
                last_checked_at="",
                error_message=result.get("summary", "Stage failed"),
            )
    return FactoryResult(
        version=brief.version,
        project_id=brief.project_id,
        run_id="run-001",
        status="complete",
        stage=last_stage,
        repo_url=brief.target_repo,
        deployment_url="",
        health_status="healthy",
        quality_score=1.0,
        monitor_signal="all_clear",
        recommended_action="none",
        last_checked_at="",
    )


if __name__ == "__main__":
    brief = BuildBrief(
        version="0.1.0",
        project_id="example-001",
        project_name="example",
        problem="Placeholder problem",
        solution="Placeholder solution",
        target_user="solo-operator",
        monetization="none",
        target_repo="ismaelloveexcel/example",
    )
    output = run_factory(brief)
    print(output)
