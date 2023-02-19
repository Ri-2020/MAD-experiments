import csv
from flask import Flask
from flask import render_template
from flask import request
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


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

filename = "data.csv"
DATA = getDataFromFile(filename)

app = Flask(__name__)


@app.route("/" , methods =["GET", "POST"])
def hello():
     if request.method == 'GET':
          
          return render_template("getDetails.html")
     elif request.method == 'POST':
          
          try:
               id_name = request.form["ID"]
          except:
               return render_template("error.html")
          if request.form['id_value'].strip() != "":
               try:
                    id_value =  int(request.form['id_value'])
               except:
                    return render_template("error.html")
          else:
               id_value = 0
          if(id_value == 0):
               return render_template("error.html")
          if id_name == "student_id":
               dataRows = []
               totalMarks = 0
               for i in range(len(DATA)):
                    if(DATA[i]['Student id'] == id_value):
                         dataRows.append(DATA[i])
                         totalMarks += DATA[i]['Marks']
               
               if(len(dataRows) == 0):
                    return render_template("error.html")
               else:
                    return render_template("studentDetails.html" , elements = dataRows , totalMarks = totalMarks )
          if id_name == "course_id":
               totalMarks = 0
               allMarks = []
               maximumMarks = 0
               count = 0
               for i in range(len(DATA)):
                    if(DATA[i]['Course id'] == id_value):
                         thisMarks = DATA[i]['Marks']
                         totalMarks += thisMarks
                         allMarks.append(thisMarks)
                         maximumMarks = max(maximumMarks , thisMarks )
                         count += 1

               if( count == 0):
                    return render_template("error.html")
               plt.hist(allMarks, bins=max(allMarks)-min(allMarks)+1, align='left', rwidth=.8)
               plt.xlabel('Marks')
               plt.ylabel('Frequency')
               plt.savefig('./static/plot.png')
               plt.close()
               
               return render_template("courseDetails.html" , MaximumMarks= maximumMarks , avgMarks = totalMarks / count )

if __name__ == "__main__":
     app.run()