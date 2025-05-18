#from fastapi import FastAPI
#from fastapi_mcp import FastApiMCP
from fastmcp import FastMCP
import os

#app = FastAPI(title="シンプルAPI")
mcp = FastMCP()

#@app.get("/hello", operation_id="say_hello")
@mcp.tool()
async def hello():
    """シンプルな挨拶エンドポイント"""
    return {"message": "Hello World"}

# MCPサーバーを作成
#mcp = FastApiMCP(app, name="シンプルMCPサービスです。")
#mcp.mount()

if __name__ == "__main__":
    import asyncio
    port = int(os.environ.get("PORT", 8000))
    host = os.environ.get("HOST", "0.0.0.0")
    #log_level = os.environ.get("LOG_LEVEL", "info").lower()
    
    #logger.info(f"Starting MCP server on {host}:{port}")
    
    # Run the FastMCP server with SSE transport
    asyncio.run(
        mcp.run_sse_async(
            host="0.0.0.0",  # Changed from 127.0.0.1 to allow external connections
            port=port,
            #log_level="debug"
        )
    )
