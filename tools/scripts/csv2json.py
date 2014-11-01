import csv
import os
import sys
from pprint import pprint
import json
import fields

'''TODO:
        Make output validate specifically against ../../spec/volume.json
        Less hardcoded headers or reflect a standard based on JSON schema
        Probably just want to move to python 3 if nothing holding back in 2.7
'''


try:
    _session_csv = sys.argv[1]     #session metadata (csv format)
    _participant_csv = sys.argv[2] #participant metadata (csv format)
    _filepath_prefix = sys.argv[3] #filename on server where assets are kept
except:
    print '''To run this, please add paths to two csv files and a name
             for the file where the video data is kept as arguments:
             e.g. `python csv2json.py session.csv participants.csv study1_files`'''
    sys.exit()


def giveMeCSV(file):
    f = open(file, 'rb')
    r = csv.reader(f)
    return r

def cleanVal(i):
    i = i.strip()
    return i


def getParticipantMap(p_csvFile):
    '''This will give us back a dictionary with participant IDs as keys and
        their records in the form of dictionaries as the values'''
    participantMap = {};
    p_reader = giveMeCSV(p_csvFile)
    p_headers = p_reader.next()


    for rec in p_reader:
        vals = {}
        for z in range(len(p_headers)):
            vals[p_headers[z]] = rec[z]

        participantMap[rec[0]] = vals

    return participantMap

def getSessionMap(s_csvFile):
    '''This will give us back a dictionary where the unique session names (IDs) are associated with a dictionary of
       values containing participant and segment arrays'''

    r = giveMeCSV(s_csvFile)
    rhead = r.next()

    sessionMap = makeOuterMostElements(r)

    vol = giveMeCSV(s_csvFile)
    vheaders = vol.next()

    tmpList = [] #track unique participants below
    for i in vol:
        segment = [i[7], i[8]] #assumes locations of segments as fixed on 7, 8 index
        if segment not in sessionMap[i[0]]['segments']:
            sessionMap[i[0]]['segments'].append(segment)


        if i[3] not in tmpList:
            tmpList.append(i[3])
            sessionMap[i[0]]['participants'].append({ i[3]: {} }) #assume this to work to keep out duplicattes, but it does not

    return sessionMap

def makeOuterMostElements(csvReader):
    '''make an empty dictionary with the session id for keys'''
    emptydict = {}

    for n in csvReader:
        emptydict[n[0]] = {'participants':[], 'segments':[], 'tasks':[]}


    return emptydict



def parseCSV2JSON(s_csvFile, p_csvFile):

    with open(s_csvFile, 'rb') as s_input:
        s_reader = csv.reader(s_input)
        s_headers = s_reader.next()

        data = []

        p_map = getParticipantMap(p_csvFile)
        s_map = getSessionMap(s_csvFile)

        for row in s_reader:
            for i in range(len(s_headers)):
                header = cleanVal(s_headers[i])

                if header == "tasks":
                    task_list = row[i].split(';')

                    for j in range(len(task_list)):
                        if cleanVal(task_list[j]) not in s_map[row[0]]['tasks']:
                            s_map[row[0]]['tasks'].append(cleanVal(task_list[j]))

                elif header == "participantID":
                    for i in range(len(s_map[row[0]]['participants'])):
                        for v in s_map[row[0]]['participants'][i]:
                            s_map[row[0]]['participants'][i][v] = p_map[v] #duplicates

                else:

                    s_map[row[0]][s_headers[i]] = row[i]

        data.append(s_map)

    res = json.dumps(data, indent=4)


    j = open('../o/output.json', 'w')
    j.write(res)

if __name__ == "__main__":
    parseCSV2JSON(_session_csv, _participant_csv)
