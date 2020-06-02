#!/usr/bin/env python3
import time


class Score:
    """Keep score of current session"""

    def __init__(self):
        self.correct = 0
        self.incorrect = 0

    def add_correct(self):
        self.correct += 1

    def add_incorrect(self):
        self.incorrect += 1

    def total(self):
        return self.correct + self.incorrect


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


class Timer:
    """Stopwatch and duration measurements for math drills"""

    def __init__(self):
        self._start_time = None
        self._stop_time = None

    def stopwatch_start(self):
        """Start new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it.")

        self._start_time = time.perf_counter()

    def stopwatch_stop(self):
        """Stop the timer and report elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it.")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time: {elapsed_time:0.2f} seconds")

    def timer_reset(self):
        if self._stop_time is not None:
            self._stop_time = None

    def timer_set(self, seconds):
        """Stopwatch for speed drills"""
        if self._stop_time is None:
            self._stop_time = time.perf_counter() + seconds
            return True
        elif self.now() < self._stop_time:
            return True
        else:
            print(f"Elapsed time: {seconds} seconds")
            self.timer_reset()
            return False

    def now(self):
        return time.perf_counter()
