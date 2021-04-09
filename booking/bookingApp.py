# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 21:17:40 2021

@author: nibedita.dutta
"""

import pycronofy
#from config.config_reader import ConfigReader
import datetime
import pandas as pd
#pycronofy.Client('O8ptPYm5lemPOYsCJ-DR7vit2ivuExJA')

class BookingInformation():
    def __init__(self):
        #self.config_reader = ConfigReader()
        #self.configuration = self.config_reader.read_config()
        #self.owmapikey = self.configuration['Pbth449JGwbJm36Jl2lrIQ79aZsacgNP']
        #get access token programmitically
        self.cronofy = pycronofy.Client(
                client_id="1TffWHMOLL-VUpgVdnlNduX7hRqjFEme",
                client_secret="ajR8fefpRPsbQ_8F8r93OtpPtIrubfS-4jmagezFeP4PNUAczztB0wDMhzw5kPBK0SxC69fMnxevyeb4Bn_iWQ",
                refresh_token="V6Lb-_Lksd__7bW8mSW1E7JyDQA4NEN1")
        p = self.cronofy.refresh_authorization()
        self.cronofy = pycronofy.Client(
                client_id="1TffWHMOLL-VUpgVdnlNduX7hRqjFEme",
                client_secret="ajR8fefpRPsbQ_8F8r93OtpPtIrubfS-4jmagezFeP4PNUAczztB0wDMhzw5kPBK0SxC69fMnxevyeb4Bn_iWQ",
                access_token=p['access_token'],
                refresh_token="V6Lb-_Lksd__7bW8mSW1E7JyDQA4NEN1")
        
        
       
       

    def get_status_info(self,name,int1,int2):
        
        events = self.cronofy.read_events(tzid='Asia/Kolkata',
                             localized_times=True)
        
        m=[]
        for event in events:
            m.append(event)
        
        
        
        dd = pd.read_csv("https://raw.githubusercontent.com/nibeditad0705/File/main/Names.csv")
        name = name.capitalize()
        if name in dd['First Name'].values.tolist():
            d1 = dd[dd['First Name']==name]['Profile'].values.tolist()
            cald=[]
            for calendar in self.cronofy.list_calendars():
               cald.append([calendar['profile_id'],calendar['calendar_id']])
            cald = pd.DataFrame(cald)
            
            cald.columns =['Profile','Calend']
            pp = cald.groupby('Profile')['Calend'].apply(list)
            pp = pd.DataFrame(pp)
            pp.reset_index(inplace=True)
            
            #get calendar id list
            cal = pp[pp['Profile'].isin(d1)]['Calend'].values.tolist()
            
            #check availablity
            k1=[]
            for i in m:
                for j in cal[0]:
                  if i['calendar_id']==j:
                    if i['start']['time']>=int1 and i['end']['time']<=int2:
                        k1.append('Busy')
                    else:
                        k1.append('Free')
            if 'Busy' in k1:       
                self.bot_says =  'The calendar looks busy for now.'
            else:
                self.bot_says =  'The calendar looks free for now.'
        else:
            self.bot_says = 'User' + name + 'Not found'
         
        return self.bot_says
    
    
    def get_avail_times(self,name,date,period):
        if len(name) ==0:
            self.bot_says = 'You need to specify the person'
        elif len(name)!=0 and period =='':
            
            events = self.cronofy.read_events(tzid='Asia/Kolkata',
                             localized_times=True)
        
            m=[]
            for event in events:
                m.append(event)
            
            
            dd = pd.read_csv("https://raw.githubusercontent.com/nibeditad0705/File/main/Names.csv")
            nam = [i.capitalize() for i in name]
            #name = nam[0]
            cal_tot=[]
            for name in nam:
              if name in dd['First Name'].values.tolist():
                d1 = dd[dd['First Name']==name]['Profile'].values.tolist()
                cald=[]
                for calendar in self.cronofy.list_calendars():
                   cald.append([calendar['profile_id'],calendar['calendar_id']])
                cald = pd.DataFrame(cald)
                
                cald.columns =['Profile','Calend']
                pp = cald.groupby('Profile')['Calend'].apply(list)
                pp = pd.DataFrame(pp)
                pp.reset_index(inplace=True)
                
                #get calendar id list
                cal = pp[pp['Profile'].isin(d1)]['Calend'].values.tolist()
                cal_tot.append(cal[0])
               
                
                def avltimes(cal,date):
                    import pycronofy
    
                    cronofy = pycronofy.Client(
                                    client_id="1TffWHMOLL-VUpgVdnlNduX7hRqjFEme",
                                    client_secret="ajR8fefpRPsbQ_8F8r93OtpPtIrubfS-4jmagezFeP4PNUAczztB0wDMhzw5kPBK0SxC69fMnxevyeb4Bn_iWQ",
                    
                                    refresh_token="V6Lb-_Lksd__7bW8mSW1E7JyDQA4NEN1")
                    
                    p = cronofy.refresh_authorization()
                    
                    p['access_token']
                    
                    cronofy = pycronofy.Client(
                                    client_id="1TffWHMOLL-VUpgVdnlNduX7hRqjFEme",
                                    client_secret="ajR8fefpRPsbQ_8F8r93OtpPtIrubfS-4jmagezFeP4PNUAczztB0wDMhzw5kPBK0SxC69fMnxevyeb4Bn_iWQ",
                                    access_token=p['access_token'],
                                    refresh_token="V6Lb-_Lksd__7bW8mSW1E7JyDQA4NEN1")
                    
                    #cronofy = pycronofy.Client(access_token="C6MLJMmvmESrkSgWKVZCKadWzGX2AJja")
                    events = cronofy.read_events(tzid='Asia/Kolkata',
                                                 localized_times=True)
                    m=[]
                    for event in events:
                         m.append(event)
                    
                    k1=[]
                    for i in m:
                        for j in cal:
                          if i['calendar_id']==j:
                            k1.append([i['start']['time'],i['end']['time']])  
                    
                    import dateutil.parser
                    from datetime import datetime, timedelta
                    
                    dt=[]
                    date1 = date.replace(hour=9, minute=0)
                    date2 = date.replace(hour=18, minute=0)
                    for it in k1:
                        dt1 = dateutil.parser.parse(it[0],ignoretz=True)
                        dt2 =  dateutil.parser.parse(it[1],ignoretz=True)
                        if dt1>=date1 and dt1<=date2:
                            dt.append((dt1,dt2))
                    hours = (date1, date2)
                    def get_slots(hours, k1, duration=timedelta(hours=0.5)):
                        slots = sorted([(hours[0], hours[0])] + k1 + [(hours[1], hours[1])])
                        m=[]
                        for start, end in ((slots[i][1], slots[i+1][0]) for i in range(len(slots)-1)):
                            #assert start <= end, "Cannot attend all appointments"
                            while start + duration <= end:
                                st1 = str(start).split()[1]
                                en = start + duration
                                en1 = str(en).split()[1]
                                k1 = st1 + '-' +en1
                                m.append(k1)
                    
                                start += duration
                        return m
    
                    h = get_slots(hours, dt)
                    return h
                
                need=[]
                for it in cal_tot:
                    need.append(avltimes(it,date))
                result = set(need[0])
            
                for s in need[1:]:
                        result.intersection_update(s)
                result=list(result)
                self.bot_says = 'You can book between ' + str(result[0]) 
        
              else:
                 self.bot_says= 'User not found'
                
           
      
        return self.bot_says
    
   
    def get_meeting(self,name,date,sttime):
        #cronofy = pycronofy.Client(access_token="C6MLJMmvmESrkSgWKVZCKadWzGX2AJja")
        events = self.cronofy.read_events(tzid='Asia/Kolkata',
                                     localized_times=True)
        m=[]
        for event in events:
             m.append(event)
        dd = pd.read_csv("https://raw.githubusercontent.com/nibeditad0705/File/main/Names.csv")
        name = [i.capitalize() for i in name]
        uss =[]
        k=[]
        for itt in name:
                    if itt in dd['First Name'].values.tolist():
                        k.append(itt)
                    else:
                        pass
        
        d1=[]
        for en in name:
            p=dd[dd['First Name']==en]['Mail'].values.tolist()
            d1.append(p[0])
        
        app=[]
        k=[]
       
        dat = sttime[0]                
        for it in m:
            for j in d1:
                    if len(it['attendees'])>0:
                         if j in it['attendees'][0]['email'] and it['start']['time']==dat:
                                  app.append([j,it['attendees'][0]['status']])
                                 
                          
      
        
        if len(app)!=0:
            for itt in app:
                    if 'needs_action' in itt[1]:
                        nam = dd[dd['Mail']==itt[0]]['First Name'].values.tolist()        
                        self.bot_says = 'Meeting has not been accepted by ' + str(nam[0]) 
                        break
                    else:
                        self.bot_says = 'Meeting has been accepted by everyone'
        else:
            self.bot_says = 'Meeting not found '+ str(k)
      
        return self.bot_says
        
        
        
    def get_inclusion(self,name,date,sttime,entime):
        #cronofy = pycronofy.Client(access_token="C6MLJMmvmESrkSgWKVZCKadWzGX2AJja")
        events = self.cronofy.read_events(tzid='Asia/Kolkata',
                                     localized_times=True)
        m=[]
        for event in events:
             m.append(event)
        dd = pd.read_csv("https://raw.githubusercontent.com/nibeditad0705/File/main/Names.csv")
        name = [i.capitalize() for i in name]
        name1 = name.copy()
        nm=[]
        for nam in name1:
                      d1 = dd[dd['First Name']==nam]['Mail'].values.tolist()
                      nm.append(d1[0])
        uss =[]
        k=[]
        
        import dateutil.parser
        dat = date.strftime('%Y-%m-%d')
        yourt1 = dateutil.parser.parse(sttime)
        tim1 = yourt1.strftime('T%H:%M:%S')
        start = dat+tim1+'+05:30'
        
        import dateutil.parser
        yourt2 = dateutil.parser.parse(entime)
        tim2 = yourt2.strftime('T%H:%M:%S')
        end = dat+tim2+'+05:30'
        for itt in name:
                    if itt in dd['First Name'].values.tolist():
                        k.append(itt)
                    else:
                        pass
        if len(k)==len(name):
       
                d1 = dd[dd['First Name']==name[0]]['Profile'].values.tolist()
                
                cald=[]
                for calendar in self.cronofy.list_calendars():
                   cald.append([calendar['profile_id'],calendar['calendar_id']])
                cald = pd.DataFrame(cald)
                
                cald.columns =['Profile','Calend']
                pp = cald.groupby('Profile')['Calend'].apply(list)
                pp = pd.DataFrame(pp)
                pp.reset_index(inplace=True)
                
                #get calendar id list
                cal = pp[pp['Profile'].isin(d1)]['Calend'].values.tolist()
                
                
                
                
                #ceck previous attendants
                app=[]
                for i in m:
                    for j in cal[0]:
                      if i['calendar_id']==j:
                        if i['start']['time']==start and i['end']['time']==end:
                              app.append(i['attendees'][0]['email'])
                    
                
                from email.mime.multipart import MIMEMultipart
                import smtplib

                from email.mime.base import MIMEBase
                from email.mime.text import MIMEText
                from email.utils import COMMASPACE, formatdate
                from email import encoders
                import os,datetime
                COMMASPACE = ', '

                import pytz
                import datetime as dt
                from datetime import timedelta
                import icalendar

                #cancel original meeting
                def send_appointment(date, attendee_email, organiser_email, subj, description, location, start_hour, start_minute,end_hour,end_minute):
                                  # Timezone to use for our dates - change as needed
                                  tz = pytz.timezone("Asia/Kolkata")
                                  start = tz.localize(dt.datetime.combine(date, dt.time(start_hour, start_minute, 0)))
                                  end = tz.localize(dt.datetime.combine(date, dt.time(end_hour, end_minute, 0)))
                                  # Build the event itself
                                  cal = icalendar.Calendar()
                                  cal.add('prodid', '-//My calendar application//example.com//')
                                  cal.add('version', '2.0')
                                  cal.add('method', "CANCEL")
                                  #cal.add('location',location)
                                  event = icalendar.Event()
                                  event.add('attendee', attendee_email)
                                  event.add('organizer', organiser_email)
                                  event.add('status', "cancelled")
                                  event.add('category', "Event")
                                  event.add('summary', subj)
                                  event.add('description', description)
                                  event.add('location', location)
                                  #event.location = location
                                  event.add('dtstart', start)
                                  event.add('dtend', end)
                                  #event.add('dtstamp', tz.localize(dt.datetime.combine(date, dt.time(6, 0, 0))))
                                  event['uid'] = '1234' # Generate some unique ID
                                  event.add('priority', 5)
                                  event.add('sequence', 1)
                                  event.add('created', tz.localize(dt.datetime.now()))

                                  # Add a reminder
                                  alarm = icalendar.Alarm()
                                  alarm.add("action", "DISPLAY")
                                  alarm.add('description', "Reminder")
                                  # The only way to convince Outlook to do it correctly
                                  alarm.add("TRIGGER;RELATED=START", "-PT{0}H".format(2))
                                  event.add_component(alarm)
                                  cal.add_component(event)

                                  # Build the email message and attach the event to it
                                  msg = MIMEMultipart("alternative")

                                  msg["Subject"] = subj
                                  msg["From"] = organiser_email
                                  msg["To"] = ','.join(attendee_email)
                                  msg["Content-class"] = "urn:content-classes:calendarmessage"

                                  msg.attach(MIMEText(description))

                                  filename = "invite.ics"
                                  part = MIMEBase('text', "calendar", method="CANCEL", name=filename)
                                  part.set_payload( cal.to_ical() )
                                  encoders.encode_base64(part)
                                  part.add_header('Content-Description', filename)
                                  part.add_header("Content-class", "urn:content-classes:calendarmessage")
                                  part.add_header("Filename", filename)
                                  part.add_header("Path", filename)
                                  msg.attach(part)

                                  # Send the email out
                                  mailServer = smtplib.SMTP('smtp.gmail.com', 587)
                                  mailServer.ehlo()
                                  mailServer.starttls()
                                  mailServer.ehlo()
                                  mailServer.login('worldwideconnecttpg@gmail.com', 'Whatwomenwant5901!')
                                  mailServer.ehlo()
                                  mailServer.sendmail(organiser_email, attendee_email, msg.as_string())
                                  mailServer.close()

              
                #mail = dd[dd['First Name']==it]['Mail'].values.tolist()
                #starthour and startminute
                
                sth = int(sttime.split(':')[0])
                stm = int(sttime.split(':')[1])
                eth = int(entime.split(':')[0])
                etm = int(entime.split(':')[1])
                
                for it in app:
                   send_appointment(date, it , 'worldwideconnecttpg@gmail.com', 'Invitation', 'Invitation','', sth, stm,eth,etm)
                
                #set another meeting with all users
                def send_appointment1(date, attendee_email, organiser_email, subj, description, location, start_hour, start_minute,end_hour,end_minute):
                      # Timezone to use for our dates - change as needed
                      tz = pytz.timezone("Asia/Kolkata")
                      start = tz.localize(dt.datetime.combine(date, dt.time(start_hour, start_minute, 0)))
                      end = tz.localize(dt.datetime.combine(date, dt.time(end_hour, end_minute, 0)))
                      # Build the event itself
                      cal = icalendar.Calendar()
                      cal.add('prodid', '-//My calendar application//example.com//')
                      cal.add('version', '2.0')
                      cal.add('method', "REQUEST")
                      #cal.add('location',location)
                      event = icalendar.Event()
                      event.add('attendee', attendee_email)
                      event.add('organizer', organiser_email)
                      event.add('status', "confirmed")
                      event.add('category', "Event")
                      event.add('summary', subj)
                      event.add('description', description)
                      event.add('location', location)
                      #event.location = location
                      event.add('dtstart', start)
                      event.add('dtend', end)
                      #event.add('dtstamp', tz.localize(dt.datetime.combine(date, dt.time(6, 0, 0))))
                      event['uid'] = '1234' # Generate some unique ID
                      event.add('priority', 5)
                      event.add('sequence', 1)
                      event.add('created', tz.localize(dt.datetime.now()))
                    
                      # Add a reminder
                      alarm = icalendar.Alarm()
                      alarm.add("action", "DISPLAY")
                      alarm.add('description', "Reminder")
                      # The only way to convince Outlook to do it correctly
                      alarm.add("TRIGGER;RELATED=START", "-PT{0}H".format(2))
                      event.add_component(alarm)
                      cal.add_component(event)
                    
                      # Build the email message and attach the event to it
                      msg = MIMEMultipart("alternative")
                    
                      msg["Subject"] = subj
                      msg["From"] = organiser_email
                      msg["To"] = ",".join(attendee_email)
                      msg["Content-class"] = "urn:content-classes:calendarmessage"
                    
                      msg.attach(MIMEText(description))
                    
                      filename = "invite.ics"
                      part = MIMEBase('text', "calendar", method="REQUEST", name=filename)
                      part.set_payload( cal.to_ical() )
                      encoders.encode_base64(part)
                      part.add_header('Content-Description', filename)
                      part.add_header("Content-class", "urn:content-classes:calendarmessage")
                      part.add_header("Filename", filename)
                      part.add_header("Path", filename)
                      msg.attach(part)
                    
                      # Send the email out
                      mailServer = smtplib.SMTP('smtp.gmail.com', 587)
                      mailServer.ehlo()
                      mailServer.starttls()
                      mailServer.ehlo()
                      mailServer.login'worldwideconnecttpg@gmail.com', 'Whatwomenwant5901!')
                      mailServer.ehlo()
                      mailServer.sendmail(organiser_email, attendee_email, msg.as_string())
                      mailServer.close()
                    
                
                

                #starthour and startminute
                sth = int(sttime.split(':')[0])
                stm = int(sttime.split(':')[1])
                eth = int(entime.split(':')[0])
                etm = int(entime.split(':')[1])
                
                
                participant = nm.append(app)
                
                for it in nm:

                #participant=list(set(participant))
              
                   send_appointment1(date, it , 'worldwideconnecttpg@gmail.com', 'Invitation', 'Invitation', '', sth, stm,eth,etm)
                self.bot_says = 'Meeting has been now scheduled with all the members you needed!'
        else:
                self.bot_says ='User not found in directory'
        return self.bot_says
                
    def reschedule_meet(self,name,date,sttime,entime):
        origdate = date[0]
        chandate = date[1]
        origsttime = sttime[0]
        chansttime = sttime[1]
        origentime = entime[0]
        chanentime = entime[1]
        dd = pd.read_csv("https://raw.githubusercontent.com/nibeditad0705/File/main/Names.csv")
        name = [i.capitalize() for i in name]
        uss =[]
        for it in name:
            if it in dd['First Name'].values.tolist():
                d1 = dd[dd['First Name']==it]['Profile'].values.tolist()
        
                from email.mime.multipart import MIMEMultipart
                import smtplib
                
                from email.mime.base import MIMEBase
                from email.mime.text import MIMEText
                from email.utils import COMMASPACE, formatdate
                from email import encoders
                import os,datetime
                COMMASPACE = ', '
                
                import pytz
                import datetime as dt
                from datetime import timedelta
                import icalendar
                
                #cancel original meeting
                def send_appointment(date, attendee_email, organiser_email, subj, description, location, start_hour, start_minute,end_hour,end_minute):
                                  # Timezone to use for our dates - change as needed
                                  tz = pytz.timezone("Asia/Kolkata")
                                  start = tz.localize(dt.datetime.combine(date, dt.time(start_hour, start_minute, 0)))
                                  end = tz.localize(dt.datetime.combine(date, dt.time(end_hour, end_minute, 0)))
                                  # Build the event itself
                                  cal = icalendar.Calendar()
                                  cal.add('prodid', '-//My calendar application//example.com//')
                                  cal.add('version', '2.0')
                                  cal.add('method', "CANCEL")
                                  #cal.add('location',location)
                                  event = icalendar.Event()
                                  event.add('attendee', attendee_email)
                                  event.add('organizer', organiser_email)
                                  event.add('status', "cancelled")
                                  event.add('category', "Event")
                                  event.add('summary', subj)
                                  event.add('description', description)
                                  event.add('location', location)
                                  #event.location = location
                                  event.add('dtstart', start)
                                  event.add('dtend', end)
                                  #event.add('dtstamp', tz.localize(dt.datetime.combine(date, dt.time(6, 0, 0))))
                                  event['uid'] = '1234' # Generate some unique ID
                                  event.add('priority', 5)
                                  event.add('sequence', 1)
                                  event.add('created', tz.localize(dt.datetime.now()))
                
                                  # Add a reminder
                                  alarm = icalendar.Alarm()
                                  alarm.add("action", "DISPLAY")
                                  alarm.add('description', "Reminder")
                                  # The only way to convince Outlook to do it correctly
                                  alarm.add("TRIGGER;RELATED=START", "-PT{0}H".format(2))
                                  event.add_component(alarm)
                                  cal.add_component(event)
                
                                  # Build the email message and attach the event to it
                                  msg = MIMEMultipart("alternative")
                
                                  msg["Subject"] = subj
                                  msg["From"] = organiser_email
                                  msg["To"] = attendee_email
                                  msg["Content-class"] = "urn:content-classes:calendarmessage"
                
                                  msg.attach(MIMEText(description))
                
                                  filename = "invite.ics"
                                  part = MIMEBase('text', "calendar", method="CANCEL", name=filename)
                                  part.set_payload( cal.to_ical() )
                                  encoders.encode_base64(part)
                                  part.add_header('Content-Description', filename)
                                  part.add_header("Content-class", "urn:content-classes:calendarmessage")
                                  part.add_header("Filename", filename)
                                  part.add_header("Path", filename)
                                  msg.attach(part)
                
                                  # Send the email out
                                  mailServer = smtplib.SMTP('smtp.gmail.com', 587)
                                  mailServer.ehlo()
                                  mailServer.starttls()
                                  mailServer.ehlo()
                                  mailServer.login('worldwideconnecttpg@gmail.com', 'Whatwomenwant5901!')
                                  mailServer.sendmail(organiser_email, attendee_email, msg.as_string())
                                  mailServer.close()
                mail = dd[dd['First Name']==it]['Mail'].values.tolist()
                #starthour and startminute
                sth = int(origsttime.split(':')[0])
                stm = int(origsttime.split(':')[1])
                eth = int(origentime.split(':')[0])
                etm = int(origentime.split(':')[1])
                
                send_appointment(origdate, mail[0] , 'worldwideconnecttpg@gmail.com', 'Invitation', 'Invitation', '', sth, stm,eth,etm)
                
                def send_appointment1(date, attendee_email, organiser_email, subj, description, location, start_hour, start_minute,end_hour,end_minute):
                      # Timezone to use for our dates - change as needed
                      tz = pytz.timezone("Asia/Kolkata")
                      start = tz.localize(dt.datetime.combine(date, dt.time(start_hour, start_minute, 0)))
                      end = tz.localize(dt.datetime.combine(date, dt.time(end_hour, end_minute, 0)))
                      # Build the event itself
                      cal = icalendar.Calendar()
                      cal.add('prodid', '-//My calendar application//example.com//')
                      cal.add('version', '2.0')
                      cal.add('method', "REQUEST")
                      #cal.add('location',location)
                      event = icalendar.Event()
                      event.add('attendee', attendee_email)
                      event.add('organizer', organiser_email)
                      event.add('status', "confirmed")
                      event.add('category', "Event")
                      event.add('summary', subj)
                      event.add('description', description)
                      event.add('location', location)
                      #event.location = location
                      event.add('dtstart', start)
                      event.add('dtend', end)
                      #event.add('dtstamp', tz.localize(dt.datetime.combine(date, dt.time(6, 0, 0))))
                      event['uid'] = '1234' # Generate some unique ID
                      event.add('priority', 5)
                      event.add('sequence', 1)
                      event.add('created', tz.localize(dt.datetime.now()))
                    
                      # Add a reminder
                      alarm = icalendar.Alarm()
                      alarm.add("action", "DISPLAY")
                      alarm.add('description', "Reminder")
                      # The only way to convince Outlook to do it correctly
                      alarm.add("TRIGGER;RELATED=START", "-PT{0}H".format(2))
                      event.add_component(alarm)
                      cal.add_component(event)
                    
                      # Build the email message and attach the event to it
                      msg = MIMEMultipart("alternative")
                    
                      msg["Subject"] = subj
                      msg["From"] = organiser_email
                      msg["To"] = attendee_email
                      msg["Content-class"] = "urn:content-classes:calendarmessage"
                    
                      msg.attach(MIMEText(description))
                    
                      filename = "invite.ics"
                      part = MIMEBase('text', "calendar", method="REQUEST", name=filename)
                      part.set_payload( cal.to_ical() )
                      encoders.encode_base64(part)
                      part.add_header('Content-Description', filename)
                      part.add_header("Content-class", "urn:content-classes:calendarmessage")
                      part.add_header("Filename", filename)
                      part.add_header("Path", filename)
                      msg.attach(part)
                    
                      # Send the email out
                      mailServer = smtplib.SMTP('smtp.gmail.com', 587)
                      mailServer.ehlo()
                      mailServer.starttls()
                      mailServer.ehlo()
                      mailServer.login('worldwideconnecttpg@gmail.com', 'Whatwomenwant5901!')
                      mailServer.sendmail(organiser_email, attendee_email, msg.as_string())
                      mailServer.close()
                    
                
                
               
                sth = int(chansttime.split(':')[0])
                stm = int(chansttime.split(':')[1])
                eth = int(chanentime.split(':')[0])
                etm = int(chanentime.split(':')[1])
                
                send_appointment1(chandate, mail[0] , 'worldwideconnecttpg@gmail.com', 'Invitation', 'Invitation', '', sth, stm,eth,etm)
                
                self.bot_says = 'Your meeting has been reschudeled'
                
            else:
                self.bot_says = 'User ' + str(it)+' could not be found'
                break
                
        return self.bot_says
                
        
    def get_booking_info(self,name,date,int1,int2,loc,topic):
        
        events = self.cronofy.read_events(tzid='Asia/Kolkata',
                             localized_times=True)
        
        m=[]
        for event in events:
            m.append(event)
        
        
        
        dd = pd.read_csv("https://raw.githubusercontent.com/nibeditad0705/File/main/Names.csv")
        name = [i.capitalize() for i in name]
        uss =[]
        for it in name:
            if it in dd['First Name'].values.tolist():
                d1 = dd[dd['First Name']==it]['Profile'].values.tolist()
                cald=[]
                for calendar in self.cronofy.list_calendars():
                   cald.append([calendar['profile_id'],calendar['calendar_id']])
                cald = pd.DataFrame(cald)
                
                cald.columns =['Profile','Calend']
                pp = cald.groupby('Profile')['Calend'].apply(list)
                pp = pd.DataFrame(pp)
                pp.reset_index(inplace=True)
                
                #get calendar id list
                cal = pp[pp['Profile'].isin(d1)]['Calend'].values.tolist()
                
                import dateutil.parser
                dat = date.strftime('%Y-%m-%d')
                yourt1 = dateutil.parser.parse(int1)
                tim1 = yourt1.strftime('T%H:%M:%S')
                start = dat+tim1+'+05:30'
                
                import dateutil.parser
                yourt2 = dateutil.parser.parse(int2)
                tim2 = yourt2.strftime('T%H:%M:%S')
                end = dat+tim2+'+05:30'

                
                
                #check availablity
                k1=[]
                for i in m:
                    for j in cal[0]:
                      if i['calendar_id']==j:
                        if i['start']['time']>=start and i['end']['time']<=end:
                            k1.append('Busy')
                        else:
                            k1.append('Free')
                if 'Busy' in k1:       
                    self.bot_says =  it + ' is busy during this time'
                    break
                    
                elif 'Busy' not in k1:
                    from email.mime.multipart import MIMEMultipart
                    import smtplib

                    from email.mime.base import MIMEBase
                    from email.mime.text import MIMEText
                    from email.utils import COMMASPACE, formatdate
                    from email import encoders
                    import os,datetime
                    COMMASPACE = ', '
                    
                    import pytz
                    import datetime as dt
                    from datetime import timedelta
                  


                  
                    #location = loc
                    if topic!='':
                        subj='Discussion on ' +topic
                        desc='Discussion on ' +topic
                    else:
                        subj = 'Invitation'
                        desc='Invitation'
                    import icalendar
                    # Imagine this function is part of a class which provides the necessary config data
                    def send_appointment(date, attendee_email, organiser_email, subj, description, location, start_hour, start_minute,end_hour,end_minute):
                      # Timezone to use for our dates - change as needed
                      tz = pytz.timezone("Asia/Kolkata")
                      start = tz.localize(dt.datetime.combine(date, dt.time(start_hour, start_minute, 0)))
                      end = tz.localize(dt.datetime.combine(date, dt.time(end_hour, end_minute, 0)))
                      # Build the event itself
                      cal = icalendar.Calendar()
                      cal.add('prodid', '-//My calendar application//example.com//')
                      cal.add('version', '2.0')
                      cal.add('method', "REQUEST")
                      #cal.add('location',location)
                      event = icalendar.Event()
                      event.add('attendee', attendee_email)
                      event.add('organizer', organiser_email)
                      event.add('status', "confirmed")
                      event.add('category', "Event")
                      event.add('summary', subj)
                      event.add('description', description)
                      event.add('location', location)
                      #event.location = location
                      event.add('dtstart', start)
                      event.add('dtend', end)
                      #event.add('dtstamp', tz.localize(dt.datetime.combine(date, dt.time(6, 0, 0))))
                      event['uid'] = '1234' # Generate some unique ID
                      event.add('priority', 5)
                      event.add('sequence', 1)
                      event.add('created', tz.localize(dt.datetime.now()))
                    
                      # Add a reminder
                      alarm = icalendar.Alarm()
                      alarm.add("action", "DISPLAY")
                      alarm.add('description', "Reminder")
                      # The only way to convince Outlook to do it correctly
                      alarm.add("TRIGGER;RELATED=START", "-PT{0}H".format(2))
                      event.add_component(alarm)
                      cal.add_component(event)
                    
                      # Build the email message and attach the event to it
                      msg = MIMEMultipart("alternative")
                    
                      msg["Subject"] = subj
                      msg["From"] = organiser_email
                      msg["To"] = attendee_email
                      msg["Content-class"] = "urn:content-classes:calendarmessage"
                    
                      msg.attach(MIMEText(description))
                    
                      filename = "invite.ics"
                      part = MIMEBase('text', "calendar", method="REQUEST", name=filename)
                      part.set_payload( cal.to_ical() )
                      encoders.encode_base64(part)
                      part.add_header('Content-Description', filename)
                      part.add_header("Content-class", "urn:content-classes:calendarmessage")
                      part.add_header("Filename", filename)
                      part.add_header("Path", filename)
                      msg.attach(part)
                    
                      # Send the email out
                      mailServer = smtplib.SMTP('smtp.gmail.com', 587)
                      mailServer.ehlo()
                      mailServer.starttls()
                      mailServer.ehlo()
                      mailServer.login('worldwideconnecttpg@gmail.com', 'Whatwomenwant5901!')
                      mailServer.sendmail(organiser_email, attendee_email, msg.as_string())
                      mailServer.close()
                    
                    
                    
                    
                    mail = dd[dd['First Name']==it]['Mail'].values.tolist()
                    #starthour and startminute
                    sth = int(int1.split(':')[0])
                    stm = int(int1.split(':')[1])
                    eth = int(int2.split(':')[0])
                    etm = int(int2.split(':')[1])
                    
                    send_appointment(date, mail[0] , 'worldwideconnecttpg@gmail.com', subj, desc, loc, sth, stm,eth,etm)
                    
                    uss.append(it)
                    
            else:
                self.bot_says = 'User ' + it + ' Not found'
                break
            
        if len(uss)!=0:
                ust = ','.join(uss)
                self.bot_says = 'Meeting invitation has been successfully sent to ' + ust
         
        return self.bot_says
