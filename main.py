#from fastapi import FastAPI
#from fastapi_mcp import FastApiMCP
from fastmcp import FastMCP
import os

#app = FastAPI(title="シンプルAPI")
mcp = FastMCP()

#@app.get("/hello", operation_id="say_hello")
@mcp.tool()
async def konbanwa(name: str) -> str:
    """あいさつ"""
    return f"わんばんこ！, {name}!"
# MCPサーバーを作成
#mcp = FastApiMCP(app, name="シンプルMCPサービスです。")
#mcp.mount()

if __name__ == "__main__":
    mcp.run(transport="stdio")
    #mcp.run(transport="sse")
