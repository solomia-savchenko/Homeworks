from flask import Flask, render_template

app = Flask(__name__)

@app.route("/main")
def main():
    return ("Homepage")

def index():
    return render_template("index.html")

app.add_url_rule("/index", "index_path", index) # in 2nd can be None


# dinamyc site
@app.route("/user/<name>")
def user_profile(name):
    return "Hello, {}".format(name)

if __name__ == "__main__":
    app.run(debug=True)