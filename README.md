# Rubix AI
## Traversing Rubix Cube State Spaces with Informed Search Algorithms 

### 1. Background and Goals
The project's goal is to analyze Search Algorithms when applied on the state spaces of Rubix Cube's. We are interested in investigating the relationship betweeen the strategies and heuristics correlated to solving a Rubix cube successfully. The task of solving Rubix cube's is evidently a challenging one when considering the state space has a branching factor of about 18 moves per state in a 3 by 3, giving it a total of approximately 4.3 × 10^19 possible states and configuerations.

### 2. How to Install and Run

    pip install -r requirements.txt 
    python3 experiment.py

#### Understanding Output
fix me

### 4. File Structure Overview

#### astar.py
This file contains the implementation of A* which is used on the Rubix Cube's State Space. 

#### cube.py
This file is responsible for storing the implementation of the Rubix Cube Data Structure and it's helper functions. In our implementation, our Rubix Cube Class implements the informedProblemState which we defined in Astar.py, making it cross functional for the rubix problem domain. This design choice is purely to make it an informed abstract approach.  


### 5. Program Configuration
Configuration parameters can be found within cube_exp.py

### 6. About Project
This group project expands upon the concepts discussed in Artifical Intelligence Courses and applies them to the domain of Combinatorics.

