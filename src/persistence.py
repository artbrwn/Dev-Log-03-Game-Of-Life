import csv

class Persistence:
    def __init__(self):
        pass

    def save_state(self, filename, universe):
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow("position")
            for coordinates in universe.cells.keys():
                writer.writerow(coordinates)
