# This is a sample Python script.
# Press Umschalt+F10 to execute it or replace it with your code.
import math


# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# ---------------------Aufgabe 1 ------------------------------------
def compute_r2d2_population(steps: int) -> tuple[int, int, int]:
    r2d2_population = {
        "young": 10,
        "adult": 10,
        "old": 10
    }

    for x in range(0, steps):
        young_to_adult = math.floor(r2d2_population["young"] / 2)
        adult_to_old = math.floor(r2d2_population["adult"] / 3)

        new_r2d2 = r2d2_population["adult"] * 4 + r2d2_population["old"] * 2

        r2d2_population["young"] = new_r2d2
        r2d2_population["adult"] = young_to_adult
        r2d2_population["old"] = adult_to_old

    return int(r2d2_population["young"]), int(r2d2_population["adult"]), int(r2d2_population["old"])

    # ---------------------Aufgabe 2 Streichholz------------------------------
    # look streichholzGame.py

    # ---------------------Aufgabe 3 Heron ------------------------------------


def heron_verfahren(area: float, threshold: float) -> float:
    """
        computes the square root using the heron method
    :param area: size of the area e.g.25
    :param threshold: threshold for the heron method e.g. 0.01
    :return:the square root of the given area according to the heron method
    """

    return 0


# ---------------------Aufgabe 4 Quersumme------------------------------
# IMPLEMENT, IF NECESSARY, EXERCISE 4 HERE BUT USE A FUNCTION!


# ---------------MANAGEMENT----------------------
# -------------COMMENT/UNCOMMENT lines to launch the different exercises
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("You need to adjust this code to run your implementation")

    # Aufgabe 1
    print(f"""
        # R2D2 Population after 5 steps is: 
        # Young: {compute_r2d2_population(5)[0]}
        # Adults: {compute_r2d2_population(5)[1]}
        # Old: {compute_r2d2_population(5)[2]}""")
    # print (compute_r2d2_population(5))

    # Aufgabe 2
    # TO BE IMPLEMENTED

    # Aufgabe 3
    print(f"Die Wurzel für die Fläche 25 und Grenze 0.01 nach Heron ist: {heron_verfahren(25, 0.01)}")

    # Aufgabe 4
    # TO BE IMPLEMENTED

    # Use a breakpoint in the code line below to debug your script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
