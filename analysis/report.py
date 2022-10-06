import pandas as pd

df = pd.read_csv("output/input.csv")

# fig = df.SEX.plot.hist().get_figure()
# fig.savefig("output/descriptive.png")

sex_count_df = (
    df
    .groupby("patient_id", as_index=False)
    ["SEX"]
    .count()
    .groupby("SEX", as_index=False)
    .count()
)
sex_count_df.columns = ["NUMBER_OF_SEX_VALUES", "FREQUENCY"]
print(sex_count_df)

fig = sex_count_df.plot(kind="bar", x="NUMBER_OF_SEX_VALUES", y="FREQUENCY").get_figure()
fig.savefig("output/descriptive.png")