from flask import Flask, render_template

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

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello_world():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
    
