import streamlit as st
from PIL import Image
import pandas as pd
import geopandas as gpd
import json
import numpy as np
from folium.features import GeoJsonTooltip
import folium
import random
from streamlit_folium import st_folium, folium_static
from map_functions import get_mydict_varlist

# 1. DESCRIPTION ########################################################
# THIS APP BRING US A MAP FOR THE CAPABILITIES OF COLIMA'S HOME TOWN ELECTION


# 2. MAIN SETTINGS ######################################################
st.set_page_config(page_title='Análisis Electoral',
                   layout="centered",
                   page_icon='data_elect/icon.png')

# 3. BRAND AND TITLE #####################################################
image = Image.open('data_elect/brand.png')
st.image(image)

st.title('PM COLIMA - 2024')

# 4. LOADING ALL DATA ####################################################

# GEOJSON
geojson = gpd.read_file('data_elect/driver.geojson')

# MERGED DATA RESUMEN PROYECCIONES AND
df = pd.read_csv("data_elect/main_data_pmcol_2024.csv")
gdf = pd.merge(geojson, df, on="seccion")

# LATLON DA
latlon = pd.read_csv('data_elect/latlon_df.csv')

# GEOJSON AND MAIN DATA MERGED



# 5. MAIN FEATURE ###########################################################

# SECTION TITLE & DESCRIPTION
st.markdown('## **1. MAPA INTERACTIVO PM COLIMA**')
select_district = 1

st.markdown("**El siguiente mapa dibuja diversas variables sobre las secciones electorales del municipio de Colima**")

# COLUMN INPUTS
sel_election, sel_var, scale_type = st.columns(3)

# first column
with sel_election:
    #
    sel_election = st.selectbox(
        'Información de interes',
        ["Proyecciones 2024", "Elecciones PM Colima 2021", "Datos socidemográficos"]
    )

selected = ""

if sel_election == "Elecciones PM Colima 2021":
    selected = st.radio("", ["Porcentajes", "Totales"], horizontal=True)


if sel_election == "Elecciones PM Colima 2021" and selected == "Porcentajes":
    selected_scale = [ 0.  , 16.24, 32.47, 48.71]
elif sel_election == "Elecciones PM Colima 2021" and selected == "Totales":
    selected_scale = [0,  509.67, 1019.33, 1529]
else:
    selected_scale = 4

# WE CALL "get_mydict" function to choice our dictionary

my_dict, varlist = get_mydict_varlist(sel_election, selected)

# second column
with sel_var:
    sel_var = st.selectbox(
        "Varaible a mostrar",
        varlist
    )

color_list = ["Blues", "Greens", "Reds"]

if sel_election == "Elecciones PM Colima 2021" and selected == "Porcentajes":
    color_list = ["Semáforo", "Blues", "Greens", "Reds"]

with scale_type:
    scale_type = st.selectbox(
        "Color de la escala",
        color_list)

# Selected the color for the map
if scale_type == "Semáforo":
    color_selected = "RdYlGn"
else:
    color_selected = scale_type

# Selected scale
#if sel_election == "Elecciones PM Colima 2021" and

# MAP AND RELATED ACCTIONS


f = folium.Map(location=[latlon['lat_x'][select_district - 1], latlon['lon_y'][select_district - 1]],
               zoom_start=12,
               tiles='openstreetmap')

folium.Choropleth(
    geo_data=geojson,
    data=gdf,
    columns=['seccion', sel_var],
    key_on='feature.properties.seccion',
    threshold_scale=selected_scale,
    fill_color=color_selected,
    nan_fill_color="rgba(0, 0, 0, 0)",
    fill_opacity=0.75,
    line_opacity=0.3,
    legend_name='MAPA INTERACTIVO PANORAMA PM COLIMA',
    highlight=True,
    line_color='black').add_to(f)

folium.features.GeoJson(
    data=gdf,
    name="Elecciones Presidencia Municipal Colima",
    smooth_factor=2,
    style_function=lambda x: {'color': 'black', 'fillColor': 'transparent',
                              'weight': 0.5},
    tooltip=folium.features.GeoJsonTooltip(
        fields=list(my_dict.keys()),
        aliases=list(my_dict.values()),
        localize=True,
        sticky=True,
        labels=True,
        style="""
            background-color: #F0EFEF;
            border: 2px solid black;
            border-radius: 3px;
            box-shadow: 3px;
        """,
        max_width=600,),
     highlight_function=lambda x: {'weight': 3, 'fillColor': 'grey'},
).add_to(f)

folium_static(f, width=700, height=400)



# The sexiest author
st.write("Author: [HugoArellano](https://github.com/HugoArellano)")



