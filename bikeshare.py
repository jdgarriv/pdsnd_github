import time
import pandas as pd
import statistics

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months  = []
days = []
hours = []

startStation = []
endStation = []
startEnd = []

totalTime = []

subscriber = []
customer = []

male = []
female = []

birthYears = []

mostCommonMonth = 0
mostCommonDay = 99

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hi! Let\'s explore some bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    filtro1 = False
    while filtro1 == False:
        print("where would you like to get data from?  type New York City, Chicago or Washington")
        city = input()
        if city == "New York City":
            city="new york city"
            filtro1 = True
            break
        elif city == "Chicago":
            city="chicago"
            filtro1 = True
            break
        elif city == "Washington":
            city="washington"
            filtro1 = True
            break
        else:
            print("input incorrect try again.")

    # get user input for month (all, january, february, ... , june)
    global mostCommonMonth
    filtro2 = False
    while filtro2 == False:
        print("Which month? January, February, March, April, May, June or All")
        month = input()
        if month == "January":
            month = 1
            filtro2 = True
            mostCommonMonth = 1
            break
        elif month == "February":
            filtro2 = True
            month = 2
            mostCommonMonth = 2

            break
        elif month == "March":
            filtro2 = True
            month = 3
            mostCommonMonth = 3

            break
        elif month == "April":
            filtro2 = True
            month = 4
            mostCommonMonth = 4

            break
        elif month == "May":
            month = 5
            filtro2 = True
            mostCommonMonth = 5

            break
        elif month == "June":
            month = 6
            filtro2 = True
            mostCommonMonth = 6
            break
        elif month == "All":
            filtro2 = True
            break
        else:
            print("input incorrect try again.")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    global mostCommonDay
    filtro3 = False
    while filtro3 == False:
        print("which day? Please type your response as an integer (e.g, 0=monday, 1=tuesday... 6=sunday or All to apply no day filter)")
        day = input()
        if day == "1":
            mostCommonDay = 1
            filtro3 = True
            break
        elif day == "2":
            mostCommonDay = 2
            filtro3 = True
            break
        elif day == "3":
            mostCommonDay = 3
            filtro3 = True
            break
        elif day == "4":
            mostCommonDay = 4
            filtro3 = True
            break
        elif day == "5":
            mostCommonDay = 5
            filtro3 = True
            break
        elif day == "6":
            mostCommonDay = 6
            filtro3 = True
            break
        elif day == "0":
            mostCommonDay = 0
            filtro3 = True
            break
        elif day == "All":
            filtro3 = True
            break
        else:
            print("input incorrect try again.")

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

    df = pd.read_csv(CITY_DATA.get(city) )



    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["End Time"] = pd.to_datetime(df["End Time"])
    df["WeekDay"] = df["Start Time"].dt.weekday
    df["month"] = df["Start Time"].dt.month
    df["StartHour"] = df["Start Time"].dt.hour
    df["startEnd"] = df["Start Station"] + '  -  ' + df["End Station"]
    df["totalTime"] = df["End Time"] - df["Start Time"]
    df["subscriber"] = df["User Type"] == "Subscriber"
    df["customer"] = df["User Type"] == "Customer"
    df["totalTime"] = df["End Time"] - df["Start Time"]


    if city == "chicago" or city == "new york city":
        df["male"] = df["Gender"] == "Male"
        df["female"] = df["Gender"] == "Female"



    if day != "All":
        is_day = df["WeekDay"]== int(day)
        df=df[is_day]
        df = df.reset_index(drop=True)


    if month != "All":
         is_month = df["month"]== int(month)
         df=df[is_month]
         df = df.reset_index(drop=True)






















    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    global mostCommonMonth



    months = df["month"]
    mostCommonMonth = statistics.mode(months)

    print("The most common month is "+str(mostCommonMonth))


    # display the most common day of week

    global mostCommonDay

    days = df["WeekDay"]
    mostCommonDay = statistics.mode(days)

    print("the most common day is "+str(mostCommonDay))

    # display the most common start hour


    hours = df["StartHour"]
    print("the most common start hour is "+str(statistics.mode(hours)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    startStation = df["Start Station"]
    print("the most common start station is "+str(statistics.mode(startStation)))

    # display most commonly used end station
    endStation = df["End Station"]
    print("the most common end station is "+str(statistics.mode(endStation)))


    # display most frequent combination of start station and end station trip
    startEnd = df["startEnd"]
    print("the most common combination between start and end station is "+str(statistics.mode(startEnd)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    totalTime = df["totalTime"]

    mysum = df["totalTime"].sum()

    print("Total travel time is "+str(mysum))



    # display mean travel time

    print("travel time mean: " + str(mysum/len(totalTime)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    subscriber = df["subscriber"].sum()
    print("total subscribers: " + str(subscriber))

    customer = df["customer"].sum()
    print("total customers: " + str(customer))


    # Display counts of gender

    if city == "washington":
        print("No gender information available")
    else:
        male = df["male"].sum()
        print("Male: " + str(male))

        female = df["female"].sum()
        print("Female: " + str(female))

    # Display earliest, most recent, and most common year of birth

    if city == "washington":
        print("No Birth Year information available")
    else:
        df["Birth Year"] = df["Birth Year"].fillna(0)

        df_bday = df["Birth Year"]>0
        df_bday=df[df_bday]
        df_bday = df_bday.reset_index(drop=True)

        birthYears = df_bday["Birth Year"]

        print("the earliest birth year is "+str(min(birthYears)))
        print("the most recent birth year is "+str(max(birthYears)))
        print("the most common birth year is "+str(statistics.mode(birthYears)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # Display raw data

    counter = 0
    counterEnd = 5
    filtroIndividualInfo = True
    while filtroIndividualInfo == True:
        print ('Would you like to get information about individual trips? Enter yes or no')
        individualInfo = input()
        print (individualInfo)

        if individualInfo == "yes":
            for x in range(counter, counterEnd):
                print(df.loc[[x]])
            counter = counter + 5
            counterEnd = counterEnd + 5

        elif individualInfo == "no":
            filtroIndividualInfo = False
            break

        else:
            print ("Please answer yes or no")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
