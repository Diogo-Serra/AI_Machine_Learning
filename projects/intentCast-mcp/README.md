# intentCast-mcp

This project lives in its own repository:
[github.com/Diogo-Serra/intentCast-mcp](https://github.com/Diogo-Serra/intentCast-mcp)

An MCP server that turns natural language prompts into structured, schema-valid
function calls, using a local LLM (Qwen/Qwen3-0.6B) with constrained decoding
so the model can only ever produce a registered function name and correctly
typed parameters - never broken JSON, hallucinated fields, or wrong types.

See the repository's README for installation, client setup (Claude Desktop,
Cursor, GitHub Copilot CLI, VS Code), and usage instructions.
