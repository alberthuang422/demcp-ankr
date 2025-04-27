# Solana RPC MCP 服务

这是一个基于MCP框架的Solana RPC客户端服务，提供各种Solana区块链API的访问。

## 功能

- 查询账户余额和信息
- 获取代币账户信息
- 查询区块链网络状态
- 获取区块和交易信息
- 其他Solana RPC API

## 安装

### 使用Docker

```bash
# 构建Docker镜像
docker build -t solana-rpc-mcp .

# 运行容器
docker run -p 8080:8080 solana-rpc-mcp
```

### 本地安装

```bash
# 安装依赖
pip install -r requirements.txt

# 运行服务
python -m src.main
```

## 环境变量

- `API_URL` - Solana RPC API地址，默认使用Helius RPC

## API文档

服务启动后，可以通过MCP客户端访问以下工具：

- `get_account_balance` - 获取Solana账户余额
- `get_account_info` - 获取Solana账户信息
- `get_token_account_balance` - 获取代币账户余额
- `get_token_accounts_by_owner` - 获取所有者的代币账户
- 更多API请参考代码实现
