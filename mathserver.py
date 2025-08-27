from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two numbers
    """
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """
    Multiply two numbers
    """
    return a * b

# The transport="stdio" argument tell the server to:
# Use standard inptu/output (stdin and stdout) to receive and respond to tool function calls.

if __name__ == "__main__":
    mcp.run(transport="stdio")
