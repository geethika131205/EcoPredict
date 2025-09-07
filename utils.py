import pandas as pd
import plotly.express as px

def load_data(station_file='data/station_day.csv', meta_file='data/stations.csv'):
    # Load station data
    station_data = pd.read_csv(station_file)
    stations_meta = pd.read_csv(meta_file)

    # Ensure both StationId columns are strings
    station_data['StationId'] = station_data['StationId'].astype(str)
    stations_meta['StationId'] = stations_meta['StationId'].astype(str)

    # Merge
    df = station_data.merge(stations_meta, on='StationId')

    # Drop rows with missing values
    df = df.dropna(subset=['Latitude','Longitude','PM2.5','PM10','NO2','CO','O3','AQI'])
    return df

def plot_city_area_heatmap(df, city, pollutant='PM2.5'):
    """
    Plot area-level heatmap for a specific city.
    """
    city_df = df[df['City'] == city]
    if city_df.empty:
        return None

    fig = px.scatter_mapbox(
        city_df,
        lat='Latitude',
        lon='Longitude',
        size=[10]*len(city_df),  # constant marker size
        color=pollutant,
        hover_name='Area',
        hover_data=[pollutant],
        color_continuous_scale='YlOrRd',
        zoom=11
    )
    fig.update_layout(mapbox_style='carto-positron')
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig
