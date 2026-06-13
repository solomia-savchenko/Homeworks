from flask import Flask, render_template, abort, redirect, url_for
import random

app = Flask(__name__)

movies = {
    1: {
        "title": "Inception",
        "description": "A thief enters people's dreams to steal secrets."
    },
    2: {
        "title": "Interstellar",
        "description": "Astronauts travel through a wormhole to save humanity."
    },
    3: {
        "title": "The Matrix",
        "description": "A hacker discovers the true nature of reality."
    }
}


@app.route("/")
def home():
    return render_template("index.html", movies=movies)


@app.route("/movie/<int:id>")
def movie(id):
    if id not in movies:
        abort(404)

    return render_template(
        "movie.html",
        movie=movies[id]
    )


@app.route("/random")
def random_movie():
    movie_id = random.choice(list(movies.keys()))
    return redirect(url_for("movie", id=movie_id))


if __name__ == "__main__":
    app.run(debug=True)