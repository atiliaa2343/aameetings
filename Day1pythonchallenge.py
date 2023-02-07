print("Welcome to RAANA (Richmond Area Alcoholics Anonymous and Narcotics Anonymous) Meeting Locator")
print("This app was designed for addicts and alcoholics to be able to locate meetings near their location on any given day or time.")  
location = input("Do you allow RAANA to access your location? (yes or no)")


if location == 'yes': 
    import re 
    import json 
    from urllib.request import urlopen 
    url = 'http://ipinfo.io/json' 
    response = urlopen(url)
    data = json.load(response)

    IP = data['ip'] 
    org = data['org']
    city = data['city'] 
    country = data['country'] 
    region = data['region']  
    postal = data['postal'] 
    print('Postal is', postal)
    


    from datetime import datetime 
    from datetime import time
    date = datetime.now() 
    day = date.strftime('%A') 
    #once I figure out everything else I will come back to add in what time it is dor the user 

    if postal == '23230' and day == 'Sunday' or 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday' or 'Saturday' or 'Sunday' and date == '6:45': 
        print('On Awakening') 
        print('Time: 6:45am Address: 4819 Monument Ave, West End 23220')
    elif postal == '23225' and day == 'Sunday' or 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday' or 'Saturday' and date == '7:30':  
        print("Early Morning Serenity")
        print("Time: 7:30am Address: 6020 Midlothian Tpke, Southside 23225") 
    elif postal == '23924' and day == 'Sunday': 
        print("Keep It Simple") 
        print("Time: 9:00am Address: 121 E 2nd St, Chase City 23924")
    elif postal == '23233' and day == 'Sunday': 
        print("Spiritual Gathering") 
        print("Time: 9:00am Address: 12050 Ridgefield Pkwy, Wst End 23233")  
    elif postal == '23221' and day == 'Sunday': 
        print("The Fireside Group ") 
        print("Time: 9:30am Address: 1300 Blanton Ave, Richmond 23221") 
    elif postal == '23832' and day == 'Sunday': 
        print("Suffered Enough on Sundays ") 
        print("Time: 9:30am Address: 6221 Newbys Bridge Rd, Southside 23832") 
    elif postal == 'Awakenings' and day == 'Sunday': 
        print("Awakenings") 
        print("Time: 9:30am Address: 31 E Belt Blvd, Southside 23224") 
    elif postal == '23220' and day == 'Sunday': 
        print("Diversity Richmond") 
        print("Time: 11:30am Address: 1407 Sherwood Ave, Richmond 23220") 
    elif postal == '23225' and day == 'Sunday': 
        print("Fe Y Esperanza") 
        print("Time: 12:00pm Address: 306 Turner Road, Southside 23225") 
    elif postal == '23233' and day == 'Sunday': 
        print("Step Sisters")
        print("12050 Ridgefield Pkwy, West End 23233") 
    elif postal == '23220' and day == 'Sunday' and date == '1:00': 
        print("Pass It On") 
        print("Time: 1:00pm Address: 2621 Grove Ave, Richmond 23220") 
    elif postal == '23220' and day == 'Sunday' or 'Saturday' and date == '1:00': 
        print("210") 
        print("Time: 1:00pm Address: 210 N Masdison Street, Richmond 23220 ")
    elif postal == '23229' and day == 'Sunday': 
        print("The Outsiders") 
        print("Time: 2:00pm Address: 2101 N Parham Road, West End 23229") 
    elif postal == '23150' and day == 'Sunday': 
        print("East End Sunday Bunch")
        print("2Time: 3:00pm Address: 3 W Williamsburg Rd, Sandston 23150") 
    elif postal == '23294' and day == 'Sunday': 
        print('Serenity Sisters Group') 
        print("Time: 3:30pm Address: 2211 SkipwithRd, West End 23294") 
    elif postal == '23230' and day == 'Sunday': 
        print("Let Go And Let God") 
        print("Time: 4:00pm Address: 4819 Monument Ave, West End 23230") 
    elif postal == '23235' and day == 'Sunday': 
        print("Keystone") 
        print("2071 Buford Rd, Southside 23235") 
    elif postal == '23005' and day == 'Sunday': 
        print("Terminally Unique") 
        print("Time: 6:00pm Address: 401 Virginia St, Ashland 23005") 
    elif postal == '23223' and day == 'Sunday': 
        print("God Could And Would")  
        print("Time: 6:00pm Address: 2301 Cedar St, Church Hill 23223 ") 
    elif postal == '23220' and day == 'Sunday' and date == '6:00': 
        print("Open Invitation") 
        print("Time: 6:00pm Address: 2621 Grove Ave, Richmond 23220") 
    elif postal == '23111' and day == 'Sunday': 
        print("Serenity Seekers") 
        print("Time: 6:30pm Address: 7046 Cold Harbor Rd, Mechanicsville") 
    elif postal == '23225' and day == 'Sunday' and date == '6:30': 
        print("Speaking of Steps") 
        print("Time: 6:30pm Address: 4401 Forest Hill Ave, Southside 23225")
    elif postal == '23832' and day == 'Sunday': 
        print("Captured By Grace") 
        print("Time: 7:00pm Address: 14411 Beach Rd, Chesterfield 23832") 
    elif postal == '23927' and day == 'Sunday': 
        print("Clarkville Recovering") 
        print("Time: 7:00pm Address: 7488 Highway 12, Clarksville 23927") 
    elif postal == '23220' and day == 'Sunday' or 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday' or 'Saturday': 
        print("Madison Street") 
        print("Time: 7:00pm Address: 210 N Madison St, Richmond 23220") 
    elif postal == '23230' and day == 'Sunday': 
        print("Westminster") 
        print("Time: 7:00pm Address: 4103 Monument Ave, West End 23230") 
    elif postal == '23901' and day == 'Sunday': 
        print("Hampton-Sydney Life Boat")
        print("Time: 7:30pm Address: 418 College Church Rd, Farmville 23901") 
    elif postal == '23111' and day == 'Sunday': 
        print("Book Study Group") 
        print("Time: 7:30pm Address: 6502 Creighton Rd, Mechanicsville 23111")
    elif postal == '23228' and day == 'Sunday': 
        print("Keep It Simple") 
        print("Time: 7:30pm Address: 8000 Hermitage Rd, Northside 23228") 
    elif postal == '23832' and day == 'Sunday': 
        print("Woodlake Group") 
        print("Time: 7:30pm Address: 15640 Hampton Park Dr, Southside 23832") 
    elif postal == '23235' and day == 'Sunday': 
        print("AA Today") 
        print("Time: 7:30pm Address: 11300 W Hugenot Rd, Southside 23235") 
    elif postal == '23226' and day == 'Sunday' : 
        print("Sunday Night Survivors") 
        print("Time: 7:30pm Address: 6000 Grove Ave, West End 23226") 
        print('') 
        print('Slip Away') 
        print('Time: 7:30pm Address: 6000 Grove Ave, West End 23226') 
    elif postal == '23233' and day == 'Sunday': 
        print('F.A.R OUT') 
        print('Time: 7:30pm Address: 12050 Ridgefield Pkwy, West End 23233') 
        print('Discovery Group') 
        print('Time: 7:30pm Address: 12050 Ridgefield Pkwy, West End 23233') 
    elif postal == '23225' and day == 'Sunday' or 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday' or 'Saturday' and date == '8:00': 
        print('Fe Y Esperanza')
        print('Time: 8:00pm Address: 306 Turner Rd, Southside 23225') 
    elif postal == '23220' and day == 'Sunday' or 'Saturday' and date == '10:30': 
        print('RVA Late Nite') 
        print('Time: 10:30pm Address: 1205 W Franklin St, Richmond 23220') 
    elif postal == '23221' and day == 'Monday': 
        print('A Faith That Works') 
        print('Time: 7:30am Address: 1000 Blanton Avenue,Richmond 23221')
    elif postal ==  '23112' and day == 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday' and date == '7:30': 
        print('Suffered Enough') 
        print('Time: 7:30am Address: 12920 Hull Street Rd, Southside 232112') 
    
    elif postal == '23229' and day == 'Monday': 
        print('Serenity U') 
        print('Time: 10:00am Address: 8600 Quioccasin Rd, West End 23229') 
    elif postal == '23059' and day == 'Monday': 
        print('Living In The Solution')
        print('Time: 10:00am Address: 5000 Pouncey Tract Rd, West End 23059') 
    elif postal == '23111' and day == 'Monday': 
        print('Mechanicsville Group')
        print('Time: 11:30am Address: 8016 Atlee Rd, Mechanicsville 23111') 
    elif postal == '23219' and day == 'Monday': 
        print('Downtowner BYOL') 
        print('Time: 12:00pm Address: 13 N Fifth St, Richmond 23219') 
    elif postal == '23229' and day == 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday': 
        print('Back Again') 
        print('Time: 12:00pm Address: 1101 Forest Ave, West End 23229') 
    elif postal == '23060' and day == 'Monday': 
        print('Monday H.O.W') 
        print('Time: 12:00pm Address: 4491 Springfield Rd, West End 23060') 
    elif postal == '23235' and day == 'Monday': 
        print('Common Bond') 
        print('Time: 1:00pm Address: 9800 W Hugenot Rd, Southside 23235') 
    elif postal == '23233' and day == 'Monday': 
        print('Dirty 5:30') 
        print('Time: 5:30pm Address: 12050 Ridgefield Pkwy, West End 23233') 
    elif postal == '23226' and day == 'Monday': 
        print('449ERS') 
        print('Time: 5:30pm Address: 6000 Grove Ave, West End 23226') 
    elif postal == '23229' and day == 'Monday': 
        print('Greenwood Commuters') 
        print('Time: 5:30pm Address: 903 Forest Ave, West End 23229') 
    elif postal == '23832' and day == 'Monday': 
        print('The Principles Group') 
        print('Time: 5:45pm Address: 6200 Courthouse Rd, Chesterfield 23832') 
    elif postal == '23111' and day == 'Monday': 
        print('Miracles on Monday') 
        print('Time: 6:00pm Address: 6930 Cold Harbor Rd, Mechanicsville 23111') 
    elif postal == '23970' and day == 'Monday': 
        print('5th Tradition') 
        print('Time: 6:00pm Address: 627 W Danville St, South Hill 23970') 
    elif postal == '23112' and day == 'Monday': 
        print('Courage') 
        print('Time: 6:00pm Address: 6601 Woodlake Village Pkwy, Southside 23112') 
    elif postal == '23901' and day == 'Monday': 
        print('Not Alone') 
        print('Time: 6:30pm Address: 212 High St, Farmville 23901') 
    elif postal == '23220' and day == 'Monday': 
        print('QCFW') 
        print("Time: 6:30pm Address: 1407 Sherwood Ave, Richmond 23220") 
    elif postal == '23224' and day == 'Monday' or 'Wednesday' or 'Saturday': 
        print('The 700 Group') 
        print('Time: 6:30pm Address: 700 Dinwiddie Ave, Southside 23224') 
        print('') 
        print('The 2220 Group') 
        print('Time: 6:30pm Address: 2220 Stockton St, Southside 23224') 
    elif postal == '23015' and day == 'Monday':
        print('Beaverdam Big Book Study') 
        print('Time: 7:00pm Address: 19110 Beaver Dam Rd, BEaverdam 23015') 
    elif postal == '23930' and day == 'Monday': 
        print('Crewe Group') 
        print('Time: 7:00pm Address: 107 1/2 East Carolina Street, Crewe 23930') 
    elif postal == '23116' and day == 'Monday': 
        print('Clearing the Wreckage') 
        print('Time: 7:00pm Address: 8391 Atlee Rd, Mechanisville 23116') 
    elif postal == '23284' and day == 'Monday': 
        print('The Grapevine') 
        print('Time: 7:00pm Address: 1103 W Marshall St, Richmond 23284') 
    elif postal == '23235' and day == 'Monday': 
        print('Big Book Thumpers') 
        print('Time: 7:00pm Address: 8320 Hull St Rd, Southside 23235') 
    elif postal == '23221' and day == 'Monday': 
        print('Time: 7:00pm Address: 4200 Cary Street Rd, West End 23221') 
    elif postal == '23005' and day == 'Monday': 
        print('Hanover- Ashland Group')
        print('Time: 7:30pm Address: 401 Virginia St, Ashland 23005') 
    elif postal == '23111' and day == 'Monday': 
        print('Next Generation Young Peoples') 
        print('Time: 7:30pm Address: 6502 Creighton Rd, Mechanicsvile 23111') 
    elif postal == '23113' and day == 'Monday': 
        print('Time: 7:30pm Address: 13617 Midlothian Tpke, Southside 23113') 
    elif postal == '23059' and day == 'Monday': 
        print(' 12 in 4 Meeting') 
        print('Time: 7:30pm Address: 5000 Pouncery Tract Rd, West End 23059') 
    elif postal == '23294' and day == 'Monday': 
        print('Hungry for Change') 
        print('Time: 7:30pm Address: 8985 Hungary Rd, West End 23294') 
    elif postal == '23226' and day == 'Monday': 
        print('Westhampton Big Book')
        print('Time: 7:30pm Address: 6100 Patterson Ave, West End 23226') 
    elif postal == '23924' and day == 'Monday': 
        print('Keep It Simple')
        print('Time: 8:00pm Address: 121 E 2nd St, Chase City 23924')
    elif postal == '23086' and day == 'Monday':
        print('King Williams Crossroads Group')
        print('Time: 8:00pm Address: 901 Sharon Rd, King William 23086') 
    elif postal == '23150' and day == 'Monday': 
        print('Sandston Group')
        print('Time: 8:00pm Address: 23 W Williamsburg Rd, Sandston 23150') 
    elif postal == '24592' and day == 'Monday': 
        print('South Boston Group') 
        print('Time: 8:00pm Address: 515 Yancy St, South Boston 24592') 
    elif postal == '23225' and day == 'Monday': 
        print('Phoenix Group') 
        print('Time: 8:00pm Address: 6023 Jahnke Rd, Southside 23225')
        print('Fe Y Esperanza') 
    elif postal == '23230' and day == 'Monday': 
        print('Easy does it Womens') 
        print('Time: 8:00pm Address: 4103 Monument Ave, West End 23230') 
    elif postal == '23220' and day == 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday' and date == '10:00': 
        print('RVA Late Nite') 
        print('Time: 10:00pm Address: 1205 W Franklin St, Richmond 23220')   
    elif postal == '23059' and day == 'Tuesday': 
        print('Sunrise Serenity') 
        print('Time: 6:45am Address: 5000 Pouncey Tract Rd, West End 23059') 
    elif postal == '23221' and day == 'Tuesday': 
        print('A Faith That Works') 
        print('Time: 7:30am Address: 1000 Blanton Avenue, Richmond 23221') 
    elif postal == '23140' and day == 'Tuesday': 
        print('Emmaus Discussion Group') 
        print('Time: 10:00am Address: 6700 Emmaus Church Rd, Providence Forge 23140') 
    elif postal == '23059' and day == 'Tuesday': 
        print('Humility Is A Gift') 
        print('Time: 10:00am Address: 5000 Pouncey Tract Rd, West End 23059') 
    elif postal == '23294' and day == 'Tuesday': 
        print('Recovering Parents') 
        print('Time: 10:00am Address: 2211 Skipwith Rd, West End 23294') 
    elif postal == '23235' and day == 'Tuesday': 
        print('Common Solution') 
        print('Time: 12:00pm Address: 2531 Buford Rd, Southside 23235') 
    elif postal == '23226' and day == 'Tuesday': 
        print('Changing Directions') 
        print('Time: 12:30pm Address: 1400 Horsepan Rd, West End 23226') 
    elif postal == '23225' and day == 'Tuesday': 
        print('Beginners Meeting') 
        print('Time: 5:30pm Address: 6020 Midlothian Tpke, Southside 23225 ') 
    elif postal == '23294' and day == 'Tuesday': 
        print('Imagine The Freedom') 
        print('Time: 5:30pm Address: 2604 N Parham Rd, West End 23294') 
    elif postal == '23229' and day == 'Tuesday': 
        print('Greenwood Commuters') 
        print('Time: 5:30pm Address: 903 Forest Ave, West End 23229')
    else: 
        print("No meeting located. ")
  
else: 
    print("What zipcode you located in?").lower()
