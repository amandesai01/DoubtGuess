import requests
import json

def GenerateIndex():
    r = requests.get(
        'https://kjsce.somaiya.edu/ajax/ajaxCall.aspx?action=Faculty&instituteid=16&type=institute&value=16&pageSize=200&pageNumber=0&site=kjsce').json()
    Dict = {}  # Initiating Empty Dictionary
    # Assigning appropriate IDs to department. Giving "0" to data with no department.
    count = 0
    for i in r:
        try:
            if i['departments'][0]['DTO1'] == 'Mechanical Engineering':
                depart = 2
            if i['departments'][0]['DTO1'] == "Computer Engineering":
                depart = 1
            if i['departments'][0]['DTO1'] == "Science and Humanities":
                depart = 6
            if i['departments'][0]['DTO1'] == "Electronics Engineering":
                depart = 4
            if i['departments'][0]['DTO1'] == "Electronics & Telecommunication Engineering":
                depart = 3
            if i['departments'][0]['DTO1'] == "Information Technology":
                depart = 5
        except IndexError:
            depart = 0
        Dict[count] = {'empid': i['empid'], 'name': i['name'], 'department': depart, 'email': i['email'],
                       'position': i['position'], 'photo': "https://kjsce.somaiya.edu" + i['photo']}
        count += 1
    return Dict