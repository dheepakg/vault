---
title: Books
---
The notes & highlights from the books are consolidated here. 

Some of the books are huge (like textbooks), their chapters are arranged as individual files. The non-fictions in most cases are available as single file.

```base
views:
  - type: cards
    name: Card View
    filters:
      and:
        - file.hasTag("book")
    order: []
    sort:
      - property: started on
        direction: DESC
    image: note.cover
    imageAspectRatio: 0.95
    imageFit: contain
  - type: table
    name: Table View
    filters:
      and:
        - file.hasTag("book")
    order:
      - title
      - Author
      - started on
      - category
    sort:
      - property: started on
        direction: DESC
    cardSize: 200

```
