
# coding: utf-8

# # Importing Libraries

# In[3]:


import time
import pandas as pd
import numpy as np


# # Loading dafa frames

# In[4]:


CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}


# In[5]:


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    
    print('Hello! Let\'s explore some US bikeshare data!')
     
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs  
    
    print('\nEnter the name of the city.. Please choose only one city: Chicago, New York City or Washington...\n')

    test_city = ['chicago', 'new york city', 'washington']

    while True:
        city = input().lower()
        if city in test_city:
            break
        else: print('\nInvalid city name. Please choose only one city: Chicago, New York City or Washington\n')
    
    # get user input for month (all, january, february, ... , june)
    
    test_month = ['january', 'february', 'march', 'april', 'may', 'june']
    
    print('\nPlease choose the month of the year: Choose from January to June...\n')
    
    while True:
        month = input().lower()
        if month =='all':
            break
        elif month in test_month:
            break
        else: print('\nSorry, there is no record. Choice from January to June\n')
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    
    test_day = ['monday' , 'tuesday', 'wednesday' , 'thrusday' , 'friday' , 'saturday', 'sunday']
    
    print('\nPlease choose a day of the week...\n')
 
    while True:
        day = input().lower()
        if day == 'all':
            break
        elif day in test_day:
            break
        else: print('\nSorry, this is not a valid day. Choose a valid day\n')
            
    print('-'*40)
    return city, month, day



# In[6]:


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


# In[7]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    month_common = df['month'].max()

    # display the most common day of week
    
    day_common = df['day_of_week'].max()

    # display the most common start hour

    start_common = df['Start Time'].max()
    
    print('Time Stats..')
    print('Most frequent month: ' ,  month_common)
    print('Most frequent day of the week: ' ,  day_common)
    print('Most frequent time: ' ,  start_common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[8]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    
    station_start_common = df['Start Station'].max()

    # display most commonly used end station
    
    station_end_common = df['End Station'].max()

    # display most frequent combination of start station and end station trip
    
    comb_station = (df['Start Station'] + '  ' + df['End Station']).max()
    
    print('Station Stats..')
    print('Most commonly used start station:  ', station_start_common)
    print('Most commonly used end station:  ', station_end_common)
    print('Most frequent combination of start station and end station trip:  ', comb_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[9]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    
    total_travel_time = df['Trip Duration'].sum()

    # display mean travel time
    
    mean_travel_time = df['Trip Duration'].mean()
    
    print('Trip Duration Stats..')
    print('Total travel time:  ' , total_travel_time)
    print('Mean travel time:  ' , mean_travel_time )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[10]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    
    total_user_types = df['User Type'].value_counts()
    
    
    # Display counts of gender
    
    if 'Gender' in df.columns:    
        gender = df['Gender'].dropna().unique()
        total_gender = len(gender) 

        print('Gender types:  ' , gender)
        print('Total genders:  ' , total_gender)

    # Display earliest, most recent, and most common year of birth
    
    if 'Birth Year' in df.columns:
    
        recent_birth = df['Birth Year'].dropna()
        recent_birth = recent_birth.astype(int)
        recent_birth = recent_birth.max()

        comon_year = df['Birth Year'].dropna()
        comon_year = comon_year.astype(int)
        comon_year = comon_year.value_counts().index[0]

        print('Most recent year of birth: ' , recent_birth)        
        print('Most common year of birth: ' , comon_year)
    
    print('User types:  ' , total_user_types)
   
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[30]:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        while True:
            data_raw = input('\nWould you like to see five rows of raw data? Enter yes or no.\n')
            if data_raw.lower() == 'no':                
                break     
            else: print(df.iloc[:6]) 
            break
  
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()


# In[ ]:




