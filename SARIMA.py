import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import warnings
import plotly.graph_objs as go
import plotly.express as px
import plotly.io as pio

# Suppress warnings
warnings.filterwarnings("ignore")

# Load and preprocess data
data = pd.read_csv("Instagram-Reach.csv", encoding="latin-1")
data["Date"] = pd.to_datetime(data["Date"])
data.set_index("Date", inplace=True)

# Ensure sorted by date and handle missing values
data.sort_index(inplace=True)
data["Instagram reach"] = data[
    "Instagram reach"
].interpolate()  # or .fillna(method="ffill")

# SARIMAX parameters
p, d, q = 8, 1, 2
P, D, Q, s = 8, 1, 2, 12

# Fit the SARIMAX model
model = sm.tsa.statespace.SARIMAX(
    data["Instagram reach"],
    order=(p, d, q),
    seasonal_order=(P, D, Q, s),
    enforce_stationarity=False,
    enforce_invertibility=False,
)

results = model.fit()

# Print the SARIMAX summary (as you want)
print(results.summary())
