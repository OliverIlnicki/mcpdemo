from mcp.server.fastmcp import FastMCP
import time
import signal
import sys

#Handle SIGINT (Ctrl+C) gracefully
def signal_handler(sig, frame):
    print("Exiting...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Create a FastMCP instance
mcp = FastMCP(
    name="count-r",
    host="127.0.0.1",
    port=5000,
    timeout=30
)

# Define tool
@mcp.tool()
def count_r(word: str) -> int:
    """
    Count the numbers of "r" in a word

    """
    try: 
        if not isinstance(word, str):
            return 0
        return word.lower().count("r")
    except Exception as e:
        #return 0 as error
        return 0
    
if __name__ == "__main__":
    try:
   # Start the server
        print("Starting MCP server 'count-r' on 127.0.0.1:5000")
        mcp.run()
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)

    