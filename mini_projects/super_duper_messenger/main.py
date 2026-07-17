from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, current_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password1234@localhost:5432/messanger'
app.config["SECRET_KEY"] = "w"

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    sent_messages = db.relationship("Messages", foreign_keys="Messages.sender", back_populates="sender_user")
    received_messages = db.relationship("Messages", foreign_keys="Messages.recipient", back_populates="recipient_user")
    sent_requests = db.relationship("Friends", foreign_keys="Friends.sender", back_populates="sender_user")
    received_requests = db.relationship("Friends", foreign_keys="Friends.recipient", back_populates="recipient_user")

    def set_password(self, raw_password):
        self.password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        return check_password_hash(self.password, raw_password)
    

class Friends(db.Model):
    __tablename__ = "friends"

    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    recipient = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    status = db.Column(db.Boolean, default=False)

    sender_user = db.relationship("User", foreign_keys=[sender], back_populates="sent_requests")
    recipient_user = db.relationship("User", foreign_keys=[recipient], back_populates="received_requests")


class Messages(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    recipient = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    message_text = db.Column(db.Text, nullable=False)
    status = db.Column(db.Boolean, default=False)

    sender_user = db.relationship("User", foreign_keys=[sender], back_populates="sent_messages")
    recipient_user = db.relationship("User", foreign_keys=[recipient], back_populates="received_messages")

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

@app.route("/")
@login_required
def index():
    return render_template("index.html", user=current_user.username)

@app.route("/friends")
@login_required
def friends():
    return render_template("friends.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for("index"))

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()
        if user:
            error = "User exists, you can login"
            return render_template("login.html", error=error)
        

        new_user = User(username=username)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        return redirect(url_for("index"))

    return render_template("register.html")



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
