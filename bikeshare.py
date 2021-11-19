import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'}

DAYS = ['All', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

MONTHS = ['All', 'January', 'February', 'March', 'April', 'May', 'June']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "All" to apply no month filter
        (str) day - name of the day of week to filter by, or "All" to apply no day filter
    """
    print("\nHello! Let's explore some US bikeshare data!\n")

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Alright! Which city would you like to see data for? (Chicago, New York City, or Washington)\n').lower()
    while city not in CITY_DATA:
        print('\nPlease check your input, we are not able to analyze it.\n')
        print("Let's try again!\n")

        city = input('Alright! Which city would you like to see data for? (Chicago, New York City, or washington)\n').lower()

    # get user input for month (all, january, february, ... , june)
    MONTHS = ['All', 'January', 'February', 'March', 'April', 'May', 'June']
    month = input('\nWhich month would you like to filter data for? (All, January, February, ..., June)\n').title()
    while month not in MONTHS:
        print('\nPlease enter a valid month, or type "All" for no month filter.\n')
        month = input('\nWhich month would you like to filter data for? (All, January, February, ..., June)\n').title()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    DAYS = ['All', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    day = input('\nWhich day would you like to filter data for? (All, Monday, Tuesday, ..., Sunday)\n').title()
    while day not in DAYS:
        print('\nPlease enter a valid day, or type "All" for no day filter.\n')
        day = input('\nWhich day would you like to filter data for? (All, Monday, Tuesday, ..., Sunday)\n').title()

    print('-' * 50)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "All" to apply no month filter
        (str) day - name of the day of week to filter by, or "All" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        MONTHS = ['January', 'February', 'March', 'April', 'May', 'June']
        month = MONTHS.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')

    start_time = time.time()

    # display the most common month
    freqMonth = df['month'].mode()[0]
    print('The most common Month is: ', freqMonth)

    # display the most common day of week
    freqDay = df['day_of_week'].mode()[0]
    print('The most common Day of Week is: ', freqDay)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    freqHour = df['hour'].mode()[0]
    print('The most common Start Hour is: ', freqHour)

    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-' * 50)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')

    start_time = time.time()

    # display most commonly used start station
    popStartS = df['Start Station'].mode()[0]
    print('The most commonly used Start Station is: ', popStartS)

    # display most commonly used end station
    popEndS = df['End Station'].mode()[0]
    print('The most commonly used End Station is: ', popEndS)

    # display most frequent combination of start station and end station trip
    freqCombination = df['Start Station'].astype(str) + df['End Station'].astype(str)
    print('\nThe most frequent combination of Start and End Stations is: \n', freqCombination)

    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-' * 50)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')

    start_time = time.time()

    # display total travel time
    totTravelT = df['Trip Duration'].sum()
    print('The total Travel Time/Trip Duration is: ', totTravelT)


    # display mean travel time
    avgTravelT = df['Trip Duration'].mean()
    print('The average Travel Time/Trip Duration is: ', avgTravelT)

    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-' * 50)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')

    start_time = time.time()

    # Display counts of user types
    uCounts = df['User Type'].value_counts()
    print('The User types are: \n', uCounts)

    # Display counts of gender
    if city.title() == 'Chicago' or city.title() == 'New York City':
        genCounts = df['Gender'].value_counts()
        print('\nThe counts of Users by Gender are: \n', genCounts)

        # Display earliest, most recent, and most common year of birth
        uEarliest = int(df['Birth Year'].min())
        print("\nThe Users' Earliest year of birth: ", uEarliest)

        uRecent = int(df['Birth Year'].max())
        print("The Users' Most Recent year of birth: ", uRecent)

        uCommon = int(df['Birth Year'].mode()[0])
        print("The Users' Most Common year of birth: ", uCommon)

    else:
        print('\nNo extra data is available data to share.')

    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-' * 50)

def display_data(city):

    vData = input("\nStill interested? We're here for you!\n Would you like to view 5 rows of individual trip data? Please enter yes or no.\n").lower()

    while vData == 'yes':
        try:
            for data in pd.read_csv(CITY_DATA[city],chunksize=5):
                print(data)

                vData = input("\nWould you like to view more 5 rows of individual trip data? Please enter yes or no.\n").lower()
                if vData != 'yes':
                    print('\nThank you! Have a safe trip!\n')
                    break
            break
        except KeyboardInterrupt:
            print('\nThank you!')



def main():
    while True:
        city, month, day = get_filters()
        print(city, month, day)
        df = load_data(city, month, day)
        print(df.head())

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
