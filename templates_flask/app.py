from flask import render_template
from flask import Flask


app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="" ,
  database="CLASH_ROYALE"
)
mycursor = mydb.cursor()

@app.route('/units ')
def unitlist():
    mycursor.execute("SELECT * FROM Clash_Unit")
    myresult = mycursor.fetchall()
    return render_template('hclash_units.html', units=myresult)