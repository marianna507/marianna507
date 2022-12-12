# Read in the CSV file
#data = pd.read_csv("/home/lornam/Downloads/demo-uber-nyc-pickups-main/pages/LORNA/Victimization.csv")

import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv('https://github.com/marianna507/marianna50/blob/main/LORNA/Victimization.csv')
df['text'] = df['Type of attack'] + '' + df['SCENE'] + ', ' + df['COUNTY'] + '' + 'DATE_TIME: ' + df['type by number'].astype(str)


fig = go.Figure(data=go.Scattergeo(
        lon = df['longitude'],
        lat = df['latitude'],
        text = df['text'],
        mode = 'markers',
        marker_color = df['type by number'],
        ))

fig.update_layout(
        title = 'Most trafficked US airports<br>(Hover for airport names)',
        geo_scope='usa',
    )
fig.show()