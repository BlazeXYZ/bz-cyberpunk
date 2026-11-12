"""Builds the files in /resources from the sources in this folder.

  1. BZ-Cyberpunk.icls (palette color names) -> resources/bz-cyberpunk.xml (hex)
  2. resources/bz-cyberpunk.theme.json + islands_overrides.json
       -> resources/bz-cyberpunk-islands.theme.json

Run from anywhere:  python ./scripts/builder/builder.py
"""
import copy
import json
import os
import re
import sys

CUR_DIR = os.path.dirname(os.path.realpath(__file__))
RESOURCES = os.path.join(CUR_DIR, '..', '..', 'resources')
THEME_JSON_PATH = os.path.join(RESOURCES, 'bz-cyberpunk.theme.json')
ISLANDS_JSON_PATH = os.path.join(RESOURCES, 'bz-cyberpunk-islands.theme.json')
ISLANDS_OVERRIDES_PATH = os.path.join(CUR_DIR, 'islands_overrides.json')
ICLS_PATH = os.path.join(CUR_DIR, 'BZ-Cyberpunk.icls')
OUTPUT_PATH = os.path.join(RESOURCES, 'bz-cyberpunk.xml')

HEX_RE = re.compile(r'^[0-9a-fA-F]{6}([0-9a-fA-F]{2})?$')


def resolve(name, colors, seen=()):
    """Resolves a palette name (which may point at another name) to '#rrggbb'."""
    value = colors[name]
    if value.startswith('#'):
        return value
    if value in seen:
        raise ValueError(f'Circular color reference: {name}')
    return resolve(value, colors, seen + (name,))


def build_color_scheme(colors):
    with open(ICLS_PATH, encoding='utf-8') as f:
        color_scheme = f.read()

    def replace(match):
        name = match.group(1)
        if name in colors:
            return f'value="{resolve(name, colors)[1:].lower()}"'
        if HEX_RE.match(name) or name.isdigit():
            return match.group(0)
        unresolved.add(name)
        return match.group(0)

    unresolved = set()
    color_scheme = re.sub(r'value="([^"]*)"', replace, color_scheme)
    if unresolved:
        sys.exit(f'Unknown palette names in {ICLS_PATH}: {sorted(unresolved)}')

    with open(OUTPUT_PATH, 'w', encoding='utf-8', newline='\n') as f:
        f.write(color_scheme)


def deep_merge(base, extra):
    for key, value in extra.items():
        if isinstance(value, dict) and isinstance(base.get(key), dict):
            deep_merge(base[key], value)
        else:
            base[key] = value
    return base


def build_islands_theme(theme):
    with open(ISLANDS_OVERRIDES_PATH, encoding='utf-8') as f:
        overrides = json.load(f)
    islands = deep_merge(copy.deepcopy(theme), overrides)
    with open(ISLANDS_JSON_PATH, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(islands, f, indent=2)
        f.write('\n')


def main():
    with open(THEME_JSON_PATH, encoding='utf-8') as f:
        theme = json.load(f)
    build_color_scheme(theme['colors'])
    build_islands_theme(theme)
    print('Built', os.path.normpath(OUTPUT_PATH))
    print('Built', os.path.normpath(ISLANDS_JSON_PATH))


if __name__ == '__main__':
    main()
