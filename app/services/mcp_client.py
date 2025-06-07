# app/services/mcp_client.py
import httpx

MCP_SERVER_URL = "https://api.openai.com/v1"  # Change to your MCP base URL

async def trigger_agent(agent_id: str, payload: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{MCP_SERVER_URL}/agents/{agent_id}/run", json=payload)
        response.raise_for_status()
        return response.json()

async def get_agent_status(agent_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{MCP_SERVER_URL}/agents/{agent_id}/status")
        response.raise_for_status()
        return response.json()
