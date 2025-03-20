from flask import Flask,render_template
from form import*
app = Flask(__name__)

app.config['SECRET_KEY'] = 'f15f3e37e75d4ef9bce64b7c089c70b378a8508f349f60bbc5bd7827c4dc2116'
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
        },
    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("HomePage.html",posts=posts)

@app.route("/about")
def hello():
    return render_template("About.html")

@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    return render_template("register.html",form=form)

if __name__=="__main__":
    app.run(debug=True)
