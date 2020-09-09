from PySide2.QtCore import QRunnable, Slot, QObject, Signal
import traceback
import sys


class WorkerSignals(QObject):
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)


class Worker (QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.is_alive = True

    @Slot()
    def run(self):
        while self.is_alive:
            try:
                self.fn(*self.args, **self.kwargs)
            except:
                traceback.print_exc()
                exctype, value = sys.exc_info()[:2]
                self.signals.error.emit((exctype, value, traceback.format_exc()))
            else:
                self.signals.result.emit("foo")  # Return the result of the processing
            finally:
                self.signals.finished.emit()  # Done

    def kill(self):
        self.is_alive = False