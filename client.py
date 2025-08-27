from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
import asyncio, os

load_dotenv()

async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["mathserver.py"],
                "transport": "stdio",
            },
            "weather": {
                "command": "python",
                "args": ["weather.py"],
                "transport": "streamable-http",
            },
        }
    )

    # Load API key from environment variable
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("GROQ_API_KEY environment variable is required. Please set it in your .env file.")
    os.environ["GROQ_API_KEY"] = groq_api_key

    tools = await client.get_tools()

    model = ChatGroq(model_name="qwen_qwq-32b")

    agent = create_react_agent(model, tools)

    math_response = await agent.ainvoke({
        "messages": [{"role": "user", "content": "What is (3+5)x12?"}]
    })
    print("Math Response:", math_response['messages'][-1].content)

asyncio.run(main())
