import csv
import streamlit as st
import folium
import pandas as pd
from streamlit_folium import st_folium

data = pd.read_csv("dummy_bank.csv")
data.index = data.index + 1
data = data.iloc[:, :-1]
data = data.rename(columns={'branch_name': 'Branch Name', 'branch_code': 'Code'})

# Calculate %target
data['%target'] = (data['des'] / data['target']) * 100
data['%target'] = data['%target'].apply(lambda x: min(x, 130))
data['%target'] = data['%target'].apply(lambda x: round(x, 1))
data = data[['Code', 'Branch Name', 'sep', 'oct', 'nov', 'des', 'target', '%target']]

# Format columns
data['sep'] = data['sep'].apply(lambda x: '{:,.0f}'.format(x))
data['oct'] = data['oct'].apply(lambda x: '{:,.0f}'.format(x))
data['nov'] = data['nov'].apply(lambda x: '{:,.0f}'.format(x))
data['des'] = data['des'].apply(lambda x: '{:,.0f}'.format(x))
data['target'] = data['target'].apply(lambda x: '{:,.0f}'.format(x))

# Define function to color rows based on %target value
def color_row(row):
    val = row['%target']
    if val > 100:
        color = 'RGBA(0,180,80,0.8)'
    elif 90 <= val <= 100:
        color = 'yellow'
    else:
        color = 'red'
    return [f'background-color: {color}']*len(row)

# Apply row coloring
styled_data = data.style.apply(color_row, axis=1)

# Display styled dataframe
st.header("Branches Performance 2024")
st.write(styled_data)

datafile = pd.read_csv("dummy_bank.csv")

JAKARTA_CENTER = [-6.207966655614447, 106.83339601722136]
map = folium.Map(location=JAKARTA_CENTER, zoom_start=16)


def get_marker_color(target):
    if target > 100:
        return 'green'
    elif 90 <= target < 100:
        return 'orange'
    else:
        return 'red'

# Add a marker for each branch with additional information in the popup
for index, row in datafile.iterrows():
    location = [row['latitude'], row['longitude']]
    popup_content = f"<strong>Branch:</strong> {row['branch_name']}<br><strong>% Target:</strong> {row['%target']}"
    marker_color = get_marker_color(float(row['%target'].strip('%')))
    folium.Marker(
        location,
        popup=popup_content,
        icon=folium.Icon(color=marker_color)
    ).add_to(map)

# Streamlit header
st.header("MAPPED PERFORMANCE")

# Display the map in Streamlit
map_component = st_folium(map, width=500, height=500)

# Inject custom CSS to style the map container
st.markdown(
    """
    <style>
    iframe {
        border: 10px solid navy; /* Thick black border */
        border-radius: 50%; /* Round shape */
        width: 500px;
        height: 500px;
    }
    </style>
    """,
    unsafe_allow_html=True
)