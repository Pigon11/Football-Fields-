from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:/// newflask.db'
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/karta')
def karta():
    return render_template("karta.html")


@app.route('/user/<string:name>/<int:id>')
def user(name,id):
    return " User page: " + name + " - " + str(id)

@app.route('/posts')
def posts():
    posts = Post.query.all()
    return render_template("posts.html", posts=posts)


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']

        post = Post(title=title, text=text)

        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/')
        except:
            return 'При добавлении возникла ошибка'
    else:
        return render_template("create.html")


if __name__== "__main__":
    app.run(debug=True)          ## чтобы в реальном времени видели изменения