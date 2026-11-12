"""Python syntax highlighting test for the BZ-Cyberpunk theme.

Open this file with the theme active to check every Python color.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Generic, TypeVar

T = TypeVar('T')
MAX_RAM = 0x2077
CHROME_LIMIT = 3.14e2
SIGNAL = 6 + 9j


@dataclass
class Implant(Generic[T]):
    """A piece of cyberware.

    :param name: what the ripperdoc calls it
    """
    name: str
    slots: list[T] = field(default_factory=list)
    _humanity: float = 100.0

    @property
    def humanity(self) -> float:
        return self._humanity

    @staticmethod
    def overclock(ram: int, *, boost: int = 2) -> int:
        return min(ram * boost, MAX_RAM)

    def install(self, slot: T) -> None:
        self.slots.append(slot)
        self._humanity -= 7.5
        if self._humanity <= 0:
            raise RuntimeError(f'{self.name} went cyberpsycho at {self._humanity:.1f}%')


async def jack_in(port: int) -> bytes:
    payload = b'\x00ICE\xff breach'
    raw = r'C:\deck\daemons\new'
    bad = 'Bad escape: \q and good: \n\t'
    return payload + raw.encode() + bad.encode()


def scan(text: str) -> list[str]:
    pattern = re.compile(r'(?P<gig>[A-Z]{3,})-\d+\.?')
    found = [m.group('gig') for m in pattern.finditer(text) if m]
    lookup = {gig: len(gig) for gig in found}
    flag = None if not lookup else True
    # TODO: route this through the Blackwall proxy
    print(*found, sep=', ', end='\n')
    return sorted(lookup, key=lambda g: lookup[g], reverse=flag is True)


def main():
    deck = Implant[str]('Sandevistan')
    deck.install('spine')
    print(deck.humanity, Implant.overclock(512, boost=4))
    print(scan('ARASAKA-1 MILITECH-22 maelstrom-3'))
    print(undefined_symbol)  # unresolved reference


if __name__ == '__main__':
    main()
