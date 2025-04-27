import asyncio
from src.ankr import mcp

if __name__ == "__main__":
    print("启动Solana RPC MCP服务...")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(mcp.run())
    loop.close() 