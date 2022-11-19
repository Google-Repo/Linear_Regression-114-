#all module imported here
import pandas as pd
import plotly.express as px
import numpy as np

#getting and csv file to the code to analysis it:
df = pd.read_csv("main.csv")

#Making an list:
TOEFL_Score = df["TOEFL Score"].tolist()
chance = df["Chance of Admit "].tolist()

#Code to make scatter graph
fig = px.scatter(x=TOEFL_Score, y=chance)
fig.show()

TOEFL_Score_array = np.array(TOEFL_Score)
chance_array = np.array(chance)

m,c = np.polyfit(TOEFL_Score_array,chance_array,1)

y=[]

for x in TOEFL_Score_array:
    y_value = m*x+c
    y.append(y_value)

fig = px.scatter(x = TOEFL_Score, y = chance_array )
fig.update_layout(shapes = [
    dict(
        type="line",
        y0=min(y), y1= max(y),
        x0= min(TOEFL_Score_array), x1=max(TOEFL_Score_array)
    )
])
fig.show()

x= 1000
y= m*x+c
print({y})

