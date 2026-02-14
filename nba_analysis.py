import pandas as pd
import matplotlib.pyplot as plt
import os

# Create folders
os.makedirs("figures", exist_ok=True)
os.makedirs("tables", exist_ok=True)

print("Loading dataset...")

df = pd.read_csv("main_df.csv")

df = df[["PTS", "3PA"]].dropna()

# Correlation
corr = df["PTS"].corr(df["3PA"])
print("Correlation:", corr)

with open("tables/correlation.txt", "w") as f:
    f.write(f"Correlation between PTS and 3PA: {corr:.3f}")

# Plot
plt.scatter(df["3PA"], df["PTS"])
plt.xlabel("Three Point Attempts")
plt.ylabel("Points Scored")
plt.title("Points vs 3PA")
plt.savefig("figures/points_vs_3pa.png")
plt.close()

print("Done.")