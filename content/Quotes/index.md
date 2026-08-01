---
title: Quotes
draft: "false"
---

```base
formulas:
  Untitled: ""
properties:
  file.name:
    displayName: Quote
  note.Quote by:
    displayName: Said by
  note.Field:
    displayName: Field/Known for
views:
  - type: table
    name: Table
    filters:
      and:
        - file.hasTag("Quote")
    order:
      - file.name
      - Quote by
      - Field
    sort:
      - property: formula.Untitled
        direction: DESC

```
