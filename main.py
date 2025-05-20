#from fastapi import FastAPI
#from fastapi_mcp import FastApiMCP
from fastmcp import FastMCP
import os

mcp = FastMCP()
async def konbanwa(name: str) -> str:
    """あいさつ"""
    return f"わんばんこ！, {name}!"

if __name__ == "__main__":
    #mcp.run(transport="stdio")
    #mcp.run(transport="sse",host="0.0.0.0",port=8888)
    mcp.run(transport="sse",host="0.0.0.0")

