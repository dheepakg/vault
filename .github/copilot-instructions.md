# Copilot instructions

## Project overview

This repository is a personal digital garden built with Quartz v5. Markdown notes in
`content/` are compiled into the static site in `public/`. The site is deployed to
GitHub Pages by `.github/workflows/deploy.yaml` whenever `main` is updated.

## Build, test, and formatting commands

Use Node 22 or newer (the repository currently pins Node 22.16.0; CI uses Node 24)
and npm.

```sh
npm ci
npm run install-plugins       # install plugins listed in quartz.config.yaml
npx quartz build              # build content/ into public/
npx quartz build --serve      # build and serve a live preview on port 8080
npm run check                 # TypeScript noEmit check + Prettier check
npm run format                # format supported source and content files
npm test                      # run all tests
npm test -- quartz/util/path.test.ts  # run one test file
```

`npm run docs` serves the Quartz documentation content and is not the normal preview
for this site. `public/` is generated output and is ignored by Git. A normal
deployment runs `npm ci`, installs configured plugins, then runs `npx quartz build`.

## Architecture

- `quartz.ts` loads `quartz.config.yaml` and the computed layout, while
  `quartz.config.yaml` is the repository's source of truth for site settings and
  external plugin configuration.
- `quartz/build.ts` orchestrates a build: it discovers files under the content
  directory, parses Markdown, reports slug collisions, filters unpublished content,
  and emits HTML/assets/manifests into the output directory.
- `quartz/processors/parse.ts` runs Markdown and HTML transformer plugins. Filters
  implement publication decisions, emitters write generated files, and page-type
  plugins create virtual pages such as folder, tag, and other generated routes.
- `quartz/components/` contains the Preact page components and browser scripts.
  `quartz/plugins/` contains built-in plugin implementations grouped by lifecycle
  role. The plugin loader resolves configured community plugins, installs them under
  `.quartz/plugins/`, validates dependencies, and orders them before instantiation.
- `.quartz/plugins/` is plugin installation/cache material managed from the YAML
  configuration. Treat installed plugin source as generated unless deliberately
  working on a local plugin.

## Repository-specific conventions

- Content is Obsidian-compatible Markdown. Use YAML frontmatter between `---`
  delimiters for titles, tags, aliases, descriptions, and publication metadata.
  Existing notes use both quoted and unquoted scalar values; preserve the established
  shape when editing a note.
- Quartz link resolution is configured as `shortest` through the crawl-links plugin,
  so Obsidian wikilinks and shortest-path Markdown links are intentional.
- `content/.obsidian`, `content/private`, `content/templates`, and `base*.base`
  files are excluded by `ignorePatterns` in `quartz.config.yaml`. Do not remove or
  publish those paths accidentally.
- Draft handling is plugin-driven. The `remove-draft` plugin is enabled, and notes
  commonly use `draft: true` or `draft: false`; check frontmatter when a page should
  or should not appear in the generated site.
- Plugin ordering in `quartz.config.yaml` is significant. Keep explicit `order`
  values consistent with the processing stage, and run `npm run install-plugins`
  after changing plugin sources or options.
- TypeScript is strict, uses Preact's automatic JSX runtime, and intentionally
  omits semicolons. Prettier settings in `.prettierrc` are authoritative.
- Tests use Node's `node:test` API and `tsx --test`, despite the generic Quartz
  community-plugin guidance mentioning Vitest. Follow the existing test files and
  run the targeted test file when iterating.

