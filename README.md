# BZ-Cyberpunk

A neon-noir dark theme for IntelliJ IDEA and other JetBrains IDEs. Its colors come
from the UI of [Cyberpunk 2077](https://www.cyberpunk.net) and the look of
*Cyberpunk: Edgerunners*.

## Install

- **Marketplace:** Settings > Plugins > Marketplace, search for **BZ-Cyberpunk**.
- **From a jar:** download `bz-cyberpunk-<version>.jar` from the
  [releases](https://github.com/blazexyz/bz-cyberpunk/releases), then go to
  Settings > Plugins > gear icon > Install Plugin from Disk...

Then pick the theme in Settings > Appearance & Behavior > Appearance > Theme.

## Variants

| Theme | UI | IDE versions |
|---|---|---|
| **BZ-Cyberpunk** | New UI (inherits *Dark*) | 2023.3+ |
| **BZ-Cyberpunk Islands** | Islands UI (inherits *Islands Dark*) | 2025.3+ |

Both variants use the **BZ-Cyberpunk** editor color scheme.

## Palette

| Role | Color | Source |
|---|---|---|
| Keywords, selection, tab underline | `#ff5952` HUD red | Cyberpunk 2077 UI |
| Caret, default buttons, TODOs, warnings | `#fcee0a` signature yellow | Cyberpunk 2077 logo / UI |
| Methods, links, focus rings | `#00f0ff` netrunner cyan | Cyberpunk 2077 UI |
| Types (classes, enums, records) | `#4dffa8` acid green | Edgerunners |
| Fields | `#ff4fd8` neon magenta | Edgerunners |
| Numbers, constants | `#b07cff` braindance violet | Cyberpunk 2077 / Edgerunners |
| Annotations, labels | `#ff9e45` orange | Cyberpunk 2077 UI |
| Strings | `#f2e46a` soft yellow | — |
| Errors | `#ff003c` glitch red | Cyberpunk 2077 logo glitch |
| Backgrounds | `#050409` to `#5d5476` indigo-black ramp | Night City at night |

## Language support

The scheme sets explicit colors for **Java**, including records, enums, type
parameters, annotations, static imports, reassigned variables and Javadoc. It
also covers Kotlin, Python, Rust, JavaScript/TypeScript, HTML/XML/CSS, Markdown,
YAML/JSON/properties and regular expressions, plus the console, logs, the
debugger, diffs and VCS. Any other language falls back to the base `DEFAULT_*`
colors.

To try it, open `syntax_tests/JavaSyntax.java` or `syntax_tests/python_syntax.py`.

See [notes.txt](notes.txt) for how to edit and build the theme.
