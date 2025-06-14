from dataclasses import dataclass


@dataclass
class Stats:
    successes: int = 0
    masturbations: int = 0
    paedophilic_attempts: int = 0
    incest_attempts: int = 0

    def __str__(self) -> str:
        return (
            f'Successes: {self.successes}\nMasturbations: {self.masturbations}\n'
            f'Paedophilic attempts: {self.paedophilic_attempts}\nIncest attempts: {self.incest_attempts}'
        )
