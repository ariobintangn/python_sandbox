import streamlit as st
import pandas as pd
import folium
import streamlit_folium as st_folium

# Load data
data = pd.read_csv("dummy_bank.csv")
data.index = data.index + 1
data = data.iloc[:, :-1]
data = data.rename(columns={'branch_name': 'Branch Name', 'branch_code': 'Code'})

# Calculate %target
data['%target'] = (data['des'] / data['target']) * 100
data['%target'] = data['%target'].apply(lambda x: min(x, 130))
data['%target'] = data['%target'].apply(lambda x: round(x, 1))
data = data[['Code', 'Branch Name','jul','aug', 'sep', 'oct', 'nov', 'des', 'target', '%target']]

# Format columns
# data['sep'] = data['sep'].apply(lambda x: '{:,.0f}'.format(x))
# data['oct'] = data['oct'].apply(lambda x: '{:,.0f}'.format(x))
# data['nov'] = data['nov'].apply(lambda x: '{:,.0f}'.format(x))
# data['des'] = data['des'].apply(lambda x: '{:,.0f}'.format(x))
# data['target'] = data['target'].apply(lambda x: '{:,.0f}'.format(x))

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
st.header("Branches Target Achievement")
st.write(styled_data)

targetData = pd.read_csv("dummy_target.csv")

targetData = targetData.rename(columns={'branch_name': 'Branch Name', 'branch_code': 'Code'})
targetData = targetData[['Branch Name', 'Code','jul_t','aug_t', 'sep_t','oct_t','nov_t','des_t']]

# Merge the dataframes on branch_code
merged_data = pd.merge(data, targetData, on="Code", suffixes=('', '_t'))

months = ['jul','aug','sep', 'oct', 'nov', 'des']
target_columns = [col + '_t' for col in months]

branch_options = ["All Branches"] + merged_data['Code'].unique().tolist()
st.title('Monthly Achievement Comparison')
selected_branch = st.selectbox("Select Branch", branch_options)

# Filter data based on selected branch
if selected_branch == "All Branches":
    plot_data = pd.DataFrame({
    'Month': months,
    'Actual': [data[col].sum() for col in months],
    'Target': [targetData[col].sum() for col in target_columns]
})
else:
    branch_data = merged_data[merged_data['Code'] == selected_branch]
    plot_data = pd.DataFrame({
        'Month': months,
        'Actual': [branch_data[col].sum() for col in months],
        'Target': [branch_data[col].sum() for col in target_columns]
    })

# Ensure the months are in the correct order
plot_data['Month'] = pd.Categorical(plot_data['Month'], categories=months, ordered=True)
plot_data = plot_data.sort_values('Month')

# Streamlit app
st.title('Monthly Achievement Comparison')

# Line chart for comparison
st.line_chart(plot_data.set_index('Month'))

# Additional code to display the filtered data table
st.dataframe(branch_data if selected_branch != "All Branches" else merged_data)