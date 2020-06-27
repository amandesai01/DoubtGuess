import requests
import json
def GetPayload(empid):
    return {"target": "FACULTY", "targetid": empid, "isOwner": "False"}

def GetData(apicall, empid):
    return requests.post("https://kjsce-old.somaiya.edu/ajax/ajaxCall.aspx/"+apicall, json=GetPayload(empid)).json()

def PersonalProfile(empid):
    return GetData("GetPersonalProfile", empid)

def Biography(empid):
    return GetData("GetBiography", empid)

def Publications(empid):
    return GetData("GetPublications", empid)
