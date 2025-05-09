import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.express as px
import plotly.io as pio

import matplotlib.pyplot as plt


pio.templates.default = "plotly_white"
data = pd.read_csv("Instagram-Reach.csv", encoding="latin-1")
# print(data.head())
data["Date"] = pd.to_datetime(data["Date"])
print(data.head())
# fig = go.Figure()
# fig.add_trace(
#     go.Scatter(
#         x=data["Date"], y=data["Instagram reach"], mode="lines", name="Instagram reach"
#     )
# )
# fig.update_layout(
#     title="Instagram Reach Trend", xaxis_title="Date", yaxis_title="Instagram Reach"
# )
# fig.show()

# fig = go.Figure()
# fig.add_trace(go.Bar(x=data["Date"], y=data["Instagram reach"], name="Instagram reach"))
# fig.update_layout(
#     title="Instagram Reach by Day", xaxis_title="Date", yaxis_title="Instagram Reach"
# )
# fig.show()

# fig = go.Figure()
# fig.add_trace(go.Box(y=data["Instagram reach"], name="Instagram reach"))
# fig.update_layout(title="Instagram Reach Box Plot", yaxis_title="Instagram Reach")
# fig.show()

# data["Day"] = data["Date"].dt.day_name()
# print(data.head())

# print(data.head())

# day_stats = (
#     data.groupby("Day")["Instagram reach"].agg(["mean", "median", "std"]).reset_index()
# )
# print(day_stats)

# fig = go.Figure()
# fig.add_trace(go.Bar(x=day_stats["Day"], y=day_stats["mean"], name="Mean"))
# fig.add_trace(go.Bar(x=day_stats["Day"], y=day_stats["median"], name="Median"))
# fig.add_trace(go.Bar(x=day_stats["Day"], y=day_stats["std"], name="Standard Deviation"))
# fig.update_layout(
#     title="Instagram Reach by Day of the Week",
#     xaxis_title="Day",
#     yaxis_title="Instagram Reach",
# )
# fig.show()

# from plotly.tools import mpl_to_plotly
# import matplotlib.pyplot as plt
# from statsmodels.tsa.seasonal import seasonal_decompose

# data = data[["Date", "Instagram reach"]]

# result = seasonal_decompose(data["Instagram reach"], model="multiplicative", period=100)

# fig = plt.figure()
# fig = result.plot()

# fig = mpl_to_plotly(fig)
# fig.show()

# pd.plotting.autocorrelation_plot(data["Instagram reach"])
# plt.title("Autocorrelation of Instagram Reach")
# plt.show()


from statsmodels.graphics.tsaplots import plot_pacf


plot_pacf(data["Instagram reach"], lags=100)
plt.title("Partial Autocorrelation of Instagram Reach")
plt.show()
