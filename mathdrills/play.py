#!/usr/bin/env python3
from mathdrills.exercises import qty_discrimination, add_integers, subtract_integers
from mathdrills.helpers import Timer, Score, str_range, process_response

t = Timer()
score = Score()


class Session:
    def __init__(self):
        self._exercise = 0
        self._mode = 0
        self._duration = 60
        self._num_list = list(range(101))

        self._exercise_list = [
            ("Which is greater?", "qty_discrimination(self._num_list)"),
            ("Addition", "add_integers(self._num_list)"),
            ("Subtraction", "subtract_integers(self._num_list)")
        ]

        self._mode_list = [
            "Speed - Timed run of the game",
            "Free Play - Play as long as you want"
        ]

    def reset_defaults(self):
        self._exercise = 0
        self._mode = 0
        self._duration = 60
        self._num_list = list(range(101))

    def menu(self):
        """Prints menu system and prompts for input"""

        print(
            "Math exercises\n"
            "\n"
            "To exit any exercise and return to this menu, enter 'exit'\n"
            "To quit the game, enter 'exit'\n"
        )
        print_options([x[0] for x in self._exercise_list])
        self._exercise = selection(str_range(1, len(self._exercise_list)))
        if self._exercise == "exit":
            print("Thanks for playing!\n"
                  "Your overall score is:\n",
                  score.total_correct / score.overall_total())
            return

        print(print_options(self._mode_list))
        mode = selection(str_range(1, len(self._mode_list)))
        if mode == 0:
            self._mode = mode
            print(
                "How long would you like your run?\n"
                "Default: 60 seconds\n"
                  )
            seconds = input("Seconds: ")
            try:
                self._duration = int(seconds)
            except ValueError:
                return
        elif mode == 1:
            self._mode = mode
        else:
            return

        print("What number range would you like to work with?\n")
        try:
            start = int(input("Start: "))
            stop = int(input("Stop: ")) + 1
            self._num_list = list(range(start, stop))
        except ValueError:
            pass

    def play(self):
        if self._mode == 0:
            while t.timer_set(self._duration):
                answer = process_response(
                    exec(self._exercise_list[self._exercise][1]))
                if answer == "correct":
                    score.add_correct()
                elif answer == "incorrect":
                    score.add_incorrect()

        print(f"You scored {score.exercise_correct} / {score.exercise_total()} correct answers")

        if self._mode == 1:
            t.stopwatch_start()
            while True:
                answer = process_response(
                    exec(self._exercise_list[self._exercise][1]))
                if answer == "correct":
                    score.add_correct()
                elif answer == "incorrect":
                    score.add_incorrect()
                else:
                    break

            t.stopwatch_stop()
            print(f"You scored {score.exercise_correct} / {score.exercise_total()} correct answers")

        score.exercise_reset()


def selection(list_of_str_numbers):
    """Checks input against a list of options

    Checks an input value against a provided set of options.
    If the input is invalid, retries up to 5 times

    :param list_of_str_numbers: List of options to check against
    :return: String value of the selection
    """
    retries = 5
    response = input("Enter your choice: ")
    if response == "":
        return
    while response not in list_of_str_numbers and retries > 0:
        response = input("Enter your choice: ")
        retries -= 1
    if response not in list_of_str_numbers and retries == 0:
        return "exit"
    return int(response) - 1


def print_options(options_list):
    """Prints the enumerated list without the first item so that
    the displayed options start numbering with 1 and the
    selection correspond with the index"""
    for k, v in enumerate(options_list, start=1):
        print(f"{k}. {v}")


def main():
    game = Session()
    while True:
        game.menu()
        game.play()


if __name__ == "__main__":
    main()
