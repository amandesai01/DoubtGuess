import requests
import json

def SendRequest():
    r = requests.get('https://kjsce.somaiya.edu/ajax/ajaxCall.aspx?action=Faculty&instituteid=16&type=institute&value=16&pageSize=200&pageNumber=0&site=kjsce').json()
    return r;

def GetDepartment(i):
    depart = 0
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
    return depart

def GetAllTeachers():
    r = SendRequest();
    Dict = {}  # Initiating Empty Dictionary
    # Assigning appropriate IDs to department. Giving "0" to data with no department.
    count = 0
    for i in r:
        Dict[count] = {'empid': i['empid'], 'name': i['name'], 'department': GetDepartment(i), 'email': i['email'],
                       'position': i['position'], 'photo': "https://kjsce.somaiya.edu" + i['photo'], 'nameSearch' : i['name'].split(' ')}
        count += 1
    # name also stored in array because querying in name is difficult for search purpose.
    return Dict

def GetTeacher(empid):
    r = SendRequest()
    Dict = {}
    for i in r:
        if i['empid'] == empid:
            Dict['data'] = {'empid': i['empid'], 'name': i['name'], 'department': GetDepartment(i), 'email': i['email'],'position': i['position'], 'photo': "https://kjsce.somaiya.edu" + i['photo'], 'nameSearch' : i['name'].split(' ')}
            Dict['status'] = 'Success'
            return Dict
    Dict['data'] = 'No Response. Check Query'
    Dict['status'] = 'Fail'
    return Dict

print(json.dumps(GetAllTeachers(), indent=4))