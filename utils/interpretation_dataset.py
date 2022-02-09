import pandas as pd
import numpy as np
import matplotlib.pyplot as mp


data = pd.read_csv("./data/cleaned_data.csv")


#mp.boxplot(data.price)
#mp.show()

# Can be deleted varaibles
round(data["price"].corr(data["open_fire"]), 3)
round(data["price"].corr(data["furnished"]), 3)


data['locality_code'] = data['locality_code'].apply(lambda x:int(x))
#print(data[["locality_code", "price_square_meters"]])

#Less expensive in Belgium
data.groupby("locality_code")["price_square_meters"].mean().sort_values(ascending=False).head(1)
data.groupby("locality_code")["price"].median().sort_values(ascending=False).tail(1)
data.groupby("locality_code")["price_square_meters"].mean().sort_values(ascending=False).tail(1)


flemish_brabant = data[(data.locality_code >= 1500) & (data.locality_code <= 1999)]
antwerp = data[(data.locality_code >= 2000) & (data.locality_code <= 2999)]
flemish_brabant2 = data[(data.locality_code >= 3000) & (data.locality_code <= 3499)]
limburg = data[(data.locality_code >= 3500) & (data.locality_code <= 3999)]
west_flanders = data[(data.locality_code >= 8000) & (data.locality_code <= 8999)]
east_flanders = data[(data.locality_code >= 9000) & (data.locality_code <= 9999)]

df_flanders = pd.concat([flemish_brabant, antwerp, flemish_brabant2, limburg, west_flanders, east_flanders], axis=0)

# Median Price
df_flanders.groupby("locality_code")["price"].median().sort_values(ascending=False).head()
# Mean price for Locality
df_flanders.groupby("locality_code")["price"].mean().sort_values(ascending=False).head()

# Less expensive in Flanders

df_flanders.groupby("locality_code")["price_square_meters"].mean().sort_values(ascending=False).head(1) # Price square meter
df_flanders.groupby("locality_code")["price"].median().sort_values(ascending=False).tail(1) # Median price per locality
df_flanders.groupby("locality_code")["price"].mean().sort_values(ascending=False).tail(1) # Average price per locality

# Less expensive Walonia

waloon_brabant = data[(data.locality_code >= 1300) & (data.locality_code <= 1499)]
liege = data[(data.locality_code >= 4000) & (data.locality_code <= 4999)]
namur = data[(data.locality_code >= 5000) & (data.locality_code <= 5999)]
hainaut = data[(data.locality_code >= 6000) & (data.locality_code <= 6599)]
luxembourg = data[(data.locality_code >= 6600) & (data.locality_code <= 6999)]
hainaut2 = data[(data.locality_code >= 7000) & (data.locality_code <= 7999)]

df_wallonia = pd.concat([waloon_brabant, liege, namur, hainaut, hainaut2,luxembourg], axis=0)

price_sq = df_wallonia.groupby("locality_code")["price_square_meters"].mean().sort_values(ascending=False).head(1) # Price square meter
df_wallonia.groupby("locality_code")["price"].median().sort_values(ascending=False).tail(1) # Median price per locality
df_wallonia.groupby("locality_code")["price"].mean().sort_values(ascending=False).tail(1)









