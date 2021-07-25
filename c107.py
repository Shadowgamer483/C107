import pandas as pd
import csv
import plotly.graph_objects as pgo
df=pd.read_csv("D:\Daksh\WhiteHatJr\C98\c107\data.csv")
studentdf=df.loc[df["student_id"]=="TRL_987"]
print(studentdf.groupby("level")["attempt"].mean())
fig=pgo.Figure(pgo.Bar(x=studentdf.groupby("level")["attempt"].mean(),y=["Level 1","Level 2","Level 3","Level 4"],orientation="h"))
fig.show()








