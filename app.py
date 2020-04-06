from flask import Flask, render_template
from flask_restful import Resource, Api
from forms import HandleForm

app = Flask(__name__)
api = Api(app)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/handle")
def get_handle():
    form = HandleForm()
    return render_template('handle.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)
