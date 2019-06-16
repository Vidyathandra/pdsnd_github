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
    city = input('Which city would you like the data to show: Chicago , Newyork or Washington:') 
    print (city)
    while (city != 'Chicago' and city != 'Newyork' and city != 'Washington'):
        city = input("Please make a valid selection : Chicago , Newyork , Washington : ")
        #print ("Inside While loop")
    print (city) 
    #print ("After while loop")
      
        
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Which month would you like the data for : January , February, March, April, May, June or All: ')
    print (month)
    while (month != 'January' and month != 'February' and month != 'March' and month != 'April' and month != 'May' and month != 'June' and month != 'All'):
        month = input("Please make a valid month selection : January , February , March , April , May , June or All : ")
        print (month)
        


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('which day would you like : Monday, Tuesday , Wednesday, Thursday , Friday , Saturday , Sunday or All : ')
    print (day)
    while (day != 'Monday' and day != 'Tuesday' and day != 'Wednesday' and day != 'Thursday' and day != 'Friday' and day != 'Saturday' and day != 'Sunday' and day != 'All'):
        day = input (" Please make a valid selection for day : Monday , Tuesday , Wednesday , Thursday , Friday , Saturday , Sunday or All : ")
        print (day)

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    if city == "Chicago":
        df = pd.read_csv("chicago.csv")
    elif city == "Washington": 
        df = pd.read_csv("washington.csv")
    else:
        df = pd.read_csv("new_york_city.csv")
    #print (df.head())
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Hour']=df['Start Time'].dt.hour
    df['Month']=df['Start Time'].dt.month
    dayOfWeek={0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
    df['Day']=df['Start Time'].dt.dayofweek.map(dayOfWeek)
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['Month'] == month]
    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['Day'] == day.title()]


    return df
def main():
    while True:
        city, month, day = get_filters()
        print (city, month, day)
        #city = 'Chicago'
        #month = 'January'
        #day = 'Sunday'
       # question = input ("Do you want to continue")
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        #time_stats(df)
        #station_stats(df)
        #trip_duration_stats(df)
        #user_stats(df)

        #restart = input('\nWould you like to restart? Enter yes or no.\n')
        #if restart.lower() != 'yes':
            #break
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month


    #df = pd.read_csv('chicago.csv')

    # TO DO: display the most common day of week


    # TO DO: display the most common start hour
    
    Popular_month = df['Month'].mode() [0]
    Popular_hour = df['Hour'].mode() [0]
    Popular_day = df['Day'].mode() [0]
    print ("Most popular hour with the specific selection : ", Popular_hour)
    print ("Most common Month with the specific selection: ", Popular_month)
    print ("Most common Day: ", Popular_day)
    
def station_stats(df):
    
    
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Popular_Start_station = df['Start Station'].mode() [0]
    print ("Most Popular Start Station : ", Popular_Start_station)


    # TO DO: display most commonly used end station
    Popular_End_station = df['End Station'].mode() [0]
    print ("Most Popular End station : ", Popular_End_station)
    
    


    # TO DO: display most frequent combination of start station and end station trip
    df['Concatenate']= df['Start Station']+ df['End Station']
    Popularcombination= df['Concatenate'].mode() [0]
    #print(df.groupby(['Start Station', 'End Station']).agg('max'))
    print ("Most Popular combination : ", Popularcombination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Diff']= df['End Time']-df['Start Time']
    Total_travel_time = df['Diff'].sum()
    print (" Total Travel time: ", Total_travel_time)


    # TO DO: display mean travel time
    Mean_travel_time = df['Diff'].mean()
    print (" Mean Travel Time : ", Mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
     #df['User Types'] = pd.read_csv(filename)
                      #print df
      #df['user_types'] = df['User Type'].value_counts()
    print(df['User Type'].value_counts())


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print(df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("Earliest Birth year :",df['Birth Year'].min())
        print("Most recent year :",df['Birth Year'].max())
        print("Most common year of birth :",df['Birth Year'].mode())
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


if __name__ == "__main__":
	main()
