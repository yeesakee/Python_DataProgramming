# Name: Yeesa Kee
# Section: AE
# This program solves 8 problems given in Homework 3.
# This includes showing specified data in the problems with the given
# csv file using pandas. Graphing specific graphs using the data in the
# given csv file, and using machine learning.


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error


def main():
    data = pd.read_csv("hw3-nces-ed-attainment.csv", na_values="---")
    print("Part 0: Problem 1")
    print(completions_between_years(data, 2007, 2008, 'F'))
    print("\n Part 0: Problem 2")
    print(compare_bachelors_1980(data))
    print("\n Part 0: Problem 3")
    print(top_2_2000s(data))
    print("\n Part 0: Problem 4")
    print(percent_change_bachelors_2000s(data))

    sns.set()
    line_plot_bachelors(data)
    bar_chart_high_school(data)
    plot_hispanic_min_degree(data)
    print("\n Part 2: Problem 1")
    print(fit_and_predict_degrees(data))


def completions_between_years(data, year_one, year_two, sex):
    """
    Returns all rows of data which matches the given sex, and between
    year_one (inclusive) and year_two (exclusive).
    Returns None if no data is found for the parameter.
    """
    # Stores a Series filtered by year_one(inclusive) and year_two(exclusive)
    year = (data['Year'] >= year_one) & (data['Year'] < year_two)
    # Stores a Series filtered by sex
    data_sex = data['Sex'] == sex
    return None if data[year & data_sex].empty else data[year & data_sex]


def compare_bachelors_1980(data):
    """
    Returns a DataFrame from data with a row for men and a row for women
    with a "Sex" column and a "Total" column. It will represent the
    percentages for women vs. men having earned a Bachelor's Degree in 1980.
    """
    # Stores a Series filtered by 'Min degree' that has the value 'bachelor's'
    degree = data['Min degree'] == "bachelor's"
    # Stores a Series filtered by 'Sex' with values that equal 'F' or 'M'
    sex = (data['Sex'] == 'F') | (data['Sex'] == 'M')
    # Stores a Series filtered by 'Year' that has the value 1980
    year = data['Year'] == 1980
    # Stores the filtered DataFrame
    filtered = data.loc[degree & sex & year]
    return filtered.loc[:, ['Sex', 'Total']]


def top_2_2000s(data):
    """
    Returns a Series with the top two values representing the two most
    commonly awarded education attainment awarded between 2000-2010(inclusive).

    The program uses the mean percent over the years to compare the values.
    """
    # Stores a Series filtered by 'Year'
    year = (data['Year'] >= 2000) & (data['Year'] <= 2010)
    # Stores a Series filtered by 'Sex'
    sex = data['Sex'] == 'A'
    # Stores a Series filtered by 'Year' and 'Sex' and is then grouped by
    # Min degree and is ordered by the mean of 'Total'
    education = data[year & sex].groupby('Min degree')['Total'].mean()
    education = education.nlargest()
    # return the top two values of the Series
    return education[:2]


def percent_change_bachelors_2000s(data, sex='A'):
    """
    Returns a float that represents the difference between the total
    percentage of people of gender sex, that have earned a bachelor's degree
    in 2000 compared to 2010.
    """
    # Stores a Series filtered by sex
    gender = data['Sex'] == sex
    # Stores a Series filtered by 'Min degree' that has the value bachelor's
    degree = data['Min degree'] == "bachelor's"
    # Stores a Series filtered by 'Year' == 2000
    year_2000 = data['Year'] == 2000
    # Stores a Series filtered by 'Year' == 2010
    year_2010 = data['Year'] == 2010
    # Stores a Series filtered by gender, degree, and year_2000
    result_2000 = data[gender & year_2000 & degree]['Total']
    # Stores a Series filtered by gender, degree, and year_2010
    result_2010 = data[gender & year_2010 & degree]['Total']
    return result_2010.squeeze() - result_2000.squeeze()


def line_plot_bachelors(data):
    """
    Creates a line plot that shows the total percentages of all people
    that have earned at least a Bachelor's degree over time.
    Saves the plot as "line_plot_bachelors.png".
    """
    # Stores a Series filtered by 'Min degree' == bachelor's
    degree = data['Min degree'] == "bachelor's"
    # Stores a Series filtered by 'Sex' == A
    sex = data['Sex'] == 'A'
    # Stores a DataFrame filtered by degree and sex
    my_data = data[degree & sex]
    # plots the line graph
    sns.relplot(x='Year', y='Total', kind='line', data=my_data)
    plt.xlabel('Year')
    plt.ylabel('Percentage')
    plt.title("Percentage Earning Bachelor's over Time")
    plt.savefig('line_plot_bachelors.png', bbox_inches='tight')


def bar_chart_high_school(data):
    """
    Creates a bar chart that shows the total percentages of women, men,
    and total people that have earned at least a high school degree in 2009.
    Saves the plot as "bar_chart_high_school.png".
    """
    # Stores a Series filtered by 'Min degree' == high school
    degree = data['Min degree'] == 'high school'
    # Stores a Series filtered by 'Year' == 2009
    year = data['Year'] == 2009
    # Stores a DataFrame filtered by degree and year
    my_data = data[degree & year]
    # plots the bar graph
    sns.catplot(x='Sex', y='Total', kind='bar', data=my_data)
    plt.xlabel('Sex')
    plt.ylabel('Percentage')
    plt.title('Percentage Completed High School by Sex')
    plt.savefig('bar_chart_high_school.png', bbox_inches='tight')


def plot_hispanic_min_degree(data):
    """
    Creates a line plot of the percentage of Hispanic individuals that have
    earned a high school or a bachelor's degree in 1990 and 2010 (inclusive).
    Saves the graph as "plot_hispanic_min_degree.png".
    """
    # Stores a Series filtered by 'Year'
    year = (data['Year'] >= 1990) & (data['Year'] <= 2010)
    # Stores a Series filtered by 'Min degree' == high school or bachelor's
    degree = (data['Min degree'] == 'high school') | \
             (data['Min degree'] == "bachelor's")
    # Stores a DataFrame filtered by year and degree with columns
    # Hispanic, Total, Year, and Min degree
    my_data = data[year & degree].loc[:,
                                      ['Hispanic', 'Total', 'Year',
                                       'Min degree']]
    # plots the line graph and create the lines based on Min degree categories
    sns.relplot(x='Year', y='Total', hue='Min degree', style='Min degree',
                kind='line', data=my_data)
    plt.xlabel("Year")
    plt.ylabel("Percentage")
    plt.title("Percentage of Hispanics Earning High School or" +
              " Bacherlor's over Time")
    plt.savefig('plot_hispanic_min_degree.png', bbox_inches='tight')


def fit_and_predict_degrees(data):
    """
    Creates a machine learning model for the provided DataFrame.
    Returns the test mean squared error.
    """
    # Stores a DataFrame with the columns Year, Min degree, Sex, and Total
    my_data = data.loc[:, ['Year', 'Min degree', 'Sex', 'Total']]
    # Drop any rows that have missing data
    my_data = my_data.dropna()
    # Stores a DataFrame with columns Year, Min degree, and Sex
    X = my_data.loc[:, ['Year', 'Min degree', 'Sex']]
    # Convert string values to their dummy encoding
    X = pd.get_dummies(X)
    # Stores a Series filtered by Total
    y = my_data['Total']
    # Split the data to train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = DecisionTreeRegressor()
    model.fit(X_train, y_train)
    y_test_predict = model.predict(X_test)
    return mean_squared_error(y_test, y_test_predict)


if __name__ == '__main__':
    main()
