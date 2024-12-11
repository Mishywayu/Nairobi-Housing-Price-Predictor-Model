import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

filepath = "nairobi_property_prices_large.csv"

def wrangle(filepath):
    df = pd.read_csv(filepath)
    return df

df = wrangle(filepath)
print(df.info())
print(df.head())

# print(df['Price Approx (USD)']) #In USD
# print(df['Price Approx (Local Currency)']) #In KES

# print(df['Currency'].nunique()) #2
print(df['Currency'].unique()) #USD & KES

# HOOD
# print(df['Place with Parent Names'].str.contains("Kilimani"))

# Property type
print(df['Property Type'].nunique())
print(df['Property Type'].unique())

#Scatter plot
# plt.figure(figsize=(10, 6))
# plt.scatter(df['Surface Covered (m2)'], df['Price per m2'], alpha=0.6, c='blue', edgecolors='k')
# plt.title("Scatter Plot of Size vs Price", fontsize=16)
# plt.xlabel("Size (in square meters)", fontsize=12)
# plt.ylabel("Price (in KES)", fontsize=12)
# plt.grid(True, linestyle='--', alpha=0.7)
# plt.show()


#Scatter map box
# fig = px.scatter_mapbox(
#     df,  # Our DataFrame
#     lat="Latitude",
#     lon="Longitude",
#     width=600,  # Width of map
#     height=600,  # Height of map
#     color="Price Approx (Local Currency)",
#     hover_data=["Price Approx (Local Currency)"],  # Display price when hovering mouse over house
# )

# fig.update_layout(mapbox_style="open-street-map")

# fig.show()