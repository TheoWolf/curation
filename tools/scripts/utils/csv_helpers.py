import csv
import sys
import time

################### QUICK OPERATIONS FOR REDUNDANT TASKS INVOLVING CSVs ###############################

### CSV IO

def giveMeTSV(file): #iohelper
    t = open(file, 'rt')
    return csv.reader(t, delimiter='\t')

def giveMeCSV(csvfile): #iohelper
    f = open(csvfile, 'rt') 
    return csv.reader(f)

def cleanVal(i):
    return i.strip()

def getHeaderIndex(headerlist): #iohelper
    return {headerlist[i]: i for i in range(len(headerlist))}


def makeNewFile(path, filename_addition="_output"): #iohelper
    '''given a filepath as an argument, we will use that to create the new file where
       output will be stored'''
    PATH_PARTS = path.split('/')
    PATH_PARTS.pop()
    PATH = ('/').join(PATH_PARTS)
    return PATH+'/'+path.split('/')[-1].split('.')[0]+filename_addition+'.csv'


### STRINGS

def assignIfThere(k, index, row, assignthis): #stringhelper
    '''all purpose check for key in header index so we know to assign a value for the row or not
        so we do not need empty columns in the spreadsheet'''

    return row[index[k]] if k in index and row[index[k]] != '' else assignthis

def assignWithEmpty(k, index, row, assignthis): #stringhelper
    '''assign none if does not exist, or assign with empty string if the column does exist'''

    return row[index[k]] if k in index else assignthis



### TIME

def parseHHMMSS(hms): #timehelper
    l = [x.strip() for x in hms.split(':')]
    if hms == "$":
        return hms
    elif len(l) == 3:
        h, m, s = l
    elif len(l) == 2:
        h = 0
        m, s = l
    if "." in s:
       s = s.split('.')[0]
    return (h, m, s)


def convertHHMMSStoMS(hms): #timehelper
    '''take a time in the form of HH:MM:SS or MM:SS and return a rounded int for milliseconds'''
    h, m, s = parseHHMMSS(hms)
    return int(h) * 3600000 + int(m) * 60000 + int(s) * 1000

def findHalfTime(t): #timehelper
    '''for now takes a time sting in the form of HH:MM:SS.mm and gives you back the halfway point in same format'''
    ms = convertHHMMSStoMS(t)
    half = ms / 2
    return convertMStoHHMMSS(half)

  


