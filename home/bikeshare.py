import time
import pandas as pd
import numpy as np
import json

# Constant to store list of months
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

# Constant to store list of days
DAYS = {'sunday':0, 'monday':1, 'tuesday':2, 'wednesday':3, \
        'thursday':4, 'friday':5, 'saturday':6 }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Would you like to see data for Chicago, New York or Washington?\n").lower()
    while(city.lower() != "chicago" and city.lower() != "new york" and city.lower() != "washington"):
        city = input("Would you like to see data for Chicago, New York or Washington?\n").lower()
        
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month? January, February, March, April, May, or June.Type 'all' for no time filter.\n").lower()
        # Checks if input matches the month in the MONTHS constant
        if month in MONTHS:
            break
        # Exceptions if filter should not specify a month
        if month == 'all':
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)    
    while True:
        day = input("Which day? Please type your response  in words(e.g .sunday).Type 'all' for no time filter.\n").lower()
         # Checks if input matches the day in the DAYS constant
        if day in DAYS:
            break
          # Exceptions if filter should not specify a particular day
        if day == 'all':
            break
            
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=""
    if(city == "chicago"):
        df = pd.read_csv('./chicago.csv')     
    if(city == "new york"):
        df = pd.read_csv('./new_york_city.csv')
    if(city == "washington"):
        df = pd.read_csv('./washington.csv')
  
     # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

     # filter by month if input was provided
    if month != 'all':
        month =  MONTHS.index(month) + 1
        df = df[ df['month'] == month ]

    # filter by day of week if input was provided
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[ df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("The most common month is :", most_common_month)

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("The most common day of week is :", most_common_day_of_week)

    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is :", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station :", most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station :", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination = (df["Start Station"] + " - " + df["End Station"]).value_counts().idxmax()
    print("The most commonly used start station and end station : {}"\
            .format(most_frequent_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time :", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # Display counts of user types
    print("Counts of user types:\n")
    count_of_users = df['User Type'].value_counts()
    for index, each_user_count in enumerate(count_of_users):
        print("  {}: {}".format(count_of_users.index[index], each_user_count))

    print()
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print("Counts of gender:\n")
        count_of_gender = df['Gender'].value_counts()
        for index,each_gender_count   in enumerate(count_of_gender):
            print("  {}: {}".format(count_of_gender.index[index], each_gender_count))
    
        print()
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        birth_year = df['Birth Year']
        
        most_common_year = birth_year.value_counts().idxmax()
        print("The most common birth year:", most_common_year)

        most_recent = birth_year.max()
        print("The most recent birth year:", most_recent)

        earliest_year = birth_year.min()
        print("The most earliest birth year:", earliest_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def load_user_option(message_type):
    '''
    Get options for restarting the program. If yes it proceeds, no ends program. 
    Invalid inputs trigger user to enter correct value
    '''
    restart = input('\n'+message_type+'\n')   
    while(restart.lower() != "yes" and restart.lower() != "no"):
         restart = input('\nInvalid Option!!!'+message_type+'\n') 
    if restart.lower() == 'yes':
        return 'yes'
    return 'no'

def display_raw_data(df):
    '''
    Prompts user to get raw data in iterations of 5
    '''
    # Gets the number of rows in a dataframe
    row_length = df.shape[0]
    for i in range(0, row_length, 5):
        
        option = load_user_option('Would you like to view individual trip data? Type "yes" or "no"')
        if option.lower() == 'no':
           break
        
        # retrieve and convert data to json format
        row_data = df.iloc[i: i + 5].to_json(orient='records', lines=True).split('\n')
        for row in row_data:
            # Loops to display each user data
            parsed_row = json.loads(row)
            json_row = json.dumps(parsed_row, indent=2)
            print(json_row)


def main():
    while True:
        # Asks user to specify a city, month, and day to analyze.
        city, month, day = get_filters()
        #Loads data for the specified city and filters by month and day if applicable.
        df = load_data(city, month, day)

        #Displays statistics on the most frequent times of travel.
        time_stats(df)
        #Displays statistics on the most popular stations and trip.
        station_stats(df)
        #Displays statistics on the total and average trip duration.
        trip_duration_stats(df)
        #Displays statistics on bikeshare users.
        user_stats(df)
        # Prompts user to get raw data
        display_raw_data(df)

        #Gets user input to run the program again or exit program
        restart = load_user_option('Would you like to restart? Enter yes or no.') 
        if restart.lower() == 'no':
            break
        
if __name__ == "__main__":
	main()
