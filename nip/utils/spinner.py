import sys
import time
import threading

from pyspin import spin


class Spinner:
    def __init__(self, message, spinning=False, frames=spin.Default, done=''):
        self.message = message
        self.spinning = spinning
        self.done_message = done
        self._spinner = spin.Spinner(frames)
        self._thread = threading.Thread(target=self._spin)
        self._thread.name = 'NIP_SPINNER'
        self._thread.daemon = True

    def _async_spin(self):
        self._thread.start()

    def _spin(self):
        self.spinning = True
        while self.is_spinning:
            print(f"\r{self._spinner.next()} {self.message}", end="")
            sys.stdout.flush()
            time.sleep(0.1)

    def start_spinner(self):
        self._async_spin()

    def stop_spinner(self):
        self.spinning = False
        print(self.done_message)

    @property
    def is_spinning(self):
        return self.spinning


def spinner_factory(spinner):
    return [
        lambda *_, **__: spinner.start_spinner(),
        lambda *_, **__: spinner.stop_spinner()
    ]


def create_spinner(message, end='.. Done.'):
    spinner = Spinner(message, done=end)
    return spinner_factory(spinner)
