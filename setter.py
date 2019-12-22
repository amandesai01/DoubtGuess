from Extractor import get
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
    
# with open('temp.json', 'w') as fp:
#     data = setpublications('0000160120')
#     json.dump(data, fp, indent=4)