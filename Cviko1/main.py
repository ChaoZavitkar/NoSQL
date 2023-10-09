from flask import Flask, render_template, redirect, request

app = Flask(__name__)

recepty = [
    {
        "název": "párek v rohlíku",
        "postup": "Vemu párek, dám ho do rohlíku, dám do toho kečup"
    },
    {
        "název": "gyros",
        "postup": "vezmu Fida a uvařím ho"
    },
    {
        "název": "nudle",
        "postup": "uvařím nudle ve vodě"
    }
]

@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/datasets")
def datasets():
    return render_template("datasets.html", receptar=recepty)

@app.route("/recepty/<idreceptu>")
def vrat_recept(idreceptu):
    return recepty[int(idreceptu)]

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    elif request.method == "POST":
        nazev = request.form.get("nazev")
        postup = request.form.get("postup")
        recepty.append({"název": nazev, "postup": postup})
        return redirect("datasets")
    else:
        return render_template("contact.html")   

if __name__ == "__main__":
    app.run(debug=True)