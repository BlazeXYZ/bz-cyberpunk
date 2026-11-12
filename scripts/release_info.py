"""Prints release info read from resources/META-INF/plugin.xml.

    python ./scripts/release_info.py version   -> 1.0.0
    python ./scripts/release_info.py notes     -> Markdown change notes for that version

Used by .github/workflows/release.yml.
"""
import html
import os
import re
import sys

PLUGIN_XML = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..',
                          'resources', 'META-INF', 'plugin.xml')


def read_plugin_xml():
    with open(PLUGIN_XML, encoding='utf-8') as f:
        return f.read()


def version(xml):
    return re.search(r'<version>\s*([^<]+?)\s*</version>', xml).group(1)


def notes(xml, ver):
    """Turns the <b>VERSION</b><ul><li>...</li></ul> block into Markdown bullets."""
    block = re.search(
        r'<b>\s*' + re.escape(ver) + r'\s*</b>\s*<ul>(.*?)</ul>', xml, re.S)
    if not block:
        return f'BZ-Cyberpunk {ver}'
    items = re.findall(r'<li>(.*?)</li>', block.group(1), re.S)
    lines = []
    for item in items:
        text = re.sub(r'<[^>]+>', '', item)        # drop inline HTML tags
        text = html.unescape(' '.join(text.split()))  # collapse wrapped lines
        lines.append(f'- {text}')
    return '\n'.join(lines)


def main():
    xml = read_plugin_xml()
    what = sys.argv[1] if len(sys.argv) > 1 else 'version'
    if what == 'version':
        print(version(xml))
    elif what == 'notes':
        print(notes(xml, version(xml)))
    else:
        sys.exit(f'Unknown argument: {what} (use "version" or "notes")')


if __name__ == '__main__':
    main()
