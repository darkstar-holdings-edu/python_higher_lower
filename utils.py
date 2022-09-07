import os


def clear_console() -> None:
    """
    Clears the console screen.
    """
    command = "clear"
    if os.name in ("nt", "dos"):
        command = "cls"

    os.system(command)
