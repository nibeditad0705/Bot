# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:01:29 2021

@author: nibedita.dutta
"""

from botbuilder.core import TurnContext,ActivityHandler
from botbuilder.ai.luis import LuisApplication,LuisPredictionOptions,LuisRecognizer
import json
from booking.bookingApp import BookingInformation
#from config.config_reader import ConfigReader
#from logger.logger import Log
class LuisConnect(ActivityHandler):
    def __init__(self):
       
        luis_app = LuisApplication('7c983e96-7992-4da8-ba51-be851e072149','a590ebf41db04b40ad36f0b18a40c201','https://lui1.cognitiveservices.azure.com/')
        luis_option = LuisPredictionOptions(include_all_intents=True,include_instance_data=True)
        self.LuisReg = LuisRecognizer(luis_app,luis_option,True)
 
 

    async def on_message_activity(self,turn_context:TurnContext):
        luis_result = await self.LuisReg.recognize(turn_context)
        intent = self.LuisReg.top_intent(luis_result)
        
        #retult = luis_result.properties["luisResult"]
        #item =''
        #if len(retult.entities)!=0:

        #await turn_context.send_activity(f" Luis Result {retult.entities[0]}")
        if intent== 'Check_Availability':
            if luis_result.entities:
                k = luis_result.entities
            m={}
            for it in k.keys():
              if it!='$instance':
                    m[it]=k[it][0]
            import dateutil.parser
            
            l =['user','date','startTime','endTime']
            
            import dateutil.parser
            from datetime import datetime
            dat=['today','tommorow']
            if m['date'] not in dat:
               date = dateutil.parser.parse(m['date'])
            elif m['date']=='today':
                
                date=datetime.today()
            elif m['date']=='tommorow':
                date = datetime.date.today() + datetime.timedelta(days=1)
            
            def chang(times): 
                if 'pm' in  times:
                    k1 = times.replace('pm','').replace(' ','')
                    kk =k1+' pm'
                    return kk
                
                elif 'am' in times:
                  k1 = times.replace('am','').replace(' ','')
                  kk =k1+' am'
                  return kk
                else:
                    return times
              
            
            import dateutil.parser
            import re
            
            def parse(timestr):
                timestr = re.sub(r"(\d{1,2})\.(\d{2})(\D*)$", r"\1:\2\3", timestr)
                return dateutil.parser.parse(timestr)
            
            def modify(time):
                    int1 = parse(chang(time)) 
                    #m['endTime'] = parse(chang(m['endTime']))   
                    #in_time = datetime.strptime(m['startTime'], "%I %p")
                    st1 = datetime.strftime(int1, "%H:%M")
                                                          
                    import dateutil.parser
                    dat = date.strftime('%Y-%m-%d')
                    yourt1 = dateutil.parser.parse(st1)
                    tim1 = yourt1.strftime('T%H:%M:%S')
                    start = dat+tim1+'+05:30'
                    return start
            
                                     
            st1 = modify(m['startTime'])
            st2 = modify(m['endTime']) 
         
            weather_info=BookingInformation()
            weather=weather_info.get_status_info(m['user'],st1,st2)
            await turn_context.send_activity(f"{weather}")
        
        elif intent == 'Suggest_Time':
            k = luis_result.entities
            user=[]
            m={}
            ent =['date','period','user']
            for it in ent:
                if it in k.keys():
                      if it!='$instance':
                            m[it]=k[it][0]
                else:
                    m[it]=''
            
            for it in k.keys():
              if it=='user':
                    user.append(k[it][0])
            
            import datetime
            import dateutil.parser
            dat=['today','tommorow','']
            if m['date'] not in dat:
               date = dateutil.parser.parse(m['date'])
            elif m['date']=='today':
                
                date=datetime.date.today()
            elif m['date']=='tommorow':
                date = datetime.date.today() + datetime.timedelta(days=1)
            elif m['date']=='':  
                date = datetime.date.today()
            
            weather_info=BookingInformation()
            weather=weather_info.get_avail_times(user,date, m['period'])
            await turn_context.send_activity(f"{weather}")
            
        elif intent == 'Resch': 
            from datetime import datetime
            import dateutil.parser
            import re
            k = luis_result.entities
            user=[]
            m={}
            ent =['date','endTime','startTime','user']
            for it in k['user']:
              
                    user.append(it)
             
            datel=[]
            for it in k['date']:
            
                   
                    dat = dateutil.parser.parse(it)
                    datel.append(dat)
                    
            sttime =[]
            for it in k['startTime']:
            
                    sttime.append(it)
            
            entime =[]
            for it in k['endTime']:
             
                    entime.append(it)
            
            def chang(times): 
                if 'pm' in  times:
                    k1 = times.replace('pm','').replace(' ','')
                    kk =k1+' pm'
                    return kk
                
                elif 'am' in times:
                  k1 = times.replace('am','').replace(' ','')
                  kk =k1+' am'
                  return kk
                else:
                    return times
              
            
            import dateutil.parser
            import re
            
            def parse(timestr):
                timestr = re.sub(r"(\d{1,2})\.(\d{2})(\D*)$", r"\1:\2\3", timestr)
                return dateutil.parser.parse(timestr)
            
            chsttime=[]
            for it in sttime:              
                   itt = parse(chang(it)) 
                   st1 = datetime.strftime(itt, "%H:%M")
                   chsttime.append(st1)
                   
            chentime=[]
            for it in entime:              
                   itt = parse(chang(it)) 
                   st1 = datetime.strftime(itt, "%H:%M")
                   chentime.append(st1)
           
            weather_info=BookingInformation()
            weather=weather_info.reschedule_meet(user,datel, chsttime, chentime)

            
            
            await turn_context.send_activity(f"{weather}")
        
        elif intent == 'Meeting_Status':    
            from datetime import datetime
            import dateutil.parser
            import re
            k = luis_result.entities
            user=[]
            m={}
            ent =['date','startTime','user']
            for it in k['user']:
                user.append(it)
            
            datel=[]
            for it in k['date']:
                dat = dateutil.parser.parse(it)
                datel.append(dat) 
            
            sttime =[]
            for it in k['startTime']:
            
                    sttime.append(it)
                    
            def chang(times): 
                if 'pm' in  times:
                    k1 = times.replace('pm','').replace(' ','')
                    kk =k1+' pm'
                    return kk
                
                elif 'am' in times:
                  k1 = times.replace('am','').replace(' ','')
                  kk =k1+' am'
                  return kk
                else:
                    return times
              
            
            import dateutil.parser
            import re
            
            def parse(timestr):
                timestr = re.sub(r"(\d{1,2})\.(\d{2})(\D*)$", r"\1:\2\3", timestr)
                return dateutil.parser.parse(timestr)
            
            def modify(time):
                    int1 = parse(chang(time)) 
                    #m['endTime'] = parse(chang(m['endTime']))   
                    #in_time = datetime.strptime(m['startTime'], "%I %p")
                    st1 = datetime.strftime(int1, "%H:%M")
                                                          
                    import dateutil.parser
                    dat = datel[0].strftime('%Y-%m-%d')
                    yourt1 = dateutil.parser.parse(st1)
                    tim1 = yourt1.strftime('T%H:%M:%S')
                    start = dat+tim1+'+05:30'
                    return start
            
                        
            chsttime=[]
            for it in sttime:              
                   itt = modify(it)
                   chsttime.append(itt)
                   
            weather_info=BookingInformation()
            weather=weather_info.get_meeting(user,datel, chsttime)
            await turn_context.send_activity(f"{weather}")
                   
            
            
        elif intent == 'Inclusion':
            from datetime import datetime
            k = luis_result.entities
            user=[]
            m={}
            ent =['date','endTime','user','startTime']
            for it in ent:
                if it in k.keys():
                      if it!='$instance':
                            m[it]=k[it][0]
                else:
                    m[it]=''
            for it in k['user']:
             
                    user.append(it)
            import dateutil.parser
            dat=['today','tommorow']
            if m['date'] not in dat:
               date = dateutil.parser.parse(m['date'])
            elif m['date']=='today':
                
                date=datetime.today()
            elif m['date']=='tommorow':
                date = datetime.date.today() + datetime.timedelta(days=1)
            
            def chang(times): 
                if 'pm' in  times:
                    k1 = times.replace('pm','').replace(' ','')
                    kk =k1+' pm'
                    return kk
                
                elif 'am' in times:
                  k1 = times.replace('am','').replace(' ','')
                  kk =k1+' am'
                  return kk
                else:
                    return times
              
            
            import dateutil.parser
            import re
            
            def parse(timestr):
                timestr = re.sub(r"(\d{1,2})\.(\d{2})(\D*)$", r"\1:\2\3", timestr)
                return dateutil.parser.parse(timestr)

                         
            m['startTime'] = parse(chang(m['startTime'])) 
            m['endTime'] = parse(chang(m['endTime']))   
            #in_time = datetime.strptime(m['startTime'], "%I %p")
            st1 = datetime.strftime(m['startTime'], "%H:%M")
            
            #in_time1 = datetime.strptime(m['endTime'], "%I %p")
            st2 = datetime.strftime(m['endTime'], "%H:%M")
            
            weather_info=BookingInformation()
            weather_info=BookingInformation()
            weather=weather_info.get_inclusion(user,date, st1,st2)
            await turn_context.send_activity(f"{weather}")
            
        elif intent == 'Book_Meeting':
            from datetime import datetime
            k = luis_result.entities
            user=[]
            m={}
            ent =['date','endTime','location','startTime','Topic']
            for it in ent:
                if it in k.keys():
                      if it!='$instance':
                            m[it]=k[it][0]
                else:
                    m[it]=''
            for it in k.keys():
              if it=='user' or it=='user1':
                    user.append(k[it][0])
            import dateutil.parser
            dat=['today','tommorow']
            if m['date'] not in dat:
               date = dateutil.parser.parse(m['date'])
            elif m['date']=='today':
                
                date=datetime.today()
            elif m['date']=='tommorow':
                date = datetime.date.today() + datetime.timedelta(days=1)
            
            def chang(times): 
                if 'pm' in  times:
                    k1 = times.replace('pm','').replace(' ','')
                    kk =k1+' pm'
                    return kk
                
                elif 'am' in times:
                  k1 = times.replace('am','').replace(' ','')
                  kk =k1+' am'
                  return kk
                else:
                    return times
              
            
            import dateutil.parser
            import re
            
            def parse(timestr):
                timestr = re.sub(r"(\d{1,2})\.(\d{2})(\D*)$", r"\1:\2\3", timestr)
                return dateutil.parser.parse(timestr)

                         
            m['startTime'] = parse(chang(m['startTime'])) 
            m['endTime'] = parse(chang(m['endTime']))   
            #in_time = datetime.strptime(m['startTime'], "%I %p")
            st1 = datetime.strftime(m['startTime'], "%H:%M")
            
            #in_time1 = datetime.strptime(m['endTime'], "%I %p")
            st2 = datetime.strftime(m['endTime'], "%H:%M")
            
            weather_info=BookingInformation()
            weather=weather_info.get_booking_info(user,date, st1,st2,m['location'],m['Topic'])
            await turn_context.send_activity(f"{weather}")
            
            
            
        #self.log.write_log(sessionID='session1',log_message="Bot Says: "+str(weather))
        
