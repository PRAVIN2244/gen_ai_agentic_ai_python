from fastmcp import Client

MCP_SERVER_URL = "http://localhost:8081/mcp"

async def get_weather(city: str):

    async with Client(MCP_SERVER_URL) as client:

        result = await client.call_tool(
            "get_weather",
            {"city": city}
        )

        if result.is_error:
            raise Exception("MCP server returned an error")

        #print(result)

        return result.data