import sys
import time
import threading

from pyspin import spin
from pyspin.spin import make_spin, Default


class Spinner:
    def __init__(self, message, spinning=False, frames=spin.Default):
        self.message = message
        self.spinning = spinning
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
        print('.. Done.')

    @property
    def is_spinning(self):
        return self.spinning


def create_spinner(message):
    spinner = Spinner(message)
    return spinner_factory(spinner)


def spinner_factory(spinner):
    return [
        lambda *_: spinner.start_spinner(),
        lambda *_: spinner.stop_spinner()
    ]


__all__ = ['create_spinner', 'Spinner', 'make_spin', 'Default']
