import icalendar
import datetime
import zoneinfo
from pathlib import Path

def today():
    """Returns a string containing all events for the day, their location and their time"""
    cal_path = Path("data/cal.ics")                                     # Rename your calendar in cal.ics and put in in a folder called data (or just change the path)
    cal = icalendar.Calendar.from_ical(cal_path.read_bytes())
    today = datetime.datetime.now(zoneinfo.ZoneInfo("Europe/Paris"))    # The date of today, in the Paris timezone, choose whichever you want
    

    attends_tab = []

    for event in cal.events:
        if event.get("DTSTART").dt.day == today.day and event.get("DTSTART").dt.month == today.month :        # Check every event in the calendar and execute the code if their are today
            event_desc = "\n"+"### "+event.get("SUMMARY")+" ###"

            event_desc += "\n"+event.get("LOCATION")

            event_desc += "\n"+"<t:"+str(round(event.get("DTSTART").dt.timestamp()))+":t> - <t:"+str(round(event.get("DTEND").dt.timestamp()))+":t>"    # Convert the date in vDDDType to a discord timestamp
            
            attends_tab.append((event_desc,event.get("DTSTART").dt.timestamp()))
    
    attends_tab_sorted = sorted(attends_tab, key= lambda x: x[1])   # Order every eent of today by ascending timestamp

    msg = "Voici l'emploi du temps du jour :\n"
    for event in attends_tab_sorted:        # Add all events to the message
        msg += event[0]
    
    return msg

