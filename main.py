#from fastapi import FastAPI
#from fastapi_mcp import FastApiMCP
from fastmcp import FastMCP
import os

mcp = FastMCP()
async def konbanwa(name: str) -> str:
    """あいさつ"""
    return f"わんばんこ！, {name}!"

#if __name__ == "__main__":
    #mcp.run(transport="stdio")
    #mcp.run(
    #    transport="sse",
    #    host="127.0.0.1",
    #    port=8888
    #)
    
    if __name__ == "__main__":
    import asyncio
    port = int(os.environ.get("PORT", 8000))
    host = os.environ.get("HOST", "0.0.0.0")
    log_level = os.environ.get("LOG_LEVEL", "info").lower()
    
    logger.info(f"Starting MCP server on {host}:{port}")
    
    # Run the FastMCP server with SSE transport
    asyncio.run(
        mcp.run_sse_async(
            host="0.0.0.0",  # Changed from 127.0.0.1 to allow external connections
            port=port,
            log_level="debug"
        )
    )
