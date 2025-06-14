class Clock:
    def __init__(self) -> None:
        self._counter = 0

    @property
    def current_tick(self) -> int:
        return self._counter

    def tick(self) -> None:
        self._counter += 1
