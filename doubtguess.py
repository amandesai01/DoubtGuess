from Extractor import get, listofteachers
import json
from Amplifier import Amplify

def setpersonalprofile(empid):
    data = get.PersonalProfile(empid)
    return Amplify.filterpersonalprofile(data)

def setbiography(empid):
    data = get.Biography(empid)
    return Amplify.filterbiography(data)

def setpublications(empid):
    data = get.Publications(empid)
    return Amplify.filterpublications(data)

def GenerateData():
    eachteacher = {}
    finaldata = {}
    index = listofteachers.GetAllTeachers()
    for i in index:
        # print(eachteacher['empid'])
        eachteacher = index[i]
        print("Processing:" + eachteacher['empid'])
        eachteacher.update(setpersonalprofile(eachteacher['empid']))
        eachteacher.update(setbiography(eachteacher['empid']))
        eachteacher.update(setpublications(eachteacher['empid']))
        finaldata[eachteacher['empid']] = eachteacher
    return finaldata

def getTeacher(empid):
    data = {}
    data.update(setpersonalprofile(eachteacher['empid']))
    data.update(setpersonalprofile(eachteacher['empid']))
    data.update(setpersonalprofile(eachteacher['empid']))
    return data
    
with open('temp.json', 'w') as fp:
    data = GenerateData()
    json.dump(data, fp, indent=4)