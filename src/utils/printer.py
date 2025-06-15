from enum import Enum


class Formatting(Enum):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'


class Printer:
    def show(
        self,
        formatting: Formatting,
        text: str,
        bold: bool = False,
        with_surrounding_underline: bool = False,
    ) -> None:
        if bold:
            text = f'{Formatting.BOLD.value}{text}'

        if with_surrounding_underline:
            underline = f'{"_" * 50}'
            text = f'{underline}\n{text}\n{underline}\n'

        print(f'{formatting.value}{text}{Formatting.ENDC.value}')

    def show_header(
        self,
        text: str,
        bold: bool = False,
        with_surrounding_underline: bool = True,
    ) -> None:
        self.show(
            Formatting.HEADER,
            text,
            bold,
            with_surrounding_underline,
        )

    def show_ok_blue(
        self,
        text: str,
        bold: bool = False,
        with_surrounding_underline: bool = False,
    ) -> None:
        self.show(
            Formatting.OKBLUE,
            text,
            bold,
            with_surrounding_underline,
        )

    def show_ok_green(
        self,
        text: str,
        bold: bool = False,
        with_surrounding_underline: bool = False,
    ) -> None:
        self.show(
            Formatting.OKGREEN,
            text,
            bold,
            with_surrounding_underline,
        )

    def show_error(
        self,
        text: str,
        bold: bool = False,
        with_surrounding_underline: bool = False,
    ) -> None:
        self.show(
            Formatting.FAIL,
            text,
            bold,
            with_surrounding_underline,
        )

    def show_error_bold(
        self,
        text: str,
        with_surrounding_underline: bool = False,
    ) -> None:
        self.show_error(
            text,
            bold=True,
            with_surrounding_underline=with_surrounding_underline,
        )

    def show_bold(
        self,
        text: str,
        with_surrounding_underline: bool = False,
    ) -> None:
        self.show(
            Formatting.BOLD,
            text,
            with_surrounding_underline=with_surrounding_underline,
        )


printer = Printer()
