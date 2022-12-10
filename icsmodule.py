def ics(rowlist):
    # imports
    from icalendar import Calendar, Event, vCalAddress, vText, Alarm
    from datetime import datetime, timedelta
    from dateutil.tz import tzlocal
    from pathlib import Path
    import os
    import pytz

    now = datetime.now()
    local_now = now.astimezone()
    local_tz = local_now.tzinfo
    local_tzname = local_tz.tzname(local_now)
    print()
    print('Rowlist')
    print(rowlist)
    print(len(rowlist))

    #print(rowlist[0]['date'])

    # init the calendar
    cal = Calendar()

    # Some properties are required to be compliant
    cal.add('prodid', '-//RE//python ics module v0.2//EN/')
    cal.add('version', '2.0')

    for i in range(0, len(rowlist)):
        ename = f"GT {rowlist[i]['start_time']} to {rowlist[i]['end_time']}"
        esumm = ename
        edesc = ''
        yr, mth, day = rowlist[i]['date'].split('-')
        h1, m1 = rowlist[i]['start_time'].split(':')
        h2, m2 = rowlist[i]['end_time'].split(':')

        yr, mth, day = int(yr), int(mth), int(day)
        h1, m1 = int(h1), int(m1)  #convert string to int
        h2, m2 = int(h2), int(m2)

        # Add subcomponents
        event = Event()
        event.add('name', ename)
        event.add('summary', esumm)
        event.add('description', edesc)
        event.add('dtstart', datetime(yr, mth, day, h1, m1))
        event.add('dtend', datetime(yr, mth, day, h2, m2))
        event.add('dtstamp', datetime.now(tz=pytz.timezone('US/Eastern')))  #Timestamp based on current time
        event['uid'] = datetime.now()  #just to give unique id for each event

        # Add the event to the calendar
        cal.add_component(event)
        
        ################################################
        #Add alarm
        alarm = Alarm()
        alarm.add('action', 'DISPLAY')

        alert_time = timedelta(
            hours=-3)  #ring alarm 3 hrs before event start time
        #alert_time = timedelta(minutes=-5)  #ring alarm 5 min before event start time
        alarm.add('trigger', alert_time)
        event.add_component(alarm)
        ################################################

    # Write to disk
    directory = Path.cwd() / 'MyCalendar'
    try:
        directory.mkdir(parents=True, exist_ok=False)
    except FileExistsError:
        print("Folder already exists")
    else:
        print("Folder was created")

    f = open(os.path.join(directory, 'time.ics'), 'wb')
    f.write(cal.to_ical())
    f.close()

    print()

    #Read the event
    e = open('MyCalendar/time.ics', 'rb')
    ecal = Calendar.from_ical(e.read())
    for component in ecal.walk():
        print(component.name)
    e.close()

    print()

    #Accessing subcomponents of event
    e = open('MyCalendar/time.ics', 'rb')
    ecal = Calendar.from_ical(e.read())
    for component in ecal.walk():
        if component.name == "VEVENT":
            print(component.get("name"))
            print(component.get("description"))
            print(component.decoded("dtstart"))
            print(component.decoded("dtend"))
    e.close()
