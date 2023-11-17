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

##### cube_exp.py
This file contains configuration variables and code for running and storing Rubix state space environments information. Options of producing a CSV and a diagram are optional.

#### Rubix Module
This module is responsible for storing all Rubix abstract shape implementations

##### cube.py
This file is responsible for storing the implementation of the Rubix Cube Data Structure and it's helper functions. In our implementation, our Rubix Cube Class is defined as an informedProblemState implementation which we, making it an abstract environment of the Rubix problem state space.  

Future environments include the Pyraminx, Megaminx, and Skewb

#### Search Module
This module is responsible for storing all Searching methods that will explore the state space.

##### astar.py
This file contains the implementation of A* which relies on the heuristic function within the Rubix classes.

##### searchStructures.py
This file contains essential classes used through out the searching algorithms like nodes, queues and classes like the priorityQueue.

### 5. Program Configuration
Configuration parameters can be found within cube_exp.py

### 6. About Project
This group project expands upon the concepts discussed in Artifical Intelligence Courses and applies them to the domain of Combinatorics.

#### Contributors to building this project:
- Jeremy Perez
- Aryan Mayor 