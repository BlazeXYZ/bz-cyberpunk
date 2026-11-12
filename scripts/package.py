"""Packages the theme into an installable plugin jar.

    python ./scripts/package.py

Runs the builder first, then writes dist/bz-cyberpunk-<version>.jar. The
version comes from resources/META-INF/plugin.xml. The jar can be installed with
Settings > Plugins > gear icon > Install Plugin from Disk..., or uploaded to the
JetBrains Marketplace.
"""
import os
import re
import subprocess
import sys
import zipfile

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
RESOURCES = os.path.join(ROOT, 'resources')
DIST = os.path.join(ROOT, 'dist')
BUILDER = os.path.join(ROOT, 'scripts', 'builder', 'builder.py')

# Everything the plugin needs at runtime, relative to /resources.
REQUIRED = [
    'META-INF/plugin.xml',
    'META-INF/pluginIcon.svg',
    'bz-cyberpunk.theme.json',
    'bz-cyberpunk-islands.theme.json',
    'bz-cyberpunk.xml',
]


def main():
    subprocess.run([sys.executable, BUILDER], check=True)

    with open(os.path.join(RESOURCES, 'META-INF', 'plugin.xml'), encoding='utf-8') as f:
        version = re.search(r'<version>([^<]+)</version>', f.read()).group(1).strip()

    missing = [p for p in REQUIRED if not os.path.isfile(os.path.join(RESOURCES, p))]
    if missing:
        sys.exit(f'Missing resources: {missing}')

    os.makedirs(DIST, exist_ok=True)
    jar_path = os.path.join(DIST, f'bz-cyberpunk-{version}.jar')
    with zipfile.ZipFile(jar_path, 'w', zipfile.ZIP_DEFLATED) as jar:
        jar.writestr('META-INF/MANIFEST.MF', 'Manifest-Version: 1.0\r\n\r\n')
        for rel in REQUIRED:
            jar.write(os.path.join(RESOURCES, rel), rel)
        license_path = os.path.join(ROOT, 'LICENSE')
        if os.path.isfile(license_path):
            jar.write(license_path, 'META-INF/LICENSE')

    print('Packaged', jar_path)


if __name__ == '__main__':
    main()
