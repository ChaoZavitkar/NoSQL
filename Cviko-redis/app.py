from flask import Flask, render_template, redirect, request
#from sqlalchemy import create_engine
import sqlite3 as sql

#engine = create_engine("sqlite:///C:\sqlite\Ovce.db")
#connection = engine.connect("OvceDB.db")

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/datasets", methods=["GET", "POST"])
def datasets():
    con = sql.connect("C:\sqlite\Ovce.db")
    con.row_factory = sql.Row
   
    cur = con.cursor()
    cur.execute("select * from ovce")
   
    rows = cur.fetchone()
    return render_template("index.html",sheeps = rows)

if __name__ == "__main__":
    app.run(debug=True)