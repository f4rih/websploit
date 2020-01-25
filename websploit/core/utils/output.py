from ezcolor import Style
import platform


class Output:

    def __init__(self):
        self._os = platform.system()
        self._style = Style()
        self._color_status = True
        if self._os == "Windows":
            self._color_status = False

    def _output(self, text, status):
        symbols = {
            "success": "[+]",
            "warning": "[!]",
            "error": "[-]",
            "info": "[>]"
        }

        if self._color_status:
            if status == "success":
                cp = self._style.add.foreground('green').prefix('done').bold.apply()
                cp(text)
            elif status == "warning":
                cp = self._style.add.foreground('yellow').prefix('warning').bold.apply()
                cp(text)
            elif status == "error":
                cp = self._style.add.foreground('red').prefix('error').bold.apply()
                cp(text)
            elif status == "info":
                cp = self._style.add.foreground('cyan').prefix('info').bold.apply()
                cp(text)
        else:
            print(f"{symbols[status]} {text}")


class CPrint(Output):
    def __init__(self):
        super().__init__()

    def success(self, text):
        self._output(text=text, status="success")

    def warning(self, text):
        self._output(text=text, status="warning")

    def error(self, text):
        self._output(text=text, status="error")

    def info(self, text):
        self._output(text=text, status="info")

