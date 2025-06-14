from enum import Enum


class Color(Enum):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Printer:
    def show(self, color: Color, text: str) -> None:
        print(color.value + text + Color.ENDC.value)

    def show_header(self, text: str) -> None:
        self.show(Color.HEADER, text)

    def show_error(self, text: str) -> None:
        self.show(Color.FAIL, text)

    def show_error_bolded(self, text: str) -> None:
        print(Color.FAIL.value + Color.BOLD.value + text + Color.ENDC.value)

    def show_ok(self, text: str) -> None:
        self.show(Color.OKBLUE, text)

    def show_bold(self, text: str) -> None:
        self.show(Color.BOLD, text)


printer = Printer()
