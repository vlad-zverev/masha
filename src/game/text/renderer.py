from typing import Optional

from pygame.color import Color
from pygame.font import Font
from pygame.surface import Surface

from .font import get_default_font


class TextRenderer:
    def __init__(self, font: Optional[Font] = None) -> None:
        self._font = font or get_default_font()

    def render(self, text: str, color: Color) -> Surface:
        return self._font.render(text, True, color)  # noqa: WPS425
