# Name: Yeesa Kee, UWnetid: yeesakee
# Section: AE
# This program uses the given shape file and csv file and do some data
# analysis involving geospatial data about the food deserts in WA.

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt


def main():
    # store the filtered GeoDataFrame
    data = (load_in_data('/course/food-access/tl_2010_53_tract00/\
tl_2010_53_tract00.shp', '/course/food-access/food-access.csv'))
    percentage_food_data(data)
    plot_map(data)
    plot_population_map(data)
    plot_population_county_map(data)
    plot_food_access_by_county(data)
    plot_low_access_tracts(data)


def load_in_data(shape_file, csv_file):
    """
    Returns a GeoDataFrame that has shape_file and csv_file merged on
    the "CTIDFP00" column for shape_file and the "CensusTract" column
    for csv_file
    """
    shape = gpd.read_file('/course/food-access/tl_2010_53_tract00/\
tl_2010_53_tract00.shp')
    csv = pd.read_csv('/course/food-access/food-access.csv')
    merged = shape.merge(csv, left_on='CTIDFP00',
                         right_on='CensusTract', how='left')
    return merged


def percentage_food_data(data):
    """
    Returns the percentage of census tracts in Washington that we have
    food access data for from the csv_file.
    """
    total = len(data['CensusTract'])
    existing_data = data['CensusTract'].count()
    return (existing_data/total) * 100


def plot_map(data):
    """
    Plots a map of Washington with the shape of all the census tracts using
    the information in data and is stored in a file named "washington_map.png"
    """
    data.plot()
    plt.title('Census Tracts of Washington')
    plt.savefig('washington_map.png')


def plot_population_map(data):
    """
    Plots a map of Washington with each census tract colored by its population
    using the information in data and is stored in a file named
    "washington_population_map.png".
    """
    census = data[['CensusTract', 'POP2010', 'geometry']]
    population = census.dissolve(by='CensusTract', aggfunc='sum')
    population.plot(column='POP2010', legend=True)
    plt.title('Population of Census Tracts in Washington')
    plt.savefig('washington_population_map.png')


def plot_population_county_map(data):
    """
    Plots a map of Washington with each county colored by its population using
    the information in data and is stored in a file named
    "washington_county_population_map.png".
    """
    county = data[['County', 'POP2010', 'CensusTract', 'geometry']]
    # group county by CensusTract and aggregate it by summing it up
    population = county.dissolve(by='CensusTract', aggfunc='sum')
    population.plot(column='POP2010', legend=True)
    plt.title('Population of Counties in Washington')
    plt.savefig('washington_county_population_map.png')


def plot_food_access_by_county(data):
    """
    Makes four plots on the same figure that shows information about
    food acess and low income of urban areas and rural areas.
    """
    filtered = data[['County', 'geometry', 'POP2010', 'lapophalf', 'lapop10',
                     'lalowihalf', 'lalowi10']]
    sum_up = filtered.dissolve('County', aggfunc='sum')
    # add a column that stores the percentage of people that are low access in
    # their group
    sum_up['lapophalf_ratio'] = sum_up['lapophalf'] / sum_up['POP2010']
    sum_up['lapop10_ratio'] = sum_up['lapop10'] / sum_up['POP2010']
    sum_up['lalowihalf_ratio'] = sum_up['lalowihalf'] / sum_up['POP2010']
    sum_up['lalowi10_ratio'] = sum_up['lalowi10'] / sum_up['POP2010']

    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, figsize=(20, 10), ncols=2)
    sum_up.plot(ax=ax1, legend=True, vmin=0, vmax=1,
                column='lapophalf_ratio')
    sum_up.plot(ax=ax2, legend=True, vmin=0, vmax=1,
                column='lalowihalf_ratio')
    sum_up.plot(ax=ax3, legend=True, vmin=0, vmax=1,
                column='lapop10_ratio')
    sum_up.plot(ax=ax4, legend=True, vmin=0, vmax=1,
                column='lalowi10_ratio')
    ax1.set_title('Low Access: Half')
    ax2.set_title('Low Access + Low Income: Half')
    ax3.set_title('Low Access: 10')
    ax4.set_title('Low Access + Low Income: 10')
    fig.savefig('washington_county_food_access.png')


def plot_low_access_tracts(data):
    """
    Plots all the census tracts that are considered low access in urban or
    rural areas.

    Dark gray is the census tracts we have food access data for and blue are
    the census tracts that are considred low access.
    """
    fig, ax = plt.subplots(1)
    census = data[['CensusTract', 'geometry']]
    # plot all the census tracts a light gray
    census.plot(color='#EEEEEE', ax=ax)
    food_access = data[(data['State'] == 'WA')][['CensusTract', 'geometry']]
    # plot all the census tracts that we have food access for in dark gray
    food_access.plot(color='#AAAAAA', ax=ax)

    urban = data[data['Urban'] == 1]
    urban_pop = urban['lapophalf'] >= 500
    # add a column that stores the percentage of people that have low access
    data['urban_percentage'] = urban['lapophalf'] / urban['POP2010']
    rural = data[data['Rural'] == 1]
    rural_pop = rural['lapop10'] >= 500
    data['rural_percentage'] = rural['lapop10'] / rural['POP2010']
    data_urban = data[urban_pop | (data['urban_percentage'] >= 0.33)]
    data_rural = data[rural_pop | (data['rural_percentage'] >= 0.33)]
    data_urban.plot(ax=ax)
    data_rural.plot(ax=ax)
    plt.title('Low Access Census Tracts in Washington')
    fig.savefig('washington_low_access.png')


if __name__ == '__main__':
    main()
