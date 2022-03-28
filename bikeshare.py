import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_data = ['January','February','March','April','June']
Days_data  = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    global city, month, day
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
         city = input('please choose a city to explore it')
        except KeyError:
            print('Invalid')
        if (city != 'Chicago') and (city != 'New york' ) and (city != 'Washington'):
          print('You should enter Chicago or New york or Washington')
          continue
        else:
          break
        

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      try:  
        month = input("Do you filter by month? enter a month that you want to filter by it.... if you don't want to filter by month enter all.")
      except KeyError:
        print('Invalid Entry')
        continue
      if month not in month_data and month != 'all':
            print('please enter a valid month name')
      else:
          break
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      try:
        day = input("Do you filter by day of a week? enter a day that you want to filter by it in numbers.... if you don't want to filter by day enter all.")
      except KeyError:
        print("That's not a valid number.... please enter a valid number")
        continue
      if day not in Days_data and day != 'all':
        print('sorry, you have entered invalid day')
        continue
      else:
        break
        
    
    print('you have entered:\nCity {}\nMonth: {}\nDay: {}'.format(city.title(), month.title(), day.title()))
    print('-'*40)
    return city, month, day




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    ''' df['month'] = df['start_time'].dt.month'''
        
    common_month = df['month'].mode()[0]
    print('The common month is', common_month)

    # TO DO: display the most common day of week
    ''' df['day'] = df['start_time'].dt.day'''
        
    common_day = df['day_of_week'].mode()[0]
    print('The common day is', common_day)

    # TO DO: display the most common start hour
    '''df['hour'] = df['start_time'].dt.hour'''
        
    common_hour = df['hour'].mode()[0]
    print('The common hour is', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

   

    # TO DO: display most commonly used start station

    popular_start_station = df['Start Station'].mode()[0]
    print('Popular start station is', popular_start_station)

    # TO DO: display most commonly used end station
    
    popular_end_station   = df['End Station'].mode()[0]
    print('Popular end station is', popular_end_station)


    # TO DO: display most frequent combination of start station and end station trip

    df['route'] = 'From' + df['Start Station'] + 'To' + df['End Station']
    popular_route = df['route'].mode()[0]
    print('Most frequent combination of start station and end station trip:\n', popular_route)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_TravelTime = df['Trip Duration'].sum().sum()
    print("Total travel time is", Total_TravelTime)

    # TO DO: display mean travel time
    TravelTime_average = df['Trip Duration'].mean()
    print('Averge Total Time = ',TravelTime_average)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('There are ', user_types, 'User Type')

    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()
    print('The count of genders', gender)
   

    # TO DO: Display earliest, most recent, and most common year of birth
    Earliest = df['Birth Year'].min()
    print('The earliest year is', Earliest)
    
    most_recent = df['Birth Year'].max()
    print('The most recent year is', most_recent)
    
    most_common = df['Birth Year'].mode()[0]
    print('The common year is', most_common)
    
    print('The Earliest Year is {}\n'
          'The Recent Year is {}\n'
          'The Most common Year is {}\n'.format(int(Earliest), int(most_recent) , int(most_common)))
          

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            
            
def load_data(city, month, day):

  df = pd.read_csv(CITY_DATA[city])
    
  df['start_time'] = pd.to_datetime(df['start_time'])
      
  df['month']       = df['Start Time'].dt.month
  df['day_of_week'] = df['Start Time'].dt.day_name()
  df['hour']        = df['hour'].dt.hour()
    
    
  if month != 'all':

    months = ['January','February','March','April','June']
    month  = months.index(month) + 1              
                
    df     = df[df['month']  == month]
                
                
    if day !='all':
        df  = df[df['day_of_week']  == day.title()]           
              
            
                 
        
    """
    Loads data for the specified city and filters by month and day if applicable.
    
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    

    return df


if __name__ == "__main__":
	main()
