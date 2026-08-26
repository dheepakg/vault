## Changelog generator

Generate a preview from Git history:

```sh
python3 scripts/generate_changelog.py
```

Write the generated entries to `content/Changelog.md`:

```sh
python3 scripts/generate_changelog.py --write
```

The generator groups changes by commit date, links files relative to the changelog,
normalizes historical paths to their current casing, and excludes Obsidian metadata,
trash, sync files, draft notes, image/PDF/base assets, and the changelog itself.