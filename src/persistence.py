import csv
import os
from src.cell import Cell

class Persistence:
    def __init__(self, universe):
        self.saves_folder_name = "saves"
        self.extension = ".csv"
        self.universe = universe

    def save_state(self, universe):
        filename = self.get_next_file_name()
        
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            for coordinates in universe.cells.keys():
                writer.writerow(coordinates)

    def get_next_file_name(self, prefix="saved_game_"):
        # Create folder saves if it does not exist one level higher
        base_dir = os.path.dirname(__file__)
        project_dir = os.path.abspath(os.path.join(base_dir, ".."))
        saves_dir = os.path.join(project_dir, self.saves_folder_name)
        if not os.path.exists(saves_dir):
            os.makedirs(saves_dir)

        # List only saved games files
        files = os.listdir(saves_dir)
        valid_files = [
            f for f in files 
            if f.startswith(prefix) and f.endswith(self.extension)
            ]
        
        # List numbers in files
        number_files = [int(file[len(prefix):-len(self.extension)]) for file in valid_files]

        # Get the biggest number in list
        max_number = max(number_files, default=0) + 1
        formatted_max_number = f"{max_number:03}"
        file_name = prefix + formatted_max_number + self.extension

        file_path = os.path.join(saves_dir, file_name)
        return file_path
    
    def load_game_files_names(self):
        base_dir = os.path.dirname(__file__)
        project_dir = os.path.abspath(os.path.join(base_dir, ".."))
        saves_dir = os.path.join(project_dir, self.saves_folder_name)
        all_files = os.listdir(saves_dir)
        valid_files = [
            f for f in all_files 
            if f.endswith(self.extension)
            ]
        return valid_files
    
    def load_saved_game(self, saved_game_file):
        # Reset existing cells
        self.universe.cells = {}
        
        # Pick the file from saves folder
        base_dir = os.path.dirname(__file__)
        project_dir = os.path.abspath(os.path.join(base_dir, ".."))
        saves_dir = os.path.join(project_dir, self.saves_folder_name)
        saved_game_file_route = os.path.join(saves_dir, saved_game_file)
        with open(saved_game_file_route, mode="r") as csvfile:
            reader = csv.reader(csvfile)
            for cell in reader:
                row, col = int(cell[0]), int(cell[1])
                self.universe.cells[(row, col)] = Cell((row, col), self.universe)