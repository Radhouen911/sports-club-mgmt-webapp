from pathlib import Path

from flask import Flask, render_template

import db

app = Flask(__name__)
app.config["DATABASE"] = Path(__file__).parent / "club.db"

db.init_app(app)

with app.app_context():
    db.init_db()


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
