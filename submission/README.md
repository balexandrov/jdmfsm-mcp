# Directory submissions

What each directory asks for, answered once. Paste from here.

| Directory | Where | What is submitted |
|---|---|---|
| Claude — MCP connector | https://claude.ai/directory/manage → Submit new → **MCP connector** | the server URL |
| Claude — plugin bundle | https://claude.ai/directory/manage → Submit new → **Plugin bundle** | this repo, folder `plugins/jdmfsm` |
| MCP Registry | `mcp-publisher login github` then `mcp-publisher publish` in the repo root | `server.json` |
| ChatGPT apps | https://platform.openai.com/apps | `dist/jdmfsm-plugin.zip` (`python build_chatgpt_zip.py`) and `chatgpt-app-submission.json` |

Submit the Claude listings from the claude.ai account that should own them for good: the first
organization to submit a repository folder holds that listing.

## Shared answers

| Field | Answer |
|---|---|
| Server URL | `https://jdmfsm.info/mcp` |
| Name | JDM Factory Service Manuals |
| One-liner | Search 2,000+ factory service manuals for Japanese cars and Jeep: trouble codes, repair procedures and wiring diagrams, with a link to every page. |
| Documentation URL | https://jdmfsm.info/Auto/mcp.html |
| Privacy policy URL | https://jdmfsm.info/Auto/privacy.html |
| Terms URL | https://jdmfsm.info/Auto/terms.html |
| Support | https://jdmfsm.info/Auto/support.html · jdmfsm1@gmail.com |
| Icon | `plugins/jdmfsm/assets/icon.png` (512×512 PNG) |
| Slug | `jdmfsm` |
| Categories | Education / Research / Reference — whichever the form offers |
| Company | jdmfsm.info · https://jdmfsm.info · jdmfsm1@gmail.com |
| Authentication | None. Every tool is public and read-only; there are no accounts. |
| Prerequisites for users | None: no account, plan or setup. |
| Reads or writes | Reads only. |
| Underlying API | Our own: the server and the manual index are run by jdmfsm.info. |
| Personal health data | No. |
| Sponsored content | No. |

### Description

Look things up in the factory service manuals a dealer workshop uses. The library at jdmfsm.info
holds more than 2,000 manuals for Nissan, Infiniti, Toyota, Lexus, Honda, Mazda, Subaru, Mitsubishi,
Suzuki, Daihatsu, Isuzu, Hyundai and Jeep.

Tell it the car (model and year, a chassis code like S15 or BM, or the VIN) and it finds the right
manual: service manual, wiring diagrams or body repair manual. Then look up a trouble code such as
P0340 to get the fault, its causes and the diagnosis pages, or search for a job or a part (timing
chain, camshaft position sensor, brake bleeding) and read the pages themselves. Wiring diagrams,
connector views and illustrations come back as page images.

Every answer links to the exact page of the manual, so you can open it and check it against your car.

### Use cases

1. **Explain a trouble code.** "What does P0340 mean on my 2004 Nissan Sentra 1.8?" — finds the 2004
   B15 Sentra service manual and returns the P0340 camshaft position sensor pages for the QG18DE,
   with the fault, its causes and the diagnosis steps.
2. **Find a repair procedure.** "How do I replace the timing chain on a 2014 Mazda3 2.0?" — finds the
   BM Mazda3 manual and the timing chain procedure for the SKYACTIV-G 2.0, summarises the steps and
   links to the pages.
3. **Show a wiring diagram.** "Show me the fuel pump wiring diagram for a 2010 Toyota Hilux (KUN16)." —
   finds the Hilux wiring diagram manual and returns the fuel pump circuit as a page image.
4. **Identify the manual.** "Which service manual covers a Nissan S15 Silvia?" — lists the S15 manuals
   with their years, types and links.

### Tools

| Tool | Title | Annotations |
|---|---|---|
| `find_manuals` | Find manuals | readOnly, not destructive, idempotent, closed world |
| `get_contents` | Table of contents | same |
| `search` | Search a manual | same |
| `lookup_dtc` | Look up a trouble code | same |
| `read_pages` | Read pages | same |
| `page_image` | Page image | same |

## Claude plugin bundle

| Field | Answer |
|---|---|
| Repository | https://github.com/balexandrov/jdmfsm-mcp |
| Branch | `main` |
| Plugin folder | `plugins/jdmfsm` |

Check before submitting: `claude plugin validate ./plugins/jdmfsm --profile directory`.
