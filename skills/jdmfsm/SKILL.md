---
name: jdmfsm
description: Looks up repairs in real factory service manuals (2,000+ for Nissan, Infiniti, Toyota, Lexus, Honda, Mazda, Subaru, Mitsubishi, Suzuki, Daihatsu, Isuzu, Hyundai, Kia and Jeep) through the jdmfsm.info MCP server, and answers with links to the exact manual pages. Use it when someone asks about a trouble code (P0340, C1234), a repair procedure, torque specs, fluid capacities, timing marks or a wiring diagram for a specific car.
---

# Factory service manuals (jdmfsm.info)

Answer car repair questions from the manufacturer's own service manual, not from memory, and give
the page link so the user can check it against their car.

## Requirement: the jdmfsm MCP server

This skill uses the public, read-only MCP server at `https://jdmfsm.info/mcp` (streamable HTTP, no
account, no key). It is the only network service involved; the skill has no scripts. If the tools
`find_manuals`, `lookup_dtc`, `search`, `read_pages`, `page_image` and `get_contents` are not
available, tell the user to connect the server first. See [references/connect.md](references/connect.md).

## Workflow

1. **Pin down the car.** You need the model and year at least; the engine, chassis code (S15, BM, A33)
   or VIN make the match certain. Ask for what is missing rather than guess, because manuals differ
   between generations and engines.
2. **Find the manual:** `find_manuals("2004 Sentra 1.8")`. Pick the result whose year, chassis code
   and engine match, and whose `type` fits the job: a service manual for repairs and diagnosis,
   a wiring diagram book for circuits, a body repair manual for panels and dimensions.
3. **Look it up in that one manual.** Every lookup takes the `manual` from step 2.
   - Trouble code: `lookup_dtc("P0340", manual)` returns the fault, likely causes and the diagnosis pages.
   - Job, part or spec: `search("timing chain tensioner", manual)`. Use the manual's own terms
     (part and system names), not sentences. Words that are not in the index come back with similar
     terms that are; retry with one of those.
   - Unsure where to look: `get_contents(manual)` lists its sections and bookmarks.
4. **Read the pages:** `read_pages(file, page)` for text. Use `page_image(file, page)` for wiring
   diagrams, connector views, exploded views and anything else that is mostly drawing.
5. **Answer with the source.** Quote specs and steps as the manual gives them (values, units,
   sequence) and include the page `url` for every page you used.

## Rules

- One car at a time. If the user changes cars, go back to step 1.
- If no manual matches, say so plainly and name the closest ones found. Do not fill the gap
  with figures from memory.
- If `search` says a code (engine, transmission, chassis) is not in this manual but in another
  model folder, follow that pointer: it usually means the wrong manual was picked.
- Torque values, clearances and capacities come only from pages you have read in this session.
- Repair work can injure people or damage the car. Mention safety steps the manual itself gives
  (depressurising the fuel system, disconnecting the battery, supporting the car on stands).

## Examples

- "What does P0340 mean on my 2004 Nissan Sentra 1.8?"
- "Timing chain replacement on a 2014 Mazda3 2.0"
- "Fuel pump wiring diagram for a 2008 Toyota Hilux"
