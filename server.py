from fastmcp import FastMCP
import random

mcp = FastMCP("DiceServer")

mcp.tool()
def roll_dice(n:int):
    '''
    Roll a dice n times
    :param n: no. of trials
    '''
    try:
        result = [r for r in random.randint(0,6)]
        return result
    except Exception as e:
        return f"Error: {e}"
    

if __name__ == "__main__":
    mcp.run()
