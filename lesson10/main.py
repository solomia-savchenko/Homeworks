from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("base.html")

@app.route("/timetable")
def timetable():
    timetable = [
        ["bus 2", "18:00"],
        ["Tram 17", "19:00"],
        ["Train 12", "19:05"],
        ["Plane 117", "20:00"]
    ]
    return render_template("timetable.html", timetable=timetable)


@app.route("/user/<name>")
def user_profile(name):
    return "Hello, {}".format(name)


if __name__ == "__main__":
    app.run(debug=True)