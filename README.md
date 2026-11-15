# jdmfsm — factory service manuals for AI assistants

Connect Claude, ChatGPT or another AI assistant to the factory service manuals at
[jdmfsm.info](https://jdmfsm.info): more than 2,000 manuals for Nissan, Infiniti, Toyota, Lexus,
Honda, Mazda, Subaru, Mitsubishi, Suzuki, Daihatsu, Isuzu, Hyundai and Jeep. Tell it the car (model
and year, a chassis code or the VIN) and ask about a trouble code, a repair job or a wiring diagram;
it answers from the manual with a link to the exact page. Free, no sign-in.

The server is a remote MCP server:

```
https://jdmfsm.info/mcp
```

This repository holds the packages and listings that point assistants at it. The server itself is
not here.

## Add it

| App | How |
|---|---|
| **Claude** (claude.ai, desktop, mobile) | Settings → Connectors → Add custom connector, paste the address. |
| **Claude Code** | `/plugin marketplace add balexandrov/jdmfsm-mcp` then `/plugin install jdmfsm@jdmfsm` (server and skill) — or the server only: `claude mcp add --transport http jdmfsm https://jdmfsm.info/mcp` |
| **ChatGPT** | Settings → Apps & Connectors → Advanced → Developer mode, then Create, paste the address, no authentication. |
| **Codex CLI** | in `~/.codex/config.toml`: `[mcp_servers.jdmfsm]` with `url = "https://jdmfsm.info/mcp"` |
| **Gemini CLI** | `gemini extensions install https://github.com/balexandrov/jdmfsm-mcp` |
| **VS Code** | `code --add-mcp '{"name":"jdmfsm","type":"http","url":"https://jdmfsm.info/mcp"}'` |
| **Cursor** | in `~/.cursor/mcp.json`: `{"mcpServers": {"jdmfsm": {"url": "https://jdmfsm.info/mcp"}}}` |
| **Anything else** | add a remote (streamable HTTP) MCP server with the address. |

ChatGPT asks "Allow file materialization?" when it shows a manual page or wiring diagram: allow it,
that is the page image.

## The skill (optional)

A skill teaches the assistant the routine: pin down the car, pick the right manual, look up the code
or job in it, show the page and link it. It needs the server connected (above).

| App | How |
|---|---|
| **Claude** (claude.ai, desktop) | Download [jdmfsm-skill.zip](https://github.com/balexandrov/jdmfsm-mcp/releases/latest/download/jdmfsm-skill.zip), then Settings → Capabilities → Skills → Upload skill. |
| **Claude Code** | included in the plugin above. |
| **Other skill-aware agents** | unzip it into the agent's skills folder (`jdmfsm/SKILL.md`). |

## Ask

- 2006 Sentra 1.8 shows P0340. What do I check?
- Fuel pump wiring diagram for a Z33 350Z.
- Torque specs for a QR25DE timing chain job.
- VIN JN1… — how do I replace the front brake pads?

Check the linked page before you trust a number.

## Tools

| Tool | What it does |
|---|---|
| `find_manuals` | the manuals for a car, by model, year, chassis code or VIN |
| `get_contents` | a manual's sections and bookmarks |
| `lookup_dtc` | a trouble code in one manual: fault, causes, diagnosis pages |
| `search` | a job, part or term in one manual |
| `read_pages` | the text of pages |
| `page_image` | a page as an image (wiring diagrams, illustrations) |

All tools are read-only and change nothing.

## What is in this repository

| Path | For |
|---|---|
| `.claude-plugin/marketplace.json` | the Claude Code plugin marketplace |
| `plugins/jdmfsm/` | the plugin: `.claude-plugin/plugin.json` (Claude), `.codex-plugin/plugin.json` (ChatGPT / Codex), the shared `.mcp.json`, the skill `skills/jdmfsm/` and icons |
| `gemini-extension.json` | the Gemini CLI extension |
| `server.json` | the listing in the [MCP Registry](https://registry.modelcontextprotocol.io) |
| `submission/` | material for the directory reviews (test cases, tool justifications) |
| `build_chatgpt_zip.py` | builds `dist/jdmfsm-plugin.zip`, the ChatGPT upload |
| `build_skill_zip.py` | builds `dist/jdmfsm-skill.zip`, the skill, attached to each [release](https://github.com/balexandrov/jdmfsm-mcp/releases) |

## Links

[About](https://jdmfsm.info/Auto/mcp.html) ·
[Support](https://jdmfsm.info/Auto/support.html) ·
[Privacy](https://jdmfsm.info/Auto/privacy.html) ·
[Terms](https://jdmfsm.info/Auto/terms.html)
