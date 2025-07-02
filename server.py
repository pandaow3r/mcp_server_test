from mcp.server.fastmcp import FastMCP
from app import dummyTool

# Initialize MCP server
mcp = FastMCP("your-mcp-name")

@mcp.tool()
async def weather_tool(location: str) -> str:
    return getWeatherInfo(location)

# Your another awsome tools can be added here
# @mcp.tool()
# async def another_awsome_tool(param: str) -> str:
#     """
#     Get better at AI.
#     """
#     # Do some awsome processing here
#     return "You are getting better at AI!"


if __name__ == "__main__":
    mcp.run(transport="stdio")
    