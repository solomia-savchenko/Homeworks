from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

participants = []


@app.route("/event_register", methods=["GET", "POST"])
def event_register():

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        time = request.form.get("time")

        if name and email and time:
            participants.append({
                "name": name,
                "email": email,
                "time": time
            })

            return redirect(url_for("participants_page"))

    return render_template("register.html")


@app.route("/participants")
def participants_page():
    return render_template(
        "participants.html",
        participants=participants
    )


if __name__ == "__main__":
    app.run(debug=True)