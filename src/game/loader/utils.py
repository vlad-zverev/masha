import pygame


def resize(
    surface: pygame.surface.Surface,
    new_x: int = 150,
) -> pygame.surface.Surface:
    current_x, current_y = surface.get_size()

    new_y = new_x / current_x * current_y

    return pygame.transform.scale(surface, (new_x, new_y))
