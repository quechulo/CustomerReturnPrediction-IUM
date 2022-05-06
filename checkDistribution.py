import matplotlib.pyplot as plt
import numpy as np
import jsonlines

np.random.seed(0)
typesOfEvents = []
timestamps = []

with jsonlines.open('./data/sessions.jsonl') as f:
    for obj in f:
        typesOfEvents.append(obj['event_type'])
        timestamps.append(obj['timestamp'][:7])
        print(obj['timestamp'][:7])

    plt.hist(typesOfEvents, density=False, bins=3)  # density=False would make counts
    plt.ylabel('Counts')
    plt.xlabel('Data')
    plt.show()
    print(timestamps.count('2022-02'))
    plt.hist(timestamps, density=False, bins=4)  # density=False would make counts
    plt.ylabel('Counts')
    # plt.xlabel('Data')
    plt.show()
