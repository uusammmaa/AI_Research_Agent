# backend/agent/models.py
from pydantic import BaseModel
from typing import List


class ResearchBrief(BaseModel):
    role: str
    company: str
    location: str
    tech_stack: List[str]
    key_requirements: List[str]
    company_summary: str
    culture_signals: List[str]
    talking_points: List[str]
    red_flags: List[str]
    sources: List[str]


class AgentStep(BaseModel):
    type: str           # "thinking" | "tool_call" | "tool_result" | "complete" | "error"
    tool: str = ""      # tool name if type == "tool_call"
    input: str = ""     # tool input summary
    output: str = ""    # tool result summary or final brief JSON
    message: str = ""   # human-readable step description
