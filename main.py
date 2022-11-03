from time import perf_counter

class TimerError(Exception):
    """A Custom Error"""

class Timer:
    """Create a new Timer() object"""
    def __init__(self):
        self._start = None
        self._elapsed = None
    def start(self):
        """Start a new Timer"""
        if self._start != None:
            raise TimerError("Timer is running. Use .stop() to reset the timer")
        self._start = perf_counter()
    def stop(self):
        """Save the elapsed time and reset the timer"""
        if self._start == None:
            raise TimerError("Timer is not running. Use .start() to start a new Timer")
        self._elapsed = perf_counter() - self._start
        self._start = None
    def elapsed(self):
        """Report elapsed time"""
        if self._elapsed == None:
            raise TimerError("Timer has not started yet. Use .start() to start a new Timer")
        return self._elapsed
    def __str__(self):
        return str(self._elapsed)
