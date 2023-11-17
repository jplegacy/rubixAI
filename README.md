# Rubix AI
## Traversing Rubix Cube State Spaces with Informed Search Algorithms 

- _For more information about this project go [here](<docs/writeup.md>)_

### 1. Background and Goals
The project's goal is to apply search algorithms to the state spaces of Rubix cubes. We are interested in investigating the relationship between successful heuristics correlated to solving a Rubix cube efficiently and effectively. Considering the state space has a branching factor of about 18 moves per state in a 3 by 3, giving it a total of approximately 4.3 × 10^19 possible states and configurations, the task of solving Rubix cubes is evidently a challenging one.

### 2. How to Install and Run

    pip install -r requirements.txt 
    python3 cube_exp.py

### 3. Understanding Output
The program by default produces a CSV file storing all of the data and seeds correlated to each run within the experimentData directory

The file produced by this program is named according to the format below:
RubixCube{***RUBIX_CUBE_SIZE***}x{**RUBIX_CUBE_SIZE**}-{**RANDOM_SCRAMBLE_LENGTH**}-{***RUNS_PER_LENGTH***}.csv

### 4. File Structure Overview

##### cube_exp.py
This file contains configuration variables and code for running and storing Rubix state space environment information. Options of producing a CSV and a diagram are optional.

#### Rubix Module
This module is responsible for storing all Rubix abstract shape implementations

##### cube.py
This file is responsible for storing the implementation of the Rubix Cube Data Structure and it's helper functions. In our implementation, our Rubix Cube Class is defined as an informedProblemState implementation which we, making it an abstract environment of the Rubix problem state space.  

Future environments include the Pyraminx, Megaminx, and Skewb

#### Search Module
This module is responsible for storing all Searching methods that will explore the state space.

##### astar.py
This file contains the implementation of A* which relies on the heuristic function within the Rubix classes.

##### uninformedSearch.py
This file contains the implementation of BFS which unlike A* does not rely on heuristic functions.

##### queues.py
This file contains essential queues and priorityQueue classes used throughout searching algorithms

### 5. Program Configuration
Configuration parameters can be found within cube_exp.py

### 6. About Project
This group project expands upon the concepts discussed in Artificial Intelligence Courses and applies them to the domain of Combinatorics.

#### Contributors to building this project:
- Jeremy Perez
- Aryan Mayor 
