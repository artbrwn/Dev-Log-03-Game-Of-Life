import csv
import os

class Persistence:
    def __init__(self):
        pass

    def save_state(self, universe):
        filename = self.get_next_file_name()
        
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            for coordinates in universe.cells.keys():
                writer.writerow(coordinates)

    def get_next_file_name(self, saves_folder_name= "saves", prefix="saved_game_", extension=".csv"):
        # Create folder saves if it does not exist one level higher
        base_dir = os.path.dirname(__file__)
        project_dir = os.path.abspath(os.path.join(base_dir, ".."))
        saves_dir = os.path.join(project_dir, saves_folder_name)
        if not os.path.exists(saves_dir):
            os.makedirs(saves_dir)

        # List only saved games files
        files = os.listdir(saves_dir)
        valid_files = [
            f for f in files 
            if f.startswith(prefix) and f.endswith(extension)
            ]
        
        # List numbers in files
        number_files = [int(file[len(prefix):-len(extension)]) for file in valid_files]

        # Get the biggest number in list
        max_number = max(number_files, default=0) + 1
        formatted_max_number = f"{max_number:03}"
        file_name = prefix + formatted_max_number + extension

        file_path = os.path.join(saves_dir, file_name)
        return file_path