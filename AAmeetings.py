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
    elif postal == '23927' and day == 'Sunday' or 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday' or 'Saturday': 
        print("Clarkville Recovering") 
        print("Time: 7:00pm Address: 7488 Highway 12, Clarksville 23927") 
    elif postal == '23220' and day == 'Sunday' or 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday' or 'Saturday' and date == '7:00': 
        print("210 Madison") 
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
    elif postal == '23221' and day == 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday' : 
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
    elif postal == '23229' and day == 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday' or 'Saturday' or 'Sunday': 
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
    elif postal == '23111' and day == 'Tuesday': 
        print('Road to Serenity Group') 
        print('Time: 5:30pm Address: 7339 Atlee Rd, Mechanicsville 23111') 
    elif postal == '23970' and day == 'Tuesday': 
        print('5th Tradition') 
        print('Time: 627 W Danville St, South Hill 23970')  
    elif postal == '23294' and day == 'Tuesday': 
        print('SkipWith Womens Group')
        print('Time:6:00pm Address: 2211 Skipwith Rd, West End 23294') 
    elif postal == '23927'and day == 'Tuesday': 
        print('Clarksville Recovering') 
        print('Time: 7:00pm Address: 219 Fifth St, Clarksville 23927') 
    elif postal == '23947' and day == 'Tuesday': 
        print('Keysville Reflections') 
        print('Time: 7:00pm Address: 181 Briery Church Rd, Keysville 23947') 
    elif postal == '23806' and day == 'Tuesday': 
        print('In The Moment') 
        print('Time: 7:00pm Address: 901 Sharon Rd, King William 23086') 
    elif postal == '23060' and day == 'Tuesday': 
        print('Filling The Void') 
        print('Time: 7:00pm Address: 1300 New York Ave, Northside 23060') 
    elif postal == '23059' and day == 'Tuesday': 
        print('The Way Out') 
        print('Time: 7:00pm Address: 10069 Brook Rd, Northside 23059') 
    elif postal == '23235' and day == 'Tuesday': 
        print('Jaywalkers Group') 
        print('Time: 7:00pm Address: 9201 W Hugenot Rd. Southside 23235') 
    elif postal == '23225' and day == 'Tuesday': 
        print('Into Action') 
        print('Time: 7:00pm Address: 5400 Forest Hill Ave, Southside 23225') 
    elif postal == '23233' and day == 'Tuesday': 
        print('Rule 62 Mens Group')
        print('Time: 7:00pm Address: 12050 Ridgefield Pkwy, West End 23233') 
    elif postal == '23221' and day == 'Tuesday': 
        print('A Sufficient Substitute') 
        print('Time: 7:00pm Address: 4200 Dover Rd, West End 23221') 
    elif postal == '23229' and day == 'Tuesday': 
        print('What is the point?')
        print('Time: 7:00pm Address: 8960 River Rd, West End 23229') 
    elif postal == '23221' and day == 'Tuesday': 
        print('Park View') 
        print('Time: 7:00pm Address: 4301 Patterson Ave, West End 23221') 
    elif postal == '23116' and day == 'Tuesday': 
        print('Serenity At Cool Spring Group') 
        print('Time: 7:30pm Address: 9283 Atlee Station Rd, Mechanicsville 23116') 
    elif postal == '23150' and day == 'Tuesday': 
        print('Time: 7:30pm Address: 100 W Williamsburg Rd, Sandston 23150') 
    elif postal == '23235' and day == 'Tuesday': 
        print('Dr.Bob Saw It Too') 
        print('Time: 7:30pm Address: 8320 Hull Street Rd, Southside 23235') 
    elif postal == '23236' and day == 'Tuesday': 
        print('Lets Get Sober')
        print('Time: 7:30pm Address: 1500 Courthouse Rd, Southside 23226') 
    elif postal == '23002' and day == 'Tuesday': 
        print('Grupo Liberacion'): 
        print('Time: 8:00pm Address: 16351 Church St, Amelia 23002') 
    elif postal == '23139' and day == 'Tuesday': 
        print('No Name Group') 
        print('Time: 8:00pm Address: 2245 Hugenot Trl, Powhatan 23139') 
    elif postal == '23221' and day == 'Tuesday': 
        print('Restored to Sanity') 
        print('Time: 8:00pm Address: 800 Blanton Ave, Richmond 23221') 
    elif postal == '23220' and day == 'Tuesday': 
        print('Mens Meeting') 
        print('Time: 8:00pm Address: 2709 Monument Ave, Richmond 23220')
    elif postal == '23113' and day == 'Wednesday': 
        print('Miracles In The Morning') 
        print('Time: 7:30am Address: 985 Hugenot Trl, Powhatan 23113')  
    elif postal == '23225' and day == 'Wednesday' or 'Thursday': 
        print('Early Morning Serenity') 
        print('Time: 7:30am Address: 6020 Midlothian Tpke, Southside 23225') 
    elif postal == '23059' and day == 'Wednesday': 
        print('Spiritual Life Is Not A Theory') 
        print('Time: 10:00am Address: 5000 Pouncey Tract Rd, West End 23059') 
    elif postal == '23225' and day == 'Wednesday': 
        print('Jefferson Street Gang') 
        print('Time: 11:00am Address: 4401 Forest Hill Ave, Southside 23225') 
    elif postal == '23111' and day == 'Wednesday': 
        print('Baby Steps') 
        print('Time: 11:30am Address: 8016 Atlee Red, Mechanicsville 23111') 
    elif postal == '23005' and day == 'Wednesday': 
        print('Reflections At Noon') 
        print('Time: 12:00pm Address: 401 Virginia St, Ashland 23005') 
    elif postal == '23284' and day == 'Wednesday': 
        print('Hitting The Books') 
        print('Time: 12:00pm Address: 1103 W Marshall St, Richmond 23284') 
    elif postal == '23220' and day == 'Wednesday': 
        print('Wednesday Noon') 
        print('Time: 12:00pm Address: 1603 Monument Ave, Richmond 23220') 
    elif postal == '24592' and day == 'Wednesday': 
        print('South Boston Group') 
        print('Time: 12:00pm Address: 800 Main St, South Boston 24592') 
    elif postal == '23832' and day == 'Wednesday': 
        print('Valentine') 
        print('Time: 12:00pm Address: 6200 Courthouse Rd, Southside 23832') 
    elif postal == '23231' and day == 'Wednesday': 
        print('Happy Survivors') 
        print('Time: 5:30pm') 
        print('Address: 2727 Charles City Rd, East End 23231') 
    elif postal == '23225' and day == 'Wednesday' or 'Thursday': 
        print('Beginners Meeting') 
        print('Time: 5:30pm Address: 6020 Midlothian Tpke, Southside 23225') 
    elif postal == '23226' and day == 'Wednesday': 
        print('Longest Journey') 
        print('Time: 5:30pm Address: 6000 Grove Ave, West End 23226') 
    elif postal == '23832' and day == 'Wednesday': 
        print('The Principles Group') 
        print('Time: 5:45pm Address: 6200 Courthouse Rd, Chesterfield 23832') 
    elif postal == '23970' and day == 'Wednesday' or 'Thursday': 
        print('5th Tradition') 
        print('627 W Danville St, South hill 23970') 
    elif postal == '23901' and day == 'Wednesday': 
        print('Not Alone') 
        print('212 High St, Framville 23901') 
    elif postal == '23086' and day == 'Wednesday': 
        print('Know Your Worth') 
        print('Time: 6:30pm Address: 172 Courthouse Ln, King William 23086') 
    elif postal == '23832' and day == 'Wednesday': 
        print('Captured By Grace') 
        print('Time: 7:00pm Address: 14411 Beach Rd, Chesterfield 23832') 
    elif postal == '23930' and day == 'Wednesday' or 'Thursday': 
        print('Crewe Group') 
        print('Time: 7:00pm Address: 107 1/2 East Carolina Street, Crewe 23930') 
    elif postal == '23063' and day == 'Wednesday': 
        print('An AA Group') 
        print('Time: 7:00pm Address: 5257 Old Columbia Rd, Goochland 23063') 
    elif postal == '23111' and day == 'Wednesday': 
        print('Free Men') 
        print('Time: 7:00pm Address: 7159 Mechanicsville Tpke,Mechanicsville 23111') 
    elif postal == '23220' and day == 'Wednesday': 
        print('Shore of Faith') 
        print('Time: 7:00pm Address: 2503 Park Ave, Richmond 23220') 
    elif postal == '23235' and day == 'Wednesday': 
        print('Buford Group') 
        print('Time: 7:00pm Address: 2071 Buford Rd, Southside 23235') 
    elif postal == '23226' and day == 'Wednesday': 
        print('Recovery Room') 
        print('Time: 7:00pm Address: 5403 Monument Ave, West End 23226') 
    elif postal == '23229' and day == 'Wednesday': 
        print('Alcoholics With Depression') 
        print('Time: 7:00pm Address: 9315 Three Chopt Rd, West End 23229') 
    elif postal == '23192' and day == 'Wednesday': 
        print('33 West Recovery') 
        print('Time: 7:30pm Address: 15599 Mountain Rd, Northside 23192') 
    elif postal == '23284' and day == 'Wednesday': 
        print('All Queer, No Beer') 
        print('Time: 7:30pm Address: 1103 W Marshall St , 23284') 
    elif postal == '23235' and day == 'Wednesday': 
        print('Bon Air Big Book Study Group') 
        print('Time: 7:30pm Address: 2040 McRae Rd, Southside 23235') 
    elif postal == '23226' and day == 'Wednesday': 
        print('Westhampton 12 and 12') 
        print('Time: 7:30pm Address: 6100 Patterson Ave, West End 23226') 
    elif postal == '23233' and day == 'Wednesday': 
        print('Happy Destiny') 
        print('Time: 7:30pm Address: 12050 Ridgefield Pkwy, West End 23233') 
    elif postal == '23150' and day == 'Wednesday': 
        print('Sandston 12 & 12 Group') 
        print('Time: 8:00pm Address: 23 W Williamsburg Rd, Sandston 23150') 
    elif postal == '23970' and day == 'Wednesday': 
        print('South hill Group') 
        print('Time: 8:00pm Address: 105 Franklin St, South Hill 23970') 
    elif postal == '23225' and day == 'Wednesday': 
        print('Speaking of Steps') 
        print('Time: 8:00pm Address: 4401 Forest Hill Ave,Southside 23225') 
    elif postal == '23233' and day == 'Wednesday': 
        print('The 164 Group') 
        print('Time: 8:00pm Address: 12320 W Broad St, West End 23233') 
    elif postal == '23059' and day == 'Thursday': 
        print('A Design For Living') 
        print('Time: 10:00am Address: 5000 Pouncey Tract Rd, West End 23059') 
    elif postal == '23235' and day == 'Thursday': 
        print('Common Solution') 
        print('Time: 12:00pm Address: 2531 Buford Rd, Southside 23235') 
    elif postal == '23224' and day == 'Thursday': 
        print('We Came To Believe') 
        print('Time: 12:00pm Address: 437 E Belt Blvd, Southside 23224') 
    elif postal == '23060' and day == 'Thursday': 
        print('Broad Highway') 
        print('Time: 12:00pm Address: 4491 Springfield Rd, West End 23060') 
    elif postal == '23226' and day == 'Thursday': 
        print('Never Alone') 
        print('Time: 12:00pm Address" 1400 Horsepen Rd, West End 23226') 
    elif postal == '23113' and day == 'Thursday': 
        print('The Way Out') 
        print('Time: 5:30pm Address: 1050 Hugenot Springs Rd, Southside 23113')
    elif postal == '23226' and day == 'Thursday': 
        print('Thursday Night Beginners') 
        print('Time: 5:30pm Address: 6000 Grove Ave, West End 23226') 
    elif postal == '23059' and day == 'Thursday': 
        print('Short Pump Serenity') 
        print('Time: 5:30pm Address: 5000 Pouncey Tract Rd, West End 23059') 
    elif postal == '23927' and day == 'Thursday': 
        print('Chicks At Six Group') 
        print('Time: 6:00pm Address: 219 Fifth St, Clarksville 23927') 
    elif postal == '23112' and day == 'Thursday': 
        print('Courage') 
        print('Time: 6:00pm Address: 6601 Woodlake Village Pkwy, Southside 23112') 
    elif postal == '23230' and day == 'Thursday': 
        print('Drop The Rock') 
        print('Time: 6:00pm Address: 4819 Monument Ave, West End 23230')  
    elif postal == '23059' and day == 'Thursday': 
        print('The Way Out') 
        print('Time: 7:00pm Address: 10069 Brook Rd, Northside 23059') 
    elif postal == '23139' and day == 'Thursday': 
        print('Powahatan Meeting') 
        print('Time: 7:00pm Address: 3910 Old Buckingham Rd, Powhatan 23139') 
    elif postal == '23284' and day == 'Thursday': 
        print('We Agnostics') 
        print('Time: 7:00pm Address: 1103 W Marshall St, Richmond 23284') 
    elif postal == '23236' and day == 'Thursday': 
        print('Belles Of The Bar') 
        print('Time: 7:00pm Address: 11000 Smoketree Dr, Southside 23236') 
    elif postal == '23225' and day == 'Thursday': 
        print('Into Action') 
        print('Time:7:00pm Address: 5400 Forest Hill Ave, Southside 23225') 
    elif postal == '23114' and day == 'Thursday': 
        print('Cornerstone') 
        print('Time: 7:00pm Address: 11551 Lucks Ln, Southside 23114') 
    elif postal == '23229' and day == 'Thursday': 
        print('Caring And Sharing') 
        print('Time: 7:00pm Address: 2101 N Parham Rd, West End 23229') 
    elif postal == '23226' and day == 'Thursday': 
        print('Womens Exp. Strength and Hope') 
        print('Time: 7:00pm Address: 6000 Grove Ave, West End 23226') 
    elif postal == '23221' and day == 'Thursday': 
        print('Outlaw SafeCracker Group') 
        print('Time: 7:00pm Address: 4200 Cary Street Rd, West End 23221') 
    elif postal == '23005' and day == 'Thursday': 
        print('Hanover-Ashland Group') 
        print('Time: 7:30pm Address: 401 Virginia St, Ashland 23005') 
    elif postal == '23831' and day == 'Thursday': 
        print('More Shall Be Revealed') 
        print('Time: 7:30pm Address: 6600 Greenyard Rd, Chester 23831') 
    elif postal == '23223' and day == 'Thursday': 
        print('Freedom Group') 
        print('Time: 7:30pm Address: 213 N 25th St, Church Hill 23223') 
    elif postal == '23235' and day == 'Thursday': 
        print('As Bill Sees It') 
        print('Time: 7:30pm Address: 10525 W Hugenot Rd, Southside 23235') 
    elif postal == '23233' and day == 'Thursday': 
        print('Ad Infinitum') 
        print('Time: 7:30pm Address: 12050 Ridgefield Pkwy, West End 23233') 
    elif postal == '23116' and day == 'Thursday': 
        print('Do The Next Right Thing') 
        print('Time: 8:00pm Address: 9019 New Bethesda Rd, Mechanicsville 23116') 
    elif postal == '23150' and day == 'Thursday': 
        print('St.Johns Group')
        print('Time: 8:00pm Address: 23 W Williamsburg Rd, Sandston 23150') 
    elif postal == '24592' and day == 'Thursday': 
        print('South Boston Group') 
        print('Time: 8:00pm Address: 800 Main St, South Boston 24592') 
    elif postal == '23220' and day == 'Thursday': 
        print('Honesty By Candlelight') 
        print('Time: 8:30pm Address: 2501 Park Ave, Richmond 23220') 
    elif postal == '23060' and day == 'Friday': 
        print('Glen Allen Group') 
        print('Time: 10:00am Address: 10299 Woodman Rd, Northside 23060') 
    elif postal == '23294' and day == 'Friday': 
        print('Recovering Parents') 
        print('Time: 10:00am Address: 2211 Skipwith Rd, West End 23294') 
    elif postal == '23059' and day == 'Friday': 
        print('Progress Not Perfection') 
        print('Time: 10:00am Address: 5000 Pouncey Tract Rd, West End 23059') 
    elif postal == '23226' and day == 'Friday': 
        print('Friendship Womens') 
        print('Time: 10:30am Address: 5200 Grove Ave, West End 23226') 
    elif postal == '23223' and day == 'Friday': 
        print('Sober All Day') 
        print('Time: 12:00pm Address: 3908 Nine Mile Rd, East End 23223') 
    elif postal == '24592' and day == 'Friday': 
        print('Time: 12:00pm Address: 800 Main St, South Boston 24592') 
    elif postal == '23226' and day == 'Friday': 
        print('Time: 12:30pm Address: 1400 Horsepen Rd, West End 23226') 
    elif postal == '23235' and day == 'Friday': 
        print('Common Bond') 
        print('Time: 1:00pm Address: 9800 W Hugenot Rd, Southside 23235') 
    elif postal == '23225' and day == 'Friday': 
        print('Skys The Limit') 
        print('Time: 5:30pm Address: 6020 Midlothian Tpke, Southside 23225') 
    elif postal == '23059' and day == 'Friday': 
        print('Short Pump Serenity') 
        print('Time: 5:30pm Address: 5000 Pouncey Tract Rd, West End 23059') 
    elif postal == '23226' and day == 'Friday': 
        print('How It Works') 
        print('Time: 5:30pm Address: 6000 Grove Ave, West End 23226') 
    elif postal == '23005' and day == 'Friday': 
        print('Ashland Womens Group') 
        print('Time: 6:00pm Address: 125 Beverly Rd, Ashland 23005') 
    elif postal == '23229' and day == 'Friday': 
        print('Essentials Of Recovery') 
        print('Time: 6:30pm Address: 920 Maybeury Dr, West End 23229') 
    elif postal == '23015' and day == 'Friday': 
        print('Beaverdam Meeting') 
        print('Time: 7:00pm Address: 19110 Beaver Dam Rd, Beaverdam 23015') 
    elif postal == '23040' and day == 'Friday': 
        print('Cumberland Group') 
        print('Time: 7:00pm Address: 50 Stoney Point Rd, Cumberland 23040') 
    elif postal == '23231' and day == 'Friday': 
        print('Daily Reprieve') 
        print('Time: 7:00pm Address: 1637 Williamsburg Rd, East End 23231') 
    elif postal == '23228' and day == 'Friday': 
        print('Lakeside Discussion')
        print('Time: 7:00pm Address: 7610 Staple Mills Rd, Northside 23228 ') 
    elif postal == '23220' and day == 'Friday': 
        print('RVA POC') 
        print('Time: 7:00pm Address: 2503 Park Ave, Richmond 23220') 
    elif postal == '23284' and day == 'Friday': 
        print('We Agnostics') 
        print('Time: 7:00pm Address: 1103 W Marshall St, Richmond 23284') 
    elif postal == '23970' and day == 'Friday': 
        print('South Hill Group')
        print('Time: 7:00pm Address: 105 Franklin St, South Hill 23970')  
    elif postal == ' 23113' and day == 'Friday': 
        print('Friday Night Group Beginners') 
        print('Time: 7:00pm ') 
    elif postal == '23113' and day == 'Friday': 
        print('Salisbury Serenity Group') 
        print('Time: 7:00pm Address: 13621 W Salisbury Rd, Southside 23113') 
    elif postal == '23974' and day == 'Friday': 
        print('Big Book Bunch') 
        print('Time: 7:00pm Address: 1423 8th St, Victoria 23974') 
    elif postal == '23238' and day == 'Friday': 
        print('Prisms Of Recovery') 
        print('Time: 7:00pm Address: 10611 Patterson Ave, West End 23238') 
    elif postal == '23226' and day == 'Friday': 
        print('In The Solution') 
        print('Time: 6006 Three Chopt Rd, West End 23226') 
    elif postal == '23116' and day == 'Friday': 
        print('Hope On Atlee Road Group')
        print('Time: 7:30pm Address: 8391 Atlee Rd, Mechanicsville 23116')
    elif postal == '23228' and day == 'Friday': 
        print('The Chair In The Center')
        print('Time: 7:30pm Address: 8000 Hermitage Rd, Northside 23228') 
    elif postal == '23220' and day == 'Friday': 
        print('Not Saints') 
        print('Time: 7:30pm Address: 8000 Hermitage Rd, Northside 23228') 
    elif postal == '23150' and day == 'Friday': 
        print('Choices and Changes Group')
        print('Time: 7:30pm Address: 100 W Williamsburg Rd, Sandston 23150') 
    elif postal == '23233' and day == 'Friday': 
        print('Free For All') 
        print('Time: 7:30pm Address: 12050 Ridgefield Pkwy, West End 23233') 
    elif postal == '23226' and day == 'Friday': 
        print('Between Scylla and Charybdis') 
        print('Time: 7:30pm Address: 5801 Bremo Rd, West End 23226')
    elif postal == '23002' and day == 'Friday': 
        print('Grupo Liberacion') 
        print('Time: 16351 Church St, Amelia 23002') 
    elif postal == '23937' and day == 'Friday': 
        print('Drakes Branch Serenity Group')
        print('Time: 8:00pm Address: 4525 Drakes Main St, Drakes Branch 23937') 
    elif postal == '23141' and day == 'Friday': 
        print('Change We Must') 
        print('Time: 8:00pm Address: 4001 New Kent Hwy, Quinton 23141') 
    elif postal == '23220' and day == 'Friday': 
        print('Midtown') 
        print('Time: 8:00pm Address: 1205 W Franklin St, Richmond 23220') 
    elif postal == '23236' and day == 'Friday': 
        print('Friday Night Step Meeting') 
        print('Time: 8:00pm Address: 901 S Providence Rd, Southside 23236') 
    elif postal == '23113' and day == 'Friday': 
        print('Wet Birds Movin On') 
        print('Time: 8:00pm Address: 2440 Hancroft Dr, Southside 23113') 
    elif postal == '23225' and day == 'Friday': 
        print('Candlelight Serenity') 
        print('Time: 10:00pm Address: 12050 Ridgefield Pkwy, ') 
    elif postal == '23229' and day == 'Saturday': 
        print('Eye Opener') 
        print('Time: 7:30am Address: 920 Mayebury Dr, West End 23229') 
    elif postal == '23059' and day == 'Saturday': 
        print('Willing To Grow') 
        print('Time: 8:30am Address: 5000 Pouncey Tract Rd, West End 23059') 
    elif postal == '23230' and day == 'Saturday': 
        print('Boiled Owls') 
        print('Time: 8:45am Address: 4819 Monument Ave, West End 23230') 
    elif postal == '23005' and day == 'Saturday': 
        print('Basic Text Big Book Study') 
        print('Time: 9:00am Address: 800 Thompson St, Ashland 23005') 
    elif postal == '23924' and day == 'Saturday': 
        print('Keep It Simple') 
        print('Time: 9:00am Address: 121 E 2nd St, Chase City 23924') 
    elif postal == '23220' and day == 'Saturday': 
        print('Sober Dreams') 
        print('Time: 9:30am Address: 1205 W Franklin St, Richmond 23220') 
    elif postal == '23114' and day == 'Saturday': 
        print('Our Way Out') 
        print('Time: 9:30am Address: 11551 Lucks Ln, Southside 23114') 
    elif postal == '23235' and day == 'Saturday': 
        print('Unity South') 
        print('Time: 9:30am Address: 923 Buford Rd, Southside 23235') 
    elif postal == '23832' and day == 'Saturday': 
        print('Saturday Morning Serenity') 
        print('Time: 10:00am Address: 6200 Courthouse Rd, Chesterfield 23832') 
    elif postal == '23141' and day == 'Saturday': 
        print('New Kent Group') 
        print('Time: 10:00am Address: 2607 New Kent Hwy, Quinton 23141') 
    elif postal == '23238' and day == 'Saturday': 
        print('A New Beginning') 
        print('Time: 10:00am Address: 12291 River Rd, West End 23238') 
    elif postal == '23226' and day == 'Saturday': 
        print('Open Doors') 
        print('Time: 10:00am Address: 5716 Monument Ave, West End 23226') 
    elif postal == '23233' and day == 'Saturday': 
        print('The Breakfast Club') 
        print('Time: 11:00am Address: 12050 Ridgefield Pkwy, West End 23233') 
    elif postal == '23284' and day == 'Saturday': 
        print('Boys II Men') 
        print('Time: 12:30pm Address: 1103 W Marshall St, Richmond 23284') 
    elif postal == '23954' and day == 'Saturday': 
        print('Joys Of Living') 
        print('Time: 1:00pm Address: 4999 Patrick Henry Hwy, Meherrin 23954') 
    elif postal == '23227' and day == 'Saturday': 
        print('Today Big Book Study Group') 
        print('Time: 2:30pm Address: 3601 Seminary Ave, Northside 23227') 
    elif postal == '23228' and day == 'Saturday': 
        print('Northside Fellowship') 
        print('Time: 5:00pm Address: 2300 Dumbarton Rd, Northside 23228') 
    elif postal == '23221' and day == 'Saturday': 
        print('Saturday Night Serenity On Grove') 
        print('Time: 5:30pm Address: 4101 Grove Ave, Richmond 23221') 
    elif postal == '23229' and day == 'Saturday': 
        print('Unity') 
        print('Time: 5:30pm Address: 920 Maybeury Dr, West End 23229') 
    elif postal == '23059' and day == 'Saturday': 
        print('Living Sober') 
        print('Time: 6:00pm Address: 12320 Winns Church Ed, Northside 23059') 
    elif postal == '23220' and day == 'Saturday': 
        print('LGBTQ+ Serenity') 
        print('Time: 6:00pm Address: 1407 Sherwood Ave, Richmond 23220') 
    elif postal == '23150' and day == 'Saturday': 
        print('A Vision For You Group') 
        print('Time: 6:00pm Address: 23 W Williamsburg Rd, Sandston 23150') 
    elif postal == '23228' and day == 'Saturday': 
        print('Northside Fellowiship Group') 
        print('Time: 7:00pm Address: 7401 Woodman Rd, Northside 23228') 
    elif postal == '23233' and day == 'Saturday': 
        print('S.O.S (Sober On Saturday)') 
        print('Time: 7:00pm Address: 12050 Ridgefield Pkwy, West End 23233') 
    elif postal == '23002' and day == 'Saturday': 
        print('Grupo Liberacion') 
        print('Time: 8:00pm Address: 16351 Church St, Amelia 23002') 
    elif postal == '23832' and day == 'Saturday': 
        print('Young and Sober') 
        print('Time: 8:00pm Address: 6200 Courthouse Rd, Chesterfield 23832') 
    elif postal == '23111' and day == 'Saturday': 
        print('God is Saturday Night') 
        print('Time: 8:00pm Address: 7159 Mechanicsville Tpke, Mechanicsville 23111') 
    elif postal == '23221' and day == 'Saturday': 
        print('Restored To Sanity') 
        print('Time: 8:00pm Address: 800 Blanton Ave, Richmond 23221') 
    elif postal == '23113' and day == 'Saturday': 
        print('Saturday Night- Huguenot') 
        print('Time: 8:00pm Address: 985 Hugenot Trl, Southside 23113') 
    elif postal == '23220' and day == 'Saturday': 
        print('Sober Dreams') 
        print('Time: 8:30pm Address: 1205 W Franklin St, Richmond 23220') 
    else: 
        print("No meeting located. ")
  
else: 
    print("What zipcode you located in?").lower()
