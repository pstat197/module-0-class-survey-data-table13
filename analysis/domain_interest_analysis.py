import pandas as pd

background = pd.read_csv("data/background-clean.csv")
interest = pd.read_csv("data/interest-clean.csv")
metadata = pd.read_csv("data/survey-metadata.csv")

print("Background shape:", background.shape)
print("Interest shape:", interest.shape)
print("Metadata shape:", metadata.shape)

# Quick peek at columns
print("Interest columns:", interest.columns.tolist())
