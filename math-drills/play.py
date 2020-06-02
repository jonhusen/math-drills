from .exercises import quantity_discrimination, add_integers, subtract_integers
from .helpers import Timer, Score, str_range

t = Timer()
score = Score()


def selection(list_of_str_numbers):
    """Checks input against a list of options

    Checks an input value against a provided set of options.
    If the input is invalid, retries up to 5 times

    :param list_of_str_numbers: List of options to check against
    :return: String value of the selection
    """
    retries = 5
    response = input("Enter your choice: ")
    while response not in list_of_str_numbers and retries > 0:
        response = input("Enter your choice: ")
        retries -= 1
    if response not in list_of_str_numbers and retries == 0:
        return "exit"
    return response


def menu():
    """Prints menu system and prompts for input"""

    print(
        f"""
        Math exercises
        
        To exit any exercise, enter "x" to return to this menu
        
        1. Which is greater?
        2. Addition
        3. Subtraction
        """
    )
    game = selection(str_range(1, 4))
    if game == "exit":
        return

    print("""
        Mode
        1. Speed - Timed run of the game
        2. Free play - Play as long as you want
        """
    )
    mode = selection(str_range(1, 3))
    duration = 60
    if mode == "exit":
        return
    elif mode == "1":
        print("""
            How long would you like your run?
            Default: 60 seconds
            """
        )
        seconds = input("Seconds: ")
        try:
            duration = int(seconds)
        except ValueError:
            pass

    print("""
        What number range would you like to work with?
        """
    )
    try:
        start = int(input("Start: "))
        stop = int(input("Stop: ")) + 1
    except ValueError:
        start = 0
        stop = 101
    num_list = list(range(int(start), int(stop)))

    return (game, mode, num_list, duration)


def play(game, mode="speed", list_of_numbers=None, seconds=60):
    if list_of_numbers is None:
        list_of_numbers = range(101)

    if mode == "speed":
        while t.timer_set(seconds):
            answer = quantity_discrimination(list_of_numbers)
            if answer == "correct":
                score.add_correct()
            elif answer == "incorrect":
                score.add_incorrect()

        print(f"You scored {score.session_correct} / {score.session_total()} correct answers")

    if mode == "infinite":
        t.stopwatch_start()
        while True:
            answer = quantity_discrimination(list_of_numbers)
            if answer == "correct":
                score.add_correct()
            elif answer == "incorrect":
                score.add_incorrect()
            else:
                break

        t.stopwatch_stop()
        print(f"You scored {score.session_correct} / {score.session_total()} correct answers")


def main():

    while True:
        game, mode, num_list, duration = menu()
        play(game-game, mode=mode, list_of_numbers=num_list, seconds=duration)


if __name__ == "__main__":
    main()
