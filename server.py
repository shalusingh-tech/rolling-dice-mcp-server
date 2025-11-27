from fastmcp import FastMCP
import random

mcp = FastMCP("DiceServer")

@mcp.tool()
def roll_dice(sides: int = 6) -> int:
    """Roll a dice with specified number of sides"""
    return random.randint(1, sides)

# CRITICAL: Local MCP servers MUST use stdio transport
if __name__ == "__main__":
    mcp.run(transport="stdio") 