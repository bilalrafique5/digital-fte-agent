from agents.planner import plan_content
from agents.writer import write_content
from agents.critic import critique_and_refine

def run_content_pipeline(topic: str, platforms: list) -> dict:
    # One shared strategy works across platforms, but we still note platform
    # context inside the planner per platform for sharper tone matching
    strategy = plan_content(topic, ", ".join(platforms))

    results = {}
    for platform in platforms:
        draft = write_content(topic, platform, strategy)
        critique = critique_and_refine(draft, platform)
        results[platform] = {
            "draft": draft,
            "final_post": critique["final_post"],
            "critic_feedback": critique["feedback"]
        }

    return {
        "status": "success",
        "strategy": strategy,
        "results": results
    }