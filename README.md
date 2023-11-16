# Rubix AI
## Traversing Rubix Cube State Spaces with Informed Search Algorithms 

### 1. Background and Goals
The project's goal is to analyze Search Algorithms when applied on the state spaces of Rubix Cube's. We are interested in investigating the relationship betweeen the strategies and heuristics correlated to solving a Rubix cube successfully. The task of solving Rubix cube's is evidently a challenging one when considering the state space has a branching factor of about 18 moves per state in a 3 by 3, giving it a total of approximately 4.3 × 10^19 possible states and configuerations.

### 2.  Prerequisites to Running
If external corpus is wanted, override the raw_analyst_ratings.csv file in the main directory and follow the format specified [`below`](#corpus).

The corpus can be downloaded from [kaggle](https://www.kaggle.com/datasets/miguelaenlle/massive-stock-news-analysis-db-for-nlpbacktests). The corpus used in the project comes from the raw_analyst_ratings.csv file in Kaggle.

### 3. How to Install and Run

    pip install -r requirements.txt 
    python3 experiment.py

#### Understanding Output
The application outputs the models' evaluation based on how successful your model was in predicting the stocks' movement. The evaluation consist of calculating the models: 

- Accuracy
- Precision
- Recall
- F-score

### 4. File Overview

#### Astar.py
This file is responsible for doing the Informed Search through the Rubix Cube's State Space. 

#### Rubix.py
This file is responsible for storing the implementation of the Rubix Cube Data Structure and it's helper functions. In our implementation, our Rubix Cube Class implements the informedProblemState which we defined in Astar.py, making it cross functional for the rubix problem domain. This design choice is purely to make it an informed abstract approach.  

<!-- <h4 id="corpus"> raw_analyst_ratings.csv </h4>  -->

### 5. Program Configuration
Configuration parameters for the predictor can be found within stock_prediction.py. Main neural structure and learning phases can be found and edited here as well

### 6. About Project
This group project expands upon the concepts discussed in Artifical Intelligence Courses and applies them to the domain of Combinatorics.

