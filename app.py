from flask import Flask, render_template, request;

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'GET':
        return (render_template('index.html'))
    else:
        username = request.form['Username']
        password = request.form['Password']
        if username == 'Opeyemi' and password == 'jembe':
            return render_template('football.html',message = 'Login Successful')
        else:
            error_meassage = 'Wrong User Crendentials!'
            return render_template('index.html', message = error_meassage)

@app.route('/football',methods=['GET'])
def football():
    return render_template('football.html')

if __name__ == '__main__':
    app.run(port=7000, debug=True)