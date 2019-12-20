import json
from Extractor.listofteachers import GetAllTeachers

def GetData():
    return GetAllTeachers()

def teacherWithName(name):
    data = GetData()
    nameQuery = name.split(' ')
    for d in data:
        i = data[d]
        match = 0
        for seg in nameQuery:
            for check in i['nameSearch']:
                if seg == check:
                    match = match + 1
        if match >= 2:
            return i['empid'] 

def teacherWithEmail(email):
    data = GetData()
    for d in data:
        i = data[d]
        if i['email'] == email:
            return i['empid']

