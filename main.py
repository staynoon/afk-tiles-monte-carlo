import numpy as np
import matplotlib.pyplot as plt

from tiles_implementation import Tiles

run_num = 1000000
key_num = 1080

winter_event = Tiles(key_num,3)
flipped_floor_count = winter_event.monte_carlo(run_num)

floors, frequency = np.unique(flipped_floor_count,return_counts=True)

average_floor = np.sum(floors * frequency)/run_num
print("The average player will be able to clear {} floors.".format(average_floor))
standard_deviation = np.sqrt(np.sum((floors - average_floor)**2 * frequency)/run_num)
print("With a standard deviation of {}.".format(standard_deviation))
twenty_plus_index = floors >= 20
twenty_plus_occurence = np.sum(frequency[twenty_plus_index])/run_num * 100
print("Approximately {}% of the playerbase will hit floor 20.".format(twenty_plus_occurence))

frequency = frequency/run_num * 100

plt.title("Monte Carlo Final Floor Frequency")
plt.xlabel('Final Floor')
plt.ylabel('Percentage Occurence (%)')
plt.bar(floors,frequency,width=0.9,align='center')
plt.savefig('Monte_Carlo_Run_{}'.format(key_num) + "_{}.png".format(run_num))