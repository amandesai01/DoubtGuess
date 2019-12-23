from bs4 import BeautifulSoup
import json

def decomposeCommonList(ele):
    val = []
    if ele['DTO1']:
        val.extend(BeautifulSoup(ele['DTO1'], 'html.parser').get_text().splitlines())
    if ele['DTO2']:
        val.extend(BeautifulSoup(ele['DTO2'], 'html.parser').get_text().splitlines())
    if ele['DTO3']:
        val.extend(BeautifulSoup(ele['DTO3'], 'html.parser').get_text().splitlines())
    if ele['DTO4']:
        val.extend(BeautifulSoup(ele['DTO4'], 'html.parser').get_text().splitlines())
    if ele['DTO5']:
        val.extend(BeautifulSoup(ele['DTO5'], 'html.parser').get_text().splitlines())
    if ele['CommonList']:
        for i in ele['CommonList']:
            try:
                val.extend(decomposeCommonList(i))
            except:
                continue
    return val

def decomposeDto(ele):
    key = ele['DTO1']
    val = []
    reply = {}
    if ele['DTO2']:
        val.extend(BeautifulSoup(ele['DTO2'], 'html.parser').get_text().splitlines())
    if ele['DTO3']:
        val.extend(BeautifulSoup(ele['DTO3'], 'html.parser').get_text().splitlines())
    if ele['DTO4']:
        val.extend(BeautifulSoup(ele['DTO4'], 'html.parser').get_text().splitlines())
    if ele['DTO5']:
        val.extend(BeautifulSoup(ele['DTO5'], 'html.parser').get_text().splitlines())
    if ele['CommonList']:
        for i in ele['CommonList']:
            try:
                val.extend(decomposeCommonList(i))
            except:
                continue
        # for i in ele['CommonList']:
        #     dic = decomposeDto(i)
        #     reply[list(dic.keys())[0]] = dic[list(dic.keys())[0]]
    
    reply[key] = val
    # print(json.dumps(reply, indent=4))
    return reply

    
        


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
            dataToken = BeautifulSoup(i["CommonList"][0]["DTO1"], 'html.parser').get_text()
            dataset = filterString(dataToken)
            value = dataset
        except IndexError:  # This specifies that specific teacher has nothing to showoff in that section
            value = []
        rawDict[key] = value
    return rawDict

def filterbiography(data):
    data = json.loads(data['d'])
    properdata = {}
    try:
        textx = BeautifulSoup(data['BIOGRAPHY_HTML'], 'html.parser').get_text()
        properdata['biographyAll'] = textx
        textx = textx.splitlines()
        properdata['Biography'] = textx
        properdata['MediaCaption'] = data['MEDIA_CAPTION']
    except:
        return properdata
    return properdata

def filterpublications(data):
    data = json.loads(data['d'])
    ndata = {}
    co = 0
    for i in data:
        temp = decomposeDto(i)
        ndata[co] = temp
        co = co + 1
        # pass
    return ndata