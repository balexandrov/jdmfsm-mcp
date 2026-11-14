# JDM Factory Service Manuals

Look things up in the factory service manuals a dealer workshop uses. The library at
[jdmfsm.info](https://jdmfsm.info) holds more than 2,000 manuals for Nissan, Infiniti, Toyota, Lexus,
Honda, Mazda, Subaru, Mitsubishi, Suzuki, Daihatsu, Isuzu, Hyundai and Jeep.

Tell Claude the car (model and year, a chassis code like S15 or BM, or the VIN) and it finds the right
manual: service manual, wiring diagrams or body repair manual. Then look up a trouble code such as
P0340 to get the fault, its causes and the diagnosis pages, or search for a job or a part (timing
chain, camshaft position sensor, brake bleeding) and read the pages themselves. Wiring diagrams,
connector views and illustrations come back as page images.

Every answer links to the exact page of the manual, so you can open it and check it against your car.

## Install

```
/plugin marketplace add balexandrov/jdmfsm-mcp
/plugin install jdmfsm@jdmfsm
```

Nothing else to set up. The plugin connects Claude to the public MCP server at `https://jdmfsm.info/mcp`; there is no
account or sign-in.

## Try

- What does P0340 mean on my 2004 Nissan Sentra 1.8?
- Timing chain replacement on a 2014 Mazda3 2.0
- Wiring diagram for the fuel pump on a Toyota Hilux

## Tools

| Tool | What it does |
|---|---|
| `find_manuals` | the manuals for a car, by model, year, chassis code or VIN |
| `get_contents` | a manual's sections and bookmarks |
| `lookup_dtc` | a trouble code in one manual: fault, causes, diagnosis pages |
| `search` | a job, part or term in one manual |
| `read_pages` | the text of pages |
| `page_image` | a page as an image (wiring diagrams, illustrations) |

All tools are read-only.

## Links

- About: https://jdmfsm.info/Auto/mcp.html
- Support: https://jdmfsm.info/Auto/support.html
- Privacy: https://jdmfsm.info/Auto/privacy.html
- Terms: https://jdmfsm.info/Auto/terms.html
