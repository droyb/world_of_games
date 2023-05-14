import os
import Utils


def add_score(difficulty: int) -> None:
    points_of_winning = (difficulty * 3) + 5

    current_score = 0
    if os.path.exists(Utils.SCORES_FILE_NAME):
        with open(Utils.SCORES_FILE_NAME, 'r') as f:
            current_score = int(f.read())

    new_score = current_score + points_of_winning

    with open(Utils.SCORES_FILE_NAME, 'w') as f:
        f.write(str(new_score))
