import csv
import random
import matplotlib.pyplot as plt
from rubix.Cube import Cube
from search import astar
from tqdm import tqdm

from multiprocessing import Pool


"""------CONFIGURATIONS-------------"""

RUNS_PER_LENGTH = 20


RUBIX_CUBE_SIZE = 2
MAX_CUBE_STATES = 1000
VERBOSE_OUTPUT = False

RANDOM_SCRAMBLE_LENGTH = 20

EXPORT_FILE = True

"""---------------------------------"""

xpoints = []
ypoints = []
ySequences = []

for i in tqdm(range(RANDOM_SCRAMBLE_LENGTH)):
    random.seed(i)
    
    for x in tqdm(range(RUNS_PER_LENGTH)):
        xpoints.append(i)

        s = Cube(RUBIX_CUBE_SIZE)
        g = Cube(RUBIX_CUBE_SIZE)

        seq = s.scramble(i)

        s = astar.InformedSearch(s, g, MAX_CUBE_STATES, VERBOSE_OUTPUT)
        numOfNodes, sequence = s.results()
        
        ypoints.append(numOfNodes)
        ySequences.append(sequence)

plt.scatter(xpoints, ypoints,color = 'hotpink')
plt.xlabel('Scramble Length')
plt.ylabel('Number of Rubix States Traversed')
plt.suptitle(f'A* performance on {RUBIX_CUBE_SIZE}x{RUBIX_CUBE_SIZE} Cubes')

plt.show()



if EXPORT_FILE:
    with open(f'experiement/RubixCube{RUBIX_CUBE_SIZE}x{RUBIX_CUBE_SIZE}-{RANDOM_SCRAMBLE_LENGTH}-{RUNS_PER_LENGTH}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Scramble Length/Seed", "States Checked", "Sequence"])

        for i,x in enumerate(xpoints):
            writer.writerow([x, ypoints, ySequences[i]])


