from flask import Flask, render_template,url_for

from forms import RgistrationForm,LoginForm




app = Flask(__name__)


app.config['SECRET_KEY'] = '3fa97c5c97086b4c7862043b86d685d9'


posts = [
    {
        'author':'cory schafer',
        'title':'Blog post',
        'content':'First post content',
        'date_posted':'April 20, 2010'
    },
    {
        'author':'Jane Doe',
        'title':'Blog post 2',
        'content':'Second post content',
        'date_posted':'April 21, 2010'
    }
    
    
]



@app.route("/")
@app.route("/home")
def hello_world():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register")
def register():
    form = RgistrationForm()
    return render_template('register.html', title='Register',form=form)
    
@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login',form=form)



if __name__ == '__main__':
    app.run(debug=True)
    
