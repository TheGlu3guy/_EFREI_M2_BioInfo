import streamlit as st


st.title("Chikungunya Data Visualization")
st.title("What is the Chikungunya?")
st.write("""The **Chikungunya** is an infection cause by the CHIK virus. Symptoms are :

    - Fever,
    - Joint pain, 
    - Headache, 
    - MusclePaint 
    - Joint Swelling 
    - and Rash

The symptoms usually last for 3 to 7 days, but the joint pain can last for months or years. The death rate is about 0.1%, the main problem of the disease being the joint pain.

The *CHIKV* is spread by two types of mosquitoes:""")

st.write('The *Aedes aegypti*')
col1, col2 = st.columns(2)
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Aedes_aegypti.jpg/1280px-Aedes_aegypti.jpg", width=300)
with col2:
    st.write('-> Its distribution')
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3f/Global_Aedes_aegypti_distribution_%28e08347%29.png", width=300)

st.write("and the *Aedes albopictus*.")
col1, col2 = st.columns(2)
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/CDC-Gathany-Aedes-albopictus-1.jpg/1280px-CDC-Gathany-Aedes-albopictus-1.jpg", width=300)
with col2:
    st.write('-> Its distribution')
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Global_Aedes_albopictus_distribution_2015.jpg/1280px-Global_Aedes_albopictus_distribution_2015.jpg", width=300)

st.title("The Datavisualization")
st.write("Now that we know what is the Chikungunya, we are going to see some visualizations of the data we have about it.")

#--- Map of the world ---
year = st.slider('Select the year', 2019, 2022, 2022)

import plotly.express as px
import pandas as pd

europe = pd.read_csv("cleaned/TotalCasesEurope.csv")
europe = europe[europe["Time"] == year]
europe = europe[['CountryCode', "RegionName", "Location", "NumValue"]].groupby(['CountryCode', "RegionName", "Location"]).sum().reset_index()

america = pd.read_csv("cleaned/TotalCasesAmerica.csv")
america = america[america["Time"] == year]
america = america[['CountryCode', "RegionName", "Location", "NumValue"]].groupby(['CountryCode', "RegionName", "Location"]).sum().reset_index()

df = pd.concat([europe, america])


import json
with open("geojson/countries.geojson") as response:
    geo = json.load(response)

import plotly.graph_objects as go
fig = go.Figure(
    go.Choroplethmapbox(
        geojson=geo,
        locations=df.CountryCode,
        featureidkey="properties.kan_name",
        z=df.NumValue,
        colorscale="sunsetdark",
        # zmin=0,
        # zmax=500000,
        marker_opacity=0.5,
        marker_line_width=0,
    )
)
fig.update_layout(
    mapbox_style="carto-positron",
    mapbox_zoom=1,
    mapbox_center={"lat": 46.8, "lon": 8.2},
    width=800,
    height=600,
)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

st.write("We can see the distribution of the disease in the world : ")
st.plotly_chart(fig)

#--- Bar chart of the world ---
st.write("By country, one look way above the others : ")
df.sort_values(by=['NumValue'], inplace=True, ascending=False)
st.bar_chart(df, x="RegionName", y="NumValue")

europe = pd.read_csv("cleaned/TotalCasesEurope.csv")
europe = europe[["NumValue", "Time"]].groupby(["Time"]).sum().reset_index()

america = pd.read_csv("cleaned/TotalCasesAmerica.csv")
america = america[["NumValue", "Time"]].groupby(["Time"]).sum().reset_index()

#--- Bar chart by year ---
st.write("By year we can see a significant drop in 2020 for obvious reasons :")
df = pd.concat([europe, america])
df = df[df["Time"] >= 2019]
df.sort_values(by=['NumValue'], inplace=True, ascending=False)
st.bar_chart(df, x="Time", y="NumValue")