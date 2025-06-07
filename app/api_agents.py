# app/api_agents.py
from fastapi import APIRouter
from app.services.mcp_client import trigger_agent, get_agent_status

router = APIRouter()

@router.post("/agents/{agent_id}/trigger")
async def trigger(agent_id: str, request: dict):
    result = await trigger_agent(agent_id, request)
    return {"result": result}

@router.get("/agents/{agent_id}/status")
async def status(agent_id: str):
    status = await get_agent_status(agent_id)
    return {"status": status}
