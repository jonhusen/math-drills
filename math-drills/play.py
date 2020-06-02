import exercises
from helpers import Timer, Score

t = Timer()
overall_score = Score()


def play(mode="speed", list_of_numbers=range(101), seconds=60):
    session_score = Score()

    if mode == "speed":
        while t.timer_set(seconds):
            answer = exercises.quantity_discrimination(list_of_numbers)
            if answer == "correct":
                session_score.add_correct()
            elif answer == "incorrect":
                session_score.add_incorrect()

        print(f"You scored {session_score.correct} / {session_score.total()} correct answers")

    if mode == "infinite":
        t.stopwatch_start()
        while True:
            answer = exercises.quantity_discrimination(list_of_numbers)
            if answer == "correct":
                session_score.add_correct()
            elif answer == "incorrect":
                session_score.add_incorrect()
            else:
                break

        t.stopwatch_stop()
        print(f"You scored {session_score.correct} / {session_score.total()} correct answers")


def main():
    play(mode="speed", list_of_numbers=range(101), seconds=60)


if __name__ == "__main__":
    main()
