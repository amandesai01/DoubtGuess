<h1 align="center"> DoubtGuess </h1>

<div align="center">

[![](https://img.shields.io/badge/IDE-Visual_Studio_Code-red?style=for-the-badge&logo=visual-studio-code)](https://code.visualstudio.com/  "Visual Studio Code")
[![](https://img.shields.io/badge/Made_with-Python-red?style=for-the-badge&logo=Python)](https://www.palletsprojects.com/p/flask/ "Python")
<hr>

[![Documentation Status](https://readthedocs.org/projects/ansicolortags/badge/?version=latest)](http://ansicolortags.readthedocs.io/?badge=latest) 
</div>
<p>This Project, on running, returns all the information of all teachers by scraping it from kjsce.somaiya.edu and applying various filtering algorithms to normalize chaotic data in JSON format in given manner. This makes it easier to query on teacher's information which will then be used to suggest appropriate teacher when passed Doubt. Template of output Json file is given below.

<h2>Json Format:</h2>
<pre>
{
    "0000160932": {
        "empid": "0000160932",
        "name": "Mr.  Abhijeet Uday Karmarkar",
        "department": 2,
        "email": "abhijeet@somaiya.edu",
        "position": "Assistant Professor",
        "photo": "https://kjsce.somaiya.edu/Media/Images/faculty/160932.jpg",
        "nameSearch": [
            "Mr.",
            "",
            "Abhijeet",
            "Uday",
            "Karmarkar"
        ],
        "COURSES TAUGHT": [],
        "RESEARCH INTERESTS": [],
        "CAREER AND EDUCATION": [],
        "OTHER DETAILS": [],
        "PERSONAL INTERESTS": [],
        "0": {
            "BOOKS": []
        },
        "1": {
            "CHAPTERS": []
        },
        "2": {
            "INTERNET PUBLICATIONS": []
        },
        "3": {
            "JOURNAL ARTICLES": []
        },
        "4": {
            "UPCOMING PUBLICATIONS": []
        },
        "5": {
            "CONFERENCES AND SEMINAR": []
        },
        "6": {
            "OTHER PUBLICATION": []
        },
        "7": {
            "INTERNATIONAL PUBLICATION": []
        }
    }
    //List Continues for all teachers.
}

</pre>

You can always use **search.py** to find empid and then fire it to get other details.

## Usage:

### Example:

```python
from doubtguess import GenerateData
from search import teacherWithName, teacherWithEmail

Data = GenerateData()
TeacherData = Data[teacherWithName('Mr.  Abhijeet Uday Karmarkar')]
TeacherData = Data[teacherWithEmail('abhijeet@somaiya.edu')]
```
After this, complete information block of that teacher will be stored in "TeacherData". You can query however you want.

<hr>
<div align="center">
<h3> Made with ❤️ By Aman Desai</h3>
</div>

