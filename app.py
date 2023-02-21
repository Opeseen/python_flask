from flask import Flask, render_template, request, session, redirect,url_for,g;
import model


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key'

username = ''
user = model.check_users()

@app.route('/',methods = ['GET'])
def home():
    if "username" in session:
        g.user=session['username']
        return render_template('football.html',message = '<img src= static/aws.jpg>')
    
    return render_template('homepage.html',message = 'Login to the page or signup!')


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session.pop('username',None)
        areYouUser = request.form['Username'].title()
        password = request.form['Password']
        db_passwd = model.check_passwd(areYouUser)
        if password == db_passwd:
            session['username'] = areYouUser
            return redirect(url_for('home'))
        else:
            error_meassage = 'Wrong User credentials'
            return render_template('index.html', message = error_meassage)
        
    return render_template('index.html')

    # if request.method == 'GET':
    #     return (render_template('index.html'))
    # else:
    #     username = request.form['Username'].title()
    #     password = request.form['Password']
    #     db_passwd = model.check_passwd(username)

    #     if password == db_passwd:
    #         message = model.show_color(username)
    #         return render_template('football.html',message = message)
    #     else:
    #         error_meassage = 'Wrong User credentials'
    #         return render_template('index.html', message = error_meassage)
        

@app.before_request
def before_request():
    g.username = None
    if 'username' in session:
        g.username = session['username']

# @app.route('/football',methods=['GET'])
# def football():
#     return render_template('football.html')


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

@app.route('/getsession')
def getsession():
    if 'username' in session:
        return session['username']
    return redirect(url_for('login'))
         
@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(port=7000, debug=True)