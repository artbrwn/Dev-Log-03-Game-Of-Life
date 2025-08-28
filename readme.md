# Conway's Game of Life (Autonomous Cells)

This is a personal implementation of Conway’s Game of Life built in **Python** with **Pygame**.  

The project was created as part of my learning journey and focuses on exploring an unusual design choice: instead of having a global controller (the “Universe”) that decides births and deaths, **cells operate autonomously**.  

Each living cell is responsible for:
- Exploring its neighborhood.  
- Deciding its own death if the rules require it.  
- Collaborating with other cells to create new cells when conditions are met.  

This decentralized design emphasizes autonomy and cooperation between cells, which is different from most standard implementations where the universe handles all the logic.

## ✨ Features
- **Autonomous Cells:**  
  Cells handle their own life cycle and coordinate to create new ones.  

- **Pygame Visualization:**  
  Simple grid-based display with alive cells shown in green.  

- **Navigation Bar:**  
  - ▶️ Play  
  - ⏸️ Pause  
  - ⏭️ Step (advance one generation)  
  - 💾 Save current game state  
  - 📂 Load saved game  

- **Persistence:**  
  Save and load game states from CSV files.  
  Saved files are automatically numbered (`saved_game_001.csv`, `saved_game_002.csv`, …).  

- **Load Menu View:**  
  A separate screen where saved games can be selected and loaded.  
  The menu reinitializes the window (`pygame.display.set_mode`) so that it can also support universes with different sizes or configurations.  

- **Console Output (optional):**  
  For debugging or text-based visualization, the universe can be printed as a grid of `O` (alive) and `.` (dead).  

## 📂 Project Structure
````
.
├── .gitignore
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── cell.py
│   ├── config
│   │   ├── __init__.py
│   │   └── colors.py
│   ├── main.py
│   ├── persistence.py
│   ├── universe.py
│   └── view
│       ├── __init__.py
│       ├── game_view.py
│       └── load_menu_view.py
└── tests
    ├── __init__.py
    ├── test_cell.py
    └── test_universe.py

````

## 🕹️ How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/game-of-life.git
   cd game-of-life
2. Install dependencies:
    ```python
    pip install -r requirements.txt
    ```
3. Run the game:
    ```python
    python3 -m src.main
    ```
    
## 🎯 Design Choices
    - Autonomous Cells:
    The key experiment in this project is removing the “god” controller and letting cells decide their own fate. This makes the code slightly more complex but highlights distributed responsibility and communication between objects.

    - Load Menu Reinitialization:
    When entering the Load Menu, the game resets the window. This design allows loading saved universes with different dimensions, not just the same grid size.

## 📜 License
This project is open source and available under the MIT License.