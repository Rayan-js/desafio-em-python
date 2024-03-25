class PrintCor:
    def __init__(
        self,
        text=None,
        color=None,
        background=None,
        bold=False,
        underline=False,
        italic=False,
    ):
        self.text = text
        self.color = color
        self.background = background
        self.bold = bold
        self.underline = underline
        self.italic = italic

    def p_color(self, color, background=None):
        black = "\033[30m"
        red = "\033[31m"
        green = "\033[32m"
        yellow = "\033[33m"
        blue = "\033[34m"
        magenta = "\033[35m"
        cyan = "\033[36m"
        white = "\033[37m"

        colors = {
            "black": black,
            "red": red,
            "green": green,
            "yellow": yellow,
            "blue": blue,
            "magenta": magenta,
            "cyan": cyan,
            "white": white,
        }

        if color not in colors:
            print(f"Invalid color '{color}'")
            return ""

        result = colors[color]

        if background:
            bg_black = "\033[40m"
            bg_red = "\033[41m"
            bg_green = "\033[42m"
            bg_yellow = "\033[43m"
            bg_blue = "\033[44m"
            bg_magenta = "\033[45m"
            bg_cyan = "\033[46m"
            bg_white = "\033[47m"

            bgs = {
                "black": bg_black,
                "red": bg_red,
                "green": bg_green,
                "yellow": bg_yellow,
                "blue": bg_blue,
                "magenta": bg_magenta,
                "cyan": bg_cyan,
                "white": bg_white,
            }

            if background not in bgs:
                print(f"Invalid background color '{background}'")
                return ""

            result += bgs[background]

        return result

    def print_text(self, text):
        code = ""
        if self.color:
            code += self.p_color(self.color, self.background)
        if self.bold:
            code += "\033[1m"
        if self.underline:
            code += "\033[4m"
        if self.italic:
            code += "\033[3m"

        return print(f"{code}{text}\033[0m")


# Pre-sets


def pRed(text):

    # Class instances
    print_red = PrintCor(color="red", bold=True)
    red = print_red.print_text(f"{text} \n")
    return red


def pGreen(text):

    # Class instances
    print_green = PrintCor(color="green", bold=True)
    green = print_green.print_text(f"{text} \n")
    return green


def pYellow(text):

    # Class instances
    print_yellow = PrintCor(color="yellow")
    yellow = print_yellow.print_text(f"{text} \n")
    return yellow


def pCyan(text):

    # Class instances
    print_cyan = PrintCor(color="cyan", bold=True)
    cyan = print_cyan.print_text(f"{text} \n")
    return cyan


pGreen("Enjoy and have fun :D !!!")
