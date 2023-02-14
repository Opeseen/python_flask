from flask import Flask, render_template, request, flash;
import model


app = Flask(__name__)

app.config['SECRET_KEY'] = 'any secret string'

@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'GET':
        return (render_template('index.html'))
    else:
        username = request.form['Username'].title()
        password = request.form['Password']
        db_passwd = model.check_passwd(username)

        if password == db_passwd:
            message = model.show_color(username)
            return render_template('football.html',message = message)
        else:
            error_meassage = 'Wrong User credentials'
            return render_template('index.html', message = error_meassage)
        


@app.route('/football',methods=['GET'])
def football():
    return render_template('football.html')


@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        message = 'Please Sign up...'
        return render_template('signup.html',message = message)
    else:
        username = request.form['Username'].title()
        password = request.form['Password']
        favorite_color = request.form['favorite_color']
        message = model.signup(username,password,favorite_color)

        return render_template('signup.html',message = message)
         

if __name__ == '__main__':
    app.run(port=7000, debug=True)