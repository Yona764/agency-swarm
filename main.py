"""
Agency Swarm FastAPI Server Entry Point

This is a sample deployment file. Customize your agents, tools, and agencies below.
"""
import os
from agency_swarm import Agency, Agent, function_tool, run_fastapi

# Example tool
@function_tool
def get_current_time() -> str:
    """Returns the current server time."""
    from datetime import datetime
    return datetime.now().isoformat()

# Create a sample agent
assistant = Agent(
    name="Assistant",
    instructions="You are a helpful AI assistant. Help users with their questions and tasks.",
    tools=[get_current_time],
)

# Create agency factory function for proper thread management
def create_agency(load_threads_callback=None, save_threads_callback=None):
    return Agency(
        assistant,
        name="main_agency",
        load_threads_callback=load_threads_callback,
        save_threads_callback=save_threads_callback,
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    run_fastapi(
        agencies={"main_agency": create_agency},
        host="0.0.0.0",
        port=port,
    )
