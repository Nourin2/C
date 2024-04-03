import numpy as np 
import pandas as pd 
import streamlit as st 
import altair as alt 
import plotly.express as px 
import csv

st.set_page_config(
    page_title='US Population Dashboard',
    page_icon='🏂',
    layout='wide',
    initial_sidebar_state='expanded'
    )
alt.themes.enable('dark')
    
#Load data 
df_reshaped = pd.read_csv(r'C:\Users\dell\Desktop\US dash\us - Sheet1.csv')
df_reshaped.head()
#Add a sidebar 
with st.sidebar:
    st.title('US POPULATION DASHBOARD')
    
    year_list = list(df_reshaped.year.unique())[::-1]
    
    selected_year = st.selectbox('Select a year', year_list, index=len(year_list)-1)
    df_selected_year = df_reshaped[df_reshaped.year == selected_year]
    df_selected_year_sorted = df_selected_year.sort_values(by="population", ascending=False)
    color_them_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    selected_color_theme = st.selectbox('select a color theme', 'color_theme_list')

#Plot chart types 
def make_heatmap(input_df, input_y, input_x, input_color, input_color_theme):
    heatmap = alt.Chart(input_df).mark_rect().encode(
            y=alt.Y(f'{input_y}:O', axis=alt.Axis(title="Year", titleFontSize=18, titlePadding=15, titleFontWeight=900, labelAngle=0)),
            x=alt.X(f'{input_x}:O', axis=alt.Axis(title="", titleFontSize=18, titlePadding=15, titleFontWeight=900)),
            color=alt.Color(f'max({input_color}):Q',
                             legend=None,
                             scale=alt.Scale(scheme=input_color_theme)),
            stroke=alt.value('black'),
            strokeWidth=alt.value(0.25),
        ).properties(width=900
        ).configure_axis(
        labelFontSize=12,
        titleFontSize=12
        ) 
    # height=300
    return heatmap
def make_choropleth(input_df, input_id, input_column, input_color_theme):
    choropleth = px.choropleth(input_df, locations=input_id, color=input_column, locationmode="USA-states",
                               color_continuous_scale=input_color_theme,
                               range_color=(0, max(df_selected_year.population)),
                               scope="usa",
                               labels={'population':'Population'}
                              )
    choropleth.update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        margin=dict(l=0, r=0, t=0, b=0),
        height=350
    )
    return choropleth

def calculate_population_difference(input_df, input_year):
    selected_year_data = input_df[input_df['year'] == input_year].reset_index()
    previous_year_data = input_df[input_df['year'] == input_year - 1].reset_index()
    selected_year_data['population_difference'] = selected_year_data.population.sub(previous_year_data.population, fill_value=0)
    return pd.concat([selected_year_data.states, selected_year_data.id, selected_year_data.population, selected_year_data.population_difference], axis=1).sort_values(by='population_difference', ascending=False)


#make donut bar 
def make_donut(input_response, input_text, input_color):
    if input_color == 'blue':
        chart_color = ['#29b5e8', '#155f7A']
    if input_color == 'green':
        chart_color = ['#27AE', '#12783D'] 
    if input_color == 'orange':
        chart_color = ['#F39C12', '#875A12']
    if input_color == 'red':
        chart_color = ['#E74C3C', '#781F16']
        
    source = pd.DataFrame({
        'Topic': ['', input_text],
        '% value': [100-input_response, input_response]
    })
    source_bg = pd.DataFrame({
        'Topic': ['', input_text],
        '% value': [100, 0]
    })
    
plot = alt.Chart(source).mark_arc(innerRadius=45, cornerRadius=25).encode(text=alt.value(f'{input_response}%'))         
theta='% value',
color=alt.Color('Topic:N',
                scale=alt.Scale(
                    #domain=['A', 'B'],
                    domain=[input_text, ''],
                    #range=['#29b5e8', '#155F7A']), #31333F
                    range=chart_color),
                legend=None),
).prperties(width=130, height)
                    


                                                                                                                    