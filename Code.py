import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('Gene.csv')

fig = go.Figure(data=[go.Table(
    columnorder = [1,2,3,4],
    columnwidth = [1,1,1,1],
    header=dict(values=list(df.columns),
                line_color= "darkslategray",
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df.Rank, df.Gene, df.RGA, df.Position],

               line_color= "darkslategray",
               fill_color='lavender',
               align='left'))
])

fig.show()
