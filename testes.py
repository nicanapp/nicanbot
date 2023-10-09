from lib.twitter import TwitterLogin, TwitterMain
from lib.navigator import Navigator

from datetime import date,timedelta
import re

#data = "Aug 22"


frutas = ['banana', 'limao', 'laranja']

print(frutas[-1])


data = "1 de out de 2021"

r = re.search("((\d+)([\s\w]+)?(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|jan|fev|mar|abr|mai|jun|jul|ago|set|out|nov|dez)([^\d]+)?(\d+)?|(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|jan|fev|mar|abr|mai|jun|jul|ago|set|out|nov|dez)([\s]+)?(\d+)([^\d]+)?(\d+)?)", data)

maparegex = {
    1:'dia',
    8:'dia',
    3:'mes',
    6:'mes',
    5:'ano',
    10:'ano'
}

mapameses = {
    'Jan':'01','jan':'01','Feb':'02','fev':'02','Mar':'03','mar':'03',
    'Apr':'04','abr':'04','May':'05','mai':'05','Jun':'06','jun':'06',
    'Jul':'07','jul':'07','Aug':'08','ago':'08','Sep':'09','set':'09',
    'Oct':'10','out':'10','Nov':'11','nov':'11','Dec':'12','Dez':'12'
}

pmap = []
mapa = {
    'dia':'',
    'mes':'',
    'ano':''
}

for key in maparegex:
    if maparegex[key] in pmap: continue
    if r.group(key+1) != None:
        pmap.append(maparegex[key])
        mapa[maparegex[key]] = r.group(key+1)

fdata = (mapa['ano'] if mapa['ano'] != '' else str(date.today().year))+"-"+mapameses[mapa['mes']]+"-"+(mapa['dia'] if len(mapa['dia']) > 9 else "0"+mapa['dia'])

print(fdata)