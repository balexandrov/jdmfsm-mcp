# Connecting the jdmfsm MCP server

Server: `https://jdmfsm.info/mcp`. Streamable HTTP, public, read-only, no sign-in.
About, privacy and terms: https://jdmfsm.info/Auto/mcp.html

## Claude Code

```
claude mcp add --transport http jdmfsm https://jdmfsm.info/mcp
```

Or as a plugin:

```
/plugin marketplace add balexandrov/jdmfsm-mcp
/plugin install jdmfsm@jdmfsm
```

## Claude (claude.ai, desktop)

Settings → Connectors → Add custom connector → URL `https://jdmfsm.info/mcp`.

## Codex CLI

In `~/.codex/config.toml`:

```toml
[mcp_servers.jdmfsm]
url = "https://jdmfsm.info/mcp"
```

## Gemini CLI

```
gemini extensions install https://github.com/balexandrov/jdmfsm-mcp
```

## Cursor, VS Code, Windsurf and other MCP clients

Add an HTTP server entry:

```json
{
  "mcpServers": {
    "jdmfsm": { "type": "http", "url": "https://jdmfsm.info/mcp" }
  }
}
```
