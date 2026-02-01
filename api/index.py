"""
Vercel Serverless Entry Point for Agency Swarm

Note: Vercel serverless functions have timeout limits (10s on hobby, 60s on pro).
For streaming AI responses, consider using a longer-running platform.
"""
import os
from agency_swarm import Agency, Agent, function_tool
from agency_swarm.integrations.fastapi import run_fastapi

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

# Create agency factory function
def create_agency(load_threads_callback=None, save_threads_callback=None):
    return Agency(
        assistant,
        name="main_agency",
        load_threads_callback=load_threads_callback,
        save_threads_callback=save_threads_callback,
    )

# Create FastAPI app for Vercel (return_app=True returns the app without running uvicorn)
app = run_fastapi(
    agencies={"main_agency": create_agency},
    tools=[],
    return_app=True,
    cors_origins=["*"],
)
