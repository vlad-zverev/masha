import pygame
from pygame.surface import Surface

from .types import Backgrounds, Beavers, LoadedImages
from .utils import resize


class Loader:
    CONTENT_DIR = './content'
    BEAVER_NEW_X = 150
    BACKGROUND_NEW_X = 1280

    def load_all(self) -> LoadedImages:
        return LoadedImages(
            forest=self.load_forest(),
            thinking_beaver=self.load_thinking_beaver(),
            attacking_beaver=self.load_attacking_beaver(),
            defending_beaver=self.load_defending_beaver(),
        )

    def load_forest(self) -> Surface:
        return self.load_background(Backgrounds.Forest)

    def load_thinking_beaver(self) -> Surface:
        return self.load_beaver(Beavers.Thinking)

    def load_attacking_beaver(self) -> Surface:
        return self.load_beaver(Beavers.Attacking)

    def load_defending_beaver(self) -> Surface:
        return self.load_beaver(Beavers.Defending)

    def load_background(self, background: Backgrounds) -> Surface:
        return resize(
            pygame.image.load(f'{self.CONTENT_DIR}/backgrounds/{background.value}'),
            self.BACKGROUND_NEW_X,
        )

    def load_beaver(self, beaver: Beavers) -> Surface:
        return resize(
            pygame.image.load(f'{self.CONTENT_DIR}/beavers/{beaver.value}'),
            self.BEAVER_NEW_X,
        )
