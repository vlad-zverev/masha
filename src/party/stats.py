from dataclasses import dataclass

from ..printer import printer


@dataclass
class Stats:
    coituses: int = 0
    masturbations: int = 0
    homo_refused_attempts: int = 0
    dominance_mismatch_cases: int = 0
    interspecies_sex_refused_attempts: int = 0
    incest_refused_attempts: int = 0
    paedophilic_incidents: int = 0

    def __str__(self) -> str:
        return (
            f'Coituses: {self.coituses}\n'
            f'Masturbations: {self.masturbations}\n'
            f'Homo refused attempts: {self.homo_refused_attempts}\n'
            f'Dominance mismatch cases: {self.dominance_mismatch_cases}\n'
            f'Interspecies sex refused attempts: {self.interspecies_sex_refused_attempts}\n'
            f'Incest refused attempts: {self.incest_refused_attempts}\n'
            f'Paedophilic incidents: {self.paedophilic_incidents}'
        )

    def show(self) -> None:
        printer.show_header(str(self))
