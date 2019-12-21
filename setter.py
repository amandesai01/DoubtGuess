from Extractor import get
import json

def setpersonalprofile(empid):
    personalprofile = get.PersonalProfile(empid)
    return personalprofile

def setbiography(empid):
    biography = get.Biography(empid)
    return biography

def setpublications(empid):
    publications = get.Publications(empid)
    return publications
    
# with open('temp.json', 'w') as fp:
#     json.dump(setpersonalprofile('0000160932'), fp, indent=4)