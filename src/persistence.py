import csv
import os
from src.cell import Cell

class Persistence:
    """
    Handles saving and loading the state of the universe to and from CSV files.
    
    This class manages persistence by writing the current state of live cells
    into `.csv` files inside a dedicated `saves/` folder. It also allows
    listing available saved games and loading them back into the universe.
    """

    def __init__(self, universe):
        self.saves_folder_name = "saves"
        self.extension = ".csv"
        self.universe = universe

    def save_state(self, universe):
        """
        Save the current state of the universe into a CSV file.

        Each row in the file contains the coordinates of a live cell.
        """

        filename = self.get_next_file_name()
        
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            for coordinates in universe.cells.keys():
                writer.writerow(coordinates)

    def get_next_file_name(self, prefix="saved_game_"):
        """
        Generate the next available file name for saving a game.

        - Ensures that the `saves/` folder exists at the project root level.
        - Files are named using an incrementing number, e.g., 
          `saved_game_001.csv`, `saved_game_002.csv`, etc.

        Args:
            prefix (str, optional): The prefix for the saved file name.
                Defaults to "saved_game_".

        Returns:
            str: Absolute path to the next available save file.
        """

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
        """
        List all available saved game file names in the `saves/` folder.

        Returns:
            list[str]: A list of file names (ending with `.csv`) found in `saves/`.
        """
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
        """
        Load a saved game from a CSV file.
        - Reads live cell coordinates from the file.
        - Recreates cells in the universe accordingly.

        Args:
            saved_game_file (str): The file name of the saved game to load.
        """
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