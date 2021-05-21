from flask import Flask, render_template, url_for, request, session

app = Flask(__name__)
app.secret_key ='1234'


@app.route('/')
def home():
    return render_template("cv.html")

@app.route('/assignment8+9')
def assignment8():
    return render_template("skill_extend.html", skills= "my skills:")


@app.route('/assignment9',methods=['GET','POST'])
def assignment9():
    users= [
        {
            "email": "michael.lawson@reqres.in",
            "first_name": "Michael",
            "last_name": "Lawson"
        },
        {
            "email": "lindsay.ferguson@reqres.in",
            "first_name": "Lindsay",
            "last_name": "Ferguson"
        },
        {
            "email": "tobias.funke@reqres.in",
            "first_name": "Tobias",
            "last_name": "Funke"
        },
        {
            "email": "byron.fields@reqres.in",
            "first_name": "Byron",
            "last_name": "Fields"
        },
        {
            "email": "george.edwards@reqres.in",
            "first_name": "George",
            "last_name": "Edwards"
        },
        {
            "email": "rachel.howell@reqres.in",
            "first_name": "Rachel",
            "last_name": "Howell"
        },
    ]
    to_search=request.args.get('find')
    result=""
    if to_search:  # if the user entered a name to the search form
        for user in users:
            if user['email']==to_search or user['first_name']==to_search or user['last_name']==to_search:
                result=user  # if he did and it was name from the list, return this user
    if to_search=="":
        result=users  # else return all list
     # register part
    user = ""
    if session:
        user= session['userName']  # user = the name of the user who registered
    if request.method == 'POST':
        session.pop('userName',None)
        session['userName'] = request.form['usr']   # session = the name of the user who registered
    return render_template("assignment9.html",result=result, user=user)

if __name__ == '__main__':
    app.debug = True
    app.run()