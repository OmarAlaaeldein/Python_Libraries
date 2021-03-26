import csv
from itertools import groupby as gp
with open('mpg.csv') as csvfile:
    mpg=list(csv.DictReader(csvfile))
print(mpg)
print(mpg[0].values())#print values of first dictionary#car#
sumyear=sum(float(i['year']) for i in mpg)#sum of years
cylset=set(i['cyl'] for i in mpg)  #unique cyl in mpg
p={}
for i in mpg:
    if i['cyl'] in p.keys():# count repition of cyl across mpg
        p[i['cyl']]+=1
    else:
        p[i['cyl']]=1
p=dict(gp(p,key=lambda x: x[1])) # sort desc by repitition