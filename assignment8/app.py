from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("cv.html")


@app.route('/assignment8')
def assignment8():
    return render_template("skill_extend.html", skills= "my skills:")


@app.route('/assignment9')
def assignment8():
    return render_template("assignment9.html")

# @app.route('/skill_extend')
# def extendBlock():
#     return render_template("skill_extend.html", skills= "my skills:")

if __name__ == '__main__':
    app.debug = True
    app.run()

