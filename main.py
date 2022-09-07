from artwork import logo, vs
from utils import clear_console
import random
import game_data

USER_CHOICE_TO_ARRAY_INDEX_MAP = {"a": 0, "b": 1}
OPTION_WEIGHTS = [50 for _ in range(len(game_data.data))]


def set_option_weight(option: dict, weight: int) -> None:
    global OPTION_WEIGHTS
    index = [data["name"] for data in game_data.data].index(option["name"])
    OPTION_WEIGHTS[index] = weight

    return


def select_options(number: int) -> list[dict]:
    global OPTION_WEIGHTS
    options = random.choices(game_data.data, weights=OPTION_WEIGHTS, k=number)

    # Set chosen option(s) weight(s) to 0 so it/they will not be picked again
    for option in options:
        set_option_weight(option, 0)

    return options


def get_option_line(option: str, data: dict) -> str:
    return f"Compare {option}: {data['name']}, a {data['description']}, from {data['country']}."


def show_board(option_a: dict, option_b: dict, status_line: str | None) -> None:
    clear_console()
    print(logo)
    if status_line:
        print(status_line)
    print("-" * 80)
    print(get_option_line("A", option_a))
    print(vs)
    print(get_option_line("B", option_b))
    print()

    return


def main():

    options = select_options(2)
    user_score = 0
    status_line = None

    game_is_running = True
    while game_is_running:
        show_board(options[0], options[1], status_line)

        user_choice = None
        while True:
            user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
            if user_choice in ["a", "b"]:
                break

            print("huh?")

        if user_choice == "a":
            if options[0]["follower_count"] < options[1]["follower_count"]:
                game_is_running = False

        else:
            if options[1]["follower_count"] < options[0]["follower_count"]:
                game_is_running = False
            else:
                options[0] = options[1]

        if game_is_running:
            user_score += 1
            status_line = f"Correct! Your current score is {user_score}."
            new_options = select_options(1)
            set_option_weight(options[0], 50)
            options[1] = new_options[0]

    print("-" * 80)
    print("That is incorrect! Game over!")
    print(f"Your final score is {user_score}.")


if __name__ == "__main__":
    main()
