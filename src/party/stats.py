from dataclasses import dataclass


@dataclass
class Stats:
    successes: int = 0
    masturbations: int = 0
    homo_refused_attempts: int = 0
    incest_refused_attempts: int = 0
    paedophilic_incidents: int = 0

    def __str__(self) -> str:
        return (
            f'Successes: {self.successes}\n'
            f'Masturbations: {self.masturbations}\n'
            f'Homo refused attempts: {self.homo_refused_attempts}\n'
            f'Incest refused attempts: {self.incest_refused_attempts}\n'
            f'Paedophilic incidents: {self.paedophilic_incidents}'
        )
