import pandas as pd

data = pd.read_csv("output/input.csv")

fig = data.SEX.plot.hist().get_figure()
fig.savefig("output/descriptive.png")