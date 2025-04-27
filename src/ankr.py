from typing import Any
import httpx
import json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ankr-mcp",host="0.0.0.0",port=8080)
USER_AGENT = "DEMCP-ANKR/1.0"
API_URL = "https://mainnet.helius-rpc.com/?api-key=66fefa32-d045-4258-930c-86f4c75d0f86"

async def make_request(url: str, method: str = "GET", payload: dict = None) -> dict[str, Any] | None:
    """Make a request to the API with proper error handling."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json"
    }
    
    if method.upper() == "POST" and payload:
        headers["Content-Type"] = "application/json"
    
    async with httpx.AsyncClient() as client:
        try:
            if method.upper() == "GET":
                response = await client.get(url, headers=headers, timeout=30.0)
            elif method.upper() == "POST":
                response = await client.post(url, headers=headers, json=payload, timeout=30.0)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
                
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error making {method} request to {url}: {str(e)}")
            return None
        


@mcp.tool(
    description="Get information about a Solana account"
)
async def get_account_info(address: str) -> dict[str, Any]:
    """Get information about a Solana account.
    
    Args:
        address (str): The address of the Solana account to get info for.
    
    Returns:
        dict: Account information or error response.
    """
    payload = {
        "jsonrpc": "2.0",
        "method": "getAccountInfo",
        "params": [
            address,
            {
                "encoding": "base58"
            }
        ],
        "id": 1
    }
    
    response = await make_request(API_URL, method="POST", payload=payload)
    if response is None:
        return {"error": "Failed to fetch account information"}
    return response




@mcp.tool(
    description="Get the balance of a Solana account"
)
async def get_account_balance(address: str) -> dict[str, Any]:

    """
    Args:
        address (str): The address of the Solana account to get the balance of.
    """
    payload = {
        "jsonrpc": "2.0",
        "method": "getBalance",
        "params": [address],
        "id": 1
    }
    
    response = await make_request(API_URL, method="POST", payload=payload)
    if response is None:
        return {"error": "Failed to fetch account balance"}
    return response


@mcp.tool(
    description="查询代币账户、NFT数据或程序状态，常用于代币管理和DeFi应用。"
)
async def get_program_accounts(program_id: str) -> dict[str, Any]:
    """
    Args:
        program_id (str): The program ID to query.
    """
    payload = {
        "jsonrpc": "2.0",
        "method": "getProgramAccounts",
        "params": [program_id],
        "id": 1
    }
    
    response = await make_request(API_URL, method="POST", payload=payload)
    if response is None:
        return {"error": "Failed to fetch program accounts"}
    return response
    
    
@mcp.tool(
    description="获取Solana代币账户余额"
)
async def get_token_account_balance(token_account: str) -> dict[str, Any]:
    """获取Solana代币账户余额
    
    Args:
        token_account (str): 代币账户地址
    """
    payload = {
        "jsonrpc": "2.0",
        "method": "getTokenAccountBalance",
        "params": [token_account],
        "id": 1
    }
    
    response = await make_request(API_URL, method="POST", payload=payload)
    if response is None:
        return {"error": "Failed to fetch token account balance"}
    return response


@mcp.tool(
    description="获取Solana代币账户所有者的所有代币账户"
)
async def get_token_accounts_by_owner(owner: str) -> dict[str, Any]:
    """获取Solana代币账户所有者的所有代币账户
    
    Args:
        owner (str): 所有者地址
    """
    payload = {
        "jsonrpc": "2.0",
        "method": "getTokenAccountsByOwner",
        "params": [
            owner, 
            {"programId": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"},
            {"encoding": "jsonParsed"}
        ],
        "id": 1
    }
    
    response = await make_request(API_URL, method="POST", payload=payload)
    if response is None:
        return {"error": "Failed to fetch token accounts"}
    return response




@mcp.tool(
    description="获取Solana区块信息"
)
async def get_blocks(start_slot: int, end_slot: int = None) -> dict[str, Any]:
    """获取Solana区块信息
    
    Args:
        start_slot (int): 起始槽位
        end_slot (int, optional): 结束槽位，如果不提供则查询到最新槽位
    """
    params = [start_slot]
    if end_slot is not None:
        params.append(end_slot)
        
    payload = {
        "jsonrpc": "2.0",
        "method": "getBlocks",
        "params": params,
        "id": 1
    }
    
    response = await make_request(API_URL, method="POST", payload=payload)
    if response is None:
        return {"error": "Failed to fetch blocks"}
    return response



@mcp.tool(
    description="获取Solana epoch调度信息"
)
async def get_epoch_schedule() -> dict[str, Any]:
    """获取Solana epoch调度信息"""
    payload = {
        "jsonrpc": "2.0",
        "method": "getEpochSchedule",
        "params": [],
        "id": 1
    }
    
    response = await make_request(API_URL, method="POST", payload=payload)
    if response is None:
        return {"error": "Failed to fetch epoch schedule"}
    return response






@mcp.tool(
    description="获取Solana最新区块哈希"
)
async def get_latest_blockhash() -> dict[str, Any]:
    """获取Solana最新区块哈希"""
    payload = {
        "jsonrpc": "2.0",
        "method": "getLatestBlockhash",
        "params": [],
        "id": 1
    }
    
    response = await make_request(API_URL, method="POST", payload=payload)
    if response is None:
        return {"error": "Failed to fetch latest blockhash"}
    return response


@mcp.tool(
    description="获取账户免租金所需的最低余额"
)
async def get_minimum_balance_for_rent_exemption(size: int) -> dict[str, Any]:
    """获取账户免租金所需的最低余额
    
    Args:
        size (int): 账户数据大小（字节）
    """
    payload = {
        "jsonrpc": "2.0",
        "method": "getMinimumBalanceForRentExemption",
        "params": [size],
        "id": 1
    }
    
    response = await make_request(API_URL, method="POST", payload=payload)
    if response is None:
        return {"error": "Failed to fetch minimum balance for rent exemption"}
    return response


@mcp.tool(
    description="获取多个Solana账户信息"
)
async def get_multiple_accounts(pubkeys: list[str]) -> dict[str, Any]:
    """获取多个Solana账户信息
    
    Args:
        pubkeys (list[str]): 账户公钥列表
    """
    payload = {
        "jsonrpc": "2.0",
        "method": "getMultipleAccounts",
        "params": [pubkeys, {"encoding": "jsonParsed"}],
        "id": 1
    }
    
    response = await make_request(API_URL, method="POST", payload=payload)
    if response is None:
        return {"error": "Failed to fetch multiple accounts"}
    return response




@mcp.tool(
    description="获取Solana当前槽位"
)
async def get_slot() -> dict[str, Any]:
    """获取Solana当前槽位"""
    payload = {
        "jsonrpc": "2.0",
        "method": "getSlot",
        "params": [],
        "id": 1
    }
    
    response = await make_request(API_URL, method="POST", payload=payload)
    if response is None:
        return {"error": "Failed to fetch current slot"}
    return response



@mcp.tool(
    description="获取Solana质押激活信息"
)
async def get_stake_activation(stake_account: str) -> dict[str, Any]:
    """获取Solana质押激活信息
    
    Args:
        stake_account (str): 质押账户地址
    """
    payload = {
        "jsonrpc": "2.0",
        "method": "getStakeActivation",
        "params": [stake_account],
        "id": 1
    }
    
    response = await make_request(API_URL, method="POST", payload=payload)
    if response is None:
        return {"error": "Failed to fetch stake activation"}
    return response


@mcp.tool(
    description="获取Solana供应信息"
)
async def get_supply() -> dict[str, Any]:
    """获取Solana供应信息"""
    payload = {
        "jsonrpc": "2.0",
        "method": "getSupply",
        "params": [{"excludeNonCirculatingAccountsList": False}],
        "id": 1
    }
    
    response = await make_request(API_URL, method="POST", payload=payload)
    if response is None:
        return {"error": "Failed to fetch supply info"}
    return response


@mcp.tool(
    description="获取Solana交易数量"
)
async def get_transaction_count() -> dict[str, Any]:
    """获取Solana交易数量"""
    payload = {
        "jsonrpc": "2.0",
        "method": "getTransactionCount",
        "params": [],
        "id": 1
    }
    
    response = await make_request(API_URL, method="POST", payload=payload)
    if response is None:
        return {"error": "Failed to fetch transaction count"}
    return response









if __name__ == "__main__":
    mcp.run(transport="sse")