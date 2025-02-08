def load_high_score():
    try:
        with open("core/score/high_score.txt", "r") as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return 0


def save_high_score(score):
    high_score = load_high_score()
    if score > high_score:
        with open("core/score/high_score.txt", "w") as file:
            file.write(str(score))
