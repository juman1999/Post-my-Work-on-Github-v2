<<<<<<< HEAD
import time
import pandas as pd
import numpy as np

# Define CITY_DATA
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city = input('Would you like to see data for Chicago , New York City or Washington ? ')
    city = city.casefold()
    while city not in CITY_DATA:
        city = input('Invalid city name.Try Again!')
        city = city.casefold()
        
       
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = input('Would you like to filter the data by month ? Enter the month from January to June OR Enter "all" for no month filter : ')
    month = month.casefold()
    while month not in months:
        month = input('Invalid month name.Try Again!')
        month = month.casefold()
        
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input('Would you like to filter the data by day ? Enter the day from Monday to Sunday OR Enter "all" for no day filter : ')
    day = day.casefold()
    while day not in days:
        day = input('Invalid day name.Try Again!')
        day = day.casefold()

    # Print line to saperte the parts
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
    # creating the dataframe.
    df = pd.read_csv(CITY_DATA[city])

    
    
    # Converte the type of the coulmn 
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    
   
    # Extract date element from Start Time 
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    
    
    # Filtering by month
    if month != 'all':
        # using index function to get the month place in the list for example june is the sixth element (5+1) in this list
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Filtering by month to create new dataframe
        df = df[df['month'] == month]

        
        
    # Filtering by day of week 
    if day != 'all':
        # Filtering by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

        

    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # Converte the type of the coulmn 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    
    
    # TO DO: display the most common month
    # create a month column
    df['month'] = df['Start Time'].dt.month
    # Finding the most common month 
    common_month = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print('Most Common Month:', months[common_month-1])

    
    
    # TO DO: display the most common day of week
    # create a day_of_week column
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    # Finding the most common day of the week from 0 to 6
    common_day = df['day_of_week'].mode()[0]
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print('Most Common Day:', days[common_day])

    
    
    # TO DO: display the most common start hour
    # create a hour column
    df['hour'] = df['Start Time'].dt.hour
    # Finding the most common hour from 0 to 23
    common_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', common_hour)


    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('~'*40)


    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    

    # TO DO: display most commonly used start station
    print('Most Commonly Used Start Station: ', df['Start Station'].mode()[0])
    
    
    
    # TO DO: display most commonly used end station
    print('Most Commonly Used End Station: ', df['End Station'].mode()[0])
    
    
    
    # TO DO: display most frequent combination of start station and end station trip
print('\nMost Frequent Combination of Start and End Station Trips:\n\n',df.groupby(['Start Station', 'End Station']).size().nlargest(1))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('~'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    
    
    # TO DO: display total travel time
    print('Total Trip Duration:', df['Trip Duration'].sum())

    
    
    # TO DO: display mean travel time
    print('Mean Trip Duration:', df['Trip Duration'].mean())

    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('~'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types,'\n')
    
    
    
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:    
           user_input = input('Please Enter Yes or No:\n')
            user_input = user_input.lower()
        n = 0        
        while True :
            if user_input.lower() == 'yes':
        
                print(df.iloc[n : n + 5])
                n += 5
                user_input = input('\nWould you like to see more data? (Type:Yes/No).\n')
                while user_input.lower() not in enter:
                    user_input = input('Please Enter Yes or No:\n')
                    user_input = user_input.lower()
            else:
                break           

                
                
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        #check wheather the user is entering the valid entry or not
        while restart.lower() not in enter:
            restart = input('Please Enter Yes or No:\n')
            restart = restart.lower()
        if restart.lower() != 'yes':
            print('Thank You!')
            break


if __name__ == "__main__":
	main()
||||||| 4362027
=======
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city = input('Would you like to see data for Chicago , New York City or Washington ? ')
    city = city.casefold()
    while city not in CITY_DATA:
        city = input('Invalid city name.Try Again!')
        city = city.casefold()
        
       
    #  get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = input('Would you like to filter the data by month ? Enter the month from January to June OR Enter "all" for no month filter : ')
    month = month.casefold()
    while month not in months:
        month = input('Invalid month name.Try Again!')
        month = month.casefold()
        
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input('Would you like to filter the data by day ? Enter the day from Monday to Sunday OR Enter "all" for no day filter : ')
    day = day.casefold()
    while day not in days:
        day = input('Invalid day name.Try Again!')
        day = day.casefold()

    
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
    # creating the dataframe.
    df = pd.read_csv(CITY_DATA[city])

    
    
    # Converte the type of the coulmn 
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    
   
    # Extract date element from Start Time 
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    
    
    # Filtering by month
    if month != 'all':
        # using index function to get the month place in the list for example june is the sixth element (5+1) in this list
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Filtering by month to create new dataframe
        df = df[df['month'] == month]

        
        
    # Filtering by day of week 
    if day != 'all':
        # Filtering by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

        

    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # Converte the type of the coulmn 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    
    
    # TO DO: display the most common month
    # create a month column
    df['month'] = df['Start Time'].dt.month
    # Finding the most common month 
    common_month = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print('Most Common Month:', months[common_month-1])

    
    
    # TO DO: display the most common day of week
    # create a day_of_week column
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    # Finding the most common day of the week from 0 to 6
    common_day = df['day_of_week'].mode()[0]
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print('Most Common Day:', days[common_day])

    
    
    # TO DO: display the most common start hour
    # create a hour column
    df['hour'] = df['Start Time'].dt.hour
    # Finding the most common hour from 0 to 23
    common_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', common_hour)


    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('~'*40)


    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    

    # TO DO: display most commonly used start station
    print('Most Commonly Used Start Station: ', df['Start Station'].mode()[0])
    
    
    
    # TO DO: display most commonly used end station
    print('Most Commonly Used End Station: ', df['End Station'].mode()[0])
    
    
    
    # TO DO: display most frequent combination of start station and end station trip
print('\nMost Frequent Combination of Start and End Station Trips:\n\n',df.groupby(['Start Station', 'End Station']).size().nlargest(1))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('~'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    
    
    # TO DO: display total travel time
    print('Total Trip Duration:', df['Trip Duration'].sum())

    
    
    # TO DO: display mean travel time
    print('Mean Trip Duration:', df['Trip Duration'].mean())

    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('~'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types,'\n')
    
    
    
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:    
           user_input = input('Please Enter Yes or No:\n')
            user_input = user_input.lower()
        n = 0        
        while True :
            if user_input.lower() == 'yes':
        
                print(df.iloc[n : n + 5])
                n += 5
                user_input = input('\nWould you like to see more data? (Type:Yes/No).\n')
                while user_input.lower() not in enter:
                    user_input = input('Please Enter Yes or No:\n')
                    user_input = user_input.lower()
            else:
                break           

                
                
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        #check wheather the user is entering the valid entry or not
        while restart.lower() not in enter:
            restart = input('Please Enter Yes or No:\n')
            restart = restart.lower()
        if restart.lower() != 'yes':
            print('Thank You!')
            break


if __name__ == "__main__":
	main()
>>>>>>> documentation
