from jinja2 import Template
import matplotlib.pyplot as plt
import csv
import sys


PAGE1 = """ 

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Student Data</title>
    <style>
        table , tr , td , th{
            border: 1px solid black;
        }
    </style>
</head>
<body>
    <h1>Student Details</h1>
    <table >
        <tr>
            <th>Student id</th>
            <th>Course id</th>
            <th>Marks</th>
        </tr>
        {% for element in elements %}
        <tr>
            <td>{{element['Student id']}}</td>
            <td>{{element['Course id']}}</td>
            <td>{{element['Marks']}}</td>
        </tr>
        {% endfor %}
        <tr>
            <td colspan="2">
                Total Marks
            </td>
            <td>{{totalMarks}}</td>
        </tr>
    </table>
</body>
</html>
 """

PAGE2 = """

   <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Course Data</title>
    <style>
        table , tr , td , th{
            border: 1px solid black;
        }
    </style>
</head>
<body>
    <h1>Course Details</h1>
    <table >
        <tr>
            <th>Average Marks</th>
            <th>Maximum Marks</th>
        </tr>
        <tr>
            <td>{{avgMarks}}</td>
            <td>{{MaximumMarks}}</td>
        </tr>
    </table>
    <img src="plot.png" alt="data">
    
</body>
</html>

"""

PAGE3 = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Someting Went Wrong</title>
</head>
<body>
    <h1>Wrong Inputs</h1>
    <p>Someting went wrong</p>
    
</body>
</html>
"""


def getDataFromFile(fileName):
    with open(fileName, "r") as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        rows = []
        for row in csv_reader:
            dict_row = {}
            for i in range(len(headers)):
                dict_row[headers[i].strip()] = int(row[i].strip())
            rows.append(dict_row)
    return rows

def showError():
    t = Template(PAGE3)
    htmlFile = open("output.html" , 'w')
    content = t.render()
    htmlFile.write(content)
    htmlFile.close()
    return 

def main():
    inp = sys.argv
    filename = "data.csv"
    data = getDataFromFile(filename)

    if(inp[1] != '-s' and inp[1] != '-c' ):
        showError()
        return

    if(inp[1] == '-s'):
        studentId = int(inp[2])
        dataRows = []
        totalMarks = 0
        for i in range(len(data)):
            if(data[i]['Student id'] == studentId):
                dataRows.append(data[i])
                totalMarks += data[i]['Marks']
        
        if(len(dataRows) == 0):
            showError()
            return 
        
        t = Template(PAGE1)
        content = t.render(elements = dataRows , totalMarks = totalMarks)
        htmlFile = open("output.html" , 'w')
        htmlFile.write(content)
        htmlFile.close()
        return 

    if(inp[1] == '-c'):
        courseId = int(inp[2])
        totalMarks = 0
        allMarks = []
        maximumMarks = 0
        count = 0
        for i in range(len(data)):
            if(data[i]['Course id'] == courseId):
                thisMarks = data[i]['Marks']
                totalMarks += thisMarks
                allMarks.append(thisMarks)
                maximumMarks = max(maximumMarks , thisMarks )
                count += 1

        if( count == 0):
            showError()
            return
        
        t = Template(PAGE2)
        plt.hist(allMarks, bins=max(allMarks)-min(allMarks)+1, align='left', rwidth=.8)
        plt.xlabel('Marks')
        plt.ylabel('Frequency')
        plt.savefig('plot.png')
        content = t.render(MaximumMarks= maximumMarks , avgMarks = totalMarks / count)
        htmlFile = open("output.html" , 'w')
        htmlFile.write(content)
        htmlFile.close()
        return 


if __name__ == "__main__":
    main()