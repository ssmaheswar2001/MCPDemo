# MCPDemo

A demonstration project using Model Context Protocol (MCP) with multiple servers for math operations and weather information.

## Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd MCPDemo
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file in the root directory with the following content:
   ```
   GROQ_API_KEY=your_actual_groq_api_key_here
   ```
   
   **Note:** Get your Groq API key from [Groq Console](https://console.groq.com/)

4. **Run the demo:**
   ```bash
   python client.py
   ```

## Project Structure

- `client.py` - Main client that connects to MCP servers
- `mathserver.py` - MCP server providing math operations (add, multiply)
- `weather.py` - MCP server providing weather information
- `main.py` - Simple hello world script

## Features

- **Math Server**: Provides addition and multiplication operations
- **Weather Server**: Provides weather information (demo implementation)
- **Multi-Server Client**: Connects to multiple MCP servers simultaneously
- **LangChain Integration**: Uses LangChain for agent-based interactions

## Security

- API keys are loaded from environment variables
- `.env` files are gitignored to prevent accidental commits
- No hardcoded secrets in the codebase
