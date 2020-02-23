# Import the relevant libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
import plotly.offline as py
#py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls
import plotly.express as px
import seaborn as sns
import json
import warnings
warnings.filterwarnings('ignore')

countries = pd.read_csv('unemployment.csv')

# List of countries
country_list = ['Afghanistan','Angola','Albania','Argentina','Armenia','Australia'
,'Austria','Azerbaijan','Burundi','Belgium','Benin','Burkina Faso','Bangladesh','Bulgaria'
,'Bahrain','Bosnia and Herzegovina','Belarus','Belize','Bolivia','Brazil','Barbados','Brunei Darussalam'
,'Bhutan','Botswana','Central African Republic','Canada','Switzerland','Chile','China','Cameroon'
,'Congo','Colombia','Comoros','Cabo Verde','Costa Rica','Cuba','Cyprus','Czech Republic','Germany'
,'Denmark','Dominican Republic','Algeria','Ecuador','Egypt','Spain','Estonia','Ethiopia','Finland','Fiji'
,'France','Gabon','United Kingdom','Georgia','Ghana','Guinea','Greece','Guatemala','Guyana','Hong Kong'
,'Honduras','Croatia','Haiti','Hungary','Indonesia','India','Ireland','Iran','Iraq','Iceland','Israel'
,'Italy','Jamaica','Jordan','Japan','Kazakhstan','Kenya','Cambodia','Korea, Rep.','Kuwait','Lebanon','Liberia'
,'Libya','Sri Lanka','Lesotho','Lithuania','Luxembourg','Latvia','Macao','Morocco','Moldova','Madagascar'
,'Maldives','Mexico','Macedonia','Mali','Malta','Myanmar','Montenegro','Mongolia','Mozambique','Mauritania'
,'Mauritius','Malawi','Malaysia','North America','Namibia','Niger','Nigeria','Nicaragua','Netherlands'
,'Norway','Nepal','New Zealand   ','Oman','Pakistan','Panama','Peru','Philippines','Papua New Guinea'
,'Poland','Puerto Rico','Portugal','Paraguay','Qatar','Romania','Russian Federation','Rwanda','Saudi Arabia'
,'Sudan','Senegal','Singapore','Solomon Islands','Sierra Leone','El Salvador','Somalia','Serbia','Slovenia'
,'Sweden','Swaziland','Syrian Arab Republic','Chad','Togo','Thailand','Tajikistan','Turkmenistan','Timor-Leste'
,'Trinidad and Tobago','Tunisia','Turkey','Tanzania','Uganda','Ukraine','Uruguay','United States','Uzbekistan'
,'Venezuela, RB','Vietnam','Yemen, Rep.','South Africa','Congo, Dem. Rep.','Zambia','Zimbabwe'
]

# Create a new dataframe with our cleaned country list
countries_cleaned = countries[countries['Country Name'].isin(country_list)]


# Plotting 2019 unemployment rate for each country

# metric scale (colors at what values) for bar
metricscale = [[0, 'rgb(102,194,80)'], [0.1, 'rgb(140,194,80)'],
              [0.2, 'rgb(171,221,164)'], [0.3, 'rgb(230,245,152)'],
              [0.4, 'rgb(255,255,191)'], [0.5, 'rgb(254,224,139)'],
              [0.6, 'rgb(253,174,97)'], [0.75, 'rgb(213,62,79)'], [1.0, 'rgb(158,1,66)']]

# Set how data will be visualized on the plot
data = [ dict(
        type = 'choropleth',
        autocolorscale = False,
        colorscale = metricscale,
        showscale = True,
        locations = countries_cleaned['Country Name'].values,
        z = countries_cleaned['2019'].values,
        locationmode = 'country names',
        text = countries_cleaned['Country Name'].values,
        marker = dict(
            line = dict(color = 'rgb(250,250,225)', width = 0.5)),
            colorbar = dict(tickprefix = '',
            title = 'Unemployment\nRate')
            )
       ]

# Setup layout of plot
layout = dict(
    title = 'Unemployment of Each Country in 2019',
    geo = dict(
        showframe = True,
        showocean = True,
        oceancolor = 'rgb(28,107,160)',
        projection = dict(
            type = 'orthographic',
                rotation = dict(
                        lon = 60,
                        lat = 10),
            ),
            lonaxis =  dict(
                    showgrid = False,
                    gridcolor = 'rgb(102, 102, 102)'
                ),
            lataxis = dict(
                    showgrid = False,
                    gridcolor = 'rgb(102, 102, 102)'
                    )
                ),
            )

fig = dict(data=data, layout=layout)
#py.iplot(fig, validate=False, filename='worldmap2019')
py.plot(fig, filename='global-unemployment.html')


# Load counties data from JSON file
with open('geojson-counties-fips.json', 'r') as response:
    counties = json.load(response)

# Store counties in a dataframe
df = pd.read_csv("fips-unemp-16.csv",
                   dtype={"fips": str})


fig = px.choropleth_mapbox(df, geojson=counties, locations='fips', color='unemp',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'unemp':'unemployment rate'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
py.plot(fig, filename='county-unemployment.html')