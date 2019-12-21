from bs4 import BeautifulSoup
import json

def filterString(strElement):
    dataset = strElement.splitlines()
    filteredDataset = [] #initiate empty list
    for i in dataset:
        temp = i.replace('\t','')
        if i != '' and i != 'Undergraduate Courses' and i != 'Post Graduate Courses':
            # print("Appended: " + i + " " + str(type(i)))
            filteredDataset.append(temp)
        # count = 0
        # while count < len(filteredDataset):
        #     if filteredDataset[count] == '\xa0':
        #         filteredDataset.remove(count)
        #     count += 1
        # filteredDataset.remove('\\xa0')
        # return filteredDataset

    return filteredDataset

def filterpersonalprofile(raw):
    # print(raw)
    raw = raw.get("d")
    # print(type(raw))
    raw = json.loads(raw)
    # print(type(raw))
    rawDict = {}  # initiate empty dictionary
    for i in raw:
        key = i["DTO1"]
        try:
            soup = BeautifulSoup(i["CommonList"][0]["DTO1"], 'html.parser')
            dataToken = soup.get_text()
            dataset = filterString(dataToken)
            value = dataset
        except IndexError:  # This specifies that specific teacher has nothing to showoff in that section
            value = []
        rawDict[key] = value
    return rawDict

def filterbiography(data):
    data = json.loads(data['d'])
    properdata = {}
    textx = BeautifulSoup(data['BIOGRAPHY_HTML'], 'html.parser').get_text()
    properdata['biographyAll'] = textx
    textx = textx.splitlines()
    properdata['Biography'] = textx
    properdata['MediaCaption'] = data['MEDIA_CAPTION']
    return properdata

