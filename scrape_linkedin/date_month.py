
import re

from datetime import datetime,date

#global mon

today = date.today()

def month2int(month1):
        if month1=="Jan":
            mon=1 
        elif month1=="Feb":
            mon=2 
        elif month1=="Mar":
            mon=3 
        elif month1=="Apr":
            mon=4             
        elif month1=="May":
            mon=5 
        elif month1=="Jun":
            mon=6         
        elif month1=="Jul":
            mon=7 
        elif month1=="Aug":
            mon=8 
        elif month1=="Sep":
            mon=9 
        elif month1=="Oct":
            mon=10
        elif month1=="Nov":
            mon=11 
        elif month1=="Dec":
            mon=12

        else:
            mon=today.month     

        return mon

def diff_month(d1, d2):
        return (d1.year - d2.year) * 12 + d1.month - d2.month

def duration(date_str):
        month_spl=re.split('\d\S*',date_str)

        year0=re.split('\D',date_str)    

        '''print(spl[0].strip(" "))
        print(spl[1].strip(" -")) 
        print(spl1[4])
        print(spl1[11])'''

        month_int=month2int(month_spl[0].strip(" "))
        month_int1=month2int(month_spl[1].strip(" -"))

        #print(str(month_int)+'-'+spl1[4])
        #print(str(month_int1)+'-'+spl1[11])

        
        if year0[11].isdigit():
            year1=year0[11]
            #print(year1)

        else: 
            year1=today.year
            #print(year1)    

        date_time1=datetime(year=int(year0[4]),month=int(month_int),day=1)

        date_time2=datetime(year=int(year1),month=month_int1,day=1)

        #print(date_time1)
        #print(date_time2)

        #duration_diff=date_time2-date_time1
        duration_diff=diff_month(date_time2,date_time1)

        return duration_diff

#duration('Feb 2011 - Feb 2014')    