import csv
import random
import numpy as np
import matplotlib.pyplot as plt
from rubix.Cube import Cube
from search import astar
from tqdm import tqdm

import multiprocessing


"""------CONFIGURATIONS-------------"""

RUNS_PER_LENGTH = 20

RUBIX_CUBE_SIZE = 3
MAX_CUBE_STATES = 2000 # Setting to 0 will uncap it 
VERBOSE_OUTPUT = False

RANDOM_SCRAMBLE_LENGTH = 20

EXPORT_FILE = True


"""---------------------------------"""
manager = multiprocessing.Manager()
mutex = manager.Lock()

xpoints = manager.list([])
ypoints =  manager.list([])
ySequences = manager.list([])

def experiment(i, mutex):
    random.seed(i)
    
    for x in range(RUNS_PER_LENGTH):

        s = Cube(RUBIX_CUBE_SIZE)
        g = Cube(RUBIX_CUBE_SIZE)

        seq = s.scramble(i)

        s = astar.InformedSearch(s, g, MAX_CUBE_STATES, VERBOSE_OUTPUT)
        numOfNodes, sequence = s.results()
        
        
        # These are shared amongst all processes a mutex is used
        mutex.acquire()
        
        xpoints.append(i)
        ypoints.append(numOfNodes)
        ySequences.append(sequence)
        
        mutex.release()

# ----------MULTIPROCESSING----------------------- 

# create all tasks
processes = [ multiprocessing.Process(target=experiment, args=(i,mutex)) for i in range(RANDOM_SCRAMBLE_LENGTH)]

# start all processes
for process in processes:
    process.start()

# wait for all processes to complete
for process in tqdm(processes):
    process.join()


# ----------PLOTTING----------------------- 

plt.style.use('dark_background')

plt.scatter(xpoints, ypoints,c=np.random.rand(len(xpoints),3))
plt.xlabel('Scramble Length')
plt.ylabel('Number of Rubix States Traversed')
plt.suptitle(f'A* performance on {RUBIX_CUBE_SIZE}x{RUBIX_CUBE_SIZE} Cubes')

plt.show()


if EXPORT_FILE:
    with open(f'experimentData/RubixCube{RUBIX_CUBE_SIZE}x{RUBIX_CUBE_SIZE}-{RANDOM_SCRAMBLE_LENGTH}-{RUNS_PER_LENGTH}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Scramble Length/Seed", "States Checked", "Sequence"])

        for i,x in enumerate(xpoints):
            writer.writerow([x, ypoints, ySequences[i]])


