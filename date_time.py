import datetime as dt
import time as tm
print(tm.time())# time in second xince epoch (1/1/1971)
datenow=dt.datetime.fromtimestamp(tm.time())# convert second since epoch to date
print(datenow.year)#select year from datenow i.e month , day, hour etc.. can be used
today,ayearago=dt.date.today(),dt.timedelta(365.25)   #perform delta operation between dates
print(today-ayearago) #date excatly from a year ago unless you say a year is not 365.25 but some non-truncated fraction
