# Design System — jacquesmsfb GitHub Profile

## Product Context
- **What this is:** Personal GitHub profile README (the special `jacquesmsfb/jacquesmsfb` repo GitHub renders as a bio page).
- **Who it's for:** Anyone visiting the GitHub profile — recruiters, collaborators, casual visitors.
- **Space/industry:** Personal developer branding.
- **Project type:** Single static markdown page, no app, no build step.

## Aesthetic Direction
- **Direction:** Brutally minimal.
- **Decoration level:** None — no badges, stats widgets, or section headers.
- **Mood:** Quiet, understated delivery of a bold idea. The page reads as a short statement, not a resume.
- **Reference research:** 2026 consensus on GitHub profile READMEs favors short, opinionated, one-screen pages over stat-widget walls (see chat session sources: [UniLink](https://app.unilink.us/blog/github-readme-templates-2026), [Codeboards](https://codeboards.io/blog/github-profile-readme-guide)).

## Typography
GitHub's markdown sanitizer strips custom fonts/CSS from profile READMEs, so typography here means choosing between GitHub's own rendering primitives, not font files.
- **Art:** Rendered as SVG text using a monospace font stack (`ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace`) baked into the SVG itself, not the markdown.
- **Quote:** GitHub's native body font, italic, wrapped in `<sub>` for a smaller, quieter register than normal body text.
- **Scale:** No modular scale — only two typographic voices exist on this page (art, quote).

## Color
- **Approach:** Fully restrained — no accent color at all.
- **Art fill:** `#24292f` (dark charcoal) for GitHub's light theme, `#e6edf3` (off-white) for dark theme — matches GitHub's own default text colors so the art reads as native content, not a foreign image.
- **Quote:** Inherits GitHub's default text color automatically (plain markdown text, no custom styling).
- **Dark mode:** Handled via `<picture>` + `prefers-color-scheme` swapping between `dragon-light.svg` and `dragon-dark.svg` — the standard GitHub-profile-README pattern for theme-adaptive images (same technique used by theme-adaptive stats-card widgets).

## Spacing
- **Base unit:** N/A — one `<br><br>` between art and quote, everything else is `<div align="center">` default flow.
- **Density:** Spacious — nothing else on the page to be dense relative to.

## Layout
- **Approach:** Single centered column.
- **Max content width:** Art rendered at `width="640"` (soft target); GitHub's `img { max-width: 100% }` rule scales it down further on narrow/mobile viewports automatically since it's an image, not raw text.
- **Why an image and not raw ASCII text:** raw `<pre>` text can't be resized responsively (GitHub strips custom CSS from README HTML), so it would force horizontal scroll on mobile. SVG solves this while staying crisp at any zoom, unlike a rasterized PNG.

## Motion
- **Approach:** None. No animated typing effects, no GIFs — a deliberate rejection of the "animated bio" GitHub-profile cliché, which also directly serves the quiet aesthetic.

## Decisions Log
| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-07-12 | Rendered ASCII art as theme-adaptive SVG instead of raw `<pre>` text | Raw text can't scale responsively on GitHub (no custom CSS allowed); SVG + `img{max-width:100%}` gives real mobile support while staying pixel-crisp |
| 2026-07-12 | No stats widgets, badges, or links | User confirmed "quiet and minimal" over "built out further" — matches 2026 profile-README trend research |
| 2026-07-12 | Two SVG color variants via `<picture>`/`prefers-color-scheme` | Standard adaptive-image technique for GitHub profile READMEs; keeps art legible in both GitHub themes |
