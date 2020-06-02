#!/usr/bin/env python3
import time


class Score:
    """Keep score of current session"""

    def __init__(self):
        self.total_correct = 0
        self.total_incorrect = 0
        self.session_correct = 0
        self.session_incorrect = 0

    def add_correct(self):
        self.total_correct += 1
        self.session_correct += 1

    def add_incorrect(self):
        self.total_incorrect += 1
        self.session_incorrect += 1

    def session_reset(self):
        self.session_correct = 0
        self.session_incorrect = 0

    def session_total(self):
        return self.session_correct + self.session_incorrect


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


def process_response(correct, allowed, response):
    """Checks a response and determines if it is correct.

    :param correct: The correct answer.
    :param allowed: List of possible answers.
    :param response: The answer provided by the player.
    :return: "correct", "incorrect", or "exit"
    """
    try:
        response = response.casefold()
    except AttributeError:
        pass

    if response not in allowed:
        return "exit"

    elif response == correct:
        print("Congratulations! Your are correct.\n")
        return "correct"

    else:
        print("Incorrect\n")
        return "incorrect"


def str_range(start=None, stop=None):
    """Takes start and stop values and returns a list of numbers as strings

    :param start: Start value of range. If not given, starts at 0
    :param stop: Stop value of range.
    :return: list of numbers as individual strings.
    """
    if start is None:
        start = 0
    return [str(x) for x in range(start, stop)]
