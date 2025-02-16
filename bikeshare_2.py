import time
import pandas as pd
import numpy as np

# loading necessary information for functions
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

time_answers = ['month','day','both','none']

months = ['january','february','march','april','may','june']

number_to_day = {
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday"
}

# function grabs the filter conditions for the questions later on
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        city (str): Name of the city to analyze.
        month (str | int): Name of the month or 9 for no month filter.
        day (int): Number representing the day of the week (1=Sunday, 7=Saturday), or 0 for no filter.
    """
    print("Hello! Let's explore some US bikeshare data!")

    # Dictionary of available cities

    def get_valid_input(prompt, valid_options=None, convert_func=None):
        """Handles user input validation."""
        while True:
            user_input = input(prompt).strip().lower()
            if valid_options and user_input in valid_options:
                return user_input
            elif convert_func:
                try:
                    return convert_func(user_input)
                except ValueError:
                    pass
            print("Invalid input. Please try again.")

    # Get city selection
    city = get_valid_input(
        "Would you like to look at data for Chicago, New York, or Washington? ",
        valid_options=CITY_DATA.keys()
    )
    print(f"\nSounds good! We will be looking at data for {city.title()}.")

    # Get time filter option
    time_answer = get_valid_input(
        '\nWould you like to filter for a specific time period? Choose one: "month", "day", "both", or "none": ',
        valid_options=time_answers
    )

    # Default values (no filters)
    month, day = 9, 0

    # Get month filter
    if time_answer in {"month", "both"}:
        month = get_valid_input(
            '\nWhat month would you like to filter for? (January - June): ',
            valid_options=months
        )

    # Get day filter
    if time_answer in {"day", "both"}:
        day = get_valid_input(
            "\nEnter a number between 1 (Sunday) and 7 (Saturday) for the day filter: ",
            convert_func=lambda x: int(x) if 1 <= int(x) <= 7 else None
        )

    print("-" * 40)
    return city, month, day


# function loads the data per the users filters
def load_data(city, month = 9, day = 0):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # path to data will differ
    path = r'/Users/austintam/Documents/learning/udacity/python section/all-project-files'+f'/{CITY_DATA.get(city)}' 

    df = pd.read_csv(path)

    # convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of the week
    df['month'] = df['Start Time'].dt.month_name()  # Full month name
    df['day_of_week'] = df['Start Time'].dt.day_name()  # Full day name

    if month != 9:
        df = df[df['month'].str.lower() == month.lower()]

    if day != 0:
        df = df[df['day_of_week'] == number_to_day.get(day)]
        
    return df

# function grabs the time stats
def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    if month != 9:
    # display the most common month
        most_common_month = df['month'].mode()[0]
        print(f'The most common month for travel is {most_common_month}')

    if day != 0:
        # display the most common day of week
        most_common_day = df['day_of_week'].mode()[0]
        print(f'The most common day for travel is {most_common_day}')

    # display the most common start hour
    most_common_hour = df['Start Time'].dt.hour.mode()[0]
    print(f'The most common hour for travel is {most_common_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# function grabs the station stats per users filters
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print(f'The most common start station is {most_common_start_station}')


    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print(f'The most common end station is {most_common_end_station}')

    # display most frequent combination of start station and end station trip
    most_common = (df.groupby(['Start Station','End Station'])
                   .size()
                   .idxmax()
    )
    start_station, end_station = most_common

    print(f'The most common start and end station combination is starting at {start_station} and ending at {end_station}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# function grabs the trip duration metrics
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = round(df['Trip Duration'].sum()/(3600*24),2) # converting it to days
    print(f'The total number of days traveled for this selection of data is {total_travel_time} days')

    # display mean travel time
    avg_travel_time = round(df['Trip Duration'].mean()/60,2) # convert to minutes
    print(f'The average trip duration is {avg_travel_time} minutes')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# filters grabs the user stats from the data
def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(f'Here is the distribution of user types \n\n {user_types}\n')

    if city != 'washington':
        # Display counts of gender
        gender_counts = df['Gender'].value_counts()
        print(f'Here is the distribution of gender \n\n {gender_counts}\n')

        # Display earliest, most recent, and most common year of birth
        min_year = int(df['Birth Year'].min())
        max_year = int(df['Birth Year'].max())
        mode_year = int(df['Birth Year'].mode()[0])

        print(f'The youngest user was born in {max_year}')
        print(f'The oldest user was born in {min_year}')
        print(f'The most common birth year for users in this slice of data is {mode_year}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# function prints raw data from users request
def display_raw_data(df):
    """ displays trip data at the users request """
    i = 0
    raw = input("Would you like to view individual trip data? Yes or No.").lower().strip()
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df[i:i+5]) 
            raw = input("Would you like to see five more rows? Yes or No: ").lower().strip()
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower().strip()

# runs all of the functions
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower().strip() in ['yes','no']:
            if restart.lower() != 'yes':
                break
        else:
            print("Please enter either yes or no.")

if __name__ == "__main__":
	main()
