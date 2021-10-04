import pandas as pd
import os
import mplcursors
df = pd.read_csv(os.path.join("Proj data", "bt_symmetric.csv"))

time_max = df["# timestamp"].max()

times = []
connections = []
for i in range(0, time_max, 300):
    df_temp = df[df["# timestamp"] == i]
    times.append(i)
    connections.append(len(df_temp))

import matplotlib.pyplot as plt
plt.plot(times, connections)
mplcursors.cursor()
plt.show()